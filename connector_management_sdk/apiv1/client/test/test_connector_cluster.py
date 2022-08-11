"""
    Connector Management API

    Connector Management API is a REST API to manage connectors.  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: rhosak-support@redhat.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import connector_management_sdk
from connector_management_sdk.model.connector_cluster_meta import ConnectorClusterMeta
from connector_management_sdk.model.connector_cluster_status import ConnectorClusterStatus
from connector_management_sdk.model.connector_cluster_status_status import ConnectorClusterStatusStatus
from connector_management_sdk.model.object_reference import ObjectReference
globals()['ConnectorClusterMeta'] = ConnectorClusterMeta
globals()['ConnectorClusterStatus'] = ConnectorClusterStatus
globals()['ConnectorClusterStatusStatus'] = ConnectorClusterStatusStatus
globals()['ObjectReference'] = ObjectReference
from connector_management_sdk.model.connector_cluster import ConnectorCluster


class TestConnectorCluster(unittest.TestCase):
    """ConnectorCluster unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConnectorCluster(self):
        """Test ConnectorCluster"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ConnectorCluster()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
