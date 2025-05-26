"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""


from connectors.core.connector import get_logger

from .zscaler_authorizations import ZscalerAuth

logger = get_logger('zscaler-private-access')


def get_all_configured_applications_segments(config, params, connector_info):
    zpa_api_client = ZscalerAuth(config)
    customer_id = params.get('customerId')
    query_params = {
        "search": params.get("search"),
        "page": params.get("page"),
        "pagesize": params.get("pagesize"),
        "microtenantId": params.get("microtenantId")
    }
    endpoint = f"/zpa/mgmtconfig/v1/admin/customers/{customer_id}/application"
    return zpa_api_client.make_api_call(config, connector_info, params=query_params, endpoint=endpoint, method="GET", )


def get_specific_application_segment_details(config, params, connector_info):
    zpa_api_client = ZscalerAuth(config)
    customer_id = params.get('customerId')
    application_id = params.get('applicationId')
    query_params = {
        "microtenantId": params.get("micro_tenant_id")
    }
    endpoint = f"/zpa/mgmtconfig/v1/admin/customers/{customer_id}/application/{application_id}"
    return zpa_api_client.make_api_call(config, connector_info, params=query_params, endpoint=endpoint, method="GET")


def get_customer_certificates(config, params, connector_info):
    zpa_api_client = ZscalerAuth(config)
    customer_id = params.get('customerId')
    endpoint = f"/zpa/mgmtconfig/v1/admin/customers/{customer_id}/certificate"
    return zpa_api_client.make_api_call(config, connector_info, endpoint=endpoint, method="GET")


def get_all_issued_certificates(config, params, connector_info):
    zpa_api_client = ZscalerAuth(config)
    customer_id=params.get('customerId')
    query_params = {
        "search": params.get("search"),
        "page": params.get("page"),
        "pagesize": params.get("pagesize"),
        "microtenantId": params.get("microtenantId")
    }
    endpoint = f"/zpa/mgmtconfig/v2/admin/customers/{customer_id}/clientlessCertificate/issued"
    return zpa_api_client.make_api_call(config, connector_info, params=query_params, endpoint=endpoint, method="GET")


def get_certificate_details(config, params, connector_info):
    zpa_api_client = ZscalerAuth(config)
    customer_id = params.get('customerId')
    certificate_id = params.get('certificateId')
    query_params = {
        "search": params.get("search"),
        "page": params.get("page"),
        "pagesize": params.get("pagesize"),
        "microtenantId": params.get("microtenantId")
    }
    endpoint = f"/mgmtconfig/v1/admin/customers/{customer_id}/clientlessCertificate/{certificate_id}"
    return zpa_api_client.make_api_call(config, connector_info, params=query_params, endpoint=endpoint, method="GET")


def execute_api_request(config, params, connector_info):
    endpoint = params.get('endpoint')
    zpa_api_client = ZscalerAuth(config)
    method = params.get('method')
    query_params = params.get('query_params')
    payload = params.get('payload')
    return zpa_api_client.make_api_call(config, connector_info, endpoint=endpoint, method=method, params=query_params,
                                        data=payload)


operations_map = {
    'get_all_configured_applications_segments': get_all_configured_applications_segments,
    'get_specific_application_segment_details': get_specific_application_segment_details,
    'get_customer_certificates': get_customer_certificates,
    'get_all_issued_certificates': get_all_issued_certificates,
    'get_certificate_details': get_certificate_details,
    'execute_api_request': execute_api_request
}
