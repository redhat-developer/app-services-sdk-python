# rhoas_connector_mgmt_sdk.ConnectorServiceApi

All URIs are relative to *https://api.openshift.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_version_metadata**](ConnectorServiceApi.md#get_version_metadata) | **GET** /api/connector_mgmt/v1 | Returns the version metadata


# **get_version_metadata**
> VersionMetadata get_version_metadata()

Returns the version metadata

Returns the version metadata

### Example


```python
import time
import rhoas_connector_mgmt_sdk
from rhoas_connector_mgmt_sdk.api import connector_service_api
from rhoas_connector_mgmt_sdk.model.version_metadata import VersionMetadata
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_connector_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)


# Enter a context with an instance of the API client
with rhoas_connector_mgmt_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = connector_service_api.ConnectorServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns the version metadata
        api_response = api_instance.get_version_metadata()
        pprint(api_response)
    except rhoas_connector_mgmt_sdk.ApiException as e:
        print("Exception when calling ConnectorServiceApi->get_version_metadata: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionMetadata**](VersionMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Version metadata |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

