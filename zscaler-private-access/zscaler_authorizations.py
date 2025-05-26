"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""


from datetime import datetime
from time import time, ctime

import requests
from connectors.core.connector import get_logger, ConnectorError
from connectors.core.utils import update_connnector_config

logger = get_logger('zscaler-private-access')


class ZscalerAuth:
    def __init__(self, config):
        self.client_id = config.get("client_id")
        self.client_id = config.get("Client ID")
        self.client_secret = config.get("client_secret")
        self.verify_ssl = config.get('verify_ssl')
        self.server_url = config.get("server_url").strip('/')
        if not self.server_url.startswith('https://') and not self.server_url.startswith('http://'):
            self.server_url = 'https://' + self.server_url
        self.token_url = config.get('token_url')
        if not self.token_url.startswith('https://') and not self.token_url.startswith('http://'):
            self.token_url = 'https://' + self.token_url

    def make_api_call(self, config, connector_info, method="GET", endpoint="", params=None, headers=None,
                      data=None,
                      json_data=None,
                      verify_ssl=False):
        try:
            headers = headers if headers else {"Authorization": self.validate_token(config, connector_info)}
            endpoint = self.server_url + endpoint
            logger.debug("endpoint: " + str(endpoint))
            logger.debug("method: " + str(method))
            logger.debug("params: " + str(params))
            logger.debug("data: " + str(data))
            response = requests.request(method=method, url=endpoint, headers=headers, data=data, json=json_data,
                                        params=params, verify=verify_ssl)
            if response.ok:
                return response.json()
            else:
                logger.error("Error: {0}".format(response.text))
                raise ConnectorError('{0}:{1}'.format(response.status_code, response.text))
        except requests.exceptions.SSLError as e:
            logger.exception('{0}'.format(e))
            raise ConnectorError('{0}'.format(e))
        except requests.exceptions.ConnectionError as e:
            logger.exception('{0}'.format(e))
            raise ConnectorError('{0}'.format(e))
        except Exception as e:
            logger.error('{0}'.format(e))
            raise ConnectorError('{0}'.format(e))

    def convert_ts_epoch(self, ts):
        datetime_object = datetime.strptime(ctime(ts), "%a %b %d %H:%M:%S %Y")
        return datetime_object.timestamp()

    def generate_token(self, config, connector_info):
        try:
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            payload = {
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'grant_type': 'client_credentials',
                'audience': 'https://api.zscaler.com',
            }
            token_resp = self.make_api_call(config, connector_info, method='POST',
                                            endpoint=self.token_url, headers=headers, data=payload)
            ts_now = time()
            token_resp['expires_in'] = (ts_now + token_resp['expires_in']) if token_resp.get("expires_in") else None
            token_resp['access_token'] = token_resp.get("access_token")
            return token_resp
        except Exception as err:
            logger.error("{0}".format(err))
            raise ConnectorError("{0}".format(err))

    def validate_token(self, connector_config, connector_info):
        try:
            ts_now = time()
            if not connector_config.get('access_token'):
                logger.error('Error occurred while connecting server: Unauthorized')
                raise ConnectorError('Error occurred while connecting server: Unauthorized')
            expires = connector_config.get('expires_in')
            expires_ts = self.convert_ts_epoch(expires)
            if ts_now > float(expires_ts):
                logger.info("Token expired at {0}".format(expires))
                token_resp = self.generate_token(connector_config, connector_info)
                connector_config['access_token'] = token_resp['access_token']
                connector_config['expires_in'] = token_resp['expires_in']
                update_connnector_config(connector_info['connector_name'], connector_info['connector_version'],
                                         connector_config,
                                         connector_config['config_id'])

                return "Bearer {0}".format(connector_config.get('access_token'))
            else:
                logger.info("Token is valid till {0}".format(expires))
                return "Bearer {0}".format(connector_config.get('access_token'))
        except Exception as err:
            logger.error("{0}".format(str(err)))
            raise ConnectorError("{0}".format(str(err)))


def test_connectivity(config, connector_info):
    try:
        zs_one_api = ZscalerAuth(config)

        if not 'access_token' in config:
            token_resp = zs_one_api.generate_token(config, connector_info)
            config['access_token'] = token_resp.get('access_token')
            config['expires_in'] = token_resp.get('expires_in')
            update_connnector_config(connector_info.get('connector_name'), connector_info.get('connector_version'),
                                     config,
                                     config.get('config_id'))
            return True
        else:
            token_resp = zs_one_api.validate_token(config, connector_info)
            return True
    except Exception as err:
        raise ConnectorError(str(err))
