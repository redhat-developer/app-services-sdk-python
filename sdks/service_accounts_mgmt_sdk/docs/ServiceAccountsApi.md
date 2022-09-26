# rhoas_service_accounts_mgmt_sdk.ServiceAccountsApi

All URIs are relative to *https://sso.redhat.com/auth/realms/redhat-external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_account**](ServiceAccountsApi.md#create_service_account) | **POST** /apis/service_accounts/v1 | Create service account
[**delete_service_account**](ServiceAccountsApi.md#delete_service_account) | **DELETE** /apis/service_accounts/v1/{id} | Delete service account by id
[**get_service_account**](ServiceAccountsApi.md#get_service_account) | **GET** /apis/service_accounts/v1/{id} | Get service account by id
[**get_service_accounts**](ServiceAccountsApi.md#get_service_accounts) | **GET** /apis/service_accounts/v1 | List all service accounts
[**reset_service_account_secret**](ServiceAccountsApi.md#reset_service_account_secret) | **POST** /apis/service_accounts/v1/{id}/resetSecret | Reset service account secret by id
[**update_service_account**](ServiceAccountsApi.md#update_service_account) | **PATCH** /apis/service_accounts/v1/{id} | Update service account


# **create_service_account**
> ServiceAccountData create_service_account(service_account_create_request_data)

Create service account

Create a service account. Created service account is associated with the user defined in the bearer token.

### Example

* OAuth Authentication (authFlow):
* OAuth Authentication (serviceAccounts):

```python
import time
import rhoas_service_accounts_mgmt_sdk
from rhoas_service_accounts_mgmt_sdk.api import service_accounts_api
from rhoas_service_accounts_mgmt_sdk.model.service_account_data import ServiceAccountData
from rhoas_service_accounts_mgmt_sdk.model.error import Error
from rhoas_service_accounts_mgmt_sdk.model.red_hat_error_representation import RedHatErrorRepresentation
from rhoas_service_accounts_mgmt_sdk.model.validation_exception_data import ValidationExceptionData
from rhoas_service_accounts_mgmt_sdk.model.service_account_create_request_data import ServiceAccountCreateRequestData
from pprint import pprint
# Defining the host is optional and defaults to https://sso.redhat.com/auth/realms/redhat-external
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_service_accounts_mgmt_sdk.Configuration(
    host = "https://sso.redhat.com/auth/realms/redhat-external"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: authFlow
configuration = rhoas_service_accounts_mgmt_sdk.Configuration(
    host = "https://sso.redhat.com/auth/realms/redhat-external"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: serviceAccounts
configuration = rhoas_service_accounts_mgmt_sdk.Configuration(
    host = "https://sso.redhat.com/auth/realms/redhat-external"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with rhoas_service_accounts_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_accounts_api.ServiceAccountsApi(api_client)
    service_account_create_request_data = ServiceAccountCreateRequestData(
        name="name_example",
        description="description_example",
    ) # ServiceAccountCreateRequestData | 'name' and 'description' of the service account

    # example passing only required values which don't have defaults set
    try:
        # Create service account
        api_response = api_instance.create_service_account(service_account_create_request_data)
        pprint(api_response)
    except rhoas_service_accounts_mgmt_sdk.ApiException as e:
        print("Exception when calling ServiceAccountsApi->create_service_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_create_request_data** | [**ServiceAccountCreateRequestData**](ServiceAccountCreateRequestData.md)| &#39;name&#39; and &#39;description&#39; of the service account |

### Return type

[**ServiceAccountData**](ServiceAccountData.md)

### Authorization

[authFlow](../README.md#authFlow), [serviceAccounts](../README.md#serviceAccounts)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | All fields did not pass validation. |  -  |
**401** | Unauthorized |  -  |
**403** | Exceeded account level threshold limits for creating service accounts. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_account**
> delete_service_account(id)

Delete service account by id

Delete service account by id. Throws not found exception if the service account is not found or the user does not have access to this service account

### Example

* OAuth Authentication (authFlow):
* OAuth Authentication (serviceAccounts):

```python
import time
import rhoas_service_accounts_mgmt_sdk
from rhoas_service_accounts_mgmt_sdk.api import service_accounts_api
from rhoas_service_accounts_mgmt_sdk.model.error import Error
from rhoas_service_accounts_mgmt_sdk.model.red_hat_error_representation import RedHatErrorRepresentation
from pprint import pprint
# Defining the host is optional and defaults to https://sso.redhat.com/auth/realms/redhat-external
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_service_accounts_mgmt_sdk.Configuration(
    host = "https://sso.redhat.com/auth/realms/redhat-external"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: authFlow
configuration = rhoas_service_accounts_mgmt_sdk.Configuration(
    host = "https://sso.redhat.com/auth/realms/redhat-external"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: serviceAccounts
configuration = rhoas_service_accounts_mgmt_sdk.Configuration(
    host = "https://sso.redhat.com/auth/realms/redhat-external"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with rhoas_service_accounts_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_accounts_api.ServiceAccountsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete service account by id
        api_instance.delete_service_account(id)
    except rhoas_service_accounts_mgmt_sdk.ApiException as e:
        print("Exception when calling ServiceAccountsApi->delete_service_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[authFlow](../README.md#authFlow), [serviceAccounts](../README.md#serviceAccounts)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_account**
> ServiceAccountData get_service_account(id)

Get service account by id

Returns service account by id. Throws not found exception if the service account is not found or the user does not have access to this service account

### Example

* OAuth Authentication (authFlow):
* OAuth Authentication (serviceAccounts):

```python
import time
import rhoas_service_accounts_mgmt_sdk
from rhoas_service_accounts_mgmt_sdk.api import service_accounts_api
from rhoas_service_accounts_mgmt_sdk.model.service_account_data import ServiceAccountData
from rhoas_service_accounts_mgmt_sdk.model.error import Error
from rhoas_service_accounts_mgmt_sdk.model.red_hat_error_representation import RedHatErrorRepresentation
from pprint import pprint
# Defining the host is optional and defaults to https://sso.redhat.com/auth/realms/redhat-external
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_service_accounts_mgmt_sdk.Configuration(
    host = "https://sso.redhat.com/auth/realms/redhat-external"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: authFlow
configuration = rhoas_service_accounts_mgmt_sdk.Configuration(
    host = "https://sso.redhat.com/auth/realms/redhat-external"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: serviceAccounts
configuration = rhoas_service_accounts_mgmt_sdk.Configuration(
    host = "https://sso.redhat.com/auth/realms/redhat-external"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with rhoas_service_accounts_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_accounts_api.ServiceAccountsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get service account by id
        api_response = api_instance.get_service_account(id)
        pprint(api_response)
    except rhoas_service_accounts_mgmt_sdk.ApiException as e:
        print("Exception when calling ServiceAccountsApi->get_service_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ServiceAccountData**](ServiceAccountData.md)

### Authorization

[authFlow](../README.md#authFlow), [serviceAccounts](../README.md#serviceAccounts)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_accounts**
> [ServiceAccountData] get_service_accounts()

List all service accounts

Returns a list of service accounts created by a user. User information is obtained from the bearer token. The list is paginated with starting index as 'first' and page size as 'max'.

### Example

* OAuth Authentication (authFlow):
* OAuth Authentication (serviceAccounts):

```python
import time
import rhoas_service_accounts_mgmt_sdk
from rhoas_service_accounts_mgmt_sdk.api import service_accounts_api
from rhoas_service_accounts_mgmt_sdk.model.service_account_data import ServiceAccountData
from rhoas_service_accounts_mgmt_sdk.model.error import Error
from rhoas_service_accounts_mgmt_sdk.model.validation_exception_data import ValidationExceptionData
from pprint import pprint
# Defining the host is optional and defaults to https://sso.redhat.com/auth/realms/redhat-external
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_service_accounts_mgmt_sdk.Configuration(
    host = "https://sso.redhat.com/auth/realms/redhat-external"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: authFlow
configuration = rhoas_service_accounts_mgmt_sdk.Configuration(
    host = "https://sso.redhat.com/auth/realms/redhat-external"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: serviceAccounts
configuration = rhoas_service_accounts_mgmt_sdk.Configuration(
    host = "https://sso.redhat.com/auth/realms/redhat-external"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with rhoas_service_accounts_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_accounts_api.ServiceAccountsApi(api_client)
    first = 0 # int |  (optional) if omitted the server will use the default value of 0
    max = 20 # int |  (optional) if omitted the server will use the default value of 20
    client_id = [
        "clientId_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all service accounts
        api_response = api_instance.get_service_accounts(first=first, max=max, client_id=client_id)
        pprint(api_response)
    except rhoas_service_accounts_mgmt_sdk.ApiException as e:
        print("Exception when calling ServiceAccountsApi->get_service_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first** | **int**|  | [optional] if omitted the server will use the default value of 0
 **max** | **int**|  | [optional] if omitted the server will use the default value of 20
 **client_id** | **[str]**|  | [optional]

### Return type

[**[ServiceAccountData]**](ServiceAccountData.md)

### Authorization

[authFlow](../README.md#authFlow), [serviceAccounts](../README.md#serviceAccounts)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request if page filters are invalid |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_service_account_secret**
> ServiceAccountData reset_service_account_secret(id)

Reset service account secret by id

Reset service account secret by id . Throws not found exception if the service account is not found or the user does not have access to this service account

### Example

* OAuth Authentication (authFlow):
* OAuth Authentication (serviceAccounts):

```python
import time
import rhoas_service_accounts_mgmt_sdk
from rhoas_service_accounts_mgmt_sdk.api import service_accounts_api
from rhoas_service_accounts_mgmt_sdk.model.service_account_data import ServiceAccountData
from rhoas_service_accounts_mgmt_sdk.model.error import Error
from rhoas_service_accounts_mgmt_sdk.model.red_hat_error_representation import RedHatErrorRepresentation
from pprint import pprint
# Defining the host is optional and defaults to https://sso.redhat.com/auth/realms/redhat-external
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_service_accounts_mgmt_sdk.Configuration(
    host = "https://sso.redhat.com/auth/realms/redhat-external"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: authFlow
configuration = rhoas_service_accounts_mgmt_sdk.Configuration(
    host = "https://sso.redhat.com/auth/realms/redhat-external"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: serviceAccounts
configuration = rhoas_service_accounts_mgmt_sdk.Configuration(
    host = "https://sso.redhat.com/auth/realms/redhat-external"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with rhoas_service_accounts_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_accounts_api.ServiceAccountsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Reset service account secret by id
        api_response = api_instance.reset_service_account_secret(id)
        pprint(api_response)
    except rhoas_service_accounts_mgmt_sdk.ApiException as e:
        print("Exception when calling ServiceAccountsApi->reset_service_account_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ServiceAccountData**](ServiceAccountData.md)

### Authorization

[authFlow](../README.md#authFlow), [serviceAccounts](../README.md#serviceAccounts)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_account**
> ServiceAccountData update_service_account(id, service_account_request_data)

Update service account

Update a service account by id.

### Example

* OAuth Authentication (authFlow):
* OAuth Authentication (serviceAccounts):

```python
import time
import rhoas_service_accounts_mgmt_sdk
from rhoas_service_accounts_mgmt_sdk.api import service_accounts_api
from rhoas_service_accounts_mgmt_sdk.model.service_account_data import ServiceAccountData
from rhoas_service_accounts_mgmt_sdk.model.service_account_request_data import ServiceAccountRequestData
from rhoas_service_accounts_mgmt_sdk.model.error import Error
from rhoas_service_accounts_mgmt_sdk.model.red_hat_error_representation import RedHatErrorRepresentation
from rhoas_service_accounts_mgmt_sdk.model.validation_exception_data import ValidationExceptionData
from pprint import pprint
# Defining the host is optional and defaults to https://sso.redhat.com/auth/realms/redhat-external
# See configuration.py for a list of all supported configuration parameters.
configuration = rhoas_service_accounts_mgmt_sdk.Configuration(
    host = "https://sso.redhat.com/auth/realms/redhat-external"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: authFlow
configuration = rhoas_service_accounts_mgmt_sdk.Configuration(
    host = "https://sso.redhat.com/auth/realms/redhat-external"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: serviceAccounts
configuration = rhoas_service_accounts_mgmt_sdk.Configuration(
    host = "https://sso.redhat.com/auth/realms/redhat-external"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with rhoas_service_accounts_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_accounts_api.ServiceAccountsApi(api_client)
    id = "id_example" # str | 
    service_account_request_data = ServiceAccountRequestData(
        name="name_example",
        description="description_example",
    ) # ServiceAccountRequestData | 'name' and 'description' of the service account

    # example passing only required values which don't have defaults set
    try:
        # Update service account
        api_response = api_instance.update_service_account(id, service_account_request_data)
        pprint(api_response)
    except rhoas_service_accounts_mgmt_sdk.ApiException as e:
        print("Exception when calling ServiceAccountsApi->update_service_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **service_account_request_data** | [**ServiceAccountRequestData**](ServiceAccountRequestData.md)| &#39;name&#39; and &#39;description&#39; of the service account |

### Return type

[**ServiceAccountData**](ServiceAccountData.md)

### Authorization

[authFlow](../README.md#authFlow), [serviceAccounts](../README.md#serviceAccounts)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

