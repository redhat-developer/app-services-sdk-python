"""
    Account Management Service API

    Manage user subscriptions and clusters  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import account_management_sdk
from account_management_sdk.model.capability import Capability
from account_management_sdk.model.label import Label
from account_management_sdk.model.organization import Organization
globals()['Capability'] = Capability
globals()['Label'] = Label
globals()['Organization'] = Organization
from account_management_sdk.model.account_all_of import AccountAllOf


class TestAccountAllOf(unittest.TestCase):
    """AccountAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAccountAllOf(self):
        """Test AccountAllOf"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AccountAllOf()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()