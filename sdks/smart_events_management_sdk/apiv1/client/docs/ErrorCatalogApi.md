# smart_events_management_sdk.ErrorCatalogApi

All URIs are relative to *https://api.stage.openshift.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_error**](ErrorCatalogApi.md#get_error) | **GET** /api/smartevents_mgmt/v1/errors/{id} | Get an error from the error catalog.
[**get_errors**](ErrorCatalogApi.md#get_errors) | **GET** /api/smartevents_mgmt/v1/errors | Get the list of errors.


# **get_error**
> BridgeError get_error(id)

Get an error from the error catalog.

Get an error from the error catalog.

### Example


```python
import time
import smart_events_management_sdk
from smart_events_management_sdk.api import error_catalog_api
from smart_events_management_sdk.model.bridge_error import BridgeError
from smart_events_management_sdk.model.errors_list import ErrorsList
from pprint import pprint
# Defining the host is optional and defaults to https://api.stage.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = smart_events_management_sdk.Configuration(
    host = "https://api.stage.openshift.com"
)


# Enter a context with an instance of the API client
with smart_events_management_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = error_catalog_api.ErrorCatalogApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get an error from the error catalog.
        api_response = api_instance.get_error(id)
        pprint(api_response)
    except smart_events_management_sdk.ApiException as e:
        print("Exception when calling ErrorCatalogApi->get_error: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**BridgeError**](BridgeError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**500** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_errors**
> ErrorListResponse get_errors()

Get the list of errors.

Get the list of errors from the error catalog.

### Example


```python
import time
import smart_events_management_sdk
from smart_events_management_sdk.api import error_catalog_api
from smart_events_management_sdk.model.error_list_response import ErrorListResponse
from smart_events_management_sdk.model.errors_list import ErrorsList
from pprint import pprint
# Defining the host is optional and defaults to https://api.stage.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = smart_events_management_sdk.Configuration(
    host = "https://api.stage.openshift.com"
)


# Enter a context with an instance of the API client
with smart_events_management_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = error_catalog_api.ErrorCatalogApi(api_client)
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    size = 100 # int |  (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the list of errors.
        api_response = api_instance.get_errors(page=page, size=size)
        pprint(api_response)
    except smart_events_management_sdk.ApiException as e:
        print("Exception when calling ErrorCatalogApi->get_errors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] if omitted the server will use the default value of 0
 **size** | **int**|  | [optional] if omitted the server will use the default value of 100

### Return type

[**ErrorListResponse**](ErrorListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**500** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

