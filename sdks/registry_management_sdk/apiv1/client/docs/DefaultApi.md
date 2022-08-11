# registry_management_sdk.DefaultApi

All URIs are relative to *https://api.openshift.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service_status**](DefaultApi.md#get_service_status) | **GET** /api/serviceregistry_mgmt/v1/status | 


# **get_service_status**
> ServiceStatus get_service_status()



Get the service status

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import registry_management_sdk
from registry_management_sdk.api import default_api
from registry_management_sdk.model.service_status import ServiceStatus
from registry_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = registry_management_sdk.Configuration(
    host = "https://api.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = registry_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with registry_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_service_status()
        pprint(api_response)
    except registry_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_service_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceStatus**](ServiceStatus.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned service status. |  -  |
**500** | Internal error retrieving service status. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
