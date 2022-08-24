"""
    Account Management Service API

    Manage user subscriptions and clusters  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import account_management_sdk
from account_management_sdk.model.cloud_account import CloudAccount
from account_management_sdk.model.object_reference import ObjectReference
from account_management_sdk.model.quota_cost_all_of import QuotaCostAllOf
from account_management_sdk.model.related_resource import RelatedResource
globals()['CloudAccount'] = CloudAccount
globals()['ObjectReference'] = ObjectReference
globals()['QuotaCostAllOf'] = QuotaCostAllOf
globals()['RelatedResource'] = RelatedResource
from account_management_sdk.model.quota_cost import QuotaCost


class TestQuotaCost(unittest.TestCase):
    """QuotaCost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testQuotaCost(self):
        """Test QuotaCost"""
        # FIXME: construct object with mandatory attributes with example values
        # model = QuotaCost()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()