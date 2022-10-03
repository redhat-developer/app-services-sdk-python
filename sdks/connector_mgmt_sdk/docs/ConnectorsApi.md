# rhoas_connector_mgmt_sdk.ConnectorsApi

All URIs are relative to *https://api.openshift.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connector**](ConnectorsApi.md#create_connector) | **POST** /api/connector_mgmt/v1/kafka_connectors | Create a new connector
[**delete_connector**](ConnectorsApi.md#delete_connector) | **DELETE** /api/connector_mgmt/v1/kafka_connectors/{id} | Delete a connector
[**get_connector**](ConnectorsApi.md#get_connector) | **GET** /api/connector_mgmt/v1/kafka_connectors/{id} | Get a connector
[**list_connectors**](ConnectorsApi.md#list_connectors) | **GET** /api/connector_mgmt/v1/kafka_connectors | Returns a list of connector types
[**patch_connector**](ConnectorsApi.md#patch_connector) | **PATCH** /api/connector_mgmt/v1/kafka_connectors/{id} | Patch a connector


# **create_connector**
> Connector create_connector(_async, connector_request)

Create a new connector

Create a new connector

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_connector_mgmt_sdk
from rhoas_connector_mgmt_sdk.api import connectors_api
from rhoas_connector_mgmt_sdk.model.connector import Connector
from rhoas_connector_mgmt_sdk.model.error import Error
from rhoas_connector_mgmt_sdk.model.connector_request import ConnectorRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_connector_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_connector_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with rhoas_connector_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectors_api.ConnectorsApi(api_client)
    _async = True # bool | Perform the action in an asynchronous manner
    connector_request = ConnectorRequest(None) # ConnectorRequest | Connector data

    # example passing only required values which don't have defaults set
    try:
        # Create a new connector
        api_response = api_instance.create_connector(_async, connector_request)
        pprint(api_response)
    except rhoas_connector_mgmt_sdk.ApiException as e:
        print("Exception when calling ConnectorsApi->create_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_async** | **bool**| Perform the action in an asynchronous manner |
 **connector_request** | [**ConnectorRequest**](ConnectorRequest.md)| Connector data |

### Return type

[**Connector**](Connector.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**404** | The requested resource doesn&#39;t exist |  -  |
**500** | An unexpected error occurred creating the connector |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connector**
> Error delete_connector(id)

Delete a connector

Delete a connector

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_connector_mgmt_sdk
from rhoas_connector_mgmt_sdk.api import connectors_api
from rhoas_connector_mgmt_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_connector_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_connector_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with rhoas_connector_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectors_api.ConnectorsApi(api_client)
    id = "id_example" # str | The ID of record

    # example passing only required values which don't have defaults set
    try:
        # Delete a connector
        api_response = api_instance.delete_connector(id)
        pprint(api_response)
    except rhoas_connector_mgmt_sdk.ApiException as e:
        print("Exception when calling ConnectorsApi->delete_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of record |

### Return type

[**Error**](Error.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deleted |  -  |
**401** | Auth token is invalid |  -  |
**404** | No kafka request with specified ID exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connector**
> Connector get_connector(id)

Get a connector

Get a connector

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_connector_mgmt_sdk
from rhoas_connector_mgmt_sdk.api import connectors_api
from rhoas_connector_mgmt_sdk.model.connector import Connector
from rhoas_connector_mgmt_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_connector_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_connector_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with rhoas_connector_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectors_api.ConnectorsApi(api_client)
    id = "id_example" # str | The ID of record

    # example passing only required values which don't have defaults set
    try:
        # Get a connector
        api_response = api_instance.get_connector(id)
        pprint(api_response)
    except rhoas_connector_mgmt_sdk.ApiException as e:
        print("Exception when calling ConnectorsApi->get_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of record |

### Return type

[**Connector**](Connector.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The connector matching the request |  -  |
**401** | Auth token is invalid |  -  |
**404** | No matching connector exists |  -  |
**410** | The requested resource doesn&#39;t exist anymore |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connectors**
> ConnectorList list_connectors()

Returns a list of connector types

Returns a list of connector types

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_connector_mgmt_sdk
from rhoas_connector_mgmt_sdk.api import connectors_api
from rhoas_connector_mgmt_sdk.model.error import Error
from rhoas_connector_mgmt_sdk.model.connector_list import ConnectorList
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_connector_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_connector_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with rhoas_connector_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectors_api.ConnectorsApi(api_client)
    page = "1" # str | Page index (optional)
    size = "100" # str | Number of items in each page (optional)
    order_by = "name asc" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the `order by` clause of an SQL statement. Each query can be ordered by any of the underlying resource fields supported in the search parameter. For example, to return all Connector types ordered by their name, use the following syntax:  ```sql name asc ```  To return all Connector types ordered by their name _and_ version, use the following syntax:  ```sql name asc, version asc ```  If the parameter isn't provided, or if the value is empty, then the results are ordered by name. (optional)
    search = "name = aws-sqs-source and channel = stable" # str | Search criteria.  The syntax of this parameter is similar to the syntax of the `where` clause of a SQL statement.  Allowed fields in the search depend on the resource type:  * Cluster: id, created_at, updated_at, owner, organisation_id, name, state, client_id * Namespace: id, created_at, updated_at, name, cluster_id, owner, expiration, tenant_user_id, tenant_organisation_id, state * Connector Types: id, created_at, updated_at, version, name, description, label, channel, featured_rank * Connectors: id, created_at, updated_at, name, owner, organisation_id, connector_type_id, desired_state, state, channel, namespace_id, kafka_id, kafka_bootstrap_server, service_account_client_id, schema_registry_id, schema_registry_url  Allowed operators are `<>`, `=`, `LIKE`, or `ILIKE`. Allowed conjunctive operators are `AND` and `OR`. However, you can use a maximum of 10 conjunctions in a search query.  Examples:  To return a Connector Type with the name `aws-sqs-source` and the channel `stable`, use the following syntax:  ``` name = aws-sqs-source and channel = stable ```[p-]  To return a connector instance with a name that starts with `aws`, use the following syntax:  ``` name like aws%25 ```  To return a connector type with a name containing `aws` matching any character case combination, use the following syntax:  ``` name ilike %25aws%25 ```  If the parameter isn't provided, or if the value is empty, then all the resources that the user has permission to see are returned.  Note. If the query is invalid, an error is returned.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of connector types
        api_response = api_instance.list_connectors(page=page, size=size, order_by=order_by, search=search)
        pprint(api_response)
    except rhoas_connector_mgmt_sdk.ApiException as e:
        print("Exception when calling ConnectorsApi->list_connectors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| Page index | [optional]
 **size** | **str**| Number of items in each page | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the &#x60;order by&#x60; clause of an SQL statement. Each query can be ordered by any of the underlying resource fields supported in the search parameter. For example, to return all Connector types ordered by their name, use the following syntax:  &#x60;&#x60;&#x60;sql name asc &#x60;&#x60;&#x60;  To return all Connector types ordered by their name _and_ version, use the following syntax:  &#x60;&#x60;&#x60;sql name asc, version asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then the results are ordered by name. | [optional]
 **search** | **str**| Search criteria.  The syntax of this parameter is similar to the syntax of the &#x60;where&#x60; clause of a SQL statement.  Allowed fields in the search depend on the resource type:  * Cluster: id, created_at, updated_at, owner, organisation_id, name, state, client_id * Namespace: id, created_at, updated_at, name, cluster_id, owner, expiration, tenant_user_id, tenant_organisation_id, state * Connector Types: id, created_at, updated_at, version, name, description, label, channel, featured_rank * Connectors: id, created_at, updated_at, name, owner, organisation_id, connector_type_id, desired_state, state, channel, namespace_id, kafka_id, kafka_bootstrap_server, service_account_client_id, schema_registry_id, schema_registry_url  Allowed operators are &#x60;&lt;&gt;&#x60;, &#x60;&#x3D;&#x60;, &#x60;LIKE&#x60;, or &#x60;ILIKE&#x60;. Allowed conjunctive operators are &#x60;AND&#x60; and &#x60;OR&#x60;. However, you can use a maximum of 10 conjunctions in a search query.  Examples:  To return a Connector Type with the name &#x60;aws-sqs-source&#x60; and the channel &#x60;stable&#x60;, use the following syntax:  &#x60;&#x60;&#x60; name &#x3D; aws-sqs-source and channel &#x3D; stable &#x60;&#x60;&#x60;[p-]  To return a connector instance with a name that starts with &#x60;aws&#x60;, use the following syntax:  &#x60;&#x60;&#x60; name like aws%25 &#x60;&#x60;&#x60;  To return a connector type with a name containing &#x60;aws&#x60; matching any character case combination, use the following syntax:  &#x60;&#x60;&#x60; name ilike %25aws%25 &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the resources that the user has permission to see are returned.  Note. If the query is invalid, an error is returned.  | [optional]

### Return type

[**ConnectorList**](ConnectorList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of connectors |  -  |
**401** | Auth token is invalid |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_connector**
> Connector patch_connector(id, body)

Patch a connector

Patch a connector

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_connector_mgmt_sdk
from rhoas_connector_mgmt_sdk.api import connectors_api
from rhoas_connector_mgmt_sdk.model.connector import Connector
from rhoas_connector_mgmt_sdk.model.error import Error
from rhoas_connector_mgmt_sdk.model.connector_request import ConnectorRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_connector_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_connector_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with rhoas_connector_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectors_api.ConnectorsApi(api_client)
    id = "id_example" # str | The ID of record
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Data to patch the connector with

    # example passing only required values which don't have defaults set
    try:
        # Patch a connector
        api_response = api_instance.patch_connector(id, body)
        pprint(api_response)
    except rhoas_connector_mgmt_sdk.ApiException as e:
        print("Exception when calling ConnectorsApi->patch_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of record |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Data to patch the connector with |

### Return type

[**Connector**](Connector.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json, application/json-patch+json, application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The connector matching the request |  -  |
**401** | Auth token is invalid |  -  |
**404** | No matching resource exists |  -  |
**410** | The requested resource doesn&#39;t exist anymore |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

