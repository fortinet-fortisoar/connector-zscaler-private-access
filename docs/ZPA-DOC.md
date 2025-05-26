
<h2>About the connector</h2>

<p>Zscaler Private Access (ZPA) is a cloud-delivered Zero Trust Network Access (ZTNA) solution that provides secure, identity-based access to internal applications without placing users on the network. It enables seamless integration with FortiSOAR for automated access control, threat response, and policy enforcement based on real-time user and application context. This connector enables automated operations such as Get All Configured Applications Segments, Get Specific Application Segment Details, Get Customer Certificates, Get All Issued Certificates, and Get Certificate Details.</p>

<p>This document provides information about the Zscaler Private Access (ZPA) connector, which facilitates automated interactions, with a Zscaler Private Access (ZPA) server using FortiSOAR&trade; playbooks. Add the Zscaler Private Access (ZPA) connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Zscaler Private Access (ZPA).</p>

<h3>Version information</h3>

<p>Connector Version: 1.0.0</p>

<p>Authored By: Fortinet</p>

<p>Certified: No</p>

<h2>Installing the connector</h2>

<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>

<pre>yum install cyops-connector-zscaler-private-access</pre>

<h2>Prerequisites to configuring the connector</h2>

<ul>
<li>You must have the credentials of Zscaler Private Access (ZPA) server to which you will connect and perform automated operations.</li>
<li>The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Zscaler Private Access (ZPA) server.</li>
</ul>

<h2>Minimum Permissions Required</h2>

<ul>
<li>Not applicable</li>
</ul>

<h2>Configuring the connector</h2>

<p>For the procedure to configure a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector">here</a></p>

<h3>Configuration parameters</h3>

<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Zscaler Private Access (ZPA)</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the host or server URL for Zscaler Private Access (ZPA) to access the Rest API endpoint.</td></tr>
<tr><td>Client ID</td><td>Specify the Client ID used for authenticating with the Zscaler Private Access (ZPA) API endpoint.</td></tr>
<tr><td>Client Secret </td><td>Specify the Client Secret used for authenticating with the Zscaler Private Access (ZPA) API endpoint.</td></tr>
<tr><td>ZIdentity's Auth Token Endpoint</td><td>Specify the ZIdentity auth token endpoint. This endpoint generates the Bearer token.</td></tr>
<tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified. <br/>By default, this option is selected, i.e., set to <code>true</code>.</td></tr>
</tbody></table>

<h2>Actions supported by the connector</h2>

<p>You can use the following automated operations in playbooks and also use the annotations to access operations:</p>

<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get All Configured Applications Segments</td><td>Gets all configured application segments for the specified customer.</td><td>get_all_configured_applications_segments <br/>Investigation</td></tr>
<tr><td>Get Specific Application Segment Details</td><td>Retrieves the configuration details of the Application Segment associated with the given Application ID.</td><td>get_specific_application_segment_details <br/>Investigation</td></tr>
<tr><td>Get Customer Certificates</td><td>Retrieves a list of all available customer certificates based on the provided Customer ID.</td><td>get_customer_certificates <br/>Investigation</td></tr>
<tr><td>Get All Issued Certificates</td><td>Retrieve all issued certificates.</td><td>get_all_issued_certificates <br/>Investigation</td></tr>
<tr><td>Get Certificate Details</td><td>Retrieves details of a specific certificate based on its ID.</td><td>get_certificate_details <br/>Investigation</td></tr>
<tr><td>Execute an API Request</td><td>Execute any Zscaler Private Access (ZPA) API endpoint using the specified API method, endpoint, and payload as input parameters.</td><td>execute_api_request <br/>Utilities</td></tr>
</tbody></table>

