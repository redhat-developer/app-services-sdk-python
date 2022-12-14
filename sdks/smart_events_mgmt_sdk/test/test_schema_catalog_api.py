"""
    Red Hat Openshift SmartEvents Fleet Manager

    The API exposed by the fleet manager of the SmartEvents service.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: openbridge-dev@redhat.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import rhoas_smart_events_mgmt_sdk
from rhoas_smart_events_mgmt_sdk.api.schema_catalog_api import SchemaCatalogApi  # noqa: E501


class TestSchemaCatalogApi(unittest.TestCase):
    """SchemaCatalogApi unit test stubs"""

    def setUp(self):
        self.api = SchemaCatalogApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_schema_api_get_action_processor_schema(self):
        """Test case for schema_api_get_action_processor_schema

        Get action processor schema  # noqa: E501
        """
        pass

    def test_schema_api_get_catalog(self):
        """Test case for schema_api_get_catalog

        Get processor catalog  # noqa: E501
        """
        pass

    def test_schema_api_get_source_processor_schema(self):
        """Test case for schema_api_get_source_processor_schema

        Get source processor schema  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
