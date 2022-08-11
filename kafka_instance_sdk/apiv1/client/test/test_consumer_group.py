"""
    Kafka Instance API

    API for interacting with Kafka Instance. Includes Produce, Consume and Admin APIs  # noqa: E501

    The version of the OpenAPI document: 0.12.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import kafka_instance_sdk
from kafka_instance_sdk.model.consumer import Consumer
from kafka_instance_sdk.model.consumer_group_all_of import ConsumerGroupAllOf
from kafka_instance_sdk.model.consumer_group_metrics import ConsumerGroupMetrics
from kafka_instance_sdk.model.consumer_group_state import ConsumerGroupState
from kafka_instance_sdk.model.object_reference import ObjectReference
globals()['Consumer'] = Consumer
globals()['ConsumerGroupAllOf'] = ConsumerGroupAllOf
globals()['ConsumerGroupMetrics'] = ConsumerGroupMetrics
globals()['ConsumerGroupState'] = ConsumerGroupState
globals()['ObjectReference'] = ObjectReference
from kafka_instance_sdk.model.consumer_group import ConsumerGroup


class TestConsumerGroup(unittest.TestCase):
    """ConsumerGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConsumerGroup(self):
        """Test ConsumerGroup"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ConsumerGroup()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