<h3>operation: Get All Configured Applications Segments</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Customer ID</td><td>Specify the unique identifier of the ZPA tenant.</td></tr>
<tr><td>Filter String</td><td>(Optional) Specify the search term for filtering applications.</td></tr>
<tr><td>Offset</td><td>(Optional) Specifies the number of records to skip before starting to return results. Used for paginating API responses in combination with the Limit.</td></tr>
<tr><td>Limit</td><td>(Optional) Specifies the page size, i.e., the maximum number of records to return for this action. If not provided, the default page size is 20. The maximum page size is 500.</td></tr>
<tr><td>Micro Tenant ID</td><td>(Optional) Specify the unique identifier of the Micro tenant for the ZPA tenant. If you are within a Micro tenant, you must pass the micro tenantId field when making an API call to retrieve data from that Micro tenant.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "totalPages": "",
    "currentCount": "",
    "totalCount": "",
    "list": [
        {
            "id": "",
            "name": "",
            "enabled": "",
            "description": "",
            "certificateId": "",
            "certificateName": "",
            "applicationPort": "",
            "applicationProtocol": "",
            "domain": "",
            "appId": "",
            "microtenantId": "",
            "microtenantName": "",
            "inconsistentConfigDetails": {
                "application": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "sraApplication": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "segmentGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "serverGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "appConnectorGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "baCertificate": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "postureProfile": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "trustedNetwork": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "branchConnectorGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "cloudConnectorGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "samlAttributes": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "scimAttributes": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "machineGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "idp": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "location": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "workloadTagGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "userPortal": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ]
            }
        }
    ]
}</pre>

