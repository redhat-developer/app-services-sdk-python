"""
    Account Management Service API

    Manage user subscriptions and clusters  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import account_management_sdk
from account_management_sdk.model.object_reference import ObjectReference
from account_management_sdk.model.summary_all_of import SummaryAllOf
from account_management_sdk.model.summary_metrics import SummaryMetrics
globals()['ObjectReference'] = ObjectReference
globals()['SummaryAllOf'] = SummaryAllOf
globals()['SummaryMetrics'] = SummaryMetrics
from account_management_sdk.model.summary import Summary


class TestSummary(unittest.TestCase):
    """Summary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSummary(self):
        """Test Summary"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Summary()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
