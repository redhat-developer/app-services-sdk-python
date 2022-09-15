# rhoas_service_registry_mgmt_sdk.RegistriesApi

All URIs are relative to *https://api.openshift.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_registry**](RegistriesApi.md#create_registry) | **POST** /api/serviceregistry_mgmt/v1/registries | 
[**delete_registry**](RegistriesApi.md#delete_registry) | **DELETE** /api/serviceregistry_mgmt/v1/registries/{id} | Delete a Registry instance
[**get_registries**](RegistriesApi.md#get_registries) | **GET** /api/serviceregistry_mgmt/v1/registries | 
[**get_registry**](RegistriesApi.md#get_registry) | **GET** /api/serviceregistry_mgmt/v1/registries/{id} | Get a Registry instance


# **create_registry**
> Registry create_registry(registry_create)



Create a new Registry instance

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_service_registry_mgmt_sdk
from rhoas_service_registry_mgmt_sdk.api import registries_api
from rhoas_service_registry_mgmt_sdk.model.registry_create import RegistryCreate
from rhoas_service_registry_mgmt_sdk.model.error import Error
from rhoas_service_registry_mgmt_sdk.model.registry import Registry
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_service_registry_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_service_registry_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with rhoas_service_registry_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = registries_api.RegistriesApi(api_client)
    registry_create = RegistryCreate(
        name="a1c2v7s6djuy1zmetozkhdomha1bae37b8ocvx8o53ow2eg7p6qw9qklp6l4y010fogx",
        description="description_example",
    ) # RegistryCreate | A new `Registry` instance to be created.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_registry(registry_create)
        pprint(api_response)
    except rhoas_service_registry_mgmt_sdk.ApiException as e:
        print("Exception when calling RegistriesApi->create_registry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_create** | [**RegistryCreate**](RegistryCreate.md)| A new &#x60;Registry&#x60; instance to be created. |

### Return type

[**Registry**](Registry.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. The full request to create a new &#x60;Registry&#x60; instance is processed asynchronously. The user should verify the result of the operation by reading the &#x60;status&#x60; property of the created &#x60;Registry&#x60; instance. |  -  |
**401** | Auth token is invalid. |  -  |
**403** | User is not authorized to access the service. |  -  |
**500** | Unexpected error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registry**
> delete_registry(id)

Delete a Registry instance

Deletes an existing `Registry` instance and all of the data that it stores. Important: Users should export the registry data before deleting the instance, e.g., using the Service Registry web console, core REST API, or `rhoas` CLI.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_service_registry_mgmt_sdk
from rhoas_service_registry_mgmt_sdk.api import registries_api
from rhoas_service_registry_mgmt_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_service_registry_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_service_registry_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with rhoas_service_registry_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = registries_api.RegistriesApi(api_client)
    id = "id_example" # str | A unique identifier for a `Registry` instance.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Registry instance
        api_instance.delete_registry(id)
    except rhoas_service_registry_mgmt_sdk.ApiException as e:
        print("Exception when calling RegistriesApi->delete_registry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique identifier for a &#x60;Registry&#x60; instance. |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful response. |  -  |
**401** | Auth token is invalid |  -  |
**403** | User is not authorized to access the service. |  -  |
**404** | No Service Registry instance with the specified id exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registries**
> RegistryList get_registries()



Get the list of all Registry instances

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_service_registry_mgmt_sdk
from rhoas_service_registry_mgmt_sdk.api import registries_api
from rhoas_service_registry_mgmt_sdk.model.registry_list import RegistryList
from rhoas_service_registry_mgmt_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_service_registry_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_service_registry_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with rhoas_service_registry_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = registries_api.RegistriesApi(api_client)
    page = 0 # int | Page index. (optional)
    size = 100 # int | Number of items in each page. (optional)
    order_by = "name asc" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement. Each query can be ordered by any of the request fields. For example, to retrieve all Registry instances ordered by their name:  ```sql name asc ```  Or to retrieve all Registry instances ordered by their name _and_ created date:  ```sql name asc, created_at asc ```  If the parameter isn't provided, or if the value is empty,  the results are ordered by name. (optional)
    search = "name = my-registry and status = AVAILABLE" # str | Search criteria.  The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement. Allowed fields in the search are: `name`, `status`. Allowed comparators are `=` or `LIKE`. Allowed joins are `AND` and `OR`, however there is a limit of max 10 joins in the search query.  Examples:  To retrieve a request with name equal `my-registry`, the value should be:  ``` name = my-registry  ```  To retrieve a request with its name starting with `my`, the value should be:  ``` name like my%25 ```  If the parameter isn't provided, or if the value is empty, all the Registry instances that the user has permission to see are returned.  Note: If the query is invalid, an error is returned.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_registries(page=page, size=size, order_by=order_by, search=search)
        pprint(api_response)
    except rhoas_service_registry_mgmt_sdk.ApiException as e:
        print("Exception when calling RegistriesApi->get_registries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page index. | [optional]
 **size** | **int**| Number of items in each page. | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement. Each query can be ordered by any of the request fields. For example, to retrieve all Registry instances ordered by their name:  &#x60;&#x60;&#x60;sql name asc &#x60;&#x60;&#x60;  Or to retrieve all Registry instances ordered by their name _and_ created date:  &#x60;&#x60;&#x60;sql name asc, created_at asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty,  the results are ordered by name. | [optional]
 **search** | **str**| Search criteria.  The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement. Allowed fields in the search are: &#x60;name&#x60;, &#x60;status&#x60;. Allowed comparators are &#x60;&#x3D;&#x60; or &#x60;LIKE&#x60;. Allowed joins are &#x60;AND&#x60; and &#x60;OR&#x60;, however there is a limit of max 10 joins in the search query.  Examples:  To retrieve a request with name equal &#x60;my-registry&#x60;, the value should be:  &#x60;&#x60;&#x60; name &#x3D; my-registry  &#x60;&#x60;&#x60;  To retrieve a request with its name starting with &#x60;my&#x60;, the value should be:  &#x60;&#x60;&#x60; name like my%25 &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, all the Registry instances that the user has permission to see are returned.  Note: If the query is invalid, an error is returned.  | [optional]

### Return type

[**RegistryList**](RegistryList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**401** | Auth token is invalid. |  -  |
**403** | User is not authorized to access the service. |  -  |
**500** | Unexpected error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registry**
> Registry get_registry(id)

Get a Registry instance

Gets the details of a single instance of a `Registry`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_service_registry_mgmt_sdk
from rhoas_service_registry_mgmt_sdk.api import registries_api
from rhoas_service_registry_mgmt_sdk.model.error import Error
from rhoas_service_registry_mgmt_sdk.model.registry import Registry
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_service_registry_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_service_registry_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with rhoas_service_registry_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = registries_api.RegistriesApi(api_client)
    id = "id_example" # str | A unique identifier for a `Registry` instance.

    # example passing only required values which don't have defaults set
    try:
        # Get a Registry instance
        api_response = api_instance.get_registry(id)
        pprint(api_response)
    except rhoas_service_registry_mgmt_sdk.ApiException as e:
        print("Exception when calling RegistriesApi->get_registry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique identifier for a &#x60;Registry&#x60; instance. |

### Return type

[**Registry**](Registry.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns a single &#x60;Registry&#x60; instance. |  -  |
**401** | Auth token is invalid. |  -  |
**403** | User is not authorized to access the service. |  -  |
**404** | No Service Registry instance with specified id exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