<h3>operation: Get Specific Application Segment Details</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Customer ID</td><td>Specify the unique identifier of the ZPA tenant.</td></tr>
<tr><td>Application ID</td><td>Specify the unique identifier of the Application Segment.</td></tr>
<tr><td>Micro Tenant ID</td><td>(Optional) Specify the unique identifier of the Micro tenant for the ZPA tenant. If you are within a Micro tenant, you must pass the micro tenantId field when making an API call to retrieve data from that Micro tenant.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "modifiedTime": "",
    "creationTime": "",
    "modifiedBy": "",
    "id": "",
    "microtenantId": "",
    "microtenantName": "",
    "domainNames": [],
    "name": "",
    "description": "",
    "IdleTimeout": "",
    "MaxAge": "",
    "serverGroups": [
        {
            "id": "",
            "modifiedTime": "",
            "creationTime": "",
            "modifiedBy": "",
            "name": "",
            "microtenantId": "",
            "microtenantName": "",
            "enabled": "",
            "dynamicDiscovery": "",
            "description": "",
            "configSpace": "",
            "weight": "",
            "passive": "",
            "extranetEnabled": "",
            "zpnErId": {
                "id": "",
                "modifiedTime": "",
                "creationTime": "",
                "modifiedBy": "",
                "ziaErId": "",
                "ziaErName": "",
                "ziaCloud": "",
                "ziaOrgId": "",
                "ziaModifiedTime": ""
            }
        }
    ],
    "enabled": "",
    "passiveHealthEnabled": "",
    "tcpPortRanges": [],
    "udpPortRanges": [],
    "tcpPortRange": [
        {
            "from": "",
            "to": ""
        }
    ],
    "udpPortRange": [
        {
            "from": "",
            "to": ""
        }
    ],
    "doubleEncrypt": "",
    "segmentGroupId": "",
    "segmentGroupName": "",
    "configSpace": "",
    "bypassType": "",
    "healthCheckType": "",
    "icmpAccessType": "",
    "isCnameEnabled": "",
    "clientlessApps": [
        {
            "id": "",
            "name": "",
            "enabled": "",
            "description": "",
            "certificateId": "",
            "certificateName": "",
            "applicationPort": "",
            "applicationProtocol": "",
            "domain": "",
            "appId": "",
            "microtenantId": "",
            "microtenantName": "",
            "inconsistentConfigDetails": {
                "application": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "sraApplication": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "segmentGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "serverGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "appConnectorGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "baCertificate": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "postureProfile": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "trustedNetwork": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "branchConnectorGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "cloudConnectorGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "samlAttributes": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "scimAttributes": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "machineGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "idp": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "location": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "workloadTagGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "userPortal": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ]
            },
            "path": "",
            "hidden": "",
            "portal": "",
            "trustUntrustedCert": "",
            "allowOptions": "",
            "localDomain": "",
            "cname": "",
            "appResource": {
                "modifiedTime": "",
                "creationTime": "",
                "modifiedBy": "",
                "id": "",
                "microtenantId": "",
                "microtenantName": "",
                "domainNames": [],
                "name": "",
                "description": "",
                "IdleTimeout": "",
                "MaxAge": "",
                "serverGroups": [
                    {
                        "id": "",
                        "modifiedTime": "",
                        "creationTime": "",
                        "modifiedBy": "",
                        "name": "",
                        "microtenantId": "",
                        "microtenantName": "",
                        "enabled": "",
                        "dynamicDiscovery": "",
                        "description": "",
                        "configSpace": "",
                        "weight": "",
                        "passive": "",
                        "extranetEnabled": "",
                        "zpnErId": {
                            "id": "",
                            "modifiedTime": "",
                            "creationTime": "",
                            "modifiedBy": "",
                            "ziaErId": "",
                            "ziaErName": "",
                            "ziaCloud": "",
                            "ziaOrgId": "",
                            "ziaModifiedTime": ""
                        }
                    }
                ],
                "enabled": "",
                "passiveHealthEnabled": "",
                "tcpPortRanges": [],
                "udpPortRanges": [],
                "tcpPortRange": [
                    {
                        "from": "",
                        "to": ""
                    }
                ],
                "udpPortRange": [
                    {
                        "from": "",
                        "to": ""
                    }
                ],
                "doubleEncrypt": "",
                "segmentGroupId": "",
                "segmentGroupName": "",
                "configSpace": "",
                "bypassType": "",
                "healthCheckType": "",
                "icmpAccessType": "",
                "isCnameEnabled": "",
                "ipAnchored": "",
                "healthReporting": "",
                "tcpKeepAlive": "",
                "appRecommendationId": "",
                "selectConnectorCloseToApp": "",
                "sharedMicrotenantDetails": {
                    "sharedToMicrotenants": [
                        {
                            "id": "",
                            "name": ""
                        }
                    ],
                    "sharedFromMicrotenant": {
                        "id": "",
                        "name": ""
                    }
                },
                "inconsistentConfigDetails": {
                    "application": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "sraApplication": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "segmentGroup": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "serverGroup": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "appConnectorGroup": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "baCertificate": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "postureProfile": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "trustedNetwork": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "branchConnectorGroup": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "cloudConnectorGroup": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "samlAttributes": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "scimAttributes": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "machineGroup": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "idp": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "location": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "workloadTagGroup": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "userPortal": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ]
                },
                "fqdnDnsCheck": ""
            },
            "extDomain": "",
            "extLabel": "",
            "extDomainName": ""
        }
    ],
    "inspectionApps": [
        {
            "id": "",
            "name": "",
            "enabled": "",
            "description": "",
            "certificateId": "",
            "certificateName": "",
            "applicationPort": "",
            "applicationProtocol": "",
            "domain": "",
            "appId": "",
            "microtenantId": "",
            "microtenantName": "",
            "inconsistentConfigDetails": {
                "application": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "sraApplication": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "segmentGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "serverGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "appConnectorGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "baCertificate": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "postureProfile": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "trustedNetwork": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "branchConnectorGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "cloudConnectorGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "samlAttributes": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "scimAttributes": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "machineGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "idp": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "location": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "workloadTagGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "userPortal": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ]
            },
            "trustUntrustedCert": "",
            "appResource": {
                "modifiedTime": "",
                "creationTime": "",
                "modifiedBy": "",
                "id": "",
                "microtenantId": "",
                "microtenantName": "",
                "domainNames": [],
                "name": "",
                "description": "",
                "IdleTimeout": "",
                "MaxAge": "",
                "serverGroups": [
                    {
                        "id": "",
                        "modifiedTime": "",
                        "creationTime": "",
                        "modifiedBy": "",
                        "name": "",
                        "microtenantId": "",
                        "microtenantName": "",
                        "enabled": "",
                        "dynamicDiscovery": "",
                        "description": "",
                        "configSpace": "",
                        "weight": "",
                        "passive": "",
                        "extranetEnabled": "",
                        "zpnErId": {
                            "id": "",
                            "modifiedTime": "",
                            "creationTime": "",
                            "modifiedBy": "",
                            "ziaErId": "",
                            "ziaErName": "",
                            "ziaCloud": "",
                            "ziaOrgId": "",
                            "ziaModifiedTime": ""
                        }
                    }
                ],
                "enabled": "",
                "passiveHealthEnabled": "",
                "tcpPortRanges": [],
                "udpPortRanges": [],
                "tcpPortRange": [
                    {
                        "from": "",
                        "to": ""
                    }
                ],
                "udpPortRange": [
                    {
                        "from": "",
                        "to": ""
                    }
                ],
                "doubleEncrypt": "",
                "segmentGroupId": "",
                "segmentGroupName": "",
                "configSpace": "",
                "bypassType": "",
                "healthCheckType": "",
                "icmpAccessType": "",
                "isCnameEnabled": "",
                "ipAnchored": "",
                "healthReporting": "",
                "tcpKeepAlive": "",
                "appRecommendationId": "",
                "selectConnectorCloseToApp": "",
                "sharedMicrotenantDetails": {
                    "sharedToMicrotenants": [
                        {
                            "id": "",
                            "name": ""
                        }
                    ],
                    "sharedFromMicrotenant": {
                        "id": "",
                        "name": ""
                    }
                },
                "inconsistentConfigDetails": {
                    "application": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "sraApplication": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "segmentGroup": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "serverGroup": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "appConnectorGroup": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "baCertificate": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "postureProfile": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "trustedNetwork": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "branchConnectorGroup": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "cloudConnectorGroup": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "samlAttributes": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "scimAttributes": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "machineGroup": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "idp": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "location": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "workloadTagGroup": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "userPortal": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ]
                },
                "fqdnDnsCheck": ""
            },
            "protocols": []
        }
    ],
    "praApps": [
        {
            "id": "",
            "name": "",
            "enabled": "",
            "description": "",
            "certificateId": "",
            "certificateName": "",
            "applicationPort": "",
            "applicationProtocol": "",
            "domain": "",
            "appId": "",
            "microtenantId": "",
            "microtenantName": "",
            "inconsistentConfigDetails": {
                "application": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "sraApplication": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "segmentGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "serverGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "appConnectorGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "baCertificate": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "postureProfile": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "trustedNetwork": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "branchConnectorGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "cloudConnectorGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "samlAttributes": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "scimAttributes": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "machineGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "idp": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "location": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "workloadTagGroup": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ],
                "userPortal": [
                    {
                        "name": "",
                        "reason": ""
                    }
                ]
            },
            "hidden": "",
            "connectionSecurity": "",
            "appResource": {
                "modifiedTime": "",
                "creationTime": "",
                "modifiedBy": "",
                "id": "",
                "microtenantId": "",
                "microtenantName": "",
                "domainNames": [],
                "name": "",
                "description": "",
                "IdleTimeout": "",
                "MaxAge": "",
                "serverGroups": [
                    {
                        "id": "",
                        "modifiedTime": "",
                        "creationTime": "",
                        "modifiedBy": "",
                        "name": "",
                        "microtenantId": "",
                        "microtenantName": "",
                        "enabled": "",
                        "dynamicDiscovery": "",
                        "description": "",
                        "configSpace": "",
                        "weight": "",
                        "passive": "",
                        "extranetEnabled": "",
                        "zpnErId": {
                            "id": "",
                            "modifiedTime": "",
                            "creationTime": "",
                            "modifiedBy": "",
                            "ziaErId": "",
                            "ziaErName": "",
                            "ziaCloud": "",
                            "ziaOrgId": "",
                            "ziaModifiedTime": ""
                        }
                    }
                ],
                "enabled": "",
                "passiveHealthEnabled": "",
                "tcpPortRanges": [],
                "udpPortRanges": [],
                "tcpPortRange": [
                    {
                        "from": "",
                        "to": ""
                    }
                ],
                "udpPortRange": [
                    {
                        "from": "",
                        "to": ""
                    }
                ],
                "doubleEncrypt": "",
                "segmentGroupId": "",
                "segmentGroupName": "",
                "configSpace": "",
                "bypassType": "",
                "healthCheckType": "",
                "icmpAccessType": "",
                "isCnameEnabled": "",
                "ipAnchored": "",
                "healthReporting": "",
                "tcpKeepAlive": "",
                "appRecommendationId": "",
                "selectConnectorCloseToApp": "",
                "sharedMicrotenantDetails": {
                    "sharedToMicrotenants": [
                        {
                            "id": "",
                            "name": ""
                        }
                    ],
                    "sharedFromMicrotenant": {
                        "id": "",
                        "name": ""
                    }
                },
                "inconsistentConfigDetails": {
                    "application": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "sraApplication": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "segmentGroup": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "serverGroup": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "appConnectorGroup": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "baCertificate": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "postureProfile": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "trustedNetwork": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "branchConnectorGroup": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "cloudConnectorGroup": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "samlAttributes": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "scimAttributes": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "machineGroup": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "idp": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "location": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "workloadTagGroup": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ],
                    "userPortal": [
                        {
                            "name": "",
                            "reason": ""
                        }
                    ]
                },
                "fqdnDnsCheck": ""
            }
        }
    ],
    "commonAppsDto": {
        "appsConfig": [
            {
                "name": "",
                "baAppId": "",
                "inspectAppId": "",
                "praAppId": "",
                "enabled": "",
                "description": "",
                "certificateId": "",
                "certificateName": "",
                "applicationPort": "",
                "applicationProtocol": "",
                "connectionSecurity": "",
                "domain": "",
                "path": "",
                "hidden": "",
                "portal": "",
                "appId": "",
                "trustUntrustedCert": "",
                "allowOptions": "",
                "cname": "",
                "localDomain": "",
                "appTypes": [
                    "BROWSER_ACCESS"
                ],
                "protocols": [],
                "adpEnabled": "",
                "extDomain": "",
                "extLabel": ""
            }
        ],
        "deletedBaApps": [],
        "deletedInspectApps": [],
        "deletedPraApps": []
    },
    "ipAnchored": "",
    "bypassOnReauth": "",
    "inspectTrafficWithZia": "",
    "healthReporting": "",
    "useInDrMode": "",
    "tcpKeepAlive": "",
    "appRecommendationId": "",
    "selectConnectorCloseToApp": "",
    "sharedMicrotenantDetails": {
        "sharedToMicrotenants": [
            {
                "id": "",
                "name": ""
            }
        ],
        "sharedFromMicrotenant": {
            "id": "",
            "name": ""
        }
    },
    "inconsistentConfigDetails": {
        "application": [
            {
                "name": "",
                "reason": ""
            }
        ],
        "sraApplication": [
            {
                "name": "",
                "reason": ""
            }
        ],
        "segmentGroup": [
            {
                "name": "",
                "reason": ""
            }
        ],
        "serverGroup": [
            {
                "name": "",
                "reason": ""
            }
        ],
        "appConnectorGroup": [
            {
                "name": "",
                "reason": ""
            }
        ],
        "baCertificate": [
            {
                "name": "",
                "reason": ""
            }
        ],
        "postureProfile": [
            {
                "name": "",
                "reason": ""
            }
        ],
        "trustedNetwork": [
            {
                "name": "",
                "reason": ""
            }
        ],
        "branchConnectorGroup": [
            {
                "name": "",
                "reason": ""
            }
        ],
        "cloudConnectorGroup": [
            {
                "name": "",
                "reason": ""
            }
        ],
        "samlAttributes": [
            {
                "name": "",
                "reason": ""
            }
        ],
        "scimAttributes": [
            {
                "name": "",
                "reason": ""
            }
        ],
        "machineGroup": [
            {
                "name": "",
                "reason": ""
            }
        ],
        "idp": [
            {
                "name": "",
                "reason": ""
            }
        ],
        "location": [
            {
                "name": "",
                "reason": ""
            }
        ],
        "workloadTagGroup": [
            {
                "name": "",
                "reason": ""
            }
        ],
        "userPortal": [
            {
                "name": "",
                "reason": ""
            }
        ]
    },
    "matchStyle": "",
    "tcpProtocols": [],
    "udpProtocols": [],
    "isIncompleteDRConfig": "",
    "adpEnabled": "",
    "autoAppProtectEnabled": "",
    "apiProtectionEnabled": "",
    "fqdnDnsCheck": "",
    "weightedLoadBalancing": "",
    "extranetEnabled": "",
    "zpnErId": {
        "id": "",
        "modifiedTime": "",
        "creationTime": "",
        "modifiedBy": "",
        "ziaErId": "",
        "ziaErName": "",
        "ziaCloud": "",
        "ziaOrgId": "",
        "ziaModifiedTime": ""
    }
}</pre>

