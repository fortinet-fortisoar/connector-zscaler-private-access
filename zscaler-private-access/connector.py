"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""


from connectors.core.connector import Connector, ConnectorError, get_logger

from .operations import operations_map
from .zscaler_authorizations import test_connectivity

logger = get_logger('zscaler-private-access')


class ZscalerPrivateAccess(Connector):
    def execute(self, config, operation, params, **kwargs):
        connector_info = {"connector_name": self._info_json.get('name'),
                          "connector_version": self._info_json.get('version')}
        action = operations_map.get(operation, connector_info)
        return action(config, params, connector_info)

    def check_health(self, config):
        try:
            connector_info = {"connector_name": self._info_json.get('name'),
                              "connector_version": self._info_json.get('version')}
            return test_connectivity(config, connector_info)
        except Exception as err:
            logger.error("Check Health Failed. Error: {0}".format(str(err)))
            raise ConnectorError(str(err))
