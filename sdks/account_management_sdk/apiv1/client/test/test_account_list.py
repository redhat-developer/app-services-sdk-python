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
from account_management_sdk.model.account_list_all_of import AccountListAllOf
from account_management_sdk.model.list import List
globals()['Account'] = Account
globals()['AccountListAllOf'] = AccountListAllOf
globals()['List'] = List
from account_management_sdk.model.account_list import AccountList


class TestAccountList(unittest.TestCase):
    """AccountList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAccountList(self):
        """Test AccountList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AccountList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