<h3>operation: Get Customer Certificates</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Customer ID</td><td>Specify the unique ZPA Tenant ID of the customer.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "totalPages": "",
    "list": [
        {
            "id": "",
            "modifiedTime": "",
            "creationTime": "",
            "modifiedBy": "",
            "name": "",
            "description": "",
            "cName": "",
            "validFromInEpochSec": "",
            "validToInEpochSec": "",
            "certificate": "",
            "issuedTo": "",
            "issuedBy": "",
            "serialNo": "",
            "publicKey": ""
        }
    ]
}</pre>

<h3>operation: Get All Issued Certificates</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Customer ID</td><td>Specify the unique ZPA Tenant ID of the customer.</td></tr>
<tr><td>Filter String</td><td>(Optional) Specify the search string for filtering the certificates. ex name LIKE client</td></tr>
<tr><td>Offset</td><td>(Optional) Specifies the number of records to skip before starting to return results. Used for paginating API responses in combination with the Limit.</td></tr>
<tr><td>Limit</td><td>(Optional) Specifies the page size, i.e., the maximum number of records to return for this action. If not provided, the default page size is 20. The maximum page size is 500.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "totalPages": "",
    "list": [
        {
            "id": "",
            "modifiedTime": "",
            "creationTime": "",
            "modifiedBy": "",
            "name": "",
            "description": "",
            "cName": "",
            "validFromInEpochSec": "",
            "validToInEpochSec": "",
            "certificate": "",
            "issuedTo": "",
            "issuedBy": "",
            "serialNo": "",
            "publicKey": ""
        }
    ]
}</pre>

