# rhoas_kafka_instance_sdk.GroupsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_consumer_group_by_id**](GroupsApi.md#delete_consumer_group_by_id) | **DELETE** /api/v1/consumer-groups/{consumerGroupId} | Delete a consumer group.
[**get_consumer_group_by_id**](GroupsApi.md#get_consumer_group_by_id) | **GET** /api/v1/consumer-groups/{consumerGroupId} | Get a single consumer group by its unique ID.
[**get_consumer_groups**](GroupsApi.md#get_consumer_groups) | **GET** /api/v1/consumer-groups | List of consumer groups in the Kafka instance.
[**reset_consumer_group_offset**](GroupsApi.md#reset_consumer_group_offset) | **POST** /api/v1/consumer-groups/{consumerGroupId}/reset-offset | Reset the offset for a consumer group.


# **delete_consumer_group_by_id**
> delete_consumer_group_by_id(consumer_group_id)

Delete a consumer group.

Delete a consumer group, along with its consumers.

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth2):

```python
import time
import rhoas_kafka_instance_sdk
from rhoas_kafka_instance_sdk.api import groups_api
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
    api_instance = groups_api.GroupsApi(api_client)
    consumer_group_id = "consumerGroupId_example" # str | Consumer group identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete a consumer group.
        api_instance.delete_consumer_group_by_id(consumer_group_id)
    except rhoas_kafka_instance_sdk.ApiException as e:
        print("Exception when calling GroupsApi->delete_consumer_group_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_group_id** | **str**| Consumer group identifier |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The consumer group was deleted successfully. |  -  |
**401** | Request authentication missing or invalid |  -  |
**403** | User is not authorized to access requested resource |  -  |
**404** | The requested resource could not be found. |  -  |
**423** | User cannot delete consumer group with active members. |  -  |
**500** | Internal server error |  -  |
**503** | Kafka service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consumer_group_by_id**
> ConsumerGroup get_consumer_group_by_id(consumer_group_id)

Get a single consumer group by its unique ID.

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth2):

```python
import time
import rhoas_kafka_instance_sdk
from rhoas_kafka_instance_sdk.api import groups_api
from rhoas_kafka_instance_sdk.model.sort_direction import SortDirection
from rhoas_kafka_instance_sdk.model.consumer_group import ConsumerGroup
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
    api_instance = groups_api.GroupsApi(api_client)
    consumer_group_id = "consumerGroupId_example" # str | Consumer group identifier
    order = SortDirection("asc") # SortDirection | Order items are sorted (optional)
    order_key = None # bool, date, datetime, dict, float, int, list, str, none_type |  (optional)
    partition_filter = 1 # int | Value of partition to include. Value -1 means filter is not active. (optional)
    topic = "topic_example" # str | Filter consumer groups for a specific topic (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a single consumer group by its unique ID.
        api_response = api_instance.get_consumer_group_by_id(consumer_group_id)
        pprint(api_response)
    except rhoas_kafka_instance_sdk.ApiException as e:
        print("Exception when calling GroupsApi->get_consumer_group_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a single consumer group by its unique ID.
        api_response = api_instance.get_consumer_group_by_id(consumer_group_id, order=order, order_key=order_key, partition_filter=partition_filter, topic=topic)
        pprint(api_response)
    except rhoas_kafka_instance_sdk.ApiException as e:
        print("Exception when calling GroupsApi->get_consumer_group_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_group_id** | **str**| Consumer group identifier |
 **order** | **SortDirection**| Order items are sorted | [optional]
 **order_key** | **bool, date, datetime, dict, float, int, list, str, none_type**|  | [optional]
 **partition_filter** | **int**| Value of partition to include. Value -1 means filter is not active. | [optional]
 **topic** | **str**| Filter consumer groups for a specific topic | [optional]

### Return type

[**ConsumerGroup**](ConsumerGroup.md)

### Authorization

[Bearer](../README.md#Bearer), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Consumer group details. |  -  |
**401** | Request authentication missing or invalid |  -  |
**403** | User is not authorized to access requested resource |  -  |
**404** | The requested resource could not be found. |  -  |
**500** | Internal server error |  -  |
**503** | Kafka service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consumer_groups**
> ConsumerGroupList get_consumer_groups()

List of consumer groups in the Kafka instance.

Returns a list of all consumer groups for a particular Kafka instance. The consumer groups returned are limited to those records the requestor is authorized to view.

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth2):

```python
import time
import rhoas_kafka_instance_sdk
from rhoas_kafka_instance_sdk.api import groups_api
from rhoas_kafka_instance_sdk.model.sort_direction import SortDirection
from rhoas_kafka_instance_sdk.model.consumer_group_list import ConsumerGroupList
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
    api_instance = groups_api.GroupsApi(api_client)
    offset = 0 # int | Offset of the first record to return, zero-based (optional)
    limit = 1 # int | Maximum number of records to return (optional)
    size = 1 # int | Number of records per page (optional)
    page = 1 # int | Page number (optional)
    topic = "topic_example" # str | Return consumer groups where the topic name contains this value (optional)
    group_id_filter = "group-id-filter_example" # str | Return the consumer groups where the ID contains this value (optional)
    order = SortDirection("asc") # SortDirection | Order items are sorted (optional)
    order_key = None # bool, date, datetime, dict, float, int, list, str, none_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List of consumer groups in the Kafka instance.
        api_response = api_instance.get_consumer_groups(offset=offset, limit=limit, size=size, page=page, topic=topic, group_id_filter=group_id_filter, order=order, order_key=order_key)
        pprint(api_response)
    except rhoas_kafka_instance_sdk.ApiException as e:
        print("Exception when calling GroupsApi->get_consumer_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset of the first record to return, zero-based | [optional]
 **limit** | **int**| Maximum number of records to return | [optional]
 **size** | **int**| Number of records per page | [optional]
 **page** | **int**| Page number | [optional]
 **topic** | **str**| Return consumer groups where the topic name contains this value | [optional]
 **group_id_filter** | **str**| Return the consumer groups where the ID contains this value | [optional]
 **order** | **SortDirection**| Order items are sorted | [optional]
 **order_key** | **bool, date, datetime, dict, float, int, list, str, none_type**|  | [optional]

### Return type

[**ConsumerGroupList**](ConsumerGroupList.md)

### Authorization

[Bearer](../README.md#Bearer), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of consumer groups matching the request parameters. The consumer groups returned are limited to those records the requestor is authorized to view. |  -  |
**400** | The client request was invalid. One or more request parameters or the request body was rejected. Additional information may be found in the response. |  -  |
**401** | Request authentication missing or invalid |  -  |
**500** | Internal server error |  -  |
**503** | Kafka service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_consumer_group_offset**
> ConsumerGroupResetOffsetResult reset_consumer_group_offset(consumer_group_id, consumer_group_reset_offset_parameters)

Reset the offset for a consumer group.

Reset the offset for a particular consumer group.

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth2):

```python
import time
import rhoas_kafka_instance_sdk
from rhoas_kafka_instance_sdk.api import groups_api
from rhoas_kafka_instance_sdk.model.consumer_group_reset_offset_result import ConsumerGroupResetOffsetResult
from rhoas_kafka_instance_sdk.model.error import Error
from rhoas_kafka_instance_sdk.model.consumer_group_reset_offset_parameters import ConsumerGroupResetOffsetParameters
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
    api_instance = groups_api.GroupsApi(api_client)
    consumer_group_id = "consumerGroupId_example" # str | Consumer group identifier
    consumer_group_reset_offset_parameters = ConsumerGroupResetOffsetParameters(
        offset=OffsetType("timestamp"),
        value="value_example",
        topics=[
            TopicsToResetOffset(
                topic="topic_example",
                partitions=[
                    1,
                ],
            ),
        ],
    ) # ConsumerGroupResetOffsetParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Reset the offset for a consumer group.
        api_response = api_instance.reset_consumer_group_offset(consumer_group_id, consumer_group_reset_offset_parameters)
        pprint(api_response)
    except rhoas_kafka_instance_sdk.ApiException as e:
        print("Exception when calling GroupsApi->reset_consumer_group_offset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_group_id** | **str**| Consumer group identifier |
 **consumer_group_reset_offset_parameters** | [**ConsumerGroupResetOffsetParameters**](ConsumerGroupResetOffsetParameters.md)|  |

### Return type

[**ConsumerGroupResetOffsetResult**](ConsumerGroupResetOffsetResult.md)

### Authorization

[Bearer](../README.md#Bearer), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | The client request was invalid. One or more request parameters or the request body was rejected. Additional information may be found in the response. |  -  |
**401** | Request authentication missing or invalid |  -  |
**403** | User is not authorized to access requested resource |  -  |
**404** | The requested resource could not be found. |  -  |
**500** | Internal server error |  -  |
**503** | Kafka service unavailable |  -  |
**200** | The consumer group offsets have been reset. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

