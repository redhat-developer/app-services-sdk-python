# smart_events_management_sdk.CloudProvidersApi

All URIs are relative to *https://api.stage.openshift.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cloud_provider**](CloudProvidersApi.md#get_cloud_provider) | **GET** /api/smartevents_mgmt/v1/cloud_providers/{id} | Get Cloud Provider.
[**list_cloud_provider_regions**](CloudProvidersApi.md#list_cloud_provider_regions) | **GET** /api/smartevents_mgmt/v1/cloud_providers/{id}/regions | List Supported Cloud Regions.
[**list_cloud_providers**](CloudProvidersApi.md#list_cloud_providers) | **GET** /api/smartevents_mgmt/v1/cloud_providers | List Supported Cloud Providers.


# **get_cloud_provider**
> CloudProviderListResponse get_cloud_provider(id)

Get Cloud Provider.

Get details of the Cloud Provider specified by id.

### Example


```python
import time
import smart_events_management_sdk
from smart_events_management_sdk.api import cloud_providers_api
from smart_events_management_sdk.model.cloud_provider_list_response import CloudProviderListResponse
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
    api_instance = cloud_providers_api.CloudProvidersApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Cloud Provider.
        api_response = api_instance.get_cloud_provider(id)
        pprint(api_response)
    except smart_events_management_sdk.ApiException as e:
        print("Exception when calling CloudProvidersApi->get_cloud_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**CloudProviderListResponse**](CloudProviderListResponse.md)

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
**404** | Not found. |  -  |
**500** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloud_provider_regions**
> CloudRegionListResponse list_cloud_provider_regions(id)

List Supported Cloud Regions.

Returns the list of supported Regions of the specified Cloud Provider.

### Example


```python
import time
import smart_events_management_sdk
from smart_events_management_sdk.api import cloud_providers_api
from smart_events_management_sdk.model.cloud_region_list_response import CloudRegionListResponse
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
    api_instance = cloud_providers_api.CloudProvidersApi(api_client)
    id = "id_example" # str | 
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    size = 100 # int |  (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    try:
        # List Supported Cloud Regions.
        api_response = api_instance.list_cloud_provider_regions(id)
        pprint(api_response)
    except smart_events_management_sdk.ApiException as e:
        print("Exception when calling CloudProvidersApi->list_cloud_provider_regions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Supported Cloud Regions.
        api_response = api_instance.list_cloud_provider_regions(id, page=page, size=size)
        pprint(api_response)
    except smart_events_management_sdk.ApiException as e:
        print("Exception when calling CloudProvidersApi->list_cloud_provider_regions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **page** | **int**|  | [optional] if omitted the server will use the default value of 0
 **size** | **int**|  | [optional] if omitted the server will use the default value of 100

### Return type

[**CloudRegionListResponse**](CloudRegionListResponse.md)

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
**500** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloud_providers**
> CloudProviderListResponse list_cloud_providers()

List Supported Cloud Providers.

Returns the list of supported Cloud Providers.

### Example


```python
import time
import smart_events_management_sdk
from smart_events_management_sdk.api import cloud_providers_api
from smart_events_management_sdk.model.cloud_provider_list_response import CloudProviderListResponse
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
    api_instance = cloud_providers_api.CloudProvidersApi(api_client)
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    size = 100 # int |  (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Supported Cloud Providers.
        api_response = api_instance.list_cloud_providers(page=page, size=size)
        pprint(api_response)
    except smart_events_management_sdk.ApiException as e:
        print("Exception when calling CloudProvidersApi->list_cloud_providers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] if omitted the server will use the default value of 0
 **size** | **int**|  | [optional] if omitted the server will use the default value of 100

### Return type

[**CloudProviderListResponse**](CloudProviderListResponse.md)

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
**500** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

