"""
    Red Hat Openshift SmartEvents Fleet Manager

    The API exposed by the fleet manager of the SmartEvents service.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: openbridge-dev@redhat.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import rhoas_smart_events_mgmt_sdk
from rhoas_smart_events_mgmt_sdk.model.list_all_of import ListAllOf
from rhoas_smart_events_mgmt_sdk.model.list_response import ListResponse
globals()['ListAllOf'] = ListAllOf
globals()['ListResponse'] = ListResponse
from rhoas_smart_events_mgmt_sdk.model.list import List


class TestList(unittest.TestCase):
    """List unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testList(self):
        """Test List"""
        # FIXME: construct object with mandatory attributes with example values
        # model = List()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
