"""
    Kafka Management API

    Kafka Management API is a REST API to manage Kafka instances  # noqa: E501

    The version of the OpenAPI document: 1.11.0
    Contact: rhosak-support@redhat.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import rhoas_kafka_mgmt_sdk
from rhoas_kafka_mgmt_sdk.model.supported_kafka_instance_type import SupportedKafkaInstanceType
from rhoas_kafka_mgmt_sdk.model.supported_kafka_instance_types_list_all_of import SupportedKafkaInstanceTypesListAllOf
globals()['SupportedKafkaInstanceType'] = SupportedKafkaInstanceType
globals()['SupportedKafkaInstanceTypesListAllOf'] = SupportedKafkaInstanceTypesListAllOf
from rhoas_kafka_mgmt_sdk.model.supported_kafka_instance_types_list import SupportedKafkaInstanceTypesList


class TestSupportedKafkaInstanceTypesList(unittest.TestCase):
    """SupportedKafkaInstanceTypesList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSupportedKafkaInstanceTypesList(self):
        """Test SupportedKafkaInstanceTypesList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SupportedKafkaInstanceTypesList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()