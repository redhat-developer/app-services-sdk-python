"""
    Red Hat Openshift SmartEvents Fleet Manager

    The API exposed by the fleet manager of the SmartEvents service.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: openbridge-dev@redhat.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import smart_events_management_sdk
from smart_events_management_sdk.api.error_catalog_api import ErrorCatalogApi  # noqa: E501


class TestErrorCatalogApi(unittest.TestCase):
    """ErrorCatalogApi unit test stubs"""

    def setUp(self):
        self.api = ErrorCatalogApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_error(self):
        """Test case for get_error

        Get an error from the error catalog.  # noqa: E501
        """
        pass

    def test_get_errors(self):
        """Test case for get_errors

        Get the list of errors.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
