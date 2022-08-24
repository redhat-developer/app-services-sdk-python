# rhoas_kafka_mgmt_sdk.SecurityApi

All URIs are relative to *https://api.openshift.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_account**](SecurityApi.md#create_service_account) | **POST** /api/kafkas_mgmt/v1/service_accounts | 
[**delete_service_account_by_id**](SecurityApi.md#delete_service_account_by_id) | **DELETE** /api/kafkas_mgmt/v1/service_accounts/{id} | 
[**get_service_account_by_id**](SecurityApi.md#get_service_account_by_id) | **GET** /api/kafkas_mgmt/v1/service_accounts/{id} | 
[**get_service_accounts**](SecurityApi.md#get_service_accounts) | **GET** /api/kafkas_mgmt/v1/service_accounts | 
[**get_sso_providers**](SecurityApi.md#get_sso_providers) | **GET** /api/kafkas_mgmt/v1/sso_providers | 
[**reset_service_account_creds**](SecurityApi.md#reset_service_account_creds) | **POST** /api/kafkas_mgmt/v1/service_accounts/{id}/reset_credentials | 


# **create_service_account**
> ServiceAccount create_service_account(service_account_request)



Creates a service account

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_kafka_mgmt_sdk
from rhoas_kafka_mgmt_sdk.api import security_api
from rhoas_kafka_mgmt_sdk.model.error import Error
from rhoas_kafka_mgmt_sdk.model.service_account import ServiceAccount
from rhoas_kafka_mgmt_sdk.model.service_account_request import ServiceAccountRequest
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
    api_instance = security_api.SecurityApi(api_client)
    service_account_request = ServiceAccountRequest(
        name="name_example",
        description="description_example",
    ) # ServiceAccountRequest | Service account request

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_service_account(service_account_request)
        pprint(api_response)
    except rhoas_kafka_mgmt_sdk.ApiException as e:
        print("Exception when calling SecurityApi->create_service_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_request** | [**ServiceAccountRequest**](ServiceAccountRequest.md)| Service account request |

### Return type

[**ServiceAccount**](ServiceAccount.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service account created |  -  |
**401** | Auth token is invalid |  -  |
**403** | List of service accounts |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_account_by_id**
> Error delete_service_account_by_id(id)



Deletes a service account by ID

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_kafka_mgmt_sdk
from rhoas_kafka_mgmt_sdk.api import security_api
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
    api_instance = security_api.SecurityApi(api_client)
    id = "id_example" # str | The ID of record

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_service_account_by_id(id)
        pprint(api_response)
    except rhoas_kafka_mgmt_sdk.ApiException as e:
        print("Exception when calling SecurityApi->delete_service_account_by_id: %s\n" % e)
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
**403** | User not authorized to access the service |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_account_by_id**
> ServiceAccount get_service_account_by_id(id)



Returned service account by ID

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_kafka_mgmt_sdk
from rhoas_kafka_mgmt_sdk.api import security_api
from rhoas_kafka_mgmt_sdk.model.service_account import ServiceAccount
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
    api_instance = security_api.SecurityApi(api_client)
    id = "id_example" # str | The ID of record

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_service_account_by_id(id)
        pprint(api_response)
    except rhoas_kafka_mgmt_sdk.ApiException as e:
        print("Exception when calling SecurityApi->get_service_account_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of record |

### Return type

[**ServiceAccount**](ServiceAccount.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a service account by ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_accounts**
> ServiceAccountList get_service_accounts()



Returns a list of service accounts

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_kafka_mgmt_sdk
from rhoas_kafka_mgmt_sdk.api import security_api
from rhoas_kafka_mgmt_sdk.model.error import Error
from rhoas_kafka_mgmt_sdk.model.service_account_list import ServiceAccountList
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
    api_instance = security_api.SecurityApi(api_client)
    client_id = "client_id_example" # str | client_id of the service account to be retrieved (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_service_accounts(client_id=client_id)
        pprint(api_response)
    except rhoas_kafka_mgmt_sdk.ApiException as e:
        print("Exception when calling SecurityApi->get_service_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| client_id of the service account to be retrieved | [optional]

### Return type

[**ServiceAccountList**](ServiceAccountList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned list of service accounts |  -  |
**401** | Auth token is invalid |  -  |
**403** | User not authorized to access the service |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sso_providers**
> SsoProvider get_sso_providers()



Return sso provider info

### Example


```python
import time
import rhoas_kafka_mgmt_sdk
from rhoas_kafka_mgmt_sdk.api import security_api
from rhoas_kafka_mgmt_sdk.model.error import Error
from rhoas_kafka_mgmt_sdk.model.sso_provider import SsoProvider
from pprint import pprint
# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    host = "https://api.openshift.com"
)


# Enter a context with an instance of the API client
with rhoas_kafka_mgmt_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = security_api.SecurityApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_sso_providers()
        pprint(api_response)
    except rhoas_kafka_mgmt_sdk.ApiException as e:
        print("Exception when calling SecurityApi->get_sso_providers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SsoProvider**](SsoProvider.md)

### Authorization

No authorization required

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

# **reset_service_account_creds**
> ServiceAccount reset_service_account_creds(id)



Resets the credentials for a service account by ID

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import rhoas_kafka_mgmt_sdk
from rhoas_kafka_mgmt_sdk.api import security_api
from rhoas_kafka_mgmt_sdk.model.error import Error
from rhoas_kafka_mgmt_sdk.model.service_account import ServiceAccount
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
    api_instance = security_api.SecurityApi(api_client)
    id = "id_example" # str | The ID of record

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.reset_service_account_creds(id)
        pprint(api_response)
    except rhoas_kafka_mgmt_sdk.ApiException as e:
        print("Exception when calling SecurityApi->reset_service_account_creds: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of record |

### Return type

[**ServiceAccount**](ServiceAccount.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reset credentials |  -  |
**401** | Auth token is invalid |  -  |
**403** | User not authorized to access the service |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

