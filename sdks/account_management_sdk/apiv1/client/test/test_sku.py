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
from account_management_sdk.model.sku_all_of import SKUAllOf
globals()['ObjectReference'] = ObjectReference
globals()['SKUAllOf'] = SKUAllOf
from account_management_sdk.model.sku import SKU


class TestSKU(unittest.TestCase):
    """SKU unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSKU(self):
        """Test SKU"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SKU()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
