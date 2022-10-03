# rhoas_connector_mgmt_sdk.ConnectorClustersApi

All URIs are relative to *https://api.openshift.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connector_cluster**](ConnectorClustersApi.md#create_connector_cluster) | **POST** /api/connector_mgmt/v1/kafka_connector_clusters | Create a new connector cluster
[**delete_connector_cluster**](ConnectorClustersApi.md#delete_connector_cluster) | **DELETE** /api/connector_mgmt/v1/kafka_connector_clusters/{connector_cluster_id} | Delete a connector cluster
[**get_connector_cluster**](ConnectorClustersApi.md#get_connector_cluster) | **GET** /api/connector_mgmt/v1/kafka_connector_clusters/{connector_cluster_id} | Get a connector cluster
[**get_connector_cluster_addon_parameters**](ConnectorClustersApi.md#get_connector_cluster_addon_parameters) | **GET** /api/connector_mgmt/v1/kafka_connector_clusters/{connector_cluster_id}/addon_parameters | Get a connector cluster&#39;s addon parameters
[**get_connector_cluster_namespaces**](ConnectorClustersApi.md#get_connector_cluster_namespaces) | **GET** /api/connector_mgmt/v1/kafka_connector_clusters/{connector_cluster_id}/namespaces | Get a connector cluster&#39;s namespaces
[**list_connector_clusters**](ConnectorClustersApi.md#list_connector_clusters) | **GET** /api/connector_mgmt/v1/kafka_connector_clusters | Returns a list of connector clusters
[**update_connector_cluster_by_id**](ConnectorClustersApi.md#update_connector_cluster_by_id) | **PUT** /api/connector_mgmt/v1/kafka_connector_clusters/{connector_cluster_id} | udpate a connector cluster


# **create_connector_cluster**
> ConnectorCluster create_connector_cluster(_async, connector_cluster_request)

Create a new connector cluster

Create a new connector cluster

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_connector_mgmt_sdk
from rhoas_connector_mgmt_sdk.api import connector_clusters_api
from rhoas_connector_mgmt_sdk.model.connector_cluster import ConnectorCluster
from rhoas_connector_mgmt_sdk.model.connector_cluster_request import ConnectorClusterRequest
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
    api_instance = connector_clusters_api.ConnectorClustersApi(api_client)
    _async = True # bool | Perform the action in an asynchronous manner
    connector_cluster_request = ConnectorClusterRequest(None) # ConnectorClusterRequest | Connector cluster data

    # example passing only required values which don't have defaults set
    try:
        # Create a new connector cluster
        api_response = api_instance.create_connector_cluster(_async, connector_cluster_request)
        pprint(api_response)
    except rhoas_connector_mgmt_sdk.ApiException as e:
        print("Exception when calling ConnectorClustersApi->create_connector_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_async** | **bool**| Perform the action in an asynchronous manner |
 **connector_cluster_request** | [**ConnectorClusterRequest**](ConnectorClusterRequest.md)| Connector cluster data |

### Return type

[**ConnectorCluster**](ConnectorCluster.md)

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
**500** | An unexpected error occurred creating the connector cluster |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connector_cluster**
> Error delete_connector_cluster(connector_cluster_id)

Delete a connector cluster

Delete a connector cluster

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_connector_mgmt_sdk
from rhoas_connector_mgmt_sdk.api import connector_clusters_api
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
    api_instance = connector_clusters_api.ConnectorClustersApi(api_client)
    connector_cluster_id = "connector_cluster_id_example" # str | The id of the connector cluster

    # example passing only required values which don't have defaults set
    try:
        # Delete a connector cluster
        api_response = api_instance.delete_connector_cluster(connector_cluster_id)
        pprint(api_response)
    except rhoas_connector_mgmt_sdk.ApiException as e:
        print("Exception when calling ConnectorClustersApi->delete_connector_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_cluster_id** | **str**| The id of the connector cluster |

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
**404** | No resource with specified ID exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connector_cluster**
> ConnectorCluster get_connector_cluster(connector_cluster_id)

Get a connector cluster

Get a connector cluster

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_connector_mgmt_sdk
from rhoas_connector_mgmt_sdk.api import connector_clusters_api
from rhoas_connector_mgmt_sdk.model.connector_cluster import ConnectorCluster
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
    api_instance = connector_clusters_api.ConnectorClustersApi(api_client)
    connector_cluster_id = "connector_cluster_id_example" # str | The id of the connector cluster

    # example passing only required values which don't have defaults set
    try:
        # Get a connector cluster
        api_response = api_instance.get_connector_cluster(connector_cluster_id)
        pprint(api_response)
    except rhoas_connector_mgmt_sdk.ApiException as e:
        print("Exception when calling ConnectorClustersApi->get_connector_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_cluster_id** | **str**| The id of the connector cluster |

### Return type

[**ConnectorCluster**](ConnectorCluster.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The connector cluster matching the request |  -  |
**401** | Auth token is invalid |  -  |
**404** | No matching connector cluster type exists |  -  |
**410** | The requested resource doesn&#39;t exist anymore |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connector_cluster_addon_parameters**
> AddonParameterList get_connector_cluster_addon_parameters(connector_cluster_id)

Get a connector cluster's addon parameters

Get a connector cluster's addon parameters

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_connector_mgmt_sdk
from rhoas_connector_mgmt_sdk.api import connector_clusters_api
from rhoas_connector_mgmt_sdk.model.addon_parameter_list import AddonParameterList
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
    api_instance = connector_clusters_api.ConnectorClustersApi(api_client)
    connector_cluster_id = "connector_cluster_id_example" # str | The id of the connector cluster
    reset_credentials = True # bool | Resets cluster service account credentials when true (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a connector cluster's addon parameters
        api_response = api_instance.get_connector_cluster_addon_parameters(connector_cluster_id)
        pprint(api_response)
    except rhoas_connector_mgmt_sdk.ApiException as e:
        print("Exception when calling ConnectorClustersApi->get_connector_cluster_addon_parameters: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a connector cluster's addon parameters
        api_response = api_instance.get_connector_cluster_addon_parameters(connector_cluster_id, reset_credentials=reset_credentials)
        pprint(api_response)
    except rhoas_connector_mgmt_sdk.ApiException as e:
        print("Exception when calling ConnectorClustersApi->get_connector_cluster_addon_parameters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_cluster_id** | **str**| The id of the connector cluster |
 **reset_credentials** | **bool**| Resets cluster service account credentials when true | [optional]

### Return type

[**AddonParameterList**](AddonParameterList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The parameters that should be used to configure the managed connector addon on the cluster. |  -  |
**401** | Auth token is invalid |  -  |
**404** | No matching connector cluster type exists |  -  |
**410** | The requested resource doesn&#39;t exist anymore |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connector_cluster_namespaces**
> ConnectorNamespaceList get_connector_cluster_namespaces(connector_cluster_id)

Get a connector cluster's namespaces

Get a connector cluster's namespaces

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_connector_mgmt_sdk
from rhoas_connector_mgmt_sdk.api import connector_clusters_api
from rhoas_connector_mgmt_sdk.model.error import Error
from rhoas_connector_mgmt_sdk.model.connector_namespace_list import ConnectorNamespaceList
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
    api_instance = connector_clusters_api.ConnectorClustersApi(api_client)
    connector_cluster_id = "connector_cluster_id_example" # str | The id of the connector cluster
    page = "1" # str | Page index (optional)
    size = "100" # str | Number of items in each page (optional)
    order_by = "name asc" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the `order by` clause of an SQL statement. Each query can be ordered by any of the underlying resource fields supported in the search parameter. For example, to return all Connector types ordered by their name, use the following syntax:  ```sql name asc ```  To return all Connector types ordered by their name _and_ version, use the following syntax:  ```sql name asc, version asc ```  If the parameter isn't provided, or if the value is empty, then the results are ordered by name. (optional)
    search = "name = aws-sqs-source and channel = stable" # str | Search criteria.  The syntax of this parameter is similar to the syntax of the `where` clause of a SQL statement.  Allowed fields in the search depend on the resource type:  * Cluster: id, created_at, updated_at, owner, organisation_id, name, state, client_id * Namespace: id, created_at, updated_at, name, cluster_id, owner, expiration, tenant_user_id, tenant_organisation_id, state * Connector Types: id, created_at, updated_at, version, name, description, label, channel, featured_rank * Connectors: id, created_at, updated_at, name, owner, organisation_id, connector_type_id, desired_state, state, channel, namespace_id, kafka_id, kafka_bootstrap_server, service_account_client_id, schema_registry_id, schema_registry_url  Allowed operators are `<>`, `=`, `LIKE`, or `ILIKE`. Allowed conjunctive operators are `AND` and `OR`. However, you can use a maximum of 10 conjunctions in a search query.  Examples:  To return a Connector Type with the name `aws-sqs-source` and the channel `stable`, use the following syntax:  ``` name = aws-sqs-source and channel = stable ```[p-]  To return a connector instance with a name that starts with `aws`, use the following syntax:  ``` name like aws%25 ```  To return a connector type with a name containing `aws` matching any character case combination, use the following syntax:  ``` name ilike %25aws%25 ```  If the parameter isn't provided, or if the value is empty, then all the resources that the user has permission to see are returned.  Note. If the query is invalid, an error is returned.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a connector cluster's namespaces
        api_response = api_instance.get_connector_cluster_namespaces(connector_cluster_id)
        pprint(api_response)
    except rhoas_connector_mgmt_sdk.ApiException as e:
        print("Exception when calling ConnectorClustersApi->get_connector_cluster_namespaces: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a connector cluster's namespaces
        api_response = api_instance.get_connector_cluster_namespaces(connector_cluster_id, page=page, size=size, order_by=order_by, search=search)
        pprint(api_response)
    except rhoas_connector_mgmt_sdk.ApiException as e:
        print("Exception when calling ConnectorClustersApi->get_connector_cluster_namespaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_cluster_id** | **str**| The id of the connector cluster |
 **page** | **str**| Page index | [optional]
 **size** | **str**| Number of items in each page | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the &#x60;order by&#x60; clause of an SQL statement. Each query can be ordered by any of the underlying resource fields supported in the search parameter. For example, to return all Connector types ordered by their name, use the following syntax:  &#x60;&#x60;&#x60;sql name asc &#x60;&#x60;&#x60;  To return all Connector types ordered by their name _and_ version, use the following syntax:  &#x60;&#x60;&#x60;sql name asc, version asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then the results are ordered by name. | [optional]
 **search** | **str**| Search criteria.  The syntax of this parameter is similar to the syntax of the &#x60;where&#x60; clause of a SQL statement.  Allowed fields in the search depend on the resource type:  * Cluster: id, created_at, updated_at, owner, organisation_id, name, state, client_id * Namespace: id, created_at, updated_at, name, cluster_id, owner, expiration, tenant_user_id, tenant_organisation_id, state * Connector Types: id, created_at, updated_at, version, name, description, label, channel, featured_rank * Connectors: id, created_at, updated_at, name, owner, organisation_id, connector_type_id, desired_state, state, channel, namespace_id, kafka_id, kafka_bootstrap_server, service_account_client_id, schema_registry_id, schema_registry_url  Allowed operators are &#x60;&lt;&gt;&#x60;, &#x60;&#x3D;&#x60;, &#x60;LIKE&#x60;, or &#x60;ILIKE&#x60;. Allowed conjunctive operators are &#x60;AND&#x60; and &#x60;OR&#x60;. However, you can use a maximum of 10 conjunctions in a search query.  Examples:  To return a Connector Type with the name &#x60;aws-sqs-source&#x60; and the channel &#x60;stable&#x60;, use the following syntax:  &#x60;&#x60;&#x60; name &#x3D; aws-sqs-source and channel &#x3D; stable &#x60;&#x60;&#x60;[p-]  To return a connector instance with a name that starts with &#x60;aws&#x60;, use the following syntax:  &#x60;&#x60;&#x60; name like aws%25 &#x60;&#x60;&#x60;  To return a connector type with a name containing &#x60;aws&#x60; matching any character case combination, use the following syntax:  &#x60;&#x60;&#x60; name ilike %25aws%25 &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the resources that the user has permission to see are returned.  Note. If the query is invalid, an error is returned.  | [optional]

### Return type

[**ConnectorNamespaceList**](ConnectorNamespaceList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The namespaces visible to user in the cluster. |  -  |
**401** | Auth token is invalid |  -  |
**404** | No matching connector cluster type exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connector_clusters**
> ConnectorClusterList list_connector_clusters()

Returns a list of connector clusters

Returns a list of connector clusters

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_connector_mgmt_sdk
from rhoas_connector_mgmt_sdk.api import connector_clusters_api
from rhoas_connector_mgmt_sdk.model.error import Error
from rhoas_connector_mgmt_sdk.model.connector_cluster_list import ConnectorClusterList
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
    api_instance = connector_clusters_api.ConnectorClustersApi(api_client)
    page = "1" # str | Page index (optional)
    size = "100" # str | Number of items in each page (optional)
    order_by = "name asc" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the `order by` clause of an SQL statement. Each query can be ordered by any of the underlying resource fields supported in the search parameter. For example, to return all Connector types ordered by their name, use the following syntax:  ```sql name asc ```  To return all Connector types ordered by their name _and_ version, use the following syntax:  ```sql name asc, version asc ```  If the parameter isn't provided, or if the value is empty, then the results are ordered by name. (optional)
    search = "name = aws-sqs-source and channel = stable" # str | Search criteria.  The syntax of this parameter is similar to the syntax of the `where` clause of a SQL statement.  Allowed fields in the search depend on the resource type:  * Cluster: id, created_at, updated_at, owner, organisation_id, name, state, client_id * Namespace: id, created_at, updated_at, name, cluster_id, owner, expiration, tenant_user_id, tenant_organisation_id, state * Connector Types: id, created_at, updated_at, version, name, description, label, channel, featured_rank * Connectors: id, created_at, updated_at, name, owner, organisation_id, connector_type_id, desired_state, state, channel, namespace_id, kafka_id, kafka_bootstrap_server, service_account_client_id, schema_registry_id, schema_registry_url  Allowed operators are `<>`, `=`, `LIKE`, or `ILIKE`. Allowed conjunctive operators are `AND` and `OR`. However, you can use a maximum of 10 conjunctions in a search query.  Examples:  To return a Connector Type with the name `aws-sqs-source` and the channel `stable`, use the following syntax:  ``` name = aws-sqs-source and channel = stable ```[p-]  To return a connector instance with a name that starts with `aws`, use the following syntax:  ``` name like aws%25 ```  To return a connector type with a name containing `aws` matching any character case combination, use the following syntax:  ``` name ilike %25aws%25 ```  If the parameter isn't provided, or if the value is empty, then all the resources that the user has permission to see are returned.  Note. If the query is invalid, an error is returned.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of connector clusters
        api_response = api_instance.list_connector_clusters(page=page, size=size, order_by=order_by, search=search)
        pprint(api_response)
    except rhoas_connector_mgmt_sdk.ApiException as e:
        print("Exception when calling ConnectorClustersApi->list_connector_clusters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| Page index | [optional]
 **size** | **str**| Number of items in each page | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the &#x60;order by&#x60; clause of an SQL statement. Each query can be ordered by any of the underlying resource fields supported in the search parameter. For example, to return all Connector types ordered by their name, use the following syntax:  &#x60;&#x60;&#x60;sql name asc &#x60;&#x60;&#x60;  To return all Connector types ordered by their name _and_ version, use the following syntax:  &#x60;&#x60;&#x60;sql name asc, version asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then the results are ordered by name. | [optional]
 **search** | **str**| Search criteria.  The syntax of this parameter is similar to the syntax of the &#x60;where&#x60; clause of a SQL statement.  Allowed fields in the search depend on the resource type:  * Cluster: id, created_at, updated_at, owner, organisation_id, name, state, client_id * Namespace: id, created_at, updated_at, name, cluster_id, owner, expiration, tenant_user_id, tenant_organisation_id, state * Connector Types: id, created_at, updated_at, version, name, description, label, channel, featured_rank * Connectors: id, created_at, updated_at, name, owner, organisation_id, connector_type_id, desired_state, state, channel, namespace_id, kafka_id, kafka_bootstrap_server, service_account_client_id, schema_registry_id, schema_registry_url  Allowed operators are &#x60;&lt;&gt;&#x60;, &#x60;&#x3D;&#x60;, &#x60;LIKE&#x60;, or &#x60;ILIKE&#x60;. Allowed conjunctive operators are &#x60;AND&#x60; and &#x60;OR&#x60;. However, you can use a maximum of 10 conjunctions in a search query.  Examples:  To return a Connector Type with the name &#x60;aws-sqs-source&#x60; and the channel &#x60;stable&#x60;, use the following syntax:  &#x60;&#x60;&#x60; name &#x3D; aws-sqs-source and channel &#x3D; stable &#x60;&#x60;&#x60;[p-]  To return a connector instance with a name that starts with &#x60;aws&#x60;, use the following syntax:  &#x60;&#x60;&#x60; name like aws%25 &#x60;&#x60;&#x60;  To return a connector type with a name containing &#x60;aws&#x60; matching any character case combination, use the following syntax:  &#x60;&#x60;&#x60; name ilike %25aws%25 &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the resources that the user has permission to see are returned.  Note. If the query is invalid, an error is returned.  | [optional]

### Return type

[**ConnectorClusterList**](ConnectorClusterList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of connector clusters |  -  |
**401** | Auth token is invalid |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connector_cluster_by_id**
> update_connector_cluster_by_id(connector_cluster_id, connector_cluster_request)

udpate a connector cluster

udpate a connector cluster

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_connector_mgmt_sdk
from rhoas_connector_mgmt_sdk.api import connector_clusters_api
from rhoas_connector_mgmt_sdk.model.connector_cluster_request import ConnectorClusterRequest
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
    api_instance = connector_clusters_api.ConnectorClustersApi(api_client)
    connector_cluster_id = "connector_cluster_id_example" # str | The id of the connector cluster
    connector_cluster_request = ConnectorClusterRequest(None) # ConnectorClusterRequest | Data to updated connector with

    # example passing only required values which don't have defaults set
    try:
        # udpate a connector cluster
        api_instance.update_connector_cluster_by_id(connector_cluster_id, connector_cluster_request)
    except rhoas_connector_mgmt_sdk.ApiException as e:
        print("Exception when calling ConnectorClustersApi->update_connector_cluster_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_cluster_id** | **str**| The id of the connector cluster |
 **connector_cluster_request** | [**ConnectorClusterRequest**](ConnectorClusterRequest.md)| Data to updated connector with |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Cluster status is updated |  -  |
**401** | Auth token is invalid |  -  |
**404** | No matching connector cluster exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

