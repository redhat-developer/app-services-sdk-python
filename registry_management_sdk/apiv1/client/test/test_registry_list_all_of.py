"""
    Service Registry Management API

    Service Registry Management API is a REST API for managing Service Registry instances. Service Registry is a datastore for event schemas and API designs, which is based on the open source Apicurio Registry project.  # noqa: E501

    The version of the OpenAPI document: 0.0.6
    Contact: rhosak-eval-support@redhat.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import registry_management_sdk
from registry_management_sdk.model.registry import Registry
globals()['Registry'] = Registry
from registry_management_sdk.model.registry_list_all_of import RegistryListAllOf


class TestRegistryListAllOf(unittest.TestCase):
    """RegistryListAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRegistryListAllOf(self):
        """Test RegistryListAllOf"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RegistryListAllOf()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
