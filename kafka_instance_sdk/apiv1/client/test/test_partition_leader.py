"""
    Kafka Instance API

    API for interacting with Kafka Instance. Includes Produce, Consume and Admin APIs  # noqa: E501

    The version of the OpenAPI document: 0.12.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import kafka_instance_sdk
from kafka_instance_sdk.model.node import Node
globals()['Node'] = Node
from kafka_instance_sdk.model.partition_leader import PartitionLeader


class TestPartitionLeader(unittest.TestCase):
    """PartitionLeader unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPartitionLeader(self):
        """Test PartitionLeader"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PartitionLeader()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
