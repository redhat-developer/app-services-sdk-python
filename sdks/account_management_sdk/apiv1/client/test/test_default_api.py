"""
    Account Management Service API

    Manage user subscriptions and clusters  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import unittest

import account_management_sdk
from account_management_sdk.api.default_api import DefaultApi  # noqa: E501


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_accounts_mgmt_v1_access_token_post(self):
        """Test case for api_accounts_mgmt_v1_access_token_post

        Return access token generated from registries in docker format  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_accounts_get(self):
        """Test case for api_accounts_mgmt_v1_accounts_get

        Returns a list of accounts  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_accounts_id_get(self):
        """Test case for api_accounts_mgmt_v1_accounts_id_get

        Get an account by id  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_accounts_id_labels_get(self):
        """Test case for api_accounts_mgmt_v1_accounts_id_labels_get

        Returns a list of labels  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_accounts_id_labels_key_delete(self):
        """Test case for api_accounts_mgmt_v1_accounts_id_labels_key_delete

        Delete a label  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_accounts_id_labels_key_get(self):
        """Test case for api_accounts_mgmt_v1_accounts_id_labels_key_get

        Get subscription labels by label key  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_accounts_id_labels_key_patch(self):
        """Test case for api_accounts_mgmt_v1_accounts_id_labels_key_patch

        Create a new label or update an existing label  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_accounts_id_labels_post(self):
        """Test case for api_accounts_mgmt_v1_accounts_id_labels_post

        Create a new label or update an existing label  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_accounts_id_patch(self):
        """Test case for api_accounts_mgmt_v1_accounts_id_patch

        Update an account  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_accounts_post(self):
        """Test case for api_accounts_mgmt_v1_accounts_post

        Create a new account  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_certificates_post(self):
        """Test case for api_accounts_mgmt_v1_certificates_post

        Fetch certificates of a particular type  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_cloud_resources_get(self):
        """Test case for api_accounts_mgmt_v1_cloud_resources_get

        Returns a list of cloud resources  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_cloud_resources_id_delete(self):
        """Test case for api_accounts_mgmt_v1_cloud_resources_id_delete

        Delete a cloud resource  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_cloud_resources_id_get(self):
        """Test case for api_accounts_mgmt_v1_cloud_resources_id_get

        Get a cloud resource  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_cloud_resources_id_patch(self):
        """Test case for api_accounts_mgmt_v1_cloud_resources_id_patch

        Update a cloud resource  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_cloud_resources_post(self):
        """Test case for api_accounts_mgmt_v1_cloud_resources_post

        Create a new cloud resource  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_cluster_authorizations_post(self):
        """Test case for api_accounts_mgmt_v1_cluster_authorizations_post

        Authorizes new cluster creation against an exsiting RH Subscription.  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_cluster_registrations_post(self):
        """Test case for api_accounts_mgmt_v1_cluster_registrations_post

        Finds or creates a cluster registration with a registy credential token and cluster ID  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_cluster_transfers_get(self):
        """Test case for api_accounts_mgmt_v1_cluster_transfers_get

        List cluster transfers - returns either an empty result set or a valid ClusterTransfer instance that is within a valid transfer window.  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_cluster_transfers_id_patch(self):
        """Test case for api_accounts_mgmt_v1_cluster_transfers_id_patch

        Update specific cluster transfer  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_cluster_transfers_post(self):
        """Test case for api_accounts_mgmt_v1_cluster_transfers_post

        Initiate cluster transfer.  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_config_skus_get(self):
        """Test case for api_accounts_mgmt_v1_config_skus_get

        Returns a list of skus  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_config_skus_id_delete(self):
        """Test case for api_accounts_mgmt_v1_config_skus_id_delete

        Delete a sku  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_config_skus_id_get(self):
        """Test case for api_accounts_mgmt_v1_config_skus_id_get

        Get a sku  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_config_skus_id_patch(self):
        """Test case for api_accounts_mgmt_v1_config_skus_id_patch

        Update a Sku  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_config_skus_post(self):
        """Test case for api_accounts_mgmt_v1_config_skus_post

        Create a new sku  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_current_account_get(self):
        """Test case for api_accounts_mgmt_v1_current_account_get

        Get the authenticated account  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_deleted_subscriptions_get(self):
        """Test case for api_accounts_mgmt_v1_deleted_subscriptions_get

        Returns a list of deleted subscriptions  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_errors_get(self):
        """Test case for api_accounts_mgmt_v1_errors_get

        Returns a list of errors  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_errors_id_get(self):
        """Test case for api_accounts_mgmt_v1_errors_id_get

        Get an error by id  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_feature_toggles_id_query_post(self):
        """Test case for api_accounts_mgmt_v1_feature_toggles_id_query_post

        Query a feature toggle by id  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_labels_get(self):
        """Test case for api_accounts_mgmt_v1_labels_get

        Returns a list of labels  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_landing_page_self_service_get(self):
        """Test case for api_accounts_mgmt_v1_landing_page_self_service_get

        Get a console.redhat.com landing page content JSON schema  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_metrics_get(self):
        """Test case for api_accounts_mgmt_v1_metrics_get

        Returns a list of metrics  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_notify_post(self):
        """Test case for api_accounts_mgmt_v1_notify_post

        Notify the owner of cluster/subscription  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_get(self):
        """Test case for api_accounts_mgmt_v1_organizations_get

        Returns a list of organizations  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_id_get(self):
        """Test case for api_accounts_mgmt_v1_organizations_id_get

        Get an organization by id  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_id_labels_get(self):
        """Test case for api_accounts_mgmt_v1_organizations_id_labels_get

        Returns a list of labels  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_id_labels_key_delete(self):
        """Test case for api_accounts_mgmt_v1_organizations_id_labels_key_delete

        Delete a label  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_id_labels_key_get(self):
        """Test case for api_accounts_mgmt_v1_organizations_id_labels_key_get

        Get subscription labels by label key  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_id_labels_key_patch(self):
        """Test case for api_accounts_mgmt_v1_organizations_id_labels_key_patch

        Create a new label or update an existing label  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_id_labels_post(self):
        """Test case for api_accounts_mgmt_v1_organizations_id_labels_post

        Create a new label or update an existing label  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_id_patch(self):
        """Test case for api_accounts_mgmt_v1_organizations_id_patch

        Update an organization  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_id_summary_dashboard_get(self):
        """Test case for api_accounts_mgmt_v1_organizations_id_summary_dashboard_get

        Returns a summary of organizations clusters based on metrics  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_acct_grp_asgn_id_delete(self):
        """Test case for api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_acct_grp_asgn_id_delete

        Delete an account group assignment  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_acct_grp_asgn_id_get(self):
        """Test case for api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_acct_grp_asgn_id_get

        Get account group assignment by id  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_get(self):
        """Test case for api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_get

        Returns a list of account group assignments for the given org  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_post(self):
        """Test case for api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_post

        Create a new AccountGroupAssignment  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_org_id_account_groups_acct_grp_id_delete(self):
        """Test case for api_accounts_mgmt_v1_organizations_org_id_account_groups_acct_grp_id_delete

        Delete an account group  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_org_id_account_groups_acct_grp_id_get(self):
        """Test case for api_accounts_mgmt_v1_organizations_org_id_account_groups_acct_grp_id_get

        Get account group by id  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_org_id_account_groups_acct_grp_id_patch(self):
        """Test case for api_accounts_mgmt_v1_organizations_org_id_account_groups_acct_grp_id_patch

        Update an account group  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_org_id_account_groups_get(self):
        """Test case for api_accounts_mgmt_v1_organizations_org_id_account_groups_get

        Returns a list of account groups for the given org  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_org_id_account_groups_post(self):
        """Test case for api_accounts_mgmt_v1_organizations_org_id_account_groups_post

        Create a new AccountGroup  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_org_id_consumed_quota_get(self):
        """Test case for api_accounts_mgmt_v1_organizations_org_id_consumed_quota_get

        Returns a list of consumed quota for an organization  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_org_id_quota_cost_get(self):
        """Test case for api_accounts_mgmt_v1_organizations_org_id_quota_cost_get

        Returns a summary of quota cost  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_org_id_resource_quota_get(self):
        """Test case for api_accounts_mgmt_v1_organizations_org_id_resource_quota_get

        Returns a list of resource quota objects  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_org_id_resource_quota_post(self):
        """Test case for api_accounts_mgmt_v1_organizations_org_id_resource_quota_post

        Create a new resource quota  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_org_id_resource_quota_quota_id_delete(self):
        """Test case for api_accounts_mgmt_v1_organizations_org_id_resource_quota_quota_id_delete

        Delete a resource quota  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_org_id_resource_quota_quota_id_get(self):
        """Test case for api_accounts_mgmt_v1_organizations_org_id_resource_quota_quota_id_get

        Get a resource quota by id  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_org_id_resource_quota_quota_id_patch(self):
        """Test case for api_accounts_mgmt_v1_organizations_org_id_resource_quota_quota_id_patch

        Update a resource quota  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_organizations_post(self):
        """Test case for api_accounts_mgmt_v1_organizations_post

        Create a new organization  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_plans_get(self):
        """Test case for api_accounts_mgmt_v1_plans_get

        Get all plans  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_plans_id_get(self):
        """Test case for api_accounts_mgmt_v1_plans_id_get

        Get a plan by id  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_pull_secrets_external_resource_id_delete(self):
        """Test case for api_accounts_mgmt_v1_pull_secrets_external_resource_id_delete

        Delete a pull secret  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_pull_secrets_post(self):
        """Test case for api_accounts_mgmt_v1_pull_secrets_post

        Return access token generated from registries in docker format  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_quota_cost_get(self):
        """Test case for api_accounts_mgmt_v1_quota_cost_get

        Returns a summary of quota cost for the authenticated user  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_quota_rules_get(self):
        """Test case for api_accounts_mgmt_v1_quota_rules_get

        Returns a list of UHC product Quota Rules  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_quotas_get(self):
        """Test case for api_accounts_mgmt_v1_quotas_get

        Returns a list of quotas  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_quotas_id_delete(self):
        """Test case for api_accounts_mgmt_v1_quotas_id_delete

        Delete a quota  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_quotas_id_get(self):
        """Test case for api_accounts_mgmt_v1_quotas_id_get

        Get a quota  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_quotas_id_patch(self):
        """Test case for api_accounts_mgmt_v1_quotas_id_patch

        Update a quota  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_quotas_post(self):
        """Test case for api_accounts_mgmt_v1_quotas_post

        Create a new quota  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_registries_get(self):
        """Test case for api_accounts_mgmt_v1_registries_get

        Returns a list of registries  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_registries_id_get(self):
        """Test case for api_accounts_mgmt_v1_registries_id_get

        Get an registry by id  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_registry_credentials_get(self):
        """Test case for api_accounts_mgmt_v1_registry_credentials_get

        """
        pass

    def test_api_accounts_mgmt_v1_registry_credentials_id_delete(self):
        """Test case for api_accounts_mgmt_v1_registry_credentials_id_delete

        Delete a registry credential by id  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_registry_credentials_id_get(self):
        """Test case for api_accounts_mgmt_v1_registry_credentials_id_get

        Get a registry credentials by id  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_registry_credentials_id_patch(self):
        """Test case for api_accounts_mgmt_v1_registry_credentials_id_patch

        Update a registry credential  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_registry_credentials_post(self):
        """Test case for api_accounts_mgmt_v1_registry_credentials_post

        Request the creation of a registry credential  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_reserved_resources_get(self):
        """Test case for api_accounts_mgmt_v1_reserved_resources_get

        Returns a list of reserved resources  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_resource_quota_get(self):
        """Test case for api_accounts_mgmt_v1_resource_quota_get

        Returns a list of resource quota objects  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_role_bindings_get(self):
        """Test case for api_accounts_mgmt_v1_role_bindings_get

        Returns a list of role bindings  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_role_bindings_id_delete(self):
        """Test case for api_accounts_mgmt_v1_role_bindings_id_delete

        Delete a role binding  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_role_bindings_id_get(self):
        """Test case for api_accounts_mgmt_v1_role_bindings_id_get

        Get a role binding  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_role_bindings_id_patch(self):
        """Test case for api_accounts_mgmt_v1_role_bindings_id_patch

        Update a role binding  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_role_bindings_post(self):
        """Test case for api_accounts_mgmt_v1_role_bindings_post

        Create a new role binding  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_roles_get(self):
        """Test case for api_accounts_mgmt_v1_roles_get

        Returns a list of roles  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_roles_id_get(self):
        """Test case for api_accounts_mgmt_v1_roles_id_get

        Get a role by id  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_self_entitlement_product_post(self):
        """Test case for api_accounts_mgmt_v1_self_entitlement_product_post

        Create or renew the entitlement to support a product for the user's organization.  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_sku_rules_get(self):
        """Test case for api_accounts_mgmt_v1_sku_rules_get

        Returns a list of UHC product SKU Rules  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_sku_rules_id_delete(self):
        """Test case for api_accounts_mgmt_v1_sku_rules_id_delete

        Delete a sku rule  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_sku_rules_id_get(self):
        """Test case for api_accounts_mgmt_v1_sku_rules_id_get

        Get a sku rules by id  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_sku_rules_id_patch(self):
        """Test case for api_accounts_mgmt_v1_sku_rules_id_patch

        Update a sku rule  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_sku_rules_post(self):
        """Test case for api_accounts_mgmt_v1_sku_rules_post

        Create a new sku rule  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_skus_get(self):
        """Test case for api_accounts_mgmt_v1_skus_get

        Returns a list of UHC product SKUs  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_skus_id_get(self):
        """Test case for api_accounts_mgmt_v1_skus_id_get

        Get a sku by id  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_subscriptions_get(self):
        """Test case for api_accounts_mgmt_v1_subscriptions_get

        Returns a list of subscriptions  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_subscriptions_id_delete(self):
        """Test case for api_accounts_mgmt_v1_subscriptions_id_delete

        Deletes a subscription by id  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_subscriptions_id_get(self):
        """Test case for api_accounts_mgmt_v1_subscriptions_id_get

        Get a subscription by id  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_subscriptions_id_labels_get(self):
        """Test case for api_accounts_mgmt_v1_subscriptions_id_labels_get

        Returns a list of labels  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_subscriptions_id_labels_key_delete(self):
        """Test case for api_accounts_mgmt_v1_subscriptions_id_labels_key_delete

        Delete a label  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_subscriptions_id_labels_key_get(self):
        """Test case for api_accounts_mgmt_v1_subscriptions_id_labels_key_get

        Get subscription labels by label key  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_subscriptions_id_labels_key_patch(self):
        """Test case for api_accounts_mgmt_v1_subscriptions_id_labels_key_patch

        Create a new label or update an existing label  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_subscriptions_id_labels_post(self):
        """Test case for api_accounts_mgmt_v1_subscriptions_id_labels_post

        Create a new label or update an existing label  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_subscriptions_id_metrics_metric_name_get(self):
        """Test case for api_accounts_mgmt_v1_subscriptions_id_metrics_metric_name_get

        Get subscription's metrics by metric name  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_subscriptions_id_notify_post(self):
        """Test case for api_accounts_mgmt_v1_subscriptions_id_notify_post

        Notify the owner of a subscription  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_subscriptions_id_patch(self):
        """Test case for api_accounts_mgmt_v1_subscriptions_id_patch

        Update a subscription  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_subscriptions_id_reserved_resources_get(self):
        """Test case for api_accounts_mgmt_v1_subscriptions_id_reserved_resources_get

        Returns a list of reserved resources  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_subscriptions_id_support_cases_get(self):
        """Test case for api_accounts_mgmt_v1_subscriptions_id_support_cases_get

        Returns a list of open support creates opened against the external cluster id of this subscrption  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_subscriptions_post(self):
        """Test case for api_accounts_mgmt_v1_subscriptions_post

        Create a new subscription  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_account_id_delete(self):
        """Test case for api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_account_id_delete

        Deletes a notification contact by subscription and account id  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_get(self):
        """Test case for api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_get

        Returns a list of notification contacts for the given subscription  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_post(self):
        """Test case for api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_post

        Add an account as a notification contact to this subscription  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_subscriptions_sub_id_reserved_resources_reserved_resource_id_delete(self):
        """Test case for api_accounts_mgmt_v1_subscriptions_sub_id_reserved_resources_reserved_resource_id_delete

        Delete reserved resources by id  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_subscriptions_sub_id_reserved_resources_reserved_resource_id_get(self):
        """Test case for api_accounts_mgmt_v1_subscriptions_sub_id_reserved_resources_reserved_resource_id_get

        Get reserved resources by id  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_subscriptions_sub_id_reserved_resources_reserved_resource_id_patch(self):
        """Test case for api_accounts_mgmt_v1_subscriptions_sub_id_reserved_resources_reserved_resource_id_patch

        Update a reserved resource  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_get(self):
        """Test case for api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_get

        Get subscription role bindings  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_id_delete(self):
        """Test case for api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_id_delete

        Delete a subscription role binding  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_id_get(self):
        """Test case for api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_id_get

        Get a Subscription Role Binding by id  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_post(self):
        """Test case for api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_post

        Create a new subscription role binding  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_support_cases_case_id_delete(self):
        """Test case for api_accounts_mgmt_v1_support_cases_case_id_delete

        Delete a support case  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_support_cases_post(self):
        """Test case for api_accounts_mgmt_v1_support_cases_post

        create a support case for the subscription  # noqa: E501
        """
        pass

    def test_api_accounts_mgmt_v1_token_authorization_post(self):
        """Test case for api_accounts_mgmt_v1_token_authorization_post

        Finds the account owner of the provided token  # noqa: E501
        """
        pass

    def test_api_authorizations_v1_access_review_post(self):
        """Test case for api_authorizations_v1_access_review_post

        Review an account's access to perform an action on a particular resource or resource type  # noqa: E501
        """
        pass

    def test_api_authorizations_v1_capability_review_post(self):
        """Test case for api_authorizations_v1_capability_review_post

        Review an account's capabilities  # noqa: E501
        """
        pass

    def test_api_authorizations_v1_export_control_review_post(self):
        """Test case for api_authorizations_v1_export_control_review_post

        Determine whether a user is restricted from downloading Red Hat software based on export control compliance.   # noqa: E501
        """
        pass

    def test_api_authorizations_v1_feature_review_post(self):
        """Test case for api_authorizations_v1_feature_review_post

        Review feature to perform an action on it such as toggle a feature on/off  # noqa: E501
        """
        pass

    def test_api_authorizations_v1_resource_review_post(self):
        """Test case for api_authorizations_v1_resource_review_post

        Obtain resource ids for resources an account may perform the specified action upon. Resource ids returned as [\"*\"] is shorthand for all ids.  # noqa: E501
        """
        pass

    def test_api_authorizations_v1_self_access_review_post(self):
        """Test case for api_authorizations_v1_self_access_review_post

        Review your ability to perform an action on a particular resource or resource type  # noqa: E501
        """
        pass

    def test_api_authorizations_v1_self_feature_review_post(self):
        """Test case for api_authorizations_v1_self_feature_review_post

        Review your ability to toggle a feature  # noqa: E501
        """
        pass

    def test_api_authorizations_v1_self_resource_review_post(self):
        """Test case for api_authorizations_v1_self_resource_review_post

        Obtain resource ids for resources you may perform the specified action upon. Resource ids returned as [\"*\"] is shorthand for all ids.  # noqa: E501
        """
        pass

    def test_api_authorizations_v1_self_terms_review_post(self):
        """Test case for api_authorizations_v1_self_terms_review_post

        Review your status of Terms  # noqa: E501
        """
        pass

    def test_api_authorizations_v1_terms_review_post(self):
        """Test case for api_authorizations_v1_terms_review_post

        Review an account's status of Terms  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()