# rhoas_kafka_instance_sdk.ErrorsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_error**](ErrorsApi.md#get_error) | **GET** /api/v1/errors/{errorId} | Get an error by its unique ID
[**get_errors**](ErrorsApi.md#get_errors) | **GET** /api/v1/errors | Get list of errors


# **get_error**
> Error get_error(error_id)

Get an error by its unique ID

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth2):

```python
import time
import rhoas_kafka_instance_sdk
from rhoas_kafka_instance_sdk.api import errors_api
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
    api_instance = errors_api.ErrorsApi(api_client)
    error_id = "errorId_example" # str | Error identifier

    # example passing only required values which don't have defaults set
    try:
        # Get an error by its unique ID
        api_response = api_instance.get_error(error_id)
        pprint(api_response)
    except rhoas_kafka_instance_sdk.ApiException as e:
        print("Exception when calling ErrorsApi->get_error: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **error_id** | **str**| Error identifier |

### Return type

[**Error**](Error.md)

### Authorization

[Bearer](../README.md#Bearer), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Error details |  -  |
**404** | The requested resource could not be found. |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_errors**
> ErrorList get_errors()

Get list of errors

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth2):

```python
import time
import rhoas_kafka_instance_sdk
from rhoas_kafka_instance_sdk.api import errors_api
from rhoas_kafka_instance_sdk.model.error import Error
from rhoas_kafka_instance_sdk.model.error_list import ErrorList
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
    api_instance = errors_api.ErrorsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get list of errors
        api_response = api_instance.get_errors()
        pprint(api_response)
    except rhoas_kafka_instance_sdk.ApiException as e:
        print("Exception when calling ErrorsApi->get_errors: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ErrorList**](ErrorList.md)

### Authorization

[Bearer](../README.md#Bearer), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Error listing |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

