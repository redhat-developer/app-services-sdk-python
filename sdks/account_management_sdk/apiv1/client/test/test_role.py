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
from account_management_sdk.model.permission import Permission
from account_management_sdk.model.role_all_of import RoleAllOf
globals()['ObjectReference'] = ObjectReference
globals()['Permission'] = Permission
globals()['RoleAllOf'] = RoleAllOf
from account_management_sdk.model.role import Role


class TestRole(unittest.TestCase):
    """Role unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRole(self):
        """Test Role"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Role()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()