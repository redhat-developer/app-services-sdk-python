# smart_events_management_sdk.SchemaCatalogApi

All URIs are relative to *https://api.stage.openshift.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_action_processor_schema**](SchemaCatalogApi.md#get_action_processor_schema) | **GET** /api/smartevents_mgmt/v1/schemas/actions/{id} | Get action processor schema
[**get_catalog**](SchemaCatalogApi.md#get_catalog) | **GET** /api/smartevents_mgmt/v1/schemas | Get processor catalog
[**get_source_processor_schema**](SchemaCatalogApi.md#get_source_processor_schema) | **GET** /api/smartevents_mgmt/v1/schemas/sources/{id} | Get source processor schema


# **get_action_processor_schema**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_action_processor_schema(id)

Get action processor schema

Get the action processor JSON schema.

### Example

* Bearer Authentication (bearer):

```python
import time
import smart_events_management_sdk
from smart_events_management_sdk.api import schema_catalog_api
from smart_events_management_sdk.model.errors_list import ErrorsList
from pprint import pprint
# Defining the host is optional and defaults to https://api.stage.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = smart_events_management_sdk.Configuration(
    host = "https://api.stage.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = smart_events_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with smart_events_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = schema_catalog_api.SchemaCatalogApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get action processor schema
        api_response = api_instance.get_action_processor_schema(id)
        pprint(api_response)
    except smart_events_management_sdk.ApiException as e:
        print("Exception when calling SchemaCatalogApi->get_action_processor_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**500** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog**
> ProcessorCatalogResponse get_catalog()

Get processor catalog

Get the processor catalog with all the available sources and actions.

### Example

* Bearer Authentication (bearer):

```python
import time
import smart_events_management_sdk
from smart_events_management_sdk.api import schema_catalog_api
from smart_events_management_sdk.model.processor_catalog_response import ProcessorCatalogResponse
from smart_events_management_sdk.model.errors_list import ErrorsList
from pprint import pprint
# Defining the host is optional and defaults to https://api.stage.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = smart_events_management_sdk.Configuration(
    host = "https://api.stage.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = smart_events_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with smart_events_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = schema_catalog_api.SchemaCatalogApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get processor catalog
        api_response = api_instance.get_catalog()
        pprint(api_response)
    except smart_events_management_sdk.ApiException as e:
        print("Exception when calling SchemaCatalogApi->get_catalog: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ProcessorCatalogResponse**](ProcessorCatalogResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**500** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_processor_schema**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_source_processor_schema(id)

Get source processor schema

Get the source processor JSON schema.

### Example

* Bearer Authentication (bearer):

```python
import time
import smart_events_management_sdk
from smart_events_management_sdk.api import schema_catalog_api
from smart_events_management_sdk.model.errors_list import ErrorsList
from pprint import pprint
# Defining the host is optional and defaults to https://api.stage.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = smart_events_management_sdk.Configuration(
    host = "https://api.stage.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = smart_events_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with smart_events_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = schema_catalog_api.SchemaCatalogApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get source processor schema
        api_response = api_instance.get_source_processor_schema(id)
        pprint(api_response)
    except smart_events_management_sdk.ApiException as e:
        print("Exception when calling SchemaCatalogApi->get_source_processor_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**500** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