<h3>operation: Get Certificate Details</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Customer ID</td><td>Specify the unique ZPA Tenant ID of the customer for whom the specific certificate is being returned.</td></tr>
<tr><td>Certificate ID</td><td>Specify the ID of the certificate for which you want to retrieve details.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "id": "",
    "modifiedTime": "",
    "creationTime": "",
    "modifiedBy": "",
    "name": "",
    "description": "",
    "cName": "",
    "validFromInEpochSec": "",
    "validToInEpochSec": "",
    "certificate": "",
    "issuedTo": "",
    "issuedBy": "",
    "serialNo": "",
    "publicKey": ""
}</pre>

<h3>operation: Execute an API Request</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Endpoint</td><td>Specify the REST API endpoint for the action to perform. Note: Do not include the host URL in the endpoint. ex /zpa/mgmtconfig/v1/admin/customers/{customerId}/policySet/policyType/{policyType} or /zpa/mgmtconfig/v1/admin/customers/{customerId}/application/{applicationId}.</td></tr>
<tr><td>Method</td><td>The HTTP Method to use</td></tr>
<tr><td>Query Parameters</td><td>(Optional) Specify the he Rest API query parameters object in JSON format.</td></tr>
<tr><td>Request Body/Payload</td><td>(Optional) The payload needed for the call. Use empty brackets if there is no payload.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains a non-dictionary value.</p>

<h2>Included playbooks</h2>

<p>The <code>Sample - Zscaler Private Access (ZPA) - 1.0.0</code> playbook collection comes bundled with the Zscaler Private Access (ZPA) connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the <strong>Automation</strong> &gt; <strong>Playbooks</strong> section in FortiSOAR&trade; after importing the Zscaler Private Access (ZPA) connector.</p>

<ul>
<li>Execute an API Request</li>
<li>Get All Configured Applications Segments</li>
<li>Get All Issued Certificates</li>
<li>Get Certificate Details</li>
<li>Get Customer Certificates</li>
<li>Get Specific Application Segment Details</li>
</ul>

<p><strong>Note</strong>: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.</p>
