# dimakis_test_smart_events_mgmt_sdk.BridgesApi

All URIs are relative to *https://api.stage.openshift.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bridges_api_create_bridge**](BridgesApi.md#bridges_api_create_bridge) | **POST** /api/smartevents_mgmt/v1/bridges | Create a Bridge instance
[**bridges_api_delete_bridge**](BridgesApi.md#bridges_api_delete_bridge) | **DELETE** /api/smartevents_mgmt/v1/bridges/{bridgeId} | Delete a Bridge instance
[**bridges_api_get_bridge**](BridgesApi.md#bridges_api_get_bridge) | **GET** /api/smartevents_mgmt/v1/bridges/{bridgeId} | Get a Bridge instance
[**bridges_api_get_bridges**](BridgesApi.md#bridges_api_get_bridges) | **GET** /api/smartevents_mgmt/v1/bridges | Get the list of Bridge instances
[**bridges_api_update_bridge**](BridgesApi.md#bridges_api_update_bridge) | **PUT** /api/smartevents_mgmt/v1/bridges/{bridgeId} | Update a Bridge instance


# **bridges_api_create_bridge**
> BridgeResponse bridges_api_create_bridge()

Create a Bridge instance

Create a Bridge instance for the authenticated user.

### Example

* Bearer Authentication (bearer):

```python
import time
import dimakis_test_smart_events_mgmt_sdk
from dimakis_test_smart_events_mgmt_sdk.api import bridges_api
from dimakis_test_smart_events_mgmt_sdk.model.bridge_response import BridgeResponse
from dimakis_test_smart_events_mgmt_sdk.model.errors_list import ErrorsList
from dimakis_test_smart_events_mgmt_sdk.model.bridge_request import BridgeRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.stage.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dimakis_test_smart_events_mgmt_sdk.Configuration(
    host = "https://api.stage.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = dimakis_test_smart_events_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with dimakis_test_smart_events_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bridges_api.BridgesApi(api_client)
    bridge_request = BridgeRequest(
        name="name_example",
        error_handler=Action(
            type="type_example",
            parameters={},
        ),
        cloud_provider="cloud_provider_example",
        region="region_example",
    ) # BridgeRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Bridge instance
        api_response = api_instance.bridges_api_create_bridge(bridge_request=bridge_request)
        pprint(api_response)
    except dimakis_test_smart_events_mgmt_sdk.ApiException as e:
        print("Exception when calling BridgesApi->bridges_api_create_bridge: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_request** | [**BridgeRequest**](BridgeRequest.md)|  | [optional]

### Return type

[**BridgeResponse**](BridgeResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**500** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bridges_api_delete_bridge**
> bridges_api_delete_bridge(bridge_id)

Delete a Bridge instance

Delete a Bridge instance of the authenticated user by ID.

### Example

* Bearer Authentication (bearer):

```python
import time
import dimakis_test_smart_events_mgmt_sdk
from dimakis_test_smart_events_mgmt_sdk.api import bridges_api
from dimakis_test_smart_events_mgmt_sdk.model.errors_list import ErrorsList
from pprint import pprint
# Defining the host is optional and defaults to https://api.stage.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dimakis_test_smart_events_mgmt_sdk.Configuration(
    host = "https://api.stage.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = dimakis_test_smart_events_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with dimakis_test_smart_events_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bridges_api.BridgesApi(api_client)
    bridge_id = "bridgeId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a Bridge instance
        api_instance.bridges_api_delete_bridge(bridge_id)
    except dimakis_test_smart_events_mgmt_sdk.ApiException as e:
        print("Exception when calling BridgesApi->bridges_api_delete_bridge: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not found. |  -  |
**500** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bridges_api_get_bridge**
> BridgeResponse bridges_api_get_bridge(bridge_id)

Get a Bridge instance

Get a Bridge instance of the authenticated user by ID.

### Example

* Bearer Authentication (bearer):

```python
import time
import dimakis_test_smart_events_mgmt_sdk
from dimakis_test_smart_events_mgmt_sdk.api import bridges_api
from dimakis_test_smart_events_mgmt_sdk.model.bridge_response import BridgeResponse
from dimakis_test_smart_events_mgmt_sdk.model.errors_list import ErrorsList
from pprint import pprint
# Defining the host is optional and defaults to https://api.stage.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dimakis_test_smart_events_mgmt_sdk.Configuration(
    host = "https://api.stage.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = dimakis_test_smart_events_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with dimakis_test_smart_events_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bridges_api.BridgesApi(api_client)
    bridge_id = "bridgeId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a Bridge instance
        api_response = api_instance.bridges_api_get_bridge(bridge_id)
        pprint(api_response)
    except dimakis_test_smart_events_mgmt_sdk.ApiException as e:
        print("Exception when calling BridgesApi->bridges_api_get_bridge: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**|  |

### Return type

[**BridgeResponse**](BridgeResponse.md)

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
**404** | Not found. |  -  |
**500** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bridges_api_get_bridges**
> BridgeListResponse bridges_api_get_bridges()

Get the list of Bridge instances

Get the list of Bridge instances for the authenticated user.

### Example

* Bearer Authentication (bearer):

```python
import time
import dimakis_test_smart_events_mgmt_sdk
from dimakis_test_smart_events_mgmt_sdk.api import bridges_api
from dimakis_test_smart_events_mgmt_sdk.model.errors_list import ErrorsList
from dimakis_test_smart_events_mgmt_sdk.model.bridge_list_response import BridgeListResponse
from dimakis_test_smart_events_mgmt_sdk.model.managed_resource_status import ManagedResourceStatus
from pprint import pprint
# Defining the host is optional and defaults to https://api.stage.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dimakis_test_smart_events_mgmt_sdk.Configuration(
    host = "https://api.stage.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = dimakis_test_smart_events_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with dimakis_test_smart_events_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bridges_api.BridgesApi(api_client)
    name = "name_example" # str |  (optional)
    page = 0 # int |  (optional) if omitted the server will use the default value of 0
    size = 100 # int |  (optional) if omitted the server will use the default value of 100
    status = [
        ManagedResourceStatus("accepted"),
    ] # [ManagedResourceStatus] |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the list of Bridge instances
        api_response = api_instance.bridges_api_get_bridges(name=name, page=page, size=size, status=status)
        pprint(api_response)
    except dimakis_test_smart_events_mgmt_sdk.ApiException as e:
        print("Exception when calling BridgesApi->bridges_api_get_bridges: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional]
 **page** | **int**|  | [optional] if omitted the server will use the default value of 0
 **size** | **int**|  | [optional] if omitted the server will use the default value of 100
 **status** | [**[ManagedResourceStatus]**](ManagedResourceStatus.md)|  | [optional]

### Return type

[**BridgeListResponse**](BridgeListResponse.md)

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
**404** | Not found. |  -  |
**500** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bridges_api_update_bridge**
> BridgeResponse bridges_api_update_bridge(bridge_id)

Update a Bridge instance

Update a Bridge instance for the authenticated user.

### Example

* Bearer Authentication (bearer):

```python
import time
import dimakis_test_smart_events_mgmt_sdk
from dimakis_test_smart_events_mgmt_sdk.api import bridges_api
from dimakis_test_smart_events_mgmt_sdk.model.bridge_response import BridgeResponse
from dimakis_test_smart_events_mgmt_sdk.model.errors_list import ErrorsList
from dimakis_test_smart_events_mgmt_sdk.model.bridge_request import BridgeRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.stage.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dimakis_test_smart_events_mgmt_sdk.Configuration(
    host = "https://api.stage.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = dimakis_test_smart_events_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with dimakis_test_smart_events_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bridges_api.BridgesApi(api_client)
    bridge_id = "bridgeId_example" # str | 
    bridge_request = BridgeRequest(
        name="name_example",
        error_handler=Action(
            type="type_example",
            parameters={},
        ),
        cloud_provider="cloud_provider_example",
        region="region_example",
    ) # BridgeRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Bridge instance
        api_response = api_instance.bridges_api_update_bridge(bridge_id)
        pprint(api_response)
    except dimakis_test_smart_events_mgmt_sdk.ApiException as e:
        print("Exception when calling BridgesApi->bridges_api_update_bridge: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Bridge instance
        api_response = api_instance.bridges_api_update_bridge(bridge_id, bridge_request=bridge_request)
        pprint(api_response)
    except dimakis_test_smart_events_mgmt_sdk.ApiException as e:
        print("Exception when calling BridgesApi->bridges_api_update_bridge: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**|  |
 **bridge_request** | [**BridgeRequest**](BridgeRequest.md)|  | [optional]

### Return type

[**BridgeResponse**](BridgeResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not found. |  -  |
**500** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

