# kafka_mgmt_client.ErrorsApi

All URIs are relative to *https://api.openshift.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_error_by_id**](ErrorsApi.md#get_error_by_id) | **GET** /api/kafkas_mgmt/v1/errors/{id} | 
[**get_errors**](ErrorsApi.md#get_errors) | **GET** /api/kafkas_mgmt/v1/errors | 


# **get_error_by_id**
> Error get_error_by_id(id)



Returns the error by Id

### Example


```python
import time
import kafka_mgmt_client
from kafka_mgmt_client.api import errors_api
from kafka_mgmt_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = kafka_mgmt_client.Configuration(
    host = "https://api.openshift.com"
)


# Enter a context with an instance of the API client
with kafka_mgmt_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = errors_api.ErrorsApi(api_client)
    id = "id_example" # str | The ID of record

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_error_by_id(id)
        pprint(api_response)
    except kafka_mgmt_client.ApiException as e:
        print("Exception when calling ErrorsApi->get_error_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of record |

### Return type

[**Error**](Error.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get error by Id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_errors**
> ErrorList get_errors()



Returns the list of possible API errors

### Example


```python
import time
import kafka_mgmt_client
from kafka_mgmt_client.api import errors_api
from kafka_mgmt_client.model.error_list import ErrorList
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = kafka_mgmt_client.Configuration(
    host = "https://api.openshift.com"
)


# Enter a context with an instance of the API client
with kafka_mgmt_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = errors_api.ErrorsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_errors()
        pprint(api_response)
    except kafka_mgmt_client.ApiException as e:
        print("Exception when calling ErrorsApi->get_errors: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ErrorList**](ErrorList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of possible errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
