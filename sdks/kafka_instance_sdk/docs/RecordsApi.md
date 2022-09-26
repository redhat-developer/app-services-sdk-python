# rhoas_kafka_instance_sdk.RecordsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consume_records**](RecordsApi.md#consume_records) | **GET** /api/v1/topics/{topicName}/records | Consume records from a topic
[**produce_record**](RecordsApi.md#produce_record) | **POST** /api/v1/topics/{topicName}/records | Send a record to a topic


# **consume_records**
> RecordList consume_records(topic_name)

Consume records from a topic

Consume a limited number of records from a topic, optionally specifying a partition and an absolute offset or timestamp as the starting point for message retrieval.

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth2):

```python
import time
import rhoas_kafka_instance_sdk
from rhoas_kafka_instance_sdk.api import records_api
from rhoas_kafka_instance_sdk.model.record_included_property import RecordIncludedProperty
from rhoas_kafka_instance_sdk.model.record_list import RecordList
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
    api_instance = records_api.RecordsApi(api_client)
    topic_name = "topicName_example" # str | Topic name
    include = [
        RecordIncludedProperty("partition"),
    ] # [RecordIncludedProperty] | List of properties to include for each record in the response (optional)
    limit = 1 # int | Limit the number of records fetched and returned (optional)
    max_value_length = 1 # int | Maximum length of string values returned in the response. Values with a length that exceeds this parameter will be truncated. When this parameter is not included in the request, the full string values will be returned. (optional)
    offset = 0 # int | Retrieve messages with an offset equal to or greater than this offset. If both `timestamp` and `offset` are requested, `timestamp` is given preference. (optional)
    partition = 1 # int | Retrieve messages only from this partition (optional)
    timestamp = None # bool, date, datetime, dict, float, int, list, str, none_type | Retrieve messages with a timestamp equal to or later than this timestamp. If both `timestamp` and `offset` are requested, `timestamp` is given preference. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Consume records from a topic
        api_response = api_instance.consume_records(topic_name)
        pprint(api_response)
    except rhoas_kafka_instance_sdk.ApiException as e:
        print("Exception when calling RecordsApi->consume_records: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Consume records from a topic
        api_response = api_instance.consume_records(topic_name, include=include, limit=limit, max_value_length=max_value_length, offset=offset, partition=partition, timestamp=timestamp)
        pprint(api_response)
    except rhoas_kafka_instance_sdk.ApiException as e:
        print("Exception when calling RecordsApi->consume_records: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_name** | **str**| Topic name |
 **include** | [**[RecordIncludedProperty]**](RecordIncludedProperty.md)| List of properties to include for each record in the response | [optional]
 **limit** | **int**| Limit the number of records fetched and returned | [optional]
 **max_value_length** | **int**| Maximum length of string values returned in the response. Values with a length that exceeds this parameter will be truncated. When this parameter is not included in the request, the full string values will be returned. | [optional]
 **offset** | **int**| Retrieve messages with an offset equal to or greater than this offset. If both &#x60;timestamp&#x60; and &#x60;offset&#x60; are requested, &#x60;timestamp&#x60; is given preference. | [optional]
 **partition** | **int**| Retrieve messages only from this partition | [optional]
 **timestamp** | **bool, date, datetime, dict, float, int, list, str, none_type**| Retrieve messages with a timestamp equal to or later than this timestamp. If both &#x60;timestamp&#x60; and &#x60;offset&#x60; are requested, &#x60;timestamp&#x60; is given preference. | [optional]

### Return type

[**RecordList**](RecordList.md)

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
**200** | List of records matching the request query parameters. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **produce_record**
> Record produce_record(topic_name, record)

Send a record to a topic

Produce (write) a single record to a topic.

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth2):

```python
import time
import rhoas_kafka_instance_sdk
from rhoas_kafka_instance_sdk.api import records_api
from rhoas_kafka_instance_sdk.model.record import Record
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
    api_instance = records_api.RecordsApi(api_client)
    topic_name = "topicName_example" # str | Topic name
    record = Record(None) # Record | 

    # example passing only required values which don't have defaults set
    try:
        # Send a record to a topic
        api_response = api_instance.produce_record(topic_name, record)
        pprint(api_response)
    except rhoas_kafka_instance_sdk.ApiException as e:
        print("Exception when calling RecordsApi->produce_record: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_name** | **str**| Topic name |
 **record** | [**Record**](Record.md)|  |

### Return type

[**Record**](Record.md)

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
**500** | Internal server error |  -  |
**503** | Kafka service unavailable |  -  |
**201** | Record was successfully sent to the topic |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

