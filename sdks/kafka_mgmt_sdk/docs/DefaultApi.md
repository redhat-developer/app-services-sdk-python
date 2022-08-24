# rhoas_kafka_mgmt_sdk.DefaultApi

All URIs are relative to *https://api.openshift.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_kafka**](DefaultApi.md#create_kafka) | **POST** /api/kafkas_mgmt/v1/kafkas | 
[**delete_kafka_by_id**](DefaultApi.md#delete_kafka_by_id) | **DELETE** /api/kafkas_mgmt/v1/kafkas/{id} | 
[**federate_metrics**](DefaultApi.md#federate_metrics) | **GET** /api/kafkas_mgmt/v1/kafkas/{id}/metrics/federate | 
[**get_cloud_provider_regions**](DefaultApi.md#get_cloud_provider_regions) | **GET** /api/kafkas_mgmt/v1/cloud_providers/{id}/regions | 
[**get_cloud_providers**](DefaultApi.md#get_cloud_providers) | **GET** /api/kafkas_mgmt/v1/cloud_providers | 
[**get_instance_types_by_cloud_provider_and_region**](DefaultApi.md#get_instance_types_by_cloud_provider_and_region) | **GET** /api/kafkas_mgmt/v1/instance_types/{cloud_provider}/{cloud_region} | 
[**get_kafka_by_id**](DefaultApi.md#get_kafka_by_id) | **GET** /api/kafkas_mgmt/v1/kafkas/{id} | 
[**get_kafkas**](DefaultApi.md#get_kafkas) | **GET** /api/kafkas_mgmt/v1/kafkas | 
[**get_metrics_by_instant_query**](DefaultApi.md#get_metrics_by_instant_query) | **GET** /api/kafkas_mgmt/v1/kafkas/{id}/metrics/query | 
[**get_metrics_by_range_query**](DefaultApi.md#get_metrics_by_range_query) | **GET** /api/kafkas_mgmt/v1/kafkas/{id}/metrics/query_range | 
[**get_version_metadata**](DefaultApi.md#get_version_metadata) | **GET** /api/kafkas_mgmt/v1 | 
[**update_kafka_by_id**](DefaultApi.md#update_kafka_by_id) | **PATCH** /api/kafkas_mgmt/v1/kafkas/{id} | 


# **create_kafka**
> KafkaRequest create_kafka(_async, kafka_request_payload)



Creates a Kafka request

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_kafka_mgmt_sdk
from rhoas_kafka_mgmt_sdk.api import default_api
from rhoas_kafka_mgmt_sdk.model.kafka_request import KafkaRequest
from rhoas_kafka_mgmt_sdk.model.kafka_request_payload import KafkaRequestPayload
from rhoas_kafka_mgmt_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with rhoas_kafka_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    _async = True # bool | Perform the action in an asynchronous manner
    kafka_request_payload = KafkaRequestPayload(
        cloud_provider="cloud_provider_example",
        name="name_example",
        region="region_example",
        reauthentication_enabled=True,
        plan="plan_example",
        billing_cloud_account_id="billing_cloud_account_id_example",
        marketplace="marketplace_example",
        billing_model="billing_model_example",
    ) # KafkaRequestPayload | Kafka data

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_kafka(_async, kafka_request_payload)
        pprint(api_response)
    except rhoas_kafka_mgmt_sdk.ApiException as e:
        print("Exception when calling DefaultApi->create_kafka: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_async** | **bool**| Perform the action in an asynchronous manner |
 **kafka_request_payload** | [**KafkaRequestPayload**](KafkaRequestPayload.md)| Kafka data |

### Return type

[**KafkaRequest**](KafkaRequest.md)

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
**403** | User forbidden either because the user is not authorized to access the service or because the maximum number of instances that can be created by this user has been reached. |  -  |
**404** | The requested resource doesn&#39;t exist |  -  |
**409** | A conflict has been detected in the creation of this resource |  -  |
**500** | An unexpected error occurred while creating the Kafka request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_kafka_by_id**
> Error delete_kafka_by_id(id, _async)



Deletes a Kafka request by ID

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_kafka_mgmt_sdk
from rhoas_kafka_mgmt_sdk.api import default_api
from rhoas_kafka_mgmt_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with rhoas_kafka_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The ID of record
    _async = True # bool | Perform the action in an asynchronous manner

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_kafka_by_id(id, _async)
        pprint(api_response)
    except rhoas_kafka_mgmt_sdk.ApiException as e:
        print("Exception when calling DefaultApi->delete_kafka_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of record |
 **_async** | **bool**| Perform the action in an asynchronous manner |

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
**202** | Deleted |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | User not authorized to access the service |  -  |
**404** | No Kafka request with specified ID exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **federate_metrics**
> str federate_metrics(id)



Returns all metrics in scrapeable format for a given kafka id

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_kafka_mgmt_sdk
from rhoas_kafka_mgmt_sdk.api import default_api
from rhoas_kafka_mgmt_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with rhoas_kafka_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The ID of record

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.federate_metrics(id)
        pprint(api_response)
    except rhoas_kafka_mgmt_sdk.ApiException as e:
        print("Exception when calling DefaultApi->federate_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of record |

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned Kafka metrics in a Prometheus text format |  -  |
**400** | Bad request |  -  |
**401** | Auth token is invalid |  -  |
**404** | Kafka id not found |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_provider_regions**
> CloudRegionList get_cloud_provider_regions(id)



Returns the list of supported regions of the supported cloud provider

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_kafka_mgmt_sdk
from rhoas_kafka_mgmt_sdk.api import default_api
from rhoas_kafka_mgmt_sdk.model.error import Error
from rhoas_kafka_mgmt_sdk.model.cloud_region_list import CloudRegionList
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with rhoas_kafka_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The ID of record
    page = "1" # str | Page index (optional)
    size = "100" # str | Number of items in each page (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cloud_provider_regions(id)
        pprint(api_response)
    except rhoas_kafka_mgmt_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_cloud_provider_regions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_cloud_provider_regions(id, page=page, size=size)
        pprint(api_response)
    except rhoas_kafka_mgmt_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_cloud_provider_regions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of record |
 **page** | **str**| Page index | [optional]
 **size** | **str**| Number of items in each page | [optional]

### Return type

[**CloudRegionList**](CloudRegionList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned list of supported cloud provider regions |  -  |
**401** | Auth token is invalid |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_providers**
> CloudProviderList get_cloud_providers()



Returns the list of supported cloud providers

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_kafka_mgmt_sdk
from rhoas_kafka_mgmt_sdk.api import default_api
from rhoas_kafka_mgmt_sdk.model.cloud_provider_list import CloudProviderList
from rhoas_kafka_mgmt_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with rhoas_kafka_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    page = "1" # str | Page index (optional)
    size = "100" # str | Number of items in each page (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_cloud_providers(page=page, size=size)
        pprint(api_response)
    except rhoas_kafka_mgmt_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_cloud_providers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| Page index | [optional]
 **size** | **str**| Number of items in each page | [optional]

### Return type

[**CloudProviderList**](CloudProviderList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned list of supported cloud providers |  -  |
**401** | Auth token is invalid |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance_types_by_cloud_provider_and_region**
> SupportedKafkaInstanceTypesList get_instance_types_by_cloud_provider_and_region(cloud_provider, cloud_region)



Returns the list of supported Kafka instance types and sizes filtered by cloud provider and region

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_kafka_mgmt_sdk
from rhoas_kafka_mgmt_sdk.api import default_api
from rhoas_kafka_mgmt_sdk.model.supported_kafka_instance_types_list import SupportedKafkaInstanceTypesList
from rhoas_kafka_mgmt_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with rhoas_kafka_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    cloud_provider = "cloud_provider_example" # str | ID of the supported cloud provider
    cloud_region = "cloud_region_example" # str | Name of the supported cloud provider region

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_instance_types_by_cloud_provider_and_region(cloud_provider, cloud_region)
        pprint(api_response)
    except rhoas_kafka_mgmt_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_instance_types_by_cloud_provider_and_region: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_provider** | **str**| ID of the supported cloud provider |
 **cloud_region** | **str**| Name of the supported cloud provider region |

### Return type

[**SupportedKafkaInstanceTypesList**](SupportedKafkaInstanceTypesList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned list of supported Kafka instance types and sizes filtered by cloud provider and region |  -  |
**400** | Cloud provider or region is not supported |  -  |
**401** | Auth token is invalid |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kafka_by_id**
> KafkaRequest get_kafka_by_id(id)



Returns a Kafka request by ID

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_kafka_mgmt_sdk
from rhoas_kafka_mgmt_sdk.api import default_api
from rhoas_kafka_mgmt_sdk.model.kafka_request import KafkaRequest
from rhoas_kafka_mgmt_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with rhoas_kafka_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The ID of record

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_kafka_by_id(id)
        pprint(api_response)
    except rhoas_kafka_mgmt_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_kafka_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of record |

### Return type

[**KafkaRequest**](KafkaRequest.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Kafka request found by ID |  -  |
**401** | Auth token is invalid |  -  |
**403** | User not authorized to access the service |  -  |
**404** | No Kafka request with specified ID exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kafkas**
> KafkaRequestList get_kafkas()



Returns a list of Kafka requests

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_kafka_mgmt_sdk
from rhoas_kafka_mgmt_sdk.api import default_api
from rhoas_kafka_mgmt_sdk.model.error import Error
from rhoas_kafka_mgmt_sdk.model.kafka_request_list import KafkaRequestList
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with rhoas_kafka_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    page = "1" # str | Page index (optional)
    size = "100" # str | Number of items in each page (optional)
    order_by = "name asc" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the `order by` clause of an SQL statement. Each query can be ordered by any of the following `kafkaRequests` fields:  * bootstrap_server_host * admin_api_server_url * cloud_provider * cluster_id * created_at * href * id * instance_type * multi_az * name * organisation_id * owner * reauthentication_enabled * region * status * updated_at * version  For example, to return all Kafka instances ordered by their name, use the following syntax:  ```sql name asc ```  To return all Kafka instances ordered by their name _and_ created date, use the following syntax:  ```sql name asc, created_at asc ```  If the parameter isn't provided, or if the value is empty, then the results are ordered by name. (optional)
    search = "name = my-kafka and cloud_provider = aws" # str | Search criteria.  The syntax of this parameter is similar to the syntax of the `where` clause of an SQL statement. Allowed fields in the search are `cloud_provider`, `name`, `owner`, `region`, and `status`. Allowed comparators are `<>`, `=`, `LIKE`, or `ILIKE`. Allowed joins are `AND` and `OR`. However, you can use a maximum of 10 joins in a search query.  Examples:  To return a Kafka instance with the name `my-kafka` and the region `aws`, use the following syntax:  ``` name = my-kafka and cloud_provider = aws ```[p-]  To return a Kafka instance with a name that starts with `my`, use the following syntax:  ``` name like my%25 ```  To return a Kafka instance with a name containing `test` matching any character case combinations, use the following syntax:  ``` name ilike %25test%25 ```  If the parameter isn't provided, or if the value is empty, then all the Kafka instances that the user has permission to see are returned.  Note. If the query is invalid, an error is returned.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_kafkas(page=page, size=size, order_by=order_by, search=search)
        pprint(api_response)
    except rhoas_kafka_mgmt_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_kafkas: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| Page index | [optional]
 **size** | **str**| Number of items in each page | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the &#x60;order by&#x60; clause of an SQL statement. Each query can be ordered by any of the following &#x60;kafkaRequests&#x60; fields:  * bootstrap_server_host * admin_api_server_url * cloud_provider * cluster_id * created_at * href * id * instance_type * multi_az * name * organisation_id * owner * reauthentication_enabled * region * status * updated_at * version  For example, to return all Kafka instances ordered by their name, use the following syntax:  &#x60;&#x60;&#x60;sql name asc &#x60;&#x60;&#x60;  To return all Kafka instances ordered by their name _and_ created date, use the following syntax:  &#x60;&#x60;&#x60;sql name asc, created_at asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then the results are ordered by name. | [optional]
 **search** | **str**| Search criteria.  The syntax of this parameter is similar to the syntax of the &#x60;where&#x60; clause of an SQL statement. Allowed fields in the search are &#x60;cloud_provider&#x60;, &#x60;name&#x60;, &#x60;owner&#x60;, &#x60;region&#x60;, and &#x60;status&#x60;. Allowed comparators are &#x60;&lt;&gt;&#x60;, &#x60;&#x3D;&#x60;, &#x60;LIKE&#x60;, or &#x60;ILIKE&#x60;. Allowed joins are &#x60;AND&#x60; and &#x60;OR&#x60;. However, you can use a maximum of 10 joins in a search query.  Examples:  To return a Kafka instance with the name &#x60;my-kafka&#x60; and the region &#x60;aws&#x60;, use the following syntax:  &#x60;&#x60;&#x60; name &#x3D; my-kafka and cloud_provider &#x3D; aws &#x60;&#x60;&#x60;[p-]  To return a Kafka instance with a name that starts with &#x60;my&#x60;, use the following syntax:  &#x60;&#x60;&#x60; name like my%25 &#x60;&#x60;&#x60;  To return a Kafka instance with a name containing &#x60;test&#x60; matching any character case combinations, use the following syntax:  &#x60;&#x60;&#x60; name ilike %25test%25 &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the Kafka instances that the user has permission to see are returned.  Note. If the query is invalid, an error is returned.  | [optional]

### Return type

[**KafkaRequestList**](KafkaRequestList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Kafka requests |  -  |
**400** | Bad request |  -  |
**401** | Auth token is invalid |  -  |
**403** | User not authorized to access the service |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metrics_by_instant_query**
> MetricsInstantQueryList get_metrics_by_instant_query(id)



Returns metrics with instant query by Kafka ID

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_kafka_mgmt_sdk
from rhoas_kafka_mgmt_sdk.api import default_api
from rhoas_kafka_mgmt_sdk.model.error import Error
from rhoas_kafka_mgmt_sdk.model.metrics_instant_query_list import MetricsInstantQueryList
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with rhoas_kafka_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The ID of record
    filters = [] # [str] | List of metrics to fetch. Fetch all metrics when empty. List entries are Kafka internal metric names. (optional) if omitted the server will use the default value of []

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_metrics_by_instant_query(id)
        pprint(api_response)
    except rhoas_kafka_mgmt_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_metrics_by_instant_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_metrics_by_instant_query(id, filters=filters)
        pprint(api_response)
    except rhoas_kafka_mgmt_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_metrics_by_instant_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of record |
 **filters** | **[str]**| List of metrics to fetch. Fetch all metrics when empty. List entries are Kafka internal metric names. | [optional] if omitted the server will use the default value of []

### Return type

[**MetricsInstantQueryList**](MetricsInstantQueryList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned JSON array of Prometheus metrics objects from observatorium |  -  |
**401** | Auth token is invalid |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metrics_by_range_query**
> MetricsRangeQueryList get_metrics_by_range_query(id, )



Returns metrics with timeseries range query by Kafka ID

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_kafka_mgmt_sdk
from rhoas_kafka_mgmt_sdk.api import default_api
from rhoas_kafka_mgmt_sdk.model.metrics_range_query_list import MetricsRangeQueryList
from rhoas_kafka_mgmt_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with rhoas_kafka_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The ID of record
    filters = [] # [str] | List of metrics to fetch. Fetch all metrics when empty. List entries are Kafka internal metric names. (optional) if omitted the server will use the default value of []

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_metrics_by_range_query(id, )
        pprint(api_response)
    except rhoas_kafka_mgmt_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_metrics_by_range_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_metrics_by_range_query(id, filters=filters)
        pprint(api_response)
    except rhoas_kafka_mgmt_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_metrics_by_range_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of record |
 **duration** | **int**| The length of time in minutes for which to return the metrics | defaults to 5
 **interval** | **int**| The interval in seconds between data points | defaults to 30
 **filters** | **[str]**| List of metrics to fetch. Fetch all metrics when empty. List entries are Kafka internal metric names. | [optional] if omitted the server will use the default value of []

### Return type

[**MetricsRangeQueryList**](MetricsRangeQueryList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned JSON array of Prometheus metrics objects from observatorium |  -  |
**401** | Auth token is invalid |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version_metadata**
> VersionMetadata get_version_metadata()



Returns the kafka Service Fleet Manager API version metadata

### Example


```python
import time
import rhoas_kafka_mgmt_sdk
from rhoas_kafka_mgmt_sdk.api import default_api
from rhoas_kafka_mgmt_sdk.model.version_metadata import VersionMetadata
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)


# Enter a context with an instance of the API client
with rhoas_kafka_mgmt_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_version_metadata()
        pprint(api_response)
    except rhoas_kafka_mgmt_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_version_metadata: %s\n" % e)
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

# **update_kafka_by_id**
> KafkaRequest update_kafka_by_id(id, kafka_update_request)



Update a Kafka instance by id

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_kafka_mgmt_sdk
from rhoas_kafka_mgmt_sdk.api import default_api
from rhoas_kafka_mgmt_sdk.model.kafka_request import KafkaRequest
from rhoas_kafka_mgmt_sdk.model.error import Error
from rhoas_kafka_mgmt_sdk.model.kafka_update_request import KafkaUpdateRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with rhoas_kafka_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The ID of record
    kafka_update_request = KafkaUpdateRequest(
        owner="owner_example",
        reauthentication_enabled=True,
    ) # KafkaUpdateRequest | Update owner of kafka

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_kafka_by_id(id, kafka_update_request)
        pprint(api_response)
    except rhoas_kafka_mgmt_sdk.ApiException as e:
        print("Exception when calling DefaultApi->update_kafka_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of record |
 **kafka_update_request** | [**KafkaUpdateRequest**](KafkaUpdateRequest.md)| Update owner of kafka |

### Return type

[**KafkaRequest**](KafkaRequest.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Kafka updated by ID |  -  |
**400** | Bad request |  -  |
**401** | Auth token is invalid |  -  |
**403** | User is not authorised to access the service |  -  |
**404** | No Kafka found with the specified ID |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

