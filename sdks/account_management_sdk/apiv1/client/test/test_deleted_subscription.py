"""
    Account Management Service API

    Manage user subscriptions and clusters  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import account_management_sdk
from account_management_sdk.model.deleted_subscription_all_of import DeletedSubscriptionAllOf
from account_management_sdk.model.subscription_common_fields import SubscriptionCommonFields
globals()['DeletedSubscriptionAllOf'] = DeletedSubscriptionAllOf
globals()['SubscriptionCommonFields'] = SubscriptionCommonFields
from account_management_sdk.model.deleted_subscription import DeletedSubscription


class TestDeletedSubscription(unittest.TestCase):
    """DeletedSubscription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDeletedSubscription(self):
        """Test DeletedSubscription"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DeletedSubscription()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()