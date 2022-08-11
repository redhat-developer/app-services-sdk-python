"""
    Kafka Instance API

    API for interacting with Kafka Instance. Includes Produce, Consume and Admin APIs  # noqa: E501

    The version of the OpenAPI document: 0.12.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import kafka_instance_sdk
from kafka_instance_sdk.model.list import List
from kafka_instance_sdk.model.record import Record
from kafka_instance_sdk.model.record_list_all_of import RecordListAllOf
globals()['List'] = List
globals()['Record'] = Record
globals()['RecordListAllOf'] = RecordListAllOf
from kafka_instance_sdk.model.record_list import RecordList


class TestRecordList(unittest.TestCase):
    """RecordList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRecordList(self):
        """Test RecordList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RecordList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
