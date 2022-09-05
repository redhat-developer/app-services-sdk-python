# create a kafka client
import time
import rhoas_kafka_mgmt_sdk
from pprint import pprint
from rhoas_kafka_mgmt_sdk.api import default_api
from rhoas_kafka_mgmt_sdk.model.cloud_provider_list import CloudProviderList
from rhoas_kafka_mgmt_sdk.model.cloud_region_list import CloudRegionList
from rhoas_kafka_mgmt_sdk.model.error import Error
from rhoas_kafka_mgmt_sdk.model.kafka_request import KafkaRequest
from rhoas_kafka_mgmt_sdk.model.kafka_request_list import KafkaRequestList
from rhoas_kafka_mgmt_sdk.model.kafka_request_payload import KafkaRequestPayload
from rhoas_kafka_mgmt_sdk.model.kafka_update_request import KafkaUpdateRequest
from rhoas_kafka_mgmt_sdk.model.metrics_instant_query_list import MetricsInstantQueryList
from rhoas_kafka_mgmt_sdk.model.metrics_range_query_list import MetricsRangeQueryList
from rhoas_kafka_mgmt_sdk.model.supported_kafka_instance_types_list import SupportedKafkaInstanceTypesList
from rhoas_kafka_mgmt_sdk.model.version_metadata import VersionMetadata
import os
from auth import rhoas_auth as auth


# Defining the host is optional and defaults to https://api.openshift.com
# See configuration.py for a list of all supported configuration parameters.

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rhoas_kafka_mgmt_sdk.Configuration(
    host = "https://api.openshift.com",
)

configuration.access_token = auth.get_access_token() 

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
        