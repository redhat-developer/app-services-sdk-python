"""
    Account Management Service API

    Manage user subscriptions and clusters  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import account_management_sdk
from account_management_sdk.model.deleted_subscription import DeletedSubscription
from account_management_sdk.model.deleted_subscription_list_all_of import DeletedSubscriptionListAllOf
from account_management_sdk.model.list import List
globals()['DeletedSubscription'] = DeletedSubscription
globals()['DeletedSubscriptionListAllOf'] = DeletedSubscriptionListAllOf
globals()['List'] = List
from account_management_sdk.model.deleted_subscription_list import DeletedSubscriptionList


class TestDeletedSubscriptionList(unittest.TestCase):
    """DeletedSubscriptionList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDeletedSubscriptionList(self):
        """Test DeletedSubscriptionList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DeletedSubscriptionList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
