# rhoas_kafka_instance_sdk.AclsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_acl**](AclsApi.md#create_acl) | **POST** /api/v1/acls | Create ACL binding
[**delete_acls**](AclsApi.md#delete_acls) | **DELETE** /api/v1/acls | Delete ACL bindings
[**get_acl_resource_operations**](AclsApi.md#get_acl_resource_operations) | **GET** /api/v1/acls/resource-operations | Retrieve allowed ACL resources and operations
[**get_acls**](AclsApi.md#get_acls) | **GET** /api/v1/acls | List ACL bindings


# **create_acl**
> create_acl(acl_binding)

Create ACL binding

Creates a new ACL binding for a Kafka instance.

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth2):

```python
import time
import rhoas_kafka_instance_sdk
from rhoas_kafka_instance_sdk.api import acls_api
from rhoas_kafka_instance_sdk.model.acl_binding import AclBinding
from rhoas_kafka_instance_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_kafka_instance_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_kafka_instance_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure OAuth2 access token for authorization: OAuth2
configuration = rhoas_kafka_instance_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with rhoas_kafka_instance_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = acls_api.AclsApi(api_client)
    acl_binding = AclBinding(None) # AclBinding | ACL to create.

    # example passing only required values which don't have defaults set
    try:
        # Create ACL binding
        api_instance.create_acl(acl_binding)
    except rhoas_kafka_instance_sdk.ApiException as e:
        print("Exception when calling AclsApi->create_acl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acl_binding** | [**AclBinding**](AclBinding.md)| ACL to create. |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ACL created successfully. |  -  |
**400** | The client request was invalid. One or more request parameters or the request body was rejected. Additional information may be found in the response. |  -  |
**401** | Request authentication missing or invalid |  -  |
**403** | User is not authorized to access requested resource |  -  |
**500** | Internal server error |  -  |
**503** | Kafka service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_acls**
> AclBindingListPage delete_acls()

Delete ACL bindings

Deletes ACL bindings that match the query parameters.

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth2):

```python
import time
import rhoas_kafka_instance_sdk
from rhoas_kafka_instance_sdk.api import acls_api
from rhoas_kafka_instance_sdk.model.acl_binding_list_page import AclBindingListPage
from rhoas_kafka_instance_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_kafka_instance_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_kafka_instance_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure OAuth2 access token for authorization: OAuth2
configuration = rhoas_kafka_instance_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with rhoas_kafka_instance_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = acls_api.AclsApi(api_client)
    resource_type = None # bool, date, datetime, dict, float, int, list, str, none_type | ACL Resource Type Filter (optional)
    resource_name = "resourceName_example" # str | ACL Resource Name Filter (optional)
    pattern_type = None # bool, date, datetime, dict, float, int, list, str, none_type | ACL Pattern Type Filter (optional)
    principal = "User:*" # str | ACL Principal Filter. Either a specific user or the wildcard user `User:*` may be provided. - When fetching by a specific user, the results will also include ACL bindings that apply to all users. - When deleting, ACL bindings to be delete must match the provided `principal` exactly. (optional) if omitted the server will use the default value of ""
    operation = None # bool, date, datetime, dict, float, int, list, str, none_type | ACL Operation Filter. The ACL binding operation provided should be valid for the resource type in the request, if not `ANY`. (optional)
    permission = None # bool, date, datetime, dict, float, int, list, str, none_type | ACL Permission Type Filter (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete ACL bindings
        api_response = api_instance.delete_acls(resource_type=resource_type, resource_name=resource_name, pattern_type=pattern_type, principal=principal, operation=operation, permission=permission)
        pprint(api_response)
    except rhoas_kafka_instance_sdk.ApiException as e:
        print("Exception when calling AclsApi->delete_acls: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **bool, date, datetime, dict, float, int, list, str, none_type**| ACL Resource Type Filter | [optional]
 **resource_name** | **str**| ACL Resource Name Filter | [optional]
 **pattern_type** | **bool, date, datetime, dict, float, int, list, str, none_type**| ACL Pattern Type Filter | [optional]
 **principal** | **str**| ACL Principal Filter. Either a specific user or the wildcard user &#x60;User:*&#x60; may be provided. - When fetching by a specific user, the results will also include ACL bindings that apply to all users. - When deleting, ACL bindings to be delete must match the provided &#x60;principal&#x60; exactly. | [optional] if omitted the server will use the default value of ""
 **operation** | **bool, date, datetime, dict, float, int, list, str, none_type**| ACL Operation Filter. The ACL binding operation provided should be valid for the resource type in the request, if not &#x60;ANY&#x60;. | [optional]
 **permission** | **bool, date, datetime, dict, float, int, list, str, none_type**| ACL Permission Type Filter | [optional]

### Return type

[**AclBindingListPage**](AclBindingListPage.md)

### Authorization

[Bearer](../README.md#Bearer), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | The client request was invalid. One or more request parameters or the request body was rejected. Additional information may be found in the response. |  -  |
**401** | Request authentication missing or invalid |  -  |
**403** | User is not authorized to access requested resource |  -  |
**500** | Internal server error |  -  |
**503** | Kafka service unavailable |  -  |
**200** | List of all ACL bindings matching the query parameters that were deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_acl_resource_operations**
> {str: ([str],)} get_acl_resource_operations()

Retrieve allowed ACL resources and operations

Retrieve the resources and associated operations that may have ACLs configured.

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth2):

```python
import time
import rhoas_kafka_instance_sdk
from rhoas_kafka_instance_sdk.api import acls_api
from rhoas_kafka_instance_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_kafka_instance_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_kafka_instance_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure OAuth2 access token for authorization: OAuth2
configuration = rhoas_kafka_instance_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with rhoas_kafka_instance_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = acls_api.AclsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve allowed ACL resources and operations
        api_response = api_instance.get_acl_resource_operations()
        pprint(api_response)
    except rhoas_kafka_instance_sdk.ApiException as e:
        print("Exception when calling AclsApi->get_acl_resource_operations: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: ([str],)}**

### Authorization

[Bearer](../README.md#Bearer), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Map of allowed resources and operations for ACL creation |  -  |
**401** | Request authentication missing or invalid |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_acls**
> AclBindingListPage get_acls()

List ACL bindings

Returns a list of all of the available ACL bindings, or the list of bindings that meet the user's URL query parameters. If no parameters are specified, all ACL bindings known to the system will be returned (with paging).

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth2):

```python
import time
import rhoas_kafka_instance_sdk
from rhoas_kafka_instance_sdk.api import acls_api
from rhoas_kafka_instance_sdk.model.sort_direction import SortDirection
from rhoas_kafka_instance_sdk.model.acl_binding_list_page import AclBindingListPage
from rhoas_kafka_instance_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_kafka_instance_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_kafka_instance_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure OAuth2 access token for authorization: OAuth2
configuration = rhoas_kafka_instance_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with rhoas_kafka_instance_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = acls_api.AclsApi(api_client)
    resource_type = None # bool, date, datetime, dict, float, int, list, str, none_type | ACL Resource Type Filter (optional)
    resource_name = "resourceName_example" # str | ACL Resource Name Filter (optional)
    pattern_type = None # bool, date, datetime, dict, float, int, list, str, none_type | ACL Pattern Type Filter (optional)
    principal = "User:*" # str | ACL Principal Filter. Either a specific user or the wildcard user `User:*` may be provided. - When fetching by a specific user, the results will also include ACL bindings that apply to all users. - When deleting, ACL bindings to be delete must match the provided `principal` exactly. (optional) if omitted the server will use the default value of ""
    operation = None # bool, date, datetime, dict, float, int, list, str, none_type | ACL Operation Filter. The ACL binding operation provided should be valid for the resource type in the request, if not `ANY`. (optional)
    permission = None # bool, date, datetime, dict, float, int, list, str, none_type | ACL Permission Type Filter (optional)
    page = 1 # int | Page number (optional)
    size = 1 # int | Number of records per page (optional)
    order = SortDirection("asc") # SortDirection | Order items are sorted (optional)
    order_key = None # bool, date, datetime, dict, float, int, list, str, none_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List ACL bindings
        api_response = api_instance.get_acls(resource_type=resource_type, resource_name=resource_name, pattern_type=pattern_type, principal=principal, operation=operation, permission=permission, page=page, size=size, order=order, order_key=order_key)
        pprint(api_response)
    except rhoas_kafka_instance_sdk.ApiException as e:
        print("Exception when calling AclsApi->get_acls: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **bool, date, datetime, dict, float, int, list, str, none_type**| ACL Resource Type Filter | [optional]
 **resource_name** | **str**| ACL Resource Name Filter | [optional]
 **pattern_type** | **bool, date, datetime, dict, float, int, list, str, none_type**| ACL Pattern Type Filter | [optional]
 **principal** | **str**| ACL Principal Filter. Either a specific user or the wildcard user &#x60;User:*&#x60; may be provided. - When fetching by a specific user, the results will also include ACL bindings that apply to all users. - When deleting, ACL bindings to be delete must match the provided &#x60;principal&#x60; exactly. | [optional] if omitted the server will use the default value of ""
 **operation** | **bool, date, datetime, dict, float, int, list, str, none_type**| ACL Operation Filter. The ACL binding operation provided should be valid for the resource type in the request, if not &#x60;ANY&#x60;. | [optional]
 **permission** | **bool, date, datetime, dict, float, int, list, str, none_type**| ACL Permission Type Filter | [optional]
 **page** | **int**| Page number | [optional]
 **size** | **int**| Number of records per page | [optional]
 **order** | **SortDirection**| Order items are sorted | [optional]
 **order_key** | **bool, date, datetime, dict, float, int, list, str, none_type**|  | [optional]

### Return type

[**AclBindingListPage**](AclBindingListPage.md)

### Authorization

[Bearer](../README.md#Bearer), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | The client request was invalid. One or more request parameters or the request body was rejected. Additional information may be found in the response. |  -  |
**401** | Request authentication missing or invalid |  -  |
**403** | User is not authorized to access requested resource |  -  |
**500** | Internal server error |  -  |
**503** | Kafka service unavailable |  -  |
**200** | List of ACL bindings matching the query parameters. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

