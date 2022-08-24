import rhoas_kafka_mgmt_sdk
from pprint import pprint
from rhoas_kafka_mgmt_sdk.api import default_api

import os

ACCESS_TOKEN = os.environ['ACCESS_TOKEN'] 

# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration = rhoas_kafka_mgmt_sdk.Configuration(
    host = "https://api.openshift.com",
    access_token = ACCESS_TOKEN
)



# Enter a context with an instance of the API client
with rhoas_kafka_mgmt_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    try:
        api_response = api_instance.get_kafkas()
        pprint(api_response)
    except rhoas_kafka_mgmt_sdk.ApiException as e:
        print("Exception when calling DefaultApi->create_kafka: %s\n" % e)
    except Exception as excep:
        print(f'Exception {excep:}')