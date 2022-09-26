# rhoas_kafka_instance_sdk.TopicsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_topic**](TopicsApi.md#create_topic) | **POST** /api/v1/topics | Creates a new topic
[**delete_topic**](TopicsApi.md#delete_topic) | **DELETE** /api/v1/topics/{topicName} | Deletes a topic
[**get_topic**](TopicsApi.md#get_topic) | **GET** /api/v1/topics/{topicName} | Retrieves a single topic
[**get_topics**](TopicsApi.md#get_topics) | **GET** /api/v1/topics | Retrieves a list of topics
[**update_topic**](TopicsApi.md#update_topic) | **PATCH** /api/v1/topics/{topicName} | Updates a single topic


# **create_topic**
> Topic create_topic(new_topic_input)

Creates a new topic

Creates a new topic for Kafka.

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth2):

```python
import time
import rhoas_kafka_instance_sdk
from rhoas_kafka_instance_sdk.api import topics_api
from rhoas_kafka_instance_sdk.model.new_topic_input import NewTopicInput
from rhoas_kafka_instance_sdk.model.error import Error
from rhoas_kafka_instance_sdk.model.topic import Topic
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
    api_instance = topics_api.TopicsApi(api_client)
    new_topic_input = NewTopicInput(
        name="o",
        settings=TopicSettings(
            num_partitions=1,
            config=[
                ConfigEntry(
                    key="o",
                    value="value_example",
                ),
            ],
        ),
    ) # NewTopicInput | Topic to create.

    # example passing only required values which don't have defaults set
    try:
        # Creates a new topic
        api_response = api_instance.create_topic(new_topic_input)
        pprint(api_response)
    except rhoas_kafka_instance_sdk.ApiException as e:
        print("Exception when calling TopicsApi->create_topic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_topic_input** | [**NewTopicInput**](NewTopicInput.md)| Topic to create. |

### Return type

[**Topic**](Topic.md)

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
**409** | The resource already exists. |  -  |
**500** | Internal server error |  -  |
**503** | Kafka service unavailable |  -  |
**201** | Topic created successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_topic**
> delete_topic(topic_name)

Deletes a topic

Deletes the topic with the specified name.

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth2):

```python
import time
import rhoas_kafka_instance_sdk
from rhoas_kafka_instance_sdk.api import topics_api
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
    api_instance = topics_api.TopicsApi(api_client)
    topic_name = "topicName_example" # str | Name of the topic to delete

    # example passing only required values which don't have defaults set
    try:
        # Deletes a topic
        api_instance.delete_topic(topic_name)
    except rhoas_kafka_instance_sdk.ApiException as e:
        print("Exception when calling TopicsApi->delete_topic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_name** | **str**| Name of the topic to delete |

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
**204** | Topic deleted successfully. |  -  |
**401** | Request authentication missing or invalid |  -  |
**403** | User is not authorized to access requested resource |  -  |
**404** | The requested resource could not be found. |  -  |
**500** | Internal server error |  -  |
**503** | Kafka service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic**
> Topic get_topic(topic_name)

Retrieves a single topic

Topic

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth2):

```python
import time
import rhoas_kafka_instance_sdk
from rhoas_kafka_instance_sdk.api import topics_api
from rhoas_kafka_instance_sdk.model.error import Error
from rhoas_kafka_instance_sdk.model.topic import Topic
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
    api_instance = topics_api.TopicsApi(api_client)
    topic_name = "topicName_example" # str | Name of the topic to describe

    # example passing only required values which don't have defaults set
    try:
        # Retrieves a single topic
        api_response = api_instance.get_topic(topic_name)
        pprint(api_response)
    except rhoas_kafka_instance_sdk.ApiException as e:
        print("Exception when calling TopicsApi->get_topic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_name** | **str**| Name of the topic to describe |

### Return type

[**Topic**](Topic.md)

### Authorization

[Bearer](../README.md#Bearer), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Request authentication missing or invalid |  -  |
**403** | User is not authorized to access requested resource |  -  |
**404** | The requested resource could not be found. |  -  |
**500** | Internal server error |  -  |
**503** | Kafka service unavailable |  -  |
**200** | Kafka topic details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topics**
> TopicsList get_topics()

Retrieves a list of topics

Returns a list of all of the available topics, or the list of topics that meet the request query parameters. The topics returned are limited to those records the requestor is authorized to view.

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth2):

```python
import time
import rhoas_kafka_instance_sdk
from rhoas_kafka_instance_sdk.api import topics_api
from rhoas_kafka_instance_sdk.model.sort_direction import SortDirection
from rhoas_kafka_instance_sdk.model.topics_list import TopicsList
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
    api_instance = topics_api.TopicsApi(api_client)
    offset = 0 # int | Offset of the first record to return, zero-based (optional)
    limit = 1 # int | Maximum number of records to return (optional)
    size = 1 # int | Number of records per page (optional)
    filter = "filter_example" # str | Filter to apply when returning the list of topics (optional)
    page = 1 # int | Page number (optional)
    order = SortDirection("asc") # SortDirection | Order items are sorted (optional)
    order_key = None # bool, date, datetime, dict, float, int, list, str, none_type | Order key to sort the topics by. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieves a list of topics
        api_response = api_instance.get_topics(offset=offset, limit=limit, size=size, filter=filter, page=page, order=order, order_key=order_key)
        pprint(api_response)
    except rhoas_kafka_instance_sdk.ApiException as e:
        print("Exception when calling TopicsApi->get_topics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset of the first record to return, zero-based | [optional]
 **limit** | **int**| Maximum number of records to return | [optional]
 **size** | **int**| Number of records per page | [optional]
 **filter** | **str**| Filter to apply when returning the list of topics | [optional]
 **page** | **int**| Page number | [optional]
 **order** | **SortDirection**| Order items are sorted | [optional]
 **order_key** | **bool, date, datetime, dict, float, int, list, str, none_type**| Order key to sort the topics by. | [optional]

### Return type

[**TopicsList**](TopicsList.md)

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
**500** | Internal server error |  -  |
**503** | Kafka service unavailable |  -  |
**200** | List of topics matching the request query parameters. The topics returned are limited to those records the requestor is authorized to view. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_topic**
> Topic update_topic(topic_name, topic_settings)

Updates a single topic

Update the configuration settings for a topic.

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth2):

```python
import time
import rhoas_kafka_instance_sdk
from rhoas_kafka_instance_sdk.api import topics_api
from rhoas_kafka_instance_sdk.model.topic_settings import TopicSettings
from rhoas_kafka_instance_sdk.model.error import Error
from rhoas_kafka_instance_sdk.model.topic import Topic
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
    api_instance = topics_api.TopicsApi(api_client)
    topic_name = "topicName_example" # str | Name of the topic to update
    topic_settings = TopicSettings(
        num_partitions=1,
        config=[
            ConfigEntry(
                key="o",
                value="value_example",
            ),
        ],
    ) # TopicSettings | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a single topic
        api_response = api_instance.update_topic(topic_name, topic_settings)
        pprint(api_response)
    except rhoas_kafka_instance_sdk.ApiException as e:
        print("Exception when calling TopicsApi->update_topic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_name** | **str**| Name of the topic to update |
 **topic_settings** | [**TopicSettings**](TopicSettings.md)|  |

### Return type

[**Topic**](Topic.md)

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
**200** | Topic updated successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

