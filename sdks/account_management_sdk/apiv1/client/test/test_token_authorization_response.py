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
globals()['Account'] = Account
from account_management_sdk.model.token_authorization_response import TokenAuthorizationResponse


class TestTokenAuthorizationResponse(unittest.TestCase):
    """TokenAuthorizationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTokenAuthorizationResponse(self):
        """Test TokenAuthorizationResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TokenAuthorizationResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()