# rhoas-service-accounts-mgmt-sdk
This is the API documentation for Service Accounts

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 5.0.19
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

The package is hosted on [PyPI](https://pypi.org/project/rhoas-sdks/), you can install directly using:

```sh
pip install rhoas-sdks
```

Then import the package:
```python
import rhoas_service_accounts_mgmt_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import rhoas_service_accounts_mgmt_sdk
from pprint import pprint
from rhoas_service_accounts_mgmt_sdk.api import service_accounts_api
from rhoas_service_accounts_mgmt_sdk.model.error import Error
from rhoas_service_accounts_mgmt_sdk.model.red_hat_error_representation import RedHatErrorRepresentation
from rhoas_service_accounts_mgmt_sdk.model.service_account_create_request_data import ServiceAccountCreateRequestData
from rhoas_service_accounts_mgmt_sdk.model.service_account_data import ServiceAccountData
from rhoas_service_accounts_mgmt_sdk.model.service_account_request_data import ServiceAccountRequestData
from rhoas_service_accounts_mgmt_sdk.model.validation_exception_data import ValidationExceptionData
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

    try:
        # Create service account
        api_response = api_instance.create_service_account(service_account_create_request_data)
        pprint(api_response)
    except rhoas_service_accounts_mgmt_sdk.ApiException as e:
        print("Exception when calling ServiceAccountsApi->create_service_account: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://sso.redhat.com/auth/realms/redhat-external*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ServiceAccountsApi* | [**create_service_account**](docs/ServiceAccountsApi.md#create_service_account) | **POST** /apis/service_accounts/v1 | Create service account
*ServiceAccountsApi* | [**delete_service_account**](docs/ServiceAccountsApi.md#delete_service_account) | **DELETE** /apis/service_accounts/v1/{id} | Delete service account by id
*ServiceAccountsApi* | [**get_service_account**](docs/ServiceAccountsApi.md#get_service_account) | **GET** /apis/service_accounts/v1/{id} | Get service account by id
*ServiceAccountsApi* | [**get_service_accounts**](docs/ServiceAccountsApi.md#get_service_accounts) | **GET** /apis/service_accounts/v1 | List all service accounts
*ServiceAccountsApi* | [**reset_service_account_secret**](docs/ServiceAccountsApi.md#reset_service_account_secret) | **POST** /apis/service_accounts/v1/{id}/resetSecret | Reset service account secret by id
*ServiceAccountsApi* | [**update_service_account**](docs/ServiceAccountsApi.md#update_service_account) | **PATCH** /apis/service_accounts/v1/{id} | Update service account


## Documentation For Models

 - [Error](docs/Error.md)
 - [RedHatErrorRepresentation](docs/RedHatErrorRepresentation.md)
 - [ServiceAccountCreateRequestData](docs/ServiceAccountCreateRequestData.md)
 - [ServiceAccountData](docs/ServiceAccountData.md)
 - [ServiceAccountRequestData](docs/ServiceAccountRequestData.md)
 - [ValidationExceptionData](docs/ValidationExceptionData.md)


## Documentation For Authorization


## authFlow

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: /auth/realms/redhat-external/protocol/openid-connect/auth
- **Scopes**: 
 - **openid**: Treat as an OIDC request
 - **api.iam.service_accounts**: Grants access to the service accounts api


## bearerAuth

- **Type**: Bearer authentication (JWT)


## serviceAccounts

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 
 - **openid**: Treat as an OIDC request
 - **api.iam.service_accounts**: Grants access to the service accounts api


## Author

it-user-team-list@redhat.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in rhoas_service_accounts_mgmt_sdk.apis and rhoas_service_accounts_mgmt_sdk.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from rhoas_service_accounts_mgmt_sdk.api.default_api import DefaultApi`
- `from rhoas_service_accounts_mgmt_sdk.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import rhoas_service_accounts_mgmt_sdk
from rhoas_service_accounts_mgmt_sdk.apis import *
from rhoas_service_accounts_mgmt_sdk.models import *
```

