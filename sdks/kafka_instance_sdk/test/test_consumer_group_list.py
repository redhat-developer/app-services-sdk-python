"""
    Kafka Instance API

    API for interacting with Kafka Instance. Includes Produce, Consume and Admin APIs  # noqa: E501

    The version of the OpenAPI document: 0.12.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import rhoas_kafka_instance_sdk
from rhoas_kafka_instance_sdk.model.consumer_group import ConsumerGroup
from rhoas_kafka_instance_sdk.model.consumer_group_list_all_of import ConsumerGroupListAllOf
from rhoas_kafka_instance_sdk.model.list_deprecated import ListDeprecated
globals()['ConsumerGroup'] = ConsumerGroup
globals()['ConsumerGroupListAllOf'] = ConsumerGroupListAllOf
globals()['ListDeprecated'] = ListDeprecated
from rhoas_kafka_instance_sdk.model.consumer_group_list import ConsumerGroupList


class TestConsumerGroupList(unittest.TestCase):
    """ConsumerGroupList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConsumerGroupList(self):
        """Test ConsumerGroupList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ConsumerGroupList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()