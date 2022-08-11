"""
    Account Management Service API

    Manage user subscriptions and clusters  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import account_management_sdk
from account_management_sdk.model.account import Account
from account_management_sdk.model.account_reference import AccountReference
from account_management_sdk.model.capability import Capability
from account_management_sdk.model.label import Label
from account_management_sdk.model.one_metric import OneMetric
from account_management_sdk.model.plan import Plan
globals()['Account'] = Account
globals()['AccountReference'] = AccountReference
globals()['Capability'] = Capability
globals()['Label'] = Label
globals()['OneMetric'] = OneMetric
globals()['Plan'] = Plan
from account_management_sdk.model.subscription_all_of import SubscriptionAllOf


class TestSubscriptionAllOf(unittest.TestCase):
    """SubscriptionAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSubscriptionAllOf(self):
        """Test SubscriptionAllOf"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SubscriptionAllOf()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
