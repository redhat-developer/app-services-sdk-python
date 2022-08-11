# account_management_sdk.DefaultApi

All URIs are relative to *http://localhost:14321*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_accounts_mgmt_v1_access_token_post**](DefaultApi.md#api_accounts_mgmt_v1_access_token_post) | **POST** /api/accounts_mgmt/v1/access_token | Return access token generated from registries in docker format
[**api_accounts_mgmt_v1_accounts_get**](DefaultApi.md#api_accounts_mgmt_v1_accounts_get) | **GET** /api/accounts_mgmt/v1/accounts | Returns a list of accounts
[**api_accounts_mgmt_v1_accounts_id_get**](DefaultApi.md#api_accounts_mgmt_v1_accounts_id_get) | **GET** /api/accounts_mgmt/v1/accounts/{id} | Get an account by id
[**api_accounts_mgmt_v1_accounts_id_labels_get**](DefaultApi.md#api_accounts_mgmt_v1_accounts_id_labels_get) | **GET** /api/accounts_mgmt/v1/accounts/{id}/labels | Returns a list of labels
[**api_accounts_mgmt_v1_accounts_id_labels_key_delete**](DefaultApi.md#api_accounts_mgmt_v1_accounts_id_labels_key_delete) | **DELETE** /api/accounts_mgmt/v1/accounts/{id}/labels/{key} | Delete a label
[**api_accounts_mgmt_v1_accounts_id_labels_key_get**](DefaultApi.md#api_accounts_mgmt_v1_accounts_id_labels_key_get) | **GET** /api/accounts_mgmt/v1/accounts/{id}/labels/{key} | Get subscription labels by label key
[**api_accounts_mgmt_v1_accounts_id_labels_key_patch**](DefaultApi.md#api_accounts_mgmt_v1_accounts_id_labels_key_patch) | **PATCH** /api/accounts_mgmt/v1/accounts/{id}/labels/{key} | Create a new label or update an existing label
[**api_accounts_mgmt_v1_accounts_id_labels_post**](DefaultApi.md#api_accounts_mgmt_v1_accounts_id_labels_post) | **POST** /api/accounts_mgmt/v1/accounts/{id}/labels | Create a new label or update an existing label
[**api_accounts_mgmt_v1_accounts_id_patch**](DefaultApi.md#api_accounts_mgmt_v1_accounts_id_patch) | **PATCH** /api/accounts_mgmt/v1/accounts/{id} | Update an account
[**api_accounts_mgmt_v1_accounts_post**](DefaultApi.md#api_accounts_mgmt_v1_accounts_post) | **POST** /api/accounts_mgmt/v1/accounts | Create a new account
[**api_accounts_mgmt_v1_certificates_post**](DefaultApi.md#api_accounts_mgmt_v1_certificates_post) | **POST** /api/accounts_mgmt/v1/certificates | Fetch certificates of a particular type
[**api_accounts_mgmt_v1_cloud_resources_get**](DefaultApi.md#api_accounts_mgmt_v1_cloud_resources_get) | **GET** /api/accounts_mgmt/v1/cloud_resources | Returns a list of cloud resources
[**api_accounts_mgmt_v1_cloud_resources_id_delete**](DefaultApi.md#api_accounts_mgmt_v1_cloud_resources_id_delete) | **DELETE** /api/accounts_mgmt/v1/cloud_resources/{id} | Delete a cloud resource
[**api_accounts_mgmt_v1_cloud_resources_id_get**](DefaultApi.md#api_accounts_mgmt_v1_cloud_resources_id_get) | **GET** /api/accounts_mgmt/v1/cloud_resources/{id} | Get a cloud resource
[**api_accounts_mgmt_v1_cloud_resources_id_patch**](DefaultApi.md#api_accounts_mgmt_v1_cloud_resources_id_patch) | **PATCH** /api/accounts_mgmt/v1/cloud_resources/{id} | Update a cloud resource
[**api_accounts_mgmt_v1_cloud_resources_post**](DefaultApi.md#api_accounts_mgmt_v1_cloud_resources_post) | **POST** /api/accounts_mgmt/v1/cloud_resources | Create a new cloud resource
[**api_accounts_mgmt_v1_cluster_authorizations_post**](DefaultApi.md#api_accounts_mgmt_v1_cluster_authorizations_post) | **POST** /api/accounts_mgmt/v1/cluster_authorizations | Authorizes new cluster creation against an exsiting RH Subscription.
[**api_accounts_mgmt_v1_cluster_registrations_post**](DefaultApi.md#api_accounts_mgmt_v1_cluster_registrations_post) | **POST** /api/accounts_mgmt/v1/cluster_registrations | Finds or creates a cluster registration with a registy credential token and cluster ID
[**api_accounts_mgmt_v1_cluster_transfers_get**](DefaultApi.md#api_accounts_mgmt_v1_cluster_transfers_get) | **GET** /api/accounts_mgmt/v1/cluster_transfers | List cluster transfers - returns either an empty result set or a valid ClusterTransfer instance that is within a valid transfer window.
[**api_accounts_mgmt_v1_cluster_transfers_id_patch**](DefaultApi.md#api_accounts_mgmt_v1_cluster_transfers_id_patch) | **PATCH** /api/accounts_mgmt/v1/cluster_transfers/{id} | Update specific cluster transfer
[**api_accounts_mgmt_v1_cluster_transfers_post**](DefaultApi.md#api_accounts_mgmt_v1_cluster_transfers_post) | **POST** /api/accounts_mgmt/v1/cluster_transfers | Initiate cluster transfer.
[**api_accounts_mgmt_v1_config_skus_get**](DefaultApi.md#api_accounts_mgmt_v1_config_skus_get) | **GET** /api/accounts_mgmt/v1/config/skus | Returns a list of skus
[**api_accounts_mgmt_v1_config_skus_id_delete**](DefaultApi.md#api_accounts_mgmt_v1_config_skus_id_delete) | **DELETE** /api/accounts_mgmt/v1/config/skus/{id} | Delete a sku
[**api_accounts_mgmt_v1_config_skus_id_get**](DefaultApi.md#api_accounts_mgmt_v1_config_skus_id_get) | **GET** /api/accounts_mgmt/v1/config/skus/{id} | Get a sku
[**api_accounts_mgmt_v1_config_skus_id_patch**](DefaultApi.md#api_accounts_mgmt_v1_config_skus_id_patch) | **PATCH** /api/accounts_mgmt/v1/config/skus/{id} | Update a Sku
[**api_accounts_mgmt_v1_config_skus_post**](DefaultApi.md#api_accounts_mgmt_v1_config_skus_post) | **POST** /api/accounts_mgmt/v1/config/skus | Create a new sku
[**api_accounts_mgmt_v1_current_account_get**](DefaultApi.md#api_accounts_mgmt_v1_current_account_get) | **GET** /api/accounts_mgmt/v1/current_account | Get the authenticated account
[**api_accounts_mgmt_v1_deleted_subscriptions_get**](DefaultApi.md#api_accounts_mgmt_v1_deleted_subscriptions_get) | **GET** /api/accounts_mgmt/v1/deleted_subscriptions | Returns a list of deleted subscriptions
[**api_accounts_mgmt_v1_errors_get**](DefaultApi.md#api_accounts_mgmt_v1_errors_get) | **GET** /api/accounts_mgmt/v1/errors | Returns a list of errors
[**api_accounts_mgmt_v1_errors_id_get**](DefaultApi.md#api_accounts_mgmt_v1_errors_id_get) | **GET** /api/accounts_mgmt/v1/errors/{id} | Get an error by id
[**api_accounts_mgmt_v1_feature_toggles_id_query_post**](DefaultApi.md#api_accounts_mgmt_v1_feature_toggles_id_query_post) | **POST** /api/accounts_mgmt/v1/feature_toggles/{id}/query | Query a feature toggle by id
[**api_accounts_mgmt_v1_labels_get**](DefaultApi.md#api_accounts_mgmt_v1_labels_get) | **GET** /api/accounts_mgmt/v1/labels | Returns a list of labels
[**api_accounts_mgmt_v1_landing_page_self_service_get**](DefaultApi.md#api_accounts_mgmt_v1_landing_page_self_service_get) | **GET** /api/accounts_mgmt/v1/landing_page/self_service | Get a console.redhat.com landing page content JSON schema
[**api_accounts_mgmt_v1_metrics_get**](DefaultApi.md#api_accounts_mgmt_v1_metrics_get) | **GET** /api/accounts_mgmt/v1/metrics | Returns a list of metrics
[**api_accounts_mgmt_v1_notify_post**](DefaultApi.md#api_accounts_mgmt_v1_notify_post) | **POST** /api/accounts_mgmt/v1/notify | Notify the owner of cluster/subscription
[**api_accounts_mgmt_v1_organizations_get**](DefaultApi.md#api_accounts_mgmt_v1_organizations_get) | **GET** /api/accounts_mgmt/v1/organizations | Returns a list of organizations
[**api_accounts_mgmt_v1_organizations_id_get**](DefaultApi.md#api_accounts_mgmt_v1_organizations_id_get) | **GET** /api/accounts_mgmt/v1/organizations/{id} | Get an organization by id
[**api_accounts_mgmt_v1_organizations_id_labels_get**](DefaultApi.md#api_accounts_mgmt_v1_organizations_id_labels_get) | **GET** /api/accounts_mgmt/v1/organizations/{id}/labels | Returns a list of labels
[**api_accounts_mgmt_v1_organizations_id_labels_key_delete**](DefaultApi.md#api_accounts_mgmt_v1_organizations_id_labels_key_delete) | **DELETE** /api/accounts_mgmt/v1/organizations/{id}/labels/{key} | Delete a label
[**api_accounts_mgmt_v1_organizations_id_labels_key_get**](DefaultApi.md#api_accounts_mgmt_v1_organizations_id_labels_key_get) | **GET** /api/accounts_mgmt/v1/organizations/{id}/labels/{key} | Get subscription labels by label key
[**api_accounts_mgmt_v1_organizations_id_labels_key_patch**](DefaultApi.md#api_accounts_mgmt_v1_organizations_id_labels_key_patch) | **PATCH** /api/accounts_mgmt/v1/organizations/{id}/labels/{key} | Create a new label or update an existing label
[**api_accounts_mgmt_v1_organizations_id_labels_post**](DefaultApi.md#api_accounts_mgmt_v1_organizations_id_labels_post) | **POST** /api/accounts_mgmt/v1/organizations/{id}/labels | Create a new label or update an existing label
[**api_accounts_mgmt_v1_organizations_id_patch**](DefaultApi.md#api_accounts_mgmt_v1_organizations_id_patch) | **PATCH** /api/accounts_mgmt/v1/organizations/{id} | Update an organization
[**api_accounts_mgmt_v1_organizations_id_summary_dashboard_get**](DefaultApi.md#api_accounts_mgmt_v1_organizations_id_summary_dashboard_get) | **GET** /api/accounts_mgmt/v1/organizations/{id}/summary_dashboard | Returns a summary of organizations clusters based on metrics
[**api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_acct_grp_asgn_id_delete**](DefaultApi.md#api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_acct_grp_asgn_id_delete) | **DELETE** /api/accounts_mgmt/v1/organizations/{orgId}/account_group_assignments/{acctGrpAsgnId} | Delete an account group assignment
[**api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_acct_grp_asgn_id_get**](DefaultApi.md#api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_acct_grp_asgn_id_get) | **GET** /api/accounts_mgmt/v1/organizations/{orgId}/account_group_assignments/{acctGrpAsgnId} | Get account group assignment by id
[**api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_get**](DefaultApi.md#api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_get) | **GET** /api/accounts_mgmt/v1/organizations/{orgId}/account_group_assignments | Returns a list of account group assignments for the given org
[**api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_post**](DefaultApi.md#api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_post) | **POST** /api/accounts_mgmt/v1/organizations/{orgId}/account_group_assignments | Create a new AccountGroupAssignment
[**api_accounts_mgmt_v1_organizations_org_id_account_groups_acct_grp_id_delete**](DefaultApi.md#api_accounts_mgmt_v1_organizations_org_id_account_groups_acct_grp_id_delete) | **DELETE** /api/accounts_mgmt/v1/organizations/{orgId}/account_groups/{acctGrpId} | Delete an account group
[**api_accounts_mgmt_v1_organizations_org_id_account_groups_acct_grp_id_get**](DefaultApi.md#api_accounts_mgmt_v1_organizations_org_id_account_groups_acct_grp_id_get) | **GET** /api/accounts_mgmt/v1/organizations/{orgId}/account_groups/{acctGrpId} | Get account group by id
[**api_accounts_mgmt_v1_organizations_org_id_account_groups_acct_grp_id_patch**](DefaultApi.md#api_accounts_mgmt_v1_organizations_org_id_account_groups_acct_grp_id_patch) | **PATCH** /api/accounts_mgmt/v1/organizations/{orgId}/account_groups/{acctGrpId} | Update an account group
[**api_accounts_mgmt_v1_organizations_org_id_account_groups_get**](DefaultApi.md#api_accounts_mgmt_v1_organizations_org_id_account_groups_get) | **GET** /api/accounts_mgmt/v1/organizations/{orgId}/account_groups | Returns a list of account groups for the given org
[**api_accounts_mgmt_v1_organizations_org_id_account_groups_post**](DefaultApi.md#api_accounts_mgmt_v1_organizations_org_id_account_groups_post) | **POST** /api/accounts_mgmt/v1/organizations/{orgId}/account_groups | Create a new AccountGroup
[**api_accounts_mgmt_v1_organizations_org_id_consumed_quota_get**](DefaultApi.md#api_accounts_mgmt_v1_organizations_org_id_consumed_quota_get) | **GET** /api/accounts_mgmt/v1/organizations/{orgId}/consumed_quota | Returns a list of consumed quota for an organization
[**api_accounts_mgmt_v1_organizations_org_id_quota_cost_get**](DefaultApi.md#api_accounts_mgmt_v1_organizations_org_id_quota_cost_get) | **GET** /api/accounts_mgmt/v1/organizations/{orgId}/quota_cost | Returns a summary of quota cost
[**api_accounts_mgmt_v1_organizations_org_id_resource_quota_get**](DefaultApi.md#api_accounts_mgmt_v1_organizations_org_id_resource_quota_get) | **GET** /api/accounts_mgmt/v1/organizations/{orgId}/resource_quota | Returns a list of resource quota objects
[**api_accounts_mgmt_v1_organizations_org_id_resource_quota_post**](DefaultApi.md#api_accounts_mgmt_v1_organizations_org_id_resource_quota_post) | **POST** /api/accounts_mgmt/v1/organizations/{orgId}/resource_quota | Create a new resource quota
[**api_accounts_mgmt_v1_organizations_org_id_resource_quota_quota_id_delete**](DefaultApi.md#api_accounts_mgmt_v1_organizations_org_id_resource_quota_quota_id_delete) | **DELETE** /api/accounts_mgmt/v1/organizations/{orgId}/resource_quota/{quotaId} | Delete a resource quota
[**api_accounts_mgmt_v1_organizations_org_id_resource_quota_quota_id_get**](DefaultApi.md#api_accounts_mgmt_v1_organizations_org_id_resource_quota_quota_id_get) | **GET** /api/accounts_mgmt/v1/organizations/{orgId}/resource_quota/{quotaId} | Get a resource quota by id
[**api_accounts_mgmt_v1_organizations_org_id_resource_quota_quota_id_patch**](DefaultApi.md#api_accounts_mgmt_v1_organizations_org_id_resource_quota_quota_id_patch) | **PATCH** /api/accounts_mgmt/v1/organizations/{orgId}/resource_quota/{quotaId} | Update a resource quota
[**api_accounts_mgmt_v1_organizations_post**](DefaultApi.md#api_accounts_mgmt_v1_organizations_post) | **POST** /api/accounts_mgmt/v1/organizations | Create a new organization
[**api_accounts_mgmt_v1_plans_get**](DefaultApi.md#api_accounts_mgmt_v1_plans_get) | **GET** /api/accounts_mgmt/v1/plans | Get all plans
[**api_accounts_mgmt_v1_plans_id_get**](DefaultApi.md#api_accounts_mgmt_v1_plans_id_get) | **GET** /api/accounts_mgmt/v1/plans/{id} | Get a plan by id
[**api_accounts_mgmt_v1_pull_secrets_external_resource_id_delete**](DefaultApi.md#api_accounts_mgmt_v1_pull_secrets_external_resource_id_delete) | **DELETE** /api/accounts_mgmt/v1/pull_secrets/{externalResourceId} | Delete a pull secret
[**api_accounts_mgmt_v1_pull_secrets_post**](DefaultApi.md#api_accounts_mgmt_v1_pull_secrets_post) | **POST** /api/accounts_mgmt/v1/pull_secrets | Return access token generated from registries in docker format
[**api_accounts_mgmt_v1_quota_cost_get**](DefaultApi.md#api_accounts_mgmt_v1_quota_cost_get) | **GET** /api/accounts_mgmt/v1/quota_cost | Returns a summary of quota cost for the authenticated user
[**api_accounts_mgmt_v1_quota_rules_get**](DefaultApi.md#api_accounts_mgmt_v1_quota_rules_get) | **GET** /api/accounts_mgmt/v1/quota_rules | Returns a list of UHC product Quota Rules
[**api_accounts_mgmt_v1_quotas_get**](DefaultApi.md#api_accounts_mgmt_v1_quotas_get) | **GET** /api/accounts_mgmt/v1/quotas | Returns a list of quotas
[**api_accounts_mgmt_v1_quotas_id_delete**](DefaultApi.md#api_accounts_mgmt_v1_quotas_id_delete) | **DELETE** /api/accounts_mgmt/v1/quotas/{id} | Delete a quota
[**api_accounts_mgmt_v1_quotas_id_get**](DefaultApi.md#api_accounts_mgmt_v1_quotas_id_get) | **GET** /api/accounts_mgmt/v1/quotas/{id} | Get a quota
[**api_accounts_mgmt_v1_quotas_id_patch**](DefaultApi.md#api_accounts_mgmt_v1_quotas_id_patch) | **PATCH** /api/accounts_mgmt/v1/quotas/{id} | Update a quota
[**api_accounts_mgmt_v1_quotas_post**](DefaultApi.md#api_accounts_mgmt_v1_quotas_post) | **POST** /api/accounts_mgmt/v1/quotas | Create a new quota
[**api_accounts_mgmt_v1_registries_get**](DefaultApi.md#api_accounts_mgmt_v1_registries_get) | **GET** /api/accounts_mgmt/v1/registries | Returns a list of registries
[**api_accounts_mgmt_v1_registries_id_get**](DefaultApi.md#api_accounts_mgmt_v1_registries_id_get) | **GET** /api/accounts_mgmt/v1/registries/{id} | Get an registry by id
[**api_accounts_mgmt_v1_registry_credentials_get**](DefaultApi.md#api_accounts_mgmt_v1_registry_credentials_get) | **GET** /api/accounts_mgmt/v1/registry_credentials | 
[**api_accounts_mgmt_v1_registry_credentials_id_delete**](DefaultApi.md#api_accounts_mgmt_v1_registry_credentials_id_delete) | **DELETE** /api/accounts_mgmt/v1/registry_credentials/{id} | Delete a registry credential by id
[**api_accounts_mgmt_v1_registry_credentials_id_get**](DefaultApi.md#api_accounts_mgmt_v1_registry_credentials_id_get) | **GET** /api/accounts_mgmt/v1/registry_credentials/{id} | Get a registry credentials by id
[**api_accounts_mgmt_v1_registry_credentials_id_patch**](DefaultApi.md#api_accounts_mgmt_v1_registry_credentials_id_patch) | **PATCH** /api/accounts_mgmt/v1/registry_credentials/{id} | Update a registry credential
[**api_accounts_mgmt_v1_registry_credentials_post**](DefaultApi.md#api_accounts_mgmt_v1_registry_credentials_post) | **POST** /api/accounts_mgmt/v1/registry_credentials | Request the creation of a registry credential
[**api_accounts_mgmt_v1_reserved_resources_get**](DefaultApi.md#api_accounts_mgmt_v1_reserved_resources_get) | **GET** /api/accounts_mgmt/v1/reserved_resources | Returns a list of reserved resources
[**api_accounts_mgmt_v1_resource_quota_get**](DefaultApi.md#api_accounts_mgmt_v1_resource_quota_get) | **GET** /api/accounts_mgmt/v1/resource_quota | Returns a list of resource quota objects
[**api_accounts_mgmt_v1_role_bindings_get**](DefaultApi.md#api_accounts_mgmt_v1_role_bindings_get) | **GET** /api/accounts_mgmt/v1/role_bindings | Returns a list of role bindings
[**api_accounts_mgmt_v1_role_bindings_id_delete**](DefaultApi.md#api_accounts_mgmt_v1_role_bindings_id_delete) | **DELETE** /api/accounts_mgmt/v1/role_bindings/{id} | Delete a role binding
[**api_accounts_mgmt_v1_role_bindings_id_get**](DefaultApi.md#api_accounts_mgmt_v1_role_bindings_id_get) | **GET** /api/accounts_mgmt/v1/role_bindings/{id} | Get a role binding
[**api_accounts_mgmt_v1_role_bindings_id_patch**](DefaultApi.md#api_accounts_mgmt_v1_role_bindings_id_patch) | **PATCH** /api/accounts_mgmt/v1/role_bindings/{id} | Update a role binding
[**api_accounts_mgmt_v1_role_bindings_post**](DefaultApi.md#api_accounts_mgmt_v1_role_bindings_post) | **POST** /api/accounts_mgmt/v1/role_bindings | Create a new role binding
[**api_accounts_mgmt_v1_roles_get**](DefaultApi.md#api_accounts_mgmt_v1_roles_get) | **GET** /api/accounts_mgmt/v1/roles | Returns a list of roles
[**api_accounts_mgmt_v1_roles_id_get**](DefaultApi.md#api_accounts_mgmt_v1_roles_id_get) | **GET** /api/accounts_mgmt/v1/roles/{id} | Get a role by id
[**api_accounts_mgmt_v1_self_entitlement_product_post**](DefaultApi.md#api_accounts_mgmt_v1_self_entitlement_product_post) | **POST** /api/accounts_mgmt/v1/self_entitlement/{product} | Create or renew the entitlement to support a product for the user&#39;s organization.
[**api_accounts_mgmt_v1_sku_rules_get**](DefaultApi.md#api_accounts_mgmt_v1_sku_rules_get) | **GET** /api/accounts_mgmt/v1/sku_rules | Returns a list of UHC product SKU Rules
[**api_accounts_mgmt_v1_sku_rules_id_delete**](DefaultApi.md#api_accounts_mgmt_v1_sku_rules_id_delete) | **DELETE** /api/accounts_mgmt/v1/sku_rules/{id} | Delete a sku rule
[**api_accounts_mgmt_v1_sku_rules_id_get**](DefaultApi.md#api_accounts_mgmt_v1_sku_rules_id_get) | **GET** /api/accounts_mgmt/v1/sku_rules/{id} | Get a sku rules by id
[**api_accounts_mgmt_v1_sku_rules_id_patch**](DefaultApi.md#api_accounts_mgmt_v1_sku_rules_id_patch) | **PATCH** /api/accounts_mgmt/v1/sku_rules/{id} | Update a sku rule
[**api_accounts_mgmt_v1_sku_rules_post**](DefaultApi.md#api_accounts_mgmt_v1_sku_rules_post) | **POST** /api/accounts_mgmt/v1/sku_rules | Create a new sku rule
[**api_accounts_mgmt_v1_skus_get**](DefaultApi.md#api_accounts_mgmt_v1_skus_get) | **GET** /api/accounts_mgmt/v1/skus | Returns a list of UHC product SKUs
[**api_accounts_mgmt_v1_skus_id_get**](DefaultApi.md#api_accounts_mgmt_v1_skus_id_get) | **GET** /api/accounts_mgmt/v1/skus/{id} | Get a sku by id
[**api_accounts_mgmt_v1_subscriptions_get**](DefaultApi.md#api_accounts_mgmt_v1_subscriptions_get) | **GET** /api/accounts_mgmt/v1/subscriptions | Returns a list of subscriptions
[**api_accounts_mgmt_v1_subscriptions_id_delete**](DefaultApi.md#api_accounts_mgmt_v1_subscriptions_id_delete) | **DELETE** /api/accounts_mgmt/v1/subscriptions/{id} | Deletes a subscription by id
[**api_accounts_mgmt_v1_subscriptions_id_get**](DefaultApi.md#api_accounts_mgmt_v1_subscriptions_id_get) | **GET** /api/accounts_mgmt/v1/subscriptions/{id} | Get a subscription by id
[**api_accounts_mgmt_v1_subscriptions_id_labels_get**](DefaultApi.md#api_accounts_mgmt_v1_subscriptions_id_labels_get) | **GET** /api/accounts_mgmt/v1/subscriptions/{id}/labels | Returns a list of labels
[**api_accounts_mgmt_v1_subscriptions_id_labels_key_delete**](DefaultApi.md#api_accounts_mgmt_v1_subscriptions_id_labels_key_delete) | **DELETE** /api/accounts_mgmt/v1/subscriptions/{id}/labels/{key} | Delete a label
[**api_accounts_mgmt_v1_subscriptions_id_labels_key_get**](DefaultApi.md#api_accounts_mgmt_v1_subscriptions_id_labels_key_get) | **GET** /api/accounts_mgmt/v1/subscriptions/{id}/labels/{key} | Get subscription labels by label key
[**api_accounts_mgmt_v1_subscriptions_id_labels_key_patch**](DefaultApi.md#api_accounts_mgmt_v1_subscriptions_id_labels_key_patch) | **PATCH** /api/accounts_mgmt/v1/subscriptions/{id}/labels/{key} | Create a new label or update an existing label
[**api_accounts_mgmt_v1_subscriptions_id_labels_post**](DefaultApi.md#api_accounts_mgmt_v1_subscriptions_id_labels_post) | **POST** /api/accounts_mgmt/v1/subscriptions/{id}/labels | Create a new label or update an existing label
[**api_accounts_mgmt_v1_subscriptions_id_metrics_metric_name_get**](DefaultApi.md#api_accounts_mgmt_v1_subscriptions_id_metrics_metric_name_get) | **GET** /api/accounts_mgmt/v1/subscriptions/{id}/metrics/{metric_name} | Get subscription&#39;s metrics by metric name
[**api_accounts_mgmt_v1_subscriptions_id_notify_post**](DefaultApi.md#api_accounts_mgmt_v1_subscriptions_id_notify_post) | **POST** /api/accounts_mgmt/v1/subscriptions/{id}/notify | Notify the owner of a subscription
[**api_accounts_mgmt_v1_subscriptions_id_patch**](DefaultApi.md#api_accounts_mgmt_v1_subscriptions_id_patch) | **PATCH** /api/accounts_mgmt/v1/subscriptions/{id} | Update a subscription
[**api_accounts_mgmt_v1_subscriptions_id_reserved_resources_get**](DefaultApi.md#api_accounts_mgmt_v1_subscriptions_id_reserved_resources_get) | **GET** /api/accounts_mgmt/v1/subscriptions/{id}/reserved_resources | Returns a list of reserved resources
[**api_accounts_mgmt_v1_subscriptions_id_support_cases_get**](DefaultApi.md#api_accounts_mgmt_v1_subscriptions_id_support_cases_get) | **GET** /api/accounts_mgmt/v1/subscriptions/{id}/support_cases | Returns a list of open support creates opened against the external cluster id of this subscrption
[**api_accounts_mgmt_v1_subscriptions_post**](DefaultApi.md#api_accounts_mgmt_v1_subscriptions_post) | **POST** /api/accounts_mgmt/v1/subscriptions | Create a new subscription
[**api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_account_id_delete**](DefaultApi.md#api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_account_id_delete) | **DELETE** /api/accounts_mgmt/v1/subscriptions/{subId}/notification_contacts/{accountId} | Deletes a notification contact by subscription and account id
[**api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_get**](DefaultApi.md#api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_get) | **GET** /api/accounts_mgmt/v1/subscriptions/{subId}/notification_contacts | Returns a list of notification contacts for the given subscription
[**api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_post**](DefaultApi.md#api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_post) | **POST** /api/accounts_mgmt/v1/subscriptions/{subId}/notification_contacts | Add an account as a notification contact to this subscription
[**api_accounts_mgmt_v1_subscriptions_sub_id_reserved_resources_reserved_resource_id_delete**](DefaultApi.md#api_accounts_mgmt_v1_subscriptions_sub_id_reserved_resources_reserved_resource_id_delete) | **DELETE** /api/accounts_mgmt/v1/subscriptions/{subId}/reserved_resources/{reservedResourceId} | Delete reserved resources by id
[**api_accounts_mgmt_v1_subscriptions_sub_id_reserved_resources_reserved_resource_id_get**](DefaultApi.md#api_accounts_mgmt_v1_subscriptions_sub_id_reserved_resources_reserved_resource_id_get) | **GET** /api/accounts_mgmt/v1/subscriptions/{subId}/reserved_resources/{reservedResourceId} | Get reserved resources by id
[**api_accounts_mgmt_v1_subscriptions_sub_id_reserved_resources_reserved_resource_id_patch**](DefaultApi.md#api_accounts_mgmt_v1_subscriptions_sub_id_reserved_resources_reserved_resource_id_patch) | **PATCH** /api/accounts_mgmt/v1/subscriptions/{subId}/reserved_resources/{reservedResourceId} | Update a reserved resource
[**api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_get**](DefaultApi.md#api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_get) | **GET** /api/accounts_mgmt/v1/subscriptions/{subId}/role_bindings | Get subscription role bindings
[**api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_id_delete**](DefaultApi.md#api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_id_delete) | **DELETE** /api/accounts_mgmt/v1/subscriptions/{subId}/role_bindings/{id} | Delete a subscription role binding
[**api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_id_get**](DefaultApi.md#api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_id_get) | **GET** /api/accounts_mgmt/v1/subscriptions/{subId}/role_bindings/{id} | Get a Subscription Role Binding by id
[**api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_post**](DefaultApi.md#api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_post) | **POST** /api/accounts_mgmt/v1/subscriptions/{subId}/role_bindings | Create a new subscription role binding
[**api_accounts_mgmt_v1_support_cases_case_id_delete**](DefaultApi.md#api_accounts_mgmt_v1_support_cases_case_id_delete) | **DELETE** /api/accounts_mgmt/v1/support_cases/{caseId} | Delete a support case
[**api_accounts_mgmt_v1_support_cases_post**](DefaultApi.md#api_accounts_mgmt_v1_support_cases_post) | **POST** /api/accounts_mgmt/v1/support_cases | create a support case for the subscription
[**api_accounts_mgmt_v1_token_authorization_post**](DefaultApi.md#api_accounts_mgmt_v1_token_authorization_post) | **POST** /api/accounts_mgmt/v1/token_authorization | Finds the account owner of the provided token
[**api_authorizations_v1_access_review_post**](DefaultApi.md#api_authorizations_v1_access_review_post) | **POST** /api/authorizations/v1/access_review | Review an account&#39;s access to perform an action on a particular resource or resource type
[**api_authorizations_v1_capability_review_post**](DefaultApi.md#api_authorizations_v1_capability_review_post) | **POST** /api/authorizations/v1/capability_review | Review an account&#39;s capabilities
[**api_authorizations_v1_export_control_review_post**](DefaultApi.md#api_authorizations_v1_export_control_review_post) | **POST** /api/authorizations/v1/export_control_review | Determine whether a user is restricted from downloading Red Hat software based on export control compliance. 
[**api_authorizations_v1_feature_review_post**](DefaultApi.md#api_authorizations_v1_feature_review_post) | **POST** /api/authorizations/v1/feature_review | Review feature to perform an action on it such as toggle a feature on/off
[**api_authorizations_v1_resource_review_post**](DefaultApi.md#api_authorizations_v1_resource_review_post) | **POST** /api/authorizations/v1/resource_review | Obtain resource ids for resources an account may perform the specified action upon. Resource ids returned as [\&quot;*\&quot;] is shorthand for all ids.
[**api_authorizations_v1_self_access_review_post**](DefaultApi.md#api_authorizations_v1_self_access_review_post) | **POST** /api/authorizations/v1/self_access_review | Review your ability to perform an action on a particular resource or resource type
[**api_authorizations_v1_self_feature_review_post**](DefaultApi.md#api_authorizations_v1_self_feature_review_post) | **POST** /api/authorizations/v1/self_feature_review | Review your ability to toggle a feature
[**api_authorizations_v1_self_resource_review_post**](DefaultApi.md#api_authorizations_v1_self_resource_review_post) | **POST** /api/authorizations/v1/self_resource_review | Obtain resource ids for resources you may perform the specified action upon. Resource ids returned as [\&quot;*\&quot;] is shorthand for all ids.
[**api_authorizations_v1_self_terms_review_post**](DefaultApi.md#api_authorizations_v1_self_terms_review_post) | **POST** /api/authorizations/v1/self_terms_review | Review your status of Terms
[**api_authorizations_v1_terms_review_post**](DefaultApi.md#api_authorizations_v1_terms_review_post) | **POST** /api/authorizations/v1/terms_review | Review an account&#39;s status of Terms


# **api_accounts_mgmt_v1_access_token_post**
> AccessTokenCfg api_accounts_mgmt_v1_access_token_post()

Return access token generated from registries in docker format

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.access_token_cfg import AccessTokenCfg
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Return access token generated from registries in docker format
        api_response = api_instance.api_accounts_mgmt_v1_access_token_post()
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_access_token_post: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessTokenCfg**](AccessTokenCfg.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | access token from registries in docker format |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | Cannot find registry |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_accounts_get**
> AccountList api_accounts_mgmt_v1_accounts_get()

Returns a list of accounts

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.account_list import AccountList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)
    order_by = "orderBy_example" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  ```sql username asc ```  Or in order to retrieve all accounts ordered by username _and_ first name:  ```sql username asc, firstName asc ```  If the parameter isn't provided, or if the value is empty, then no explicit ordering will be applied. (optional)
    fields = "fields_example" # str | Supplies a comma-separated list of fields to be returned. Fields of sub-structures and of arrays use <structure>.<field> notation. <stucture>.* means all field of a structure Example: For each Subscription to get id, href, plan(id and kind) and labels (all fields)  ``` ocm get subscriptions --parameter fields=id,href,plan.id,plan.kind,labels.* --parameter fetchLabels=true ``` (optional)
    fetch_labels = True # bool | If true, includes the labels on a subscription/organization/account in the output. Could slow request response time. (optional)
    fetch_capabilities = True # bool | If true, includes the capabilities on a subscription in the output. Could slow request response time. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of accounts
        api_response = api_instance.api_accounts_mgmt_v1_accounts_get(page=page, size=size, search=search, order_by=order_by, fields=fields, fetch_labels=fetch_labels, fetch_capabilities=fetch_capabilities)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_accounts_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  &#x60;&#x60;&#x60;sql username asc &#x60;&#x60;&#x60;  Or in order to retrieve all accounts ordered by username _and_ first name:  &#x60;&#x60;&#x60;sql username asc, firstName asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then no explicit ordering will be applied. | [optional]
 **fields** | **str**| Supplies a comma-separated list of fields to be returned. Fields of sub-structures and of arrays use &lt;structure&gt;.&lt;field&gt; notation. &lt;stucture&gt;.* means all field of a structure Example: For each Subscription to get id, href, plan(id and kind) and labels (all fields)  &#x60;&#x60;&#x60; ocm get subscriptions --parameter fields&#x3D;id,href,plan.id,plan.kind,labels.* --parameter fetchLabels&#x3D;true &#x60;&#x60;&#x60; | [optional]
 **fetch_labels** | **bool**| If true, includes the labels on a subscription/organization/account in the output. Could slow request response time. | [optional]
 **fetch_capabilities** | **bool**| If true, includes the capabilities on a subscription in the output. Could slow request response time. | [optional]

### Return type

[**AccountList**](AccountList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of account objects |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_accounts_id_get**
> Account api_accounts_mgmt_v1_accounts_id_get(id)

Get an account by id

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.account import Account
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    fetch_labels = True # bool | If true, includes the labels on a subscription/organization/account in the output. Could slow request response time. (optional)
    fetch_capabilities = True # bool | If true, includes the capabilities on a subscription in the output. Could slow request response time. (optional)
    fetch_rhit = True # bool | If true, includes the RHIT account_id in the output. Could slow request response time. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get an account by id
        api_response = api_instance.api_accounts_mgmt_v1_accounts_id_get(id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_accounts_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get an account by id
        api_response = api_instance.api_accounts_mgmt_v1_accounts_id_get(id, fetch_labels=fetch_labels, fetch_capabilities=fetch_capabilities, fetch_rhit=fetch_rhit)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_accounts_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **fetch_labels** | **bool**| If true, includes the labels on a subscription/organization/account in the output. Could slow request response time. | [optional]
 **fetch_capabilities** | **bool**| If true, includes the capabilities on a subscription in the output. Could slow request response time. | [optional]
 **fetch_rhit** | **bool**| If true, includes the RHIT account_id in the output. Could slow request response time. | [optional]

### Return type

[**Account**](Account.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account found by id |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No account with specified id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_accounts_id_labels_get**
> LabelList api_accounts_mgmt_v1_accounts_id_labels_get(id)

Returns a list of labels

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.label_list import LabelList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)
    order_by = "orderBy_example" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  ```sql username asc ```  Or in order to retrieve all accounts ordered by username _and_ first name:  ```sql username asc, firstName asc ```  If the parameter isn't provided, or if the value is empty, then no explicit ordering will be applied. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of labels
        api_response = api_instance.api_accounts_mgmt_v1_accounts_id_labels_get(id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_accounts_id_labels_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of labels
        api_response = api_instance.api_accounts_mgmt_v1_accounts_id_labels_get(id, page=page, size=size, search=search, order_by=order_by)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_accounts_id_labels_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  &#x60;&#x60;&#x60;sql username asc &#x60;&#x60;&#x60;  Or in order to retrieve all accounts ordered by username _and_ first name:  &#x60;&#x60;&#x60;sql username asc, firstName asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then no explicit ordering will be applied. | [optional]

### Return type

[**LabelList**](LabelList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of label |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_accounts_id_labels_key_delete**
> api_accounts_mgmt_v1_accounts_id_labels_key_delete(id, key)

Delete a label

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    key = "key_example" # str | The key of the label

    # example passing only required values which don't have defaults set
    try:
        # Delete a label
        api_instance.api_accounts_mgmt_v1_accounts_id_labels_key_delete(id, key)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_accounts_id_labels_key_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **key** | **str**| The key of the label |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Label successfully deleted |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No label with specified key on specified organizations id exists |  -  |
**500** | An unexpected error occurred deleting the label |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_accounts_id_labels_key_get**
> Label api_accounts_mgmt_v1_accounts_id_labels_key_get(id, key)

Get subscription labels by label key

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.label import Label
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    key = "key_example" # str | The key of the label

    # example passing only required values which don't have defaults set
    try:
        # Get subscription labels by label key
        api_response = api_instance.api_accounts_mgmt_v1_accounts_id_labels_key_get(id, key)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_accounts_id_labels_key_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **key** | **str**| The key of the label |

### Return type

[**Label**](Label.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Labels found by key |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No label with specified key on specified organizations id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_accounts_id_labels_key_patch**
> Label api_accounts_mgmt_v1_accounts_id_labels_key_patch(id, key, label)

Create a new label or update an existing label

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.label import Label
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    key = "key_example" # str | The key of the label
    label = Label(None) # Label | Label data

    # example passing only required values which don't have defaults set
    try:
        # Create a new label or update an existing label
        api_response = api_instance.api_accounts_mgmt_v1_accounts_id_labels_key_patch(id, key, label)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_accounts_id_labels_key_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **key** | **str**| The key of the label |
 **label** | [**Label**](Label.md)| Label data |

### Return type

[**Label**](Label.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created or updated label successfully |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**409** | Label already exists and cannot be updated |  -  |
**500** | Unexpected error updating organizations label |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_accounts_id_labels_post**
> Label api_accounts_mgmt_v1_accounts_id_labels_post(id, label)

Create a new label or update an existing label

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.label import Label
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    label = Label(None) # Label | Label data

    # example passing only required values which don't have defaults set
    try:
        # Create a new label or update an existing label
        api_response = api_instance.api_accounts_mgmt_v1_accounts_id_labels_post(id, label)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_accounts_id_labels_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **label** | [**Label**](Label.md)| Label data |

### Return type

[**Label**](Label.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created or updated label successfully |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | An unexpected error occurred creating the label |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_accounts_id_patch**
> Account api_accounts_mgmt_v1_accounts_id_patch(id, account_patch_request)

Update an account

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.account import Account
from account_management_sdk.model.account_patch_request import AccountPatchRequest
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    account_patch_request = AccountPatchRequest(
        ban_code="ban_code_example",
        ban_description="ban_description_example",
        banned=True,
        email="email_example",
        first_name="first_name_example",
        last_name="last_name_example",
        organization_id="organization_id_example",
        service_account=True,
    ) # AccountPatchRequest | Updated account data

    # example passing only required values which don't have defaults set
    try:
        # Update an account
        api_response = api_instance.api_accounts_mgmt_v1_accounts_id_patch(id, account_patch_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_accounts_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **account_patch_request** | [**AccountPatchRequest**](AccountPatchRequest.md)| Updated account data |

### Return type

[**Account**](Account.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account updated successfully |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No account with specified id exists |  -  |
**409** | Account already exists |  -  |
**500** | Unexpected error updating account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_accounts_post**
> Account api_accounts_mgmt_v1_accounts_post(account)

Create a new account

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.account import Account
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    account = Account(None) # Account | Account data
    dry_run = True # bool | If true, instructs API to avoid making any changes, but rather run through validations only. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new account
        api_response = api_instance.api_accounts_mgmt_v1_accounts_post(account)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_accounts_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new account
        api_response = api_instance.api_accounts_mgmt_v1_accounts_post(account, dry_run=dry_run)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_accounts_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | [**Account**](Account.md)| Account data |
 **dry_run** | **bool**| If true, instructs API to avoid making any changes, but rather run through validations only. | [optional]

### Return type

[**Account**](Account.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account can be created without dryRun parameter |  -  |
**201** | Created |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**409** | Account already exists |  -  |
**500** | An unexpected error occurred creating the account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_certificates_post**
> Certificate api_accounts_mgmt_v1_certificates_post(certificates_request)

Fetch certificates of a particular type

### Example

* Api Key Authentication (AccessToken):
* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.certificate import Certificate
from account_management_sdk.model.certificates_request import CertificatesRequest
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    certificates_request = CertificatesRequest(
        arch="x86",
        type="sca",
    ) # CertificatesRequest | # The payload depends on the type of the requested certificate The examples for supported types: * {\"type\": \"sca\", \"arch\": \"x86_64\"} 

    # example passing only required values which don't have defaults set
    try:
        # Fetch certificates of a particular type
        api_response = api_instance.api_accounts_mgmt_v1_certificates_post(certificates_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_certificates_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificates_request** | [**CertificatesRequest**](CertificatesRequest.md)| # The payload depends on the type of the requested certificate The examples for supported types: * {\&quot;type\&quot;: \&quot;sca\&quot;, \&quot;arch\&quot;: \&quot;x86_64\&quot;}  |

### Return type

[**Certificate**](Certificate.md)

### Authorization

[AccessToken](../README.md#AccessToken), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The certificate associated with the organization |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | The certificate is not avaialbe for the organization |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_cloud_resources_get**
> CloudResourceList api_accounts_mgmt_v1_cloud_resources_get()

Returns a list of cloud resources

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.cloud_resource_list import CloudResourceList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of cloud resources
        api_response = api_instance.api_accounts_mgmt_v1_cloud_resources_get(page=page, size=size, search=search)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_cloud_resources_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]

### Return type

[**CloudResourceList**](CloudResourceList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of cloud resource objects |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_cloud_resources_id_delete**
> api_accounts_mgmt_v1_cloud_resources_id_delete(id)

Delete a cloud resource

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record

    # example passing only required values which don't have defaults set
    try:
        # Delete a cloud resource
        api_instance.api_accounts_mgmt_v1_cloud_resources_id_delete(id)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_cloud_resources_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Cloud resource successfully deleted |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No resource with specified id exists |  -  |
**500** | An unexpected error occurred deleting the resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_cloud_resources_id_get**
> CloudResource api_accounts_mgmt_v1_cloud_resources_id_get(id)

Get a cloud resource

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.cloud_resource import CloudResource
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record

    # example passing only required values which don't have defaults set
    try:
        # Get a cloud resource
        api_response = api_instance.api_accounts_mgmt_v1_cloud_resources_id_get(id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_cloud_resources_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |

### Return type

[**CloudResource**](CloudResource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cloud resource found by id |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No cloud resource with specified id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_cloud_resources_id_patch**
> CloudResource api_accounts_mgmt_v1_cloud_resources_id_patch(id, cloud_resource)

Update a cloud resource

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.cloud_resource import CloudResource
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    cloud_resource = CloudResource(None) # CloudResource | Updated cloud resource data

    # example passing only required values which don't have defaults set
    try:
        # Update a cloud resource
        api_response = api_instance.api_accounts_mgmt_v1_cloud_resources_id_patch(id, cloud_resource)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_cloud_resources_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **cloud_resource** | [**CloudResource**](CloudResource.md)| Updated cloud resource data |

### Return type

[**CloudResource**](CloudResource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cloud resource updated successfully |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No resource with specified id exists |  -  |
**500** | Unexpected error updating resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_cloud_resources_post**
> CloudResource api_accounts_mgmt_v1_cloud_resources_post(cloud_resource)

Create a new cloud resource

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.cloud_resource import CloudResource
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    cloud_resource = CloudResource(None) # CloudResource | Cloud resource data

    # example passing only required values which don't have defaults set
    try:
        # Create a new cloud resource
        api_response = api_instance.api_accounts_mgmt_v1_cloud_resources_post(cloud_resource)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_cloud_resources_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_resource** | [**CloudResource**](CloudResource.md)| Cloud resource data |

### Return type

[**CloudResource**](CloudResource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**409** | Resource already exists |  -  |
**500** | An unexpected error occurred creating resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_cluster_authorizations_post**
> ClusterAuthorizationResponse api_accounts_mgmt_v1_cluster_authorizations_post(cluster_authorization_request)

Authorizes new cluster creation against an exsiting RH Subscription.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.cluster_authorization_response import ClusterAuthorizationResponse
from account_management_sdk.model.cluster_authorization_request import ClusterAuthorizationRequest
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    cluster_authorization_request = ClusterAuthorizationRequest(
        account_username="account_username_example",
        availability_zone="availability_zone_example",
        byoc=True,
        cloud_account_id="cloud_account_id_example",
        cloud_provider_id="cloud_provider_id_example",
        cluster_id="cluster_id_example",
        disconnected=True,
        display_name="display_name_example",
        external_cluster_id="external_cluster_id_example",
        managed=True,
        product_category="assistedInstall",
        product_id="osd",
        quota_version="quota_version_example",
        reserve=True,
        resources=[
            ReservedResource(None),
        ],
    ) # ClusterAuthorizationRequest | Cluster and authorization data

    # example passing only required values which don't have defaults set
    try:
        # Authorizes new cluster creation against an exsiting RH Subscription.
        api_response = api_instance.api_accounts_mgmt_v1_cluster_authorizations_post(cluster_authorization_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_cluster_authorizations_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_authorization_request** | [**ClusterAuthorizationRequest**](ClusterAuthorizationRequest.md)| Cluster and authorization data |

### Return type

[**ClusterAuthorizationResponse**](ClusterAuthorizationResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The authorization is successful, the requested cluster has a valid subscription and is within resource limits. |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**409** | AMS subscription exists but is associated with another account |  -  |
**429** | The limits for this subscription are exceeded. |  -  |
**500** | Other cluster authorization error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_cluster_registrations_post**
> ClusterRegistrationResponse api_accounts_mgmt_v1_cluster_registrations_post(cluster_registration_request)

Finds or creates a cluster registration with a registy credential token and cluster ID

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.cluster_registration_request import ClusterRegistrationRequest
from account_management_sdk.model.cluster_registration_response import ClusterRegistrationResponse
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    cluster_registration_request = ClusterRegistrationRequest(
        authorization_token="authorization_token_example",
        cluster_id="cluster_id_example",
    ) # ClusterRegistrationRequest | Cluster and authorization data

    # example passing only required values which don't have defaults set
    try:
        # Finds or creates a cluster registration with a registy credential token and cluster ID
        api_response = api_instance.api_accounts_mgmt_v1_cluster_registrations_post(cluster_registration_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_cluster_registrations_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_registration_request** | [**ClusterRegistrationRequest**](ClusterRegistrationRequest.md)| Cluster and authorization data |

### Return type

[**ClusterRegistrationResponse**](ClusterRegistrationResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A cluster with the specified cluster_id exists and belongs to the user with the specified registry credential token |  -  |
**201** | No cluster with the specified cluster exists, one was successfully created and associated with the account with the specified registry credential token |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Registry credential token is invalid |  -  |
**409** | Cluster with specified cluster_id already associated with another user |  -  |
**422** | cluster_id provided is invalid |  -  |
**429** | Too many clusters have been associated with this user recently |  -  |
**500** | Other cluster registration error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_cluster_transfers_get**
> ClusterTransferList api_accounts_mgmt_v1_cluster_transfers_get()

List cluster transfers - returns either an empty result set or a valid ClusterTransfer instance that is within a valid transfer window.

### Example

* Api Key Authentication (AccessToken):
* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.cluster_transfer_list import ClusterTransferList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)
    order_by = "orderBy_example" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  ```sql username asc ```  Or in order to retrieve all accounts ordered by username _and_ first name:  ```sql username asc, firstName asc ```  If the parameter isn't provided, or if the value is empty, then no explicit ordering will be applied. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List cluster transfers - returns either an empty result set or a valid ClusterTransfer instance that is within a valid transfer window.
        api_response = api_instance.api_accounts_mgmt_v1_cluster_transfers_get(page=page, size=size, search=search, order_by=order_by)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_cluster_transfers_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  &#x60;&#x60;&#x60;sql username asc &#x60;&#x60;&#x60;  Or in order to retrieve all accounts ordered by username _and_ first name:  &#x60;&#x60;&#x60;sql username asc, firstName asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then no explicit ordering will be applied. | [optional]

### Return type

[**ClusterTransferList**](ClusterTransferList.md)

### Authorization

[AccessToken](../README.md#AccessToken), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | cluster transfer detected |  -  |
**204** | ClusterTransfer does not exist for a specific cluster |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_cluster_transfers_id_patch**
> ClusterTransfer api_accounts_mgmt_v1_cluster_transfers_id_patch(id, cluster_transfer_patch_request)

Update specific cluster transfer

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.cluster_transfer_patch_request import ClusterTransferPatchRequest
from account_management_sdk.model.cluster_transfer import ClusterTransfer
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    cluster_transfer_patch_request = ClusterTransferPatchRequest(
        status="status_example",
    ) # ClusterTransferPatchRequest | Updated cluster transfer

    # example passing only required values which don't have defaults set
    try:
        # Update specific cluster transfer
        api_response = api_instance.api_accounts_mgmt_v1_cluster_transfers_id_patch(id, cluster_transfer_patch_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_cluster_transfers_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **cluster_transfer_patch_request** | [**ClusterTransferPatchRequest**](ClusterTransferPatchRequest.md)| Updated cluster transfer |

### Return type

[**ClusterTransfer**](ClusterTransfer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster transfer updated successfully |  -  |
**204** | ClusterTransfer does not exist for a specific cluster |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**409** | Conflict during cluster transfer update |  -  |
**500** | Unexpected error updating cluster transfer |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_cluster_transfers_post**
> ClusterTransfer api_accounts_mgmt_v1_cluster_transfers_post(cluster_transfer_request)

Initiate cluster transfer.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.cluster_transfer_request import ClusterTransferRequest
from account_management_sdk.model.cluster_transfer import ClusterTransfer
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    cluster_transfer_request = ClusterTransferRequest(
        cluster_uuid="cluster_uuid_example",
        owner="owner_example",
        recipient="recipient_example",
    ) # ClusterTransferRequest | The contents of the cluster transfer creation request

    # example passing only required values which don't have defaults set
    try:
        # Initiate cluster transfer.
        api_response = api_instance.api_accounts_mgmt_v1_cluster_transfers_post(cluster_transfer_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_cluster_transfers_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_transfer_request** | [**ClusterTransferRequest**](ClusterTransferRequest.md)| The contents of the cluster transfer creation request |

### Return type

[**ClusterTransfer**](ClusterTransfer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | the cluster transfer has been created |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_config_skus_get**
> SkuList api_accounts_mgmt_v1_config_skus_get()

Returns a list of skus

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.sku_list import SkuList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of skus
        api_response = api_instance.api_accounts_mgmt_v1_config_skus_get(page=page, size=size, search=search)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_config_skus_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]

### Return type

[**SkuList**](SkuList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of sku objects |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_config_skus_id_delete**
> api_accounts_mgmt_v1_config_skus_id_delete(id)

Delete a sku

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record

    # example passing only required values which don't have defaults set
    try:
        # Delete a sku
        api_instance.api_accounts_mgmt_v1_config_skus_id_delete(id)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_config_skus_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Sku successfully deleted |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No sku with specified id exists |  -  |
**500** | An unexpected error occurred deleting the sku |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_config_skus_id_get**
> SKU api_accounts_mgmt_v1_config_skus_id_get(id)

Get a sku

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.sku import SKU
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record

    # example passing only required values which don't have defaults set
    try:
        # Get a sku
        api_response = api_instance.api_accounts_mgmt_v1_config_skus_id_get(id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_config_skus_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |

### Return type

[**SKU**](SKU.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sku found by id |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No SKU with specified id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_config_skus_id_patch**
> SKU api_accounts_mgmt_v1_config_skus_id_patch(id, sku)

Update a Sku

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.sku import SKU
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    sku = SKU(None) # SKU | Updated sku data

    # example passing only required values which don't have defaults set
    try:
        # Update a Sku
        api_response = api_instance.api_accounts_mgmt_v1_config_skus_id_patch(id, sku)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_config_skus_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **sku** | [**SKU**](SKU.md)| Updated sku data |

### Return type

[**SKU**](SKU.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sku updated successfully |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No sku with specified id exists |  -  |
**500** | Unexpected error updating sku |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_config_skus_post**
> SKU api_accounts_mgmt_v1_config_skus_post(sku)

Create a new sku

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.sku import SKU
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    sku = SKU(None) # SKU | Sku data

    # example passing only required values which don't have defaults set
    try:
        # Create a new sku
        api_response = api_instance.api_accounts_mgmt_v1_config_skus_post(sku)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_config_skus_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | [**SKU**](SKU.md)| Sku data |

### Return type

[**SKU**](SKU.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**409** | Sku already exists |  -  |
**500** | An unexpected error occurred creating sku |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_current_account_get**
> Account api_accounts_mgmt_v1_current_account_get()

Get the authenticated account

### Example

* Api Key Authentication (AccessToken):
* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.account import Account
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    fetch_labels = True # bool | If true, includes the labels on a subscription/organization/account in the output. Could slow request response time. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the authenticated account
        api_response = api_instance.api_accounts_mgmt_v1_current_account_get(fetch_labels=fetch_labels)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_current_account_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fetch_labels** | **bool**| If true, includes the labels on a subscription/organization/account in the output. Could slow request response time. | [optional]

### Return type

[**Account**](Account.md)

### Authorization

[AccessToken](../README.md#AccessToken), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account found via JWT |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_deleted_subscriptions_get**
> DeletedSubscriptionList api_accounts_mgmt_v1_deleted_subscriptions_get()

Returns a list of deleted subscriptions

### Example

* Api Key Authentication (AccessToken):
* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.deleted_subscription_list import DeletedSubscriptionList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)
    order_by = "orderBy_example" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  ```sql username asc ```  Or in order to retrieve all accounts ordered by username _and_ first name:  ```sql username asc, firstName asc ```  If the parameter isn't provided, or if the value is empty, then no explicit ordering will be applied. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of deleted subscriptions
        api_response = api_instance.api_accounts_mgmt_v1_deleted_subscriptions_get(page=page, size=size, search=search, order_by=order_by)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_deleted_subscriptions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  &#x60;&#x60;&#x60;sql username asc &#x60;&#x60;&#x60;  Or in order to retrieve all accounts ordered by username _and_ first name:  &#x60;&#x60;&#x60;sql username asc, firstName asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then no explicit ordering will be applied. | [optional]

### Return type

[**DeletedSubscriptionList**](DeletedSubscriptionList.md)

### Authorization

[AccessToken](../README.md#AccessToken), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of deleted subscription objects |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_errors_get**
> ErrorList api_accounts_mgmt_v1_errors_get()

Returns a list of errors

### Example


```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error_list import ErrorList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)


# Enter a context with an instance of the API client
with account_management_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of errors
        api_response = api_instance.api_accounts_mgmt_v1_errors_get(page=page, size=size, search=search)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_errors_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]

### Return type

[**ErrorList**](ErrorList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array or errors |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_errors_id_get**
> Error api_accounts_mgmt_v1_errors_id_get(id)

Get an error by id

### Example


```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)


# Enter a context with an instance of the API client
with account_management_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record

    # example passing only required values which don't have defaults set
    try:
        # Get an error by id
        api_response = api_instance.api_accounts_mgmt_v1_errors_id_get(id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_errors_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |

### Return type

[**Error**](Error.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Error found by id |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No error with specified id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_feature_toggles_id_query_post**
> FeatureToggle api_accounts_mgmt_v1_feature_toggles_id_query_post(id, feature_toggle_query_request)

Query a feature toggle by id

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.feature_toggle_query_request import FeatureToggleQueryRequest
from account_management_sdk.model.feature_toggle import FeatureToggle
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    feature_toggle_query_request = FeatureToggleQueryRequest(None) # FeatureToggleQueryRequest | The context of the query

    # example passing only required values which don't have defaults set
    try:
        # Query a feature toggle by id
        api_response = api_instance.api_accounts_mgmt_v1_feature_toggles_id_query_post(id, feature_toggle_query_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_feature_toggles_id_query_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **feature_toggle_query_request** | [**FeatureToggleQueryRequest**](FeatureToggleQueryRequest.md)| The context of the query |

### Return type

[**FeatureToggle**](FeatureToggle.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Feature toggle found by id |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_labels_get**
> LabelList api_accounts_mgmt_v1_labels_get()

Returns a list of labels

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.label_list import LabelList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)
    order_by = "orderBy_example" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  ```sql username asc ```  Or in order to retrieve all accounts ordered by username _and_ first name:  ```sql username asc, firstName asc ```  If the parameter isn't provided, or if the value is empty, then no explicit ordering will be applied. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of labels
        api_response = api_instance.api_accounts_mgmt_v1_labels_get(page=page, size=size, search=search, order_by=order_by)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_labels_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  &#x60;&#x60;&#x60;sql username asc &#x60;&#x60;&#x60;  Or in order to retrieve all accounts ordered by username _and_ first name:  &#x60;&#x60;&#x60;sql username asc, firstName asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then no explicit ordering will be applied. | [optional]

### Return type

[**LabelList**](LabelList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of label objects |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_landing_page_self_service_get**
> SelfServiceLandingPageSchema api_accounts_mgmt_v1_landing_page_self_service_get()

Get a console.redhat.com landing page content JSON schema

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.self_service_landing_page_schema import SelfServiceLandingPageSchema
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a console.redhat.com landing page content JSON schema
        api_response = api_instance.api_accounts_mgmt_v1_landing_page_self_service_get()
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_landing_page_self_service_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SelfServiceLandingPageSchema**](SelfServiceLandingPageSchema.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | self service schema created |  -  |
**401** | Auth token is invalid |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_metrics_get**
> MetricsList api_accounts_mgmt_v1_metrics_get()

Returns a list of metrics

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.metrics_list import MetricsList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of metrics
        api_response = api_instance.api_accounts_mgmt_v1_metrics_get(search=search)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_metrics_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]

### Return type

[**MetricsList**](MetricsList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of metrics objects |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_notify_post**
> api_accounts_mgmt_v1_notify_post(notification_request)

Notify the owner of cluster/subscription

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.notification_request import NotificationRequest
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    notification_request = NotificationRequest(
        bcc_address="bcc_address_example",
        cluster_id="cluster_id_example",
        cluster_uuid="cluster_uuid_example",
        include_red_hat_associates=True,
        internal_only=True,
        subject="subject_example",
        subscription_id="subscription_id_example",
        template_name="template_name_example",
        template_parameters=[
            TemplateParameter(
                content="content_example",
                name="name_example",
            ),
        ],
    ) # NotificationRequest | The contents of the notification to send to the owner of a cluster/subscription in addition to the set of template parameters which are sent automatically ACCOUNT_USERNAME, FIRST_NAME, LAST_NAME, ORGANIZATION_NAME, ORGANIZATION_EXTERNAL_ID

    # example passing only required values which don't have defaults set
    try:
        # Notify the owner of cluster/subscription
        api_instance.api_accounts_mgmt_v1_notify_post(notification_request)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_notify_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_request** | [**NotificationRequest**](NotificationRequest.md)| The contents of the notification to send to the owner of a cluster/subscription in addition to the set of template parameters which are sent automatically ACCOUNT_USERNAME, FIRST_NAME, LAST_NAME, ORGANIZATION_NAME, ORGANIZATION_EXTERNAL_ID |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Notification created and queued to be sent soon |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_get**
> OrganizationList api_accounts_mgmt_v1_organizations_get()

Returns a list of organizations

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.organization_list import OrganizationList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)
    order_by = "orderBy_example" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  ```sql username asc ```  Or in order to retrieve all accounts ordered by username _and_ first name:  ```sql username asc, firstName asc ```  If the parameter isn't provided, or if the value is empty, then no explicit ordering will be applied. (optional)
    fetch_labels = True # bool | If true, includes the labels on a subscription/organization/account in the output. Could slow request response time. (optional)
    fetch_capabilities = True # bool | If true, includes the capabilities on a subscription in the output. Could slow request response time. (optional)
    fields = "fields_example" # str | Supplies a comma-separated list of fields to be returned. Fields of sub-structures and of arrays use <structure>.<field> notation. <stucture>.* means all field of a structure Example: For each Subscription to get id, href, plan(id and kind) and labels (all fields)  ``` ocm get subscriptions --parameter fields=id,href,plan.id,plan.kind,labels.* --parameter fetchLabels=true ``` (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of organizations
        api_response = api_instance.api_accounts_mgmt_v1_organizations_get(page=page, size=size, search=search, order_by=order_by, fetch_labels=fetch_labels, fetch_capabilities=fetch_capabilities, fields=fields)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  &#x60;&#x60;&#x60;sql username asc &#x60;&#x60;&#x60;  Or in order to retrieve all accounts ordered by username _and_ first name:  &#x60;&#x60;&#x60;sql username asc, firstName asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then no explicit ordering will be applied. | [optional]
 **fetch_labels** | **bool**| If true, includes the labels on a subscription/organization/account in the output. Could slow request response time. | [optional]
 **fetch_capabilities** | **bool**| If true, includes the capabilities on a subscription in the output. Could slow request response time. | [optional]
 **fields** | **str**| Supplies a comma-separated list of fields to be returned. Fields of sub-structures and of arrays use &lt;structure&gt;.&lt;field&gt; notation. &lt;stucture&gt;.* means all field of a structure Example: For each Subscription to get id, href, plan(id and kind) and labels (all fields)  &#x60;&#x60;&#x60; ocm get subscriptions --parameter fields&#x3D;id,href,plan.id,plan.kind,labels.* --parameter fetchLabels&#x3D;true &#x60;&#x60;&#x60; | [optional]

### Return type

[**OrganizationList**](OrganizationList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of organization objects |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_id_get**
> Organization api_accounts_mgmt_v1_organizations_id_get(id)

Get an organization by id

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from account_management_sdk.model.organization import Organization
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    fetch_labels = True # bool | If true, includes the labels on a subscription/organization/account in the output. Could slow request response time. (optional)
    fetch_capabilities = True # bool | If true, includes the capabilities on a subscription in the output. Could slow request response time. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get an organization by id
        api_response = api_instance.api_accounts_mgmt_v1_organizations_id_get(id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get an organization by id
        api_response = api_instance.api_accounts_mgmt_v1_organizations_id_get(id, fetch_labels=fetch_labels, fetch_capabilities=fetch_capabilities)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **fetch_labels** | **bool**| If true, includes the labels on a subscription/organization/account in the output. Could slow request response time. | [optional]
 **fetch_capabilities** | **bool**| If true, includes the capabilities on a subscription in the output. Could slow request response time. | [optional]

### Return type

[**Organization**](Organization.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Organization found by id |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No organization with specified id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_id_labels_get**
> LabelList api_accounts_mgmt_v1_organizations_id_labels_get(id)

Returns a list of labels

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.label_list import LabelList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)
    order_by = "orderBy_example" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  ```sql username asc ```  Or in order to retrieve all accounts ordered by username _and_ first name:  ```sql username asc, firstName asc ```  If the parameter isn't provided, or if the value is empty, then no explicit ordering will be applied. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of labels
        api_response = api_instance.api_accounts_mgmt_v1_organizations_id_labels_get(id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_id_labels_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of labels
        api_response = api_instance.api_accounts_mgmt_v1_organizations_id_labels_get(id, page=page, size=size, search=search, order_by=order_by)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_id_labels_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  &#x60;&#x60;&#x60;sql username asc &#x60;&#x60;&#x60;  Or in order to retrieve all accounts ordered by username _and_ first name:  &#x60;&#x60;&#x60;sql username asc, firstName asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then no explicit ordering will be applied. | [optional]

### Return type

[**LabelList**](LabelList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of label |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_id_labels_key_delete**
> api_accounts_mgmt_v1_organizations_id_labels_key_delete(id, key)

Delete a label

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    key = "key_example" # str | The key of the label

    # example passing only required values which don't have defaults set
    try:
        # Delete a label
        api_instance.api_accounts_mgmt_v1_organizations_id_labels_key_delete(id, key)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_id_labels_key_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **key** | **str**| The key of the label |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Label successfully deleted |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No label with specified key on specified organizations id exists |  -  |
**500** | An unexpected error occurred deleting the label |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_id_labels_key_get**
> Label api_accounts_mgmt_v1_organizations_id_labels_key_get(id, key)

Get subscription labels by label key

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.label import Label
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    key = "key_example" # str | The key of the label

    # example passing only required values which don't have defaults set
    try:
        # Get subscription labels by label key
        api_response = api_instance.api_accounts_mgmt_v1_organizations_id_labels_key_get(id, key)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_id_labels_key_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **key** | **str**| The key of the label |

### Return type

[**Label**](Label.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Labels found by key |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No label with specified key on specified organizations id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_id_labels_key_patch**
> Label api_accounts_mgmt_v1_organizations_id_labels_key_patch(id, key, label)

Create a new label or update an existing label

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.label import Label
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    key = "key_example" # str | The key of the label
    label = Label(None) # Label | Label data

    # example passing only required values which don't have defaults set
    try:
        # Create a new label or update an existing label
        api_response = api_instance.api_accounts_mgmt_v1_organizations_id_labels_key_patch(id, key, label)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_id_labels_key_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **key** | **str**| The key of the label |
 **label** | [**Label**](Label.md)| Label data |

### Return type

[**Label**](Label.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created or updated label successfully |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**409** | Label already exists and cannot be updated |  -  |
**500** | Unexpected error updating organizations label |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_id_labels_post**
> Label api_accounts_mgmt_v1_organizations_id_labels_post(id, label)

Create a new label or update an existing label

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.label import Label
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    label = Label(None) # Label | Label data

    # example passing only required values which don't have defaults set
    try:
        # Create a new label or update an existing label
        api_response = api_instance.api_accounts_mgmt_v1_organizations_id_labels_post(id, label)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_id_labels_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **label** | [**Label**](Label.md)| Label data |

### Return type

[**Label**](Label.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created or updated label successfully |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | An unexpected error occurred creating the label |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_id_patch**
> Organization api_accounts_mgmt_v1_organizations_id_patch(id, organization_patch_request)

Update an organization

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.organization_patch_request import OrganizationPatchRequest
from account_management_sdk.model.error import Error
from account_management_sdk.model.organization import Organization
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    organization_patch_request = OrganizationPatchRequest(
        ebs_account_id="ebs_account_id_example",
        external_id="external_id_example",
        name="name_example",
    ) # OrganizationPatchRequest | Updated organization data

    # example passing only required values which don't have defaults set
    try:
        # Update an organization
        api_response = api_instance.api_accounts_mgmt_v1_organizations_id_patch(id, organization_patch_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **organization_patch_request** | [**OrganizationPatchRequest**](OrganizationPatchRequest.md)| Updated organization data |

### Return type

[**Organization**](Organization.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Organization updated successfully |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No organization with specified id exists |  -  |
**500** | Unexpected error updating organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_id_summary_dashboard_get**
> Summary api_accounts_mgmt_v1_organizations_id_summary_dashboard_get(id)

Returns a summary of organizations clusters based on metrics

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.summary import Summary
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record

    # example passing only required values which don't have defaults set
    try:
        # Returns a summary of organizations clusters based on metrics
        api_response = api_instance.api_accounts_mgmt_v1_organizations_id_summary_dashboard_get(id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_id_summary_dashboard_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |

### Return type

[**Summary**](Summary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of metrics objects |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_acct_grp_asgn_id_delete**
> api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_acct_grp_asgn_id_delete(org_id, acct_grp_asgn_id)

Delete an account group assignment

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    org_id = "orgId_example" # str | The id of organization
    acct_grp_asgn_id = "acctGrpAsgnId_example" # str | The id of account group assignment

    # example passing only required values which don't have defaults set
    try:
        # Delete an account group assignment
        api_instance.api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_acct_grp_asgn_id_delete(org_id, acct_grp_asgn_id)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_acct_grp_asgn_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The id of organization |
 **acct_grp_asgn_id** | **str**| The id of account group assignment |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Account group assignment successfully deleted |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No organization or account group assignment with specified id exists |  -  |
**500** | An unexpected error occurred deleting the account group assignment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_acct_grp_asgn_id_get**
> AccountGroupAssignment api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_acct_grp_asgn_id_get(org_id, acct_grp_asgn_id)

Get account group assignment by id

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from account_management_sdk.model.account_group_assignment import AccountGroupAssignment
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    org_id = "orgId_example" # str | The id of organization
    acct_grp_asgn_id = "acctGrpAsgnId_example" # str | The id of account group assignment

    # example passing only required values which don't have defaults set
    try:
        # Get account group assignment by id
        api_response = api_instance.api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_acct_grp_asgn_id_get(org_id, acct_grp_asgn_id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_acct_grp_asgn_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The id of organization |
 **acct_grp_asgn_id** | **str**| The id of account group assignment |

### Return type

[**AccountGroupAssignment**](AccountGroupAssignment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account group assignment found |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No organization with specified id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_get**
> AccountGroupAssignmentList api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_get(org_id)

Returns a list of account group assignments for the given org

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.account_group_assignment_list import AccountGroupAssignmentList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    org_id = "orgId_example" # str | The id of organization
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)
    order_by = "orderBy_example" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  ```sql username asc ```  Or in order to retrieve all accounts ordered by username _and_ first name:  ```sql username asc, firstName asc ```  If the parameter isn't provided, or if the value is empty, then no explicit ordering will be applied. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of account group assignments for the given org
        api_response = api_instance.api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_get(org_id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of account group assignments for the given org
        api_response = api_instance.api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_get(org_id, page=page, size=size, search=search, order_by=order_by)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The id of organization |
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  &#x60;&#x60;&#x60;sql username asc &#x60;&#x60;&#x60;  Or in order to retrieve all accounts ordered by username _and_ first name:  &#x60;&#x60;&#x60;sql username asc, firstName asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then no explicit ordering will be applied. | [optional]

### Return type

[**AccountGroupAssignmentList**](AccountGroupAssignmentList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of account groups |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No organization with specified id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_post**
> AccountGroupAssignment api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_post(org_id, account_group_assignment)

Create a new AccountGroupAssignment

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from account_management_sdk.model.account_group_assignment import AccountGroupAssignment
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    org_id = "orgId_example" # str | The id of organization
    account_group_assignment = AccountGroupAssignment(None) # AccountGroupAssignment | New AccountGroup data

    # example passing only required values which don't have defaults set
    try:
        # Create a new AccountGroupAssignment
        api_response = api_instance.api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_post(org_id, account_group_assignment)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_org_id_account_group_assignments_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The id of organization |
 **account_group_assignment** | [**AccountGroupAssignment**](AccountGroupAssignment.md)| New AccountGroup data |

### Return type

[**AccountGroupAssignment**](AccountGroupAssignment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created AccountGroupAssignment successfully |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No organization with specified id exists |  -  |
**500** | An unexpected error occurred creating the label |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_org_id_account_groups_acct_grp_id_delete**
> api_accounts_mgmt_v1_organizations_org_id_account_groups_acct_grp_id_delete(org_id, acct_grp_id)

Delete an account group

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    org_id = "orgId_example" # str | The id of organization
    acct_grp_id = "acctGrpId_example" # str | The id of account group

    # example passing only required values which don't have defaults set
    try:
        # Delete an account group
        api_instance.api_accounts_mgmt_v1_organizations_org_id_account_groups_acct_grp_id_delete(org_id, acct_grp_id)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_org_id_account_groups_acct_grp_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The id of organization |
 **acct_grp_id** | **str**| The id of account group |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Account group successfully deleted |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No organization or account group with specified id exists |  -  |
**500** | An unexpected error occurred deleting the account group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_org_id_account_groups_acct_grp_id_get**
> AccountGroup api_accounts_mgmt_v1_organizations_org_id_account_groups_acct_grp_id_get(org_id, acct_grp_id)

Get account group by id

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.account_group import AccountGroup
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    org_id = "orgId_example" # str | The id of organization
    acct_grp_id = "acctGrpId_example" # str | The id of account group

    # example passing only required values which don't have defaults set
    try:
        # Get account group by id
        api_response = api_instance.api_accounts_mgmt_v1_organizations_org_id_account_groups_acct_grp_id_get(org_id, acct_grp_id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_org_id_account_groups_acct_grp_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The id of organization |
 **acct_grp_id** | **str**| The id of account group |

### Return type

[**AccountGroup**](AccountGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account group found |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No organization or account group with specified id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_org_id_account_groups_acct_grp_id_patch**
> AccountGroup api_accounts_mgmt_v1_organizations_org_id_account_groups_acct_grp_id_patch(org_id, acct_grp_id, account_group_request)

Update an account group

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.account_group import AccountGroup
from account_management_sdk.model.account_group_request import AccountGroupRequest
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    org_id = "orgId_example" # str | The id of organization
    acct_grp_id = "acctGrpId_example" # str | The id of account group
    account_group_request = AccountGroupRequest(None) # AccountGroupRequest | Updated account group data

    # example passing only required values which don't have defaults set
    try:
        # Update an account group
        api_response = api_instance.api_accounts_mgmt_v1_organizations_org_id_account_groups_acct_grp_id_patch(org_id, acct_grp_id, account_group_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_org_id_account_groups_acct_grp_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The id of organization |
 **acct_grp_id** | **str**| The id of account group |
 **account_group_request** | [**AccountGroupRequest**](AccountGroupRequest.md)| Updated account group data |

### Return type

[**AccountGroup**](AccountGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account group updated successfully |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No account group with specified id exists |  -  |
**500** | Unexpected error updating account group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_org_id_account_groups_get**
> AccountGroupList api_accounts_mgmt_v1_organizations_org_id_account_groups_get(org_id)

Returns a list of account groups for the given org

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.account_group_list import AccountGroupList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    org_id = "orgId_example" # str | The id of organization
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)
    order_by = "orderBy_example" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  ```sql username asc ```  Or in order to retrieve all accounts ordered by username _and_ first name:  ```sql username asc, firstName asc ```  If the parameter isn't provided, or if the value is empty, then no explicit ordering will be applied. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of account groups for the given org
        api_response = api_instance.api_accounts_mgmt_v1_organizations_org_id_account_groups_get(org_id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_org_id_account_groups_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of account groups for the given org
        api_response = api_instance.api_accounts_mgmt_v1_organizations_org_id_account_groups_get(org_id, page=page, size=size, search=search, order_by=order_by)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_org_id_account_groups_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The id of organization |
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  &#x60;&#x60;&#x60;sql username asc &#x60;&#x60;&#x60;  Or in order to retrieve all accounts ordered by username _and_ first name:  &#x60;&#x60;&#x60;sql username asc, firstName asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then no explicit ordering will be applied. | [optional]

### Return type

[**AccountGroupList**](AccountGroupList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of account groups |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No organization with specified id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_org_id_account_groups_post**
> AccountGroup api_accounts_mgmt_v1_organizations_org_id_account_groups_post(org_id, account_group_request)

Create a new AccountGroup

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.account_group import AccountGroup
from account_management_sdk.model.account_group_request import AccountGroupRequest
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    org_id = "orgId_example" # str | The id of organization
    account_group_request = AccountGroupRequest(None) # AccountGroupRequest | New AccountGroup data

    # example passing only required values which don't have defaults set
    try:
        # Create a new AccountGroup
        api_response = api_instance.api_accounts_mgmt_v1_organizations_org_id_account_groups_post(org_id, account_group_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_org_id_account_groups_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The id of organization |
 **account_group_request** | [**AccountGroupRequest**](AccountGroupRequest.md)| New AccountGroup data |

### Return type

[**AccountGroup**](AccountGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created AccountGroup successfully |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No organization with specified id exists |  -  |
**500** | An unexpected error occurred creating the label |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_org_id_consumed_quota_get**
> ConsumedQuotaList api_accounts_mgmt_v1_organizations_org_id_consumed_quota_get(org_id)

Returns a list of consumed quota for an organization

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.consumed_quota_list import ConsumedQuotaList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    org_id = "orgId_example" # str | The id of organization
    force_recalc = True # bool | If true, includes that ConsumedQuota should be recalculated. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of consumed quota for an organization
        api_response = api_instance.api_accounts_mgmt_v1_organizations_org_id_consumed_quota_get(org_id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_org_id_consumed_quota_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of consumed quota for an organization
        api_response = api_instance.api_accounts_mgmt_v1_organizations_org_id_consumed_quota_get(org_id, force_recalc=force_recalc)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_org_id_consumed_quota_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The id of organization |
 **force_recalc** | **bool**| If true, includes that ConsumedQuota should be recalculated. | [optional]

### Return type

[**ConsumedQuotaList**](ConsumedQuotaList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of ConsumedQuota objects |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No organization with specified id exists |  -  |
**500** | An unexpected error occurred when getting this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_org_id_quota_cost_get**
> QuotaCostList api_accounts_mgmt_v1_organizations_org_id_quota_cost_get(org_id)

Returns a summary of quota cost

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from account_management_sdk.model.quota_cost_list import QuotaCostList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    org_id = "orgId_example" # str | The id of organization
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)
    fetch_related_resources = True # bool | If true, includes the related resources in the output. Could slow request response time. (optional)
    force_recalc = True # bool | If true, includes that ConsumedQuota should be recalculated. (optional)
    fetch_cloud_accounts = True # bool | If true, includes the marketplace cloud accounts in the output. Could slow request response time. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a summary of quota cost
        api_response = api_instance.api_accounts_mgmt_v1_organizations_org_id_quota_cost_get(org_id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_org_id_quota_cost_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a summary of quota cost
        api_response = api_instance.api_accounts_mgmt_v1_organizations_org_id_quota_cost_get(org_id, search=search, fetch_related_resources=fetch_related_resources, force_recalc=force_recalc, fetch_cloud_accounts=fetch_cloud_accounts)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_org_id_quota_cost_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The id of organization |
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]
 **fetch_related_resources** | **bool**| If true, includes the related resources in the output. Could slow request response time. | [optional]
 **force_recalc** | **bool**| If true, includes that ConsumedQuota should be recalculated. | [optional]
 **fetch_cloud_accounts** | **bool**| If true, includes the marketplace cloud accounts in the output. Could slow request response time. | [optional]

### Return type

[**QuotaCostList**](QuotaCostList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of QuotaCost objects |  -  |
**404** | No organization with specified id exists |  -  |
**500** | An unexpected error occurred when getting this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_org_id_resource_quota_get**
> ResourceQuotaList api_accounts_mgmt_v1_organizations_org_id_resource_quota_get(org_id)

Returns a list of resource quota objects

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.resource_quota_list import ResourceQuotaList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    org_id = "orgId_example" # str | The id of organization
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)
    order_by = "orderBy_example" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  ```sql username asc ```  Or in order to retrieve all accounts ordered by username _and_ first name:  ```sql username asc, firstName asc ```  If the parameter isn't provided, or if the value is empty, then no explicit ordering will be applied. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of resource quota objects
        api_response = api_instance.api_accounts_mgmt_v1_organizations_org_id_resource_quota_get(org_id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_org_id_resource_quota_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of resource quota objects
        api_response = api_instance.api_accounts_mgmt_v1_organizations_org_id_resource_quota_get(org_id, page=page, size=size, search=search, order_by=order_by)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_org_id_resource_quota_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The id of organization |
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  &#x60;&#x60;&#x60;sql username asc &#x60;&#x60;&#x60;  Or in order to retrieve all accounts ordered by username _and_ first name:  &#x60;&#x60;&#x60;sql username asc, firstName asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then no explicit ordering will be applied. | [optional]

### Return type

[**ResourceQuotaList**](ResourceQuotaList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of ResourceQuota objects |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No organization with specified id exists |  -  |
**500** | An unexpected error occurred when getting this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_org_id_resource_quota_post**
> ResourceQuota api_accounts_mgmt_v1_organizations_org_id_resource_quota_post(org_id, resource_quota_request)

Create a new resource quota

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.resource_quota import ResourceQuota
from account_management_sdk.model.resource_quota_request import ResourceQuotaRequest
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    org_id = "orgId_example" # str | The id of organization
    resource_quota_request = ResourceQuotaRequest(
        sku="sku_example",
        sku_count=1,
        type="Config",
    ) # ResourceQuotaRequest | Resource quota data

    # example passing only required values which don't have defaults set
    try:
        # Create a new resource quota
        api_response = api_instance.api_accounts_mgmt_v1_organizations_org_id_resource_quota_post(org_id, resource_quota_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_org_id_resource_quota_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The id of organization |
 **resource_quota_request** | [**ResourceQuotaRequest**](ResourceQuotaRequest.md)| Resource quota data |

### Return type

[**ResourceQuota**](ResourceQuota.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**409** | ResourceQuota already exists |  -  |
**500** | An unexpected error occurred creating the resource quota |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_org_id_resource_quota_quota_id_delete**
> api_accounts_mgmt_v1_organizations_org_id_resource_quota_quota_id_delete(org_id, quota_id)

Delete a resource quota

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    org_id = "orgId_example" # str | The id of organization
    quota_id = "quotaId_example" # str | The id of quota

    # example passing only required values which don't have defaults set
    try:
        # Delete a resource quota
        api_instance.api_accounts_mgmt_v1_organizations_org_id_resource_quota_quota_id_delete(org_id, quota_id)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_org_id_resource_quota_quota_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The id of organization |
 **quota_id** | **str**| The id of quota |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resource Quota successfully deleted |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No Resource Quota with specified id exists |  -  |
**500** | An unexpected error occurred deleting the Resource Quota |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_org_id_resource_quota_quota_id_get**
> ResourceQuota api_accounts_mgmt_v1_organizations_org_id_resource_quota_quota_id_get(org_id, quota_id)

Get a resource quota by id

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.resource_quota import ResourceQuota
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    org_id = "orgId_example" # str | The id of organization
    quota_id = "quotaId_example" # str | The id of quota

    # example passing only required values which don't have defaults set
    try:
        # Get a resource quota by id
        api_response = api_instance.api_accounts_mgmt_v1_organizations_org_id_resource_quota_quota_id_get(org_id, quota_id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_org_id_resource_quota_quota_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The id of organization |
 **quota_id** | **str**| The id of quota |

### Return type

[**ResourceQuota**](ResourceQuota.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource quota found by id |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No resource quota with specified id exists |  -  |
**500** | An unexpected error occurred when getting this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_org_id_resource_quota_quota_id_patch**
> ResourceQuota api_accounts_mgmt_v1_organizations_org_id_resource_quota_quota_id_patch(org_id, quota_id, resource_quota_request)

Update a resource quota

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.resource_quota import ResourceQuota
from account_management_sdk.model.resource_quota_request import ResourceQuotaRequest
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    org_id = "orgId_example" # str | The id of organization
    quota_id = "quotaId_example" # str | The id of quota
    resource_quota_request = ResourceQuotaRequest(
        sku="sku_example",
        sku_count=1,
        type="Config",
    ) # ResourceQuotaRequest | Updated resource quota data

    # example passing only required values which don't have defaults set
    try:
        # Update a resource quota
        api_response = api_instance.api_accounts_mgmt_v1_organizations_org_id_resource_quota_quota_id_patch(org_id, quota_id, resource_quota_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_org_id_resource_quota_quota_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| The id of organization |
 **quota_id** | **str**| The id of quota |
 **resource_quota_request** | [**ResourceQuotaRequest**](ResourceQuotaRequest.md)| Updated resource quota data |

### Return type

[**ResourceQuota**](ResourceQuota.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource Quota updated successfully |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No resource quota with specified id exists |  -  |
**500** | Unexpected error updating resource quota |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_organizations_post**
> Organization api_accounts_mgmt_v1_organizations_post(organization)

Create a new organization

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from account_management_sdk.model.organization import Organization
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    organization = Organization(None) # Organization | Organization data

    # example passing only required values which don't have defaults set
    try:
        # Create a new organization
        api_response = api_instance.api_accounts_mgmt_v1_organizations_post(organization)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_organizations_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | [**Organization**](Organization.md)| Organization data |

### Return type

[**Organization**](Organization.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**409** | Organization already exists |  -  |
**500** | An unexpected error occurred creating the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_plans_get**
> PlanList api_accounts_mgmt_v1_plans_get()

Get all plans

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.plan_list import PlanList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all plans
        api_response = api_instance.api_accounts_mgmt_v1_plans_get(page=page, size=size, search=search)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_plans_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]

### Return type

[**PlanList**](PlanList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plans list |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_plans_id_get**
> Plan api_accounts_mgmt_v1_plans_id_get(id)

Get a plan by id

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.plan import Plan
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record

    # example passing only required values which don't have defaults set
    try:
        # Get a plan by id
        api_response = api_instance.api_accounts_mgmt_v1_plans_id_get(id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_plans_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |

### Return type

[**Plan**](Plan.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plan found |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No plan with specified id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_pull_secrets_external_resource_id_delete**
> api_accounts_mgmt_v1_pull_secrets_external_resource_id_delete(external_resource_id)

Delete a pull secret

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    external_resource_id = "externalResourceId_example" # str | The external resource id of record

    # example passing only required values which don't have defaults set
    try:
        # Delete a pull secret
        api_instance.api_accounts_mgmt_v1_pull_secrets_external_resource_id_delete(external_resource_id)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_pull_secrets_external_resource_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_resource_id** | **str**| The external resource id of record |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Pull secret successfully deleted |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to delete pull secret |  -  |
**404** | No Pull secret with specified id exists |  -  |
**500** | An unexpected error occurred deleting the pull secret |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_pull_secrets_post**
> AccessTokenCfg api_accounts_mgmt_v1_pull_secrets_post(pull_secret_request)

Return access token generated from registries in docker format

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.access_token_cfg import AccessTokenCfg
from account_management_sdk.model.pull_secret_request import PullSecretRequest
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    pull_secret_request = PullSecretRequest(
        external_resource_id="external_resource_id_example",
    ) # PullSecretRequest | Identifier of the resource in the external service that this pull secret relates to

    # example passing only required values which don't have defaults set
    try:
        # Return access token generated from registries in docker format
        api_response = api_instance.api_accounts_mgmt_v1_pull_secrets_post(pull_secret_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_pull_secrets_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pull_secret_request** | [**PullSecretRequest**](PullSecretRequest.md)| Identifier of the resource in the external service that this pull secret relates to |

### Return type

[**AccessTokenCfg**](AccessTokenCfg.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | access token from registries in docker format |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | Cannot find registry |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_quota_cost_get**
> QuotaCostList api_accounts_mgmt_v1_quota_cost_get()

Returns a summary of quota cost for the authenticated user

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from account_management_sdk.model.quota_cost_list import QuotaCostList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)
    fetch_related_resources = True # bool | If true, includes the related resources in the output. Could slow request response time. (optional)
    fetch_cloud_accounts = True # bool | If true, includes the marketplace cloud accounts in the output. Could slow request response time. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a summary of quota cost for the authenticated user
        api_response = api_instance.api_accounts_mgmt_v1_quota_cost_get(search=search, fetch_related_resources=fetch_related_resources, fetch_cloud_accounts=fetch_cloud_accounts)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_quota_cost_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]
 **fetch_related_resources** | **bool**| If true, includes the related resources in the output. Could slow request response time. | [optional]
 **fetch_cloud_accounts** | **bool**| If true, includes the marketplace cloud accounts in the output. Could slow request response time. | [optional]

### Return type

[**QuotaCostList**](QuotaCostList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of QuotaCost objects |  -  |
**400** | Validation errors occurred |  -  |
**500** | An unexpected error occurred when getting this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_quota_rules_get**
> QuotaRulesList api_accounts_mgmt_v1_quota_rules_get()

Returns a list of UHC product Quota Rules

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.quota_rules_list import QuotaRulesList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of UHC product Quota Rules
        api_response = api_instance.api_accounts_mgmt_v1_quota_rules_get(page=page, size=size, search=search)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_quota_rules_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]

### Return type

[**QuotaRulesList**](QuotaRulesList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of quota rules objects |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_quotas_get**
> QuotaList api_accounts_mgmt_v1_quotas_get()

Returns a list of quotas

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.quota_list import QuotaList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of quotas
        api_response = api_instance.api_accounts_mgmt_v1_quotas_get(page=page, size=size, search=search)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_quotas_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]

### Return type

[**QuotaList**](QuotaList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of quota objects |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_quotas_id_delete**
> api_accounts_mgmt_v1_quotas_id_delete(id)

Delete a quota

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record

    # example passing only required values which don't have defaults set
    try:
        # Delete a quota
        api_instance.api_accounts_mgmt_v1_quotas_id_delete(id)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_quotas_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Quota successfully deleted |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No quota with specified id exists |  -  |
**500** | An unexpected error occurred deleting the quota |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_quotas_id_get**
> Quota api_accounts_mgmt_v1_quotas_id_get(id)

Get a quota

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.quota import Quota
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record

    # example passing only required values which don't have defaults set
    try:
        # Get a quota
        api_response = api_instance.api_accounts_mgmt_v1_quotas_id_get(id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_quotas_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |

### Return type

[**Quota**](Quota.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Quota found by id |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No quota with specified id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_quotas_id_patch**
> Quota api_accounts_mgmt_v1_quotas_id_patch(id, quota)

Update a quota

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.quota import Quota
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    quota = Quota(None) # Quota | Updated quota data

    # example passing only required values which don't have defaults set
    try:
        # Update a quota
        api_response = api_instance.api_accounts_mgmt_v1_quotas_id_patch(id, quota)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_quotas_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **quota** | [**Quota**](Quota.md)| Updated quota data |

### Return type

[**Quota**](Quota.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Quota updated successfully |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No quota with specified id exists |  -  |
**500** | Unexpected error updating quota |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_quotas_post**
> Quota api_accounts_mgmt_v1_quotas_post(quota)

Create a new quota

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.quota import Quota
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    quota = Quota(None) # Quota | Quota data

    # example passing only required values which don't have defaults set
    try:
        # Create a new quota
        api_response = api_instance.api_accounts_mgmt_v1_quotas_post(quota)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_quotas_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quota** | [**Quota**](Quota.md)| Quota data |

### Return type

[**Quota**](Quota.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**409** | Quota already exists |  -  |
**500** | An unexpected error occurred creating quota |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_registries_get**
> RegistryList api_accounts_mgmt_v1_registries_get()

Returns a list of registries

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.registry_list import RegistryList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)
    order_by = "orderBy_example" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  ```sql username asc ```  Or in order to retrieve all accounts ordered by username _and_ first name:  ```sql username asc, firstName asc ```  If the parameter isn't provided, or if the value is empty, then no explicit ordering will be applied. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of registries
        api_response = api_instance.api_accounts_mgmt_v1_registries_get(page=page, size=size, search=search, order_by=order_by)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_registries_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  &#x60;&#x60;&#x60;sql username asc &#x60;&#x60;&#x60;  Or in order to retrieve all accounts ordered by username _and_ first name:  &#x60;&#x60;&#x60;sql username asc, firstName asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then no explicit ordering will be applied. | [optional]

### Return type

[**RegistryList**](RegistryList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of registry objects |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_registries_id_get**
> Registry api_accounts_mgmt_v1_registries_id_get(id)

Get an registry by id

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.registry import Registry
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record

    # example passing only required values which don't have defaults set
    try:
        # Get an registry by id
        api_response = api_instance.api_accounts_mgmt_v1_registries_id_get(id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_registries_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |

### Return type

[**Registry**](Registry.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Registry found by id |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No registry with specified id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_registry_credentials_get**
> RegistryCredentialList api_accounts_mgmt_v1_registry_credentials_get()



List Registry Credentials

### Example


```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.registry_credential_list import RegistryCredentialList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)


# Enter a context with an instance of the API client
with account_management_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)
    order_by = "orderBy_example" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  ```sql username asc ```  Or in order to retrieve all accounts ordered by username _and_ first name:  ```sql username asc, firstName asc ```  If the parameter isn't provided, or if the value is empty, then no explicit ordering will be applied. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_accounts_mgmt_v1_registry_credentials_get(page=page, size=size, search=search, order_by=order_by)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_registry_credentials_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  &#x60;&#x60;&#x60;sql username asc &#x60;&#x60;&#x60;  Or in order to retrieve all accounts ordered by username _and_ first name:  &#x60;&#x60;&#x60;sql username asc, firstName asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then no explicit ordering will be applied. | [optional]

### Return type

[**RegistryCredentialList**](RegistryCredentialList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of RegistryCredential objects |  -  |
**401** | Auth token is invalid |  -  |
**403** | Not allowed to list RegistryCredentials |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_registry_credentials_id_delete**
> api_accounts_mgmt_v1_registry_credentials_id_delete(id)

Delete a registry credential by id

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record

    # example passing only required values which don't have defaults set
    try:
        # Delete a registry credential by id
        api_instance.api_accounts_mgmt_v1_registry_credentials_id_delete(id)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_registry_credentials_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Registry credential successfully deleted |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No registry credential with specified id exists |  -  |
**500** | An unexpected error occurred deleting the registry credential |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_registry_credentials_id_get**
> RegistryCredential api_accounts_mgmt_v1_registry_credentials_id_get(id)

Get a registry credentials by id

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.registry_credential import RegistryCredential
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record

    # example passing only required values which don't have defaults set
    try:
        # Get a registry credentials by id
        api_response = api_instance.api_accounts_mgmt_v1_registry_credentials_id_get(id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_registry_credentials_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |

### Return type

[**RegistryCredential**](RegistryCredential.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Registry credential found |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No registry credential with specified id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_registry_credentials_id_patch**
> RegistryCredential api_accounts_mgmt_v1_registry_credentials_id_patch(id, registry_credential_patch_request)

Update a registry credential

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.registry_credential_patch_request import RegistryCredentialPatchRequest
from account_management_sdk.model.registry_credential import RegistryCredential
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    registry_credential_patch_request = RegistryCredentialPatchRequest(
        account_id="account_id_example",
        external_resource_id="external_resource_id_example",
        registry_id="registry_id_example",
        token="token_example",
        username="username_example",
    ) # RegistryCredentialPatchRequest | Updated registry credential data

    # example passing only required values which don't have defaults set
    try:
        # Update a registry credential
        api_response = api_instance.api_accounts_mgmt_v1_registry_credentials_id_patch(id, registry_credential_patch_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_registry_credentials_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **registry_credential_patch_request** | [**RegistryCredentialPatchRequest**](RegistryCredentialPatchRequest.md)| Updated registry credential data |

### Return type

[**RegistryCredential**](RegistryCredential.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Registry credential updated successfully |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Not allowed to update registry credential or the specified field(s) |  -  |
**404** | No registry credential with specified id exists |  -  |
**500** | Unexpected error updating registry credential |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_registry_credentials_post**
> RegistryCredential api_accounts_mgmt_v1_registry_credentials_post(registry_credential)

Request the creation of a registry credential

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.registry_credential import RegistryCredential
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    registry_credential = RegistryCredential(None) # RegistryCredential | Registry credential data

    # example passing only required values which don't have defaults set
    try:
        # Request the creation of a registry credential
        api_response = api_instance.api_accounts_mgmt_v1_registry_credentials_post(registry_credential)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_registry_credentials_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_credential** | [**RegistryCredential**](RegistryCredential.md)| Registry credential data |

### Return type

[**RegistryCredential**](RegistryCredential.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Registry credential created |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Not allowed to create RegistryCredentials |  -  |
**409** | A RegistryCredential with this type already exists for this user |  -  |
**500** | Unable to create Registry Credential |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_reserved_resources_get**
> ReservedResourceList api_accounts_mgmt_v1_reserved_resources_get()

Returns a list of reserved resources

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.reserved_resource_list import ReservedResourceList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)
    order_by = "orderBy_example" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  ```sql username asc ```  Or in order to retrieve all accounts ordered by username _and_ first name:  ```sql username asc, firstName asc ```  If the parameter isn't provided, or if the value is empty, then no explicit ordering will be applied. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of reserved resources
        api_response = api_instance.api_accounts_mgmt_v1_reserved_resources_get(page=page, size=size, search=search, order_by=order_by)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_reserved_resources_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  &#x60;&#x60;&#x60;sql username asc &#x60;&#x60;&#x60;  Or in order to retrieve all accounts ordered by username _and_ first name:  &#x60;&#x60;&#x60;sql username asc, firstName asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then no explicit ordering will be applied. | [optional]

### Return type

[**ReservedResourceList**](ReservedResourceList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of reserved resource objects |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_resource_quota_get**
> ResourceQuotaList api_accounts_mgmt_v1_resource_quota_get()

Returns a list of resource quota objects

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.resource_quota_list import ResourceQuotaList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)
    order_by = "orderBy_example" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  ```sql username asc ```  Or in order to retrieve all accounts ordered by username _and_ first name:  ```sql username asc, firstName asc ```  If the parameter isn't provided, or if the value is empty, then no explicit ordering will be applied. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of resource quota objects
        api_response = api_instance.api_accounts_mgmt_v1_resource_quota_get(page=page, size=size, search=search, order_by=order_by)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_resource_quota_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  &#x60;&#x60;&#x60;sql username asc &#x60;&#x60;&#x60;  Or in order to retrieve all accounts ordered by username _and_ first name:  &#x60;&#x60;&#x60;sql username asc, firstName asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then no explicit ordering will be applied. | [optional]

### Return type

[**ResourceQuotaList**](ResourceQuotaList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of ResourceQuota objects |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | An unexpected error occurred when getting this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_role_bindings_get**
> RoleBindingList api_accounts_mgmt_v1_role_bindings_get()

Returns a list of role bindings

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.role_binding_list import RoleBindingList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)
    order_by = "orderBy_example" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  ```sql username asc ```  Or in order to retrieve all accounts ordered by username _and_ first name:  ```sql username asc, firstName asc ```  If the parameter isn't provided, or if the value is empty, then no explicit ordering will be applied. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of role bindings
        api_response = api_instance.api_accounts_mgmt_v1_role_bindings_get(page=page, size=size, search=search, order_by=order_by)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_role_bindings_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  &#x60;&#x60;&#x60;sql username asc &#x60;&#x60;&#x60;  Or in order to retrieve all accounts ordered by username _and_ first name:  &#x60;&#x60;&#x60;sql username asc, firstName asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then no explicit ordering will be applied. | [optional]

### Return type

[**RoleBindingList**](RoleBindingList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of role binding objects |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_role_bindings_id_delete**
> api_accounts_mgmt_v1_role_bindings_id_delete(id)

Delete a role binding

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record

    # example passing only required values which don't have defaults set
    try:
        # Delete a role binding
        api_instance.api_accounts_mgmt_v1_role_bindings_id_delete(id)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_role_bindings_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Role binding successfully deleted |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No role binding with specified id exists |  -  |
**500** | An unexpected error occurred deleting the role binding |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_role_bindings_id_get**
> RoleBinding api_accounts_mgmt_v1_role_bindings_id_get(id)

Get a role binding

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.role_binding import RoleBinding
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record

    # example passing only required values which don't have defaults set
    try:
        # Get a role binding
        api_response = api_instance.api_accounts_mgmt_v1_role_bindings_id_get(id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_role_bindings_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |

### Return type

[**RoleBinding**](RoleBinding.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Role binding found by id |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No role binding with specified id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_role_bindings_id_patch**
> RoleBinding api_accounts_mgmt_v1_role_bindings_id_patch(id, role_binding_request)

Update a role binding

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.role_binding import RoleBinding
from account_management_sdk.model.role_binding_request import RoleBindingRequest
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    role_binding_request = RoleBindingRequest(
        account_group_id="account_group_id_example",
        account_id="account_id_example",
        config_managed=True,
        managed_by="managed_by_example",
        organization_id="organization_id_example",
        role_id="role_id_example",
        subscription_id="subscription_id_example",
        type="type_example",
    ) # RoleBindingRequest | Updated role binding data

    # example passing only required values which don't have defaults set
    try:
        # Update a role binding
        api_response = api_instance.api_accounts_mgmt_v1_role_bindings_id_patch(id, role_binding_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_role_bindings_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **role_binding_request** | [**RoleBindingRequest**](RoleBindingRequest.md)| Updated role binding data |

### Return type

[**RoleBinding**](RoleBinding.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Role Binding updated successfully |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No role binding with specified id exists |  -  |
**500** | Unexpected error updating role binding |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_role_bindings_post**
> RoleBinding api_accounts_mgmt_v1_role_bindings_post(role_binding_create_request)

Create a new role binding

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.role_binding_create_request import RoleBindingCreateRequest
from account_management_sdk.model.role_binding import RoleBinding
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    role_binding_create_request = RoleBindingCreateRequest(None) # RoleBindingCreateRequest | Role binding data

    # example passing only required values which don't have defaults set
    try:
        # Create a new role binding
        api_response = api_instance.api_accounts_mgmt_v1_role_bindings_post(role_binding_create_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_role_bindings_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_binding_create_request** | [**RoleBindingCreateRequest**](RoleBindingCreateRequest.md)| Role binding data |

### Return type

[**RoleBinding**](RoleBinding.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**409** | Role binding already exists |  -  |
**500** | An unexpected error occurred creating role binding |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_roles_get**
> RoleList api_accounts_mgmt_v1_roles_get()

Returns a list of roles

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.role_list import RoleList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of roles
        api_response = api_instance.api_accounts_mgmt_v1_roles_get(page=page, size=size, search=search)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_roles_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]

### Return type

[**RoleList**](RoleList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of role objects |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_roles_id_get**
> Role api_accounts_mgmt_v1_roles_id_get(id)

Get a role by id

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.role import Role
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record

    # example passing only required values which don't have defaults set
    try:
        # Get a role by id
        api_response = api_instance.api_accounts_mgmt_v1_roles_id_get(id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_roles_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |

### Return type

[**Role**](Role.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Role found by id |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No role with specified id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_self_entitlement_product_post**
> SelfEntitlementStatus api_accounts_mgmt_v1_self_entitlement_product_post(product)

Create or renew the entitlement to support a product for the user's organization.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.self_entitlement_status import SelfEntitlementStatus
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    product = "product_example" # str | The product for self_entitlement. The supported products are [rosa].

    # example passing only required values which don't have defaults set
    try:
        # Create or renew the entitlement to support a product for the user's organization.
        api_response = api_instance.api_accounts_mgmt_v1_self_entitlement_product_post(product)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_self_entitlement_product_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**| The product for self_entitlement. The supported products are [rosa]. |

### Return type

[**SelfEntitlementStatus**](SelfEntitlementStatus.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the requested entitlement already exists |  -  |
**201** | the requested entitlement has been created or renewed |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | Cannot find account or organization |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_sku_rules_get**
> SkuRulesList api_accounts_mgmt_v1_sku_rules_get()

Returns a list of UHC product SKU Rules

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.sku_rules_list import SkuRulesList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of UHC product SKU Rules
        api_response = api_instance.api_accounts_mgmt_v1_sku_rules_get(search=search)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_sku_rules_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]

### Return type

[**SkuRulesList**](SkuRulesList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of sku rules objects |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_sku_rules_id_delete**
> api_accounts_mgmt_v1_sku_rules_id_delete(id)

Delete a sku rule

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record

    # example passing only required values which don't have defaults set
    try:
        # Delete a sku rule
        api_instance.api_accounts_mgmt_v1_sku_rules_id_delete(id)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_sku_rules_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Sku rule successfully deleted |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No sku rule with specified id exists |  -  |
**500** | An unexpected error occurred deleting the sku rule |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_sku_rules_id_get**
> SkuRules api_accounts_mgmt_v1_sku_rules_id_get(id)

Get a sku rules by id

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.sku_rules import SkuRules
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record

    # example passing only required values which don't have defaults set
    try:
        # Get a sku rules by id
        api_response = api_instance.api_accounts_mgmt_v1_sku_rules_id_get(id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_sku_rules_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |

### Return type

[**SkuRules**](SkuRules.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | sku rules found by id |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No sku rules with specified id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_sku_rules_id_patch**
> SkuRules api_accounts_mgmt_v1_sku_rules_id_patch(id, sku_rules)

Update a sku rule

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.sku_rules import SkuRules
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    sku_rules = SkuRules(None) # SkuRules | Updated sku rule data

    # example passing only required values which don't have defaults set
    try:
        # Update a sku rule
        api_response = api_instance.api_accounts_mgmt_v1_sku_rules_id_patch(id, sku_rules)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_sku_rules_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **sku_rules** | [**SkuRules**](SkuRules.md)| Updated sku rule data |

### Return type

[**SkuRules**](SkuRules.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sku rule updated successfully |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No sku rule with specified id exists |  -  |
**500** | Unexpected error updating sku rule |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_sku_rules_post**
> SkuRules api_accounts_mgmt_v1_sku_rules_post(sku_rules)

Create a new sku rule

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.sku_rules import SkuRules
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    sku_rules = SkuRules(None) # SkuRules | Sku rule data

    # example passing only required values which don't have defaults set
    try:
        # Create a new sku rule
        api_response = api_instance.api_accounts_mgmt_v1_sku_rules_post(sku_rules)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_sku_rules_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku_rules** | [**SkuRules**](SkuRules.md)| Sku rule data |

### Return type

[**SkuRules**](SkuRules.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**409** | Sku rule already exists |  -  |
**500** | An unexpected error occurred creating sku rule |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_skus_get**
> SkuList api_accounts_mgmt_v1_skus_get()

Returns a list of UHC product SKUs

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.sku_list import SkuList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of UHC product SKUs
        api_response = api_instance.api_accounts_mgmt_v1_skus_get(search=search)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_skus_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]

### Return type

[**SkuList**](SkuList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of sku objects |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_skus_id_get**
> SKU api_accounts_mgmt_v1_skus_id_get(id)

Get a sku by id

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.sku import SKU
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record

    # example passing only required values which don't have defaults set
    try:
        # Get a sku by id
        api_response = api_instance.api_accounts_mgmt_v1_skus_id_get(id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_skus_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |

### Return type

[**SKU**](SKU.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | sku found by id |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No sku with specified id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_subscriptions_get**
> SubscriptionList api_accounts_mgmt_v1_subscriptions_get()

Returns a list of subscriptions

### Example

* Api Key Authentication (AccessToken):
* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.subscription_list import SubscriptionList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)
    fetch_accounts = True # bool | If true, includes the account reference information in the output. Could slow request response time. (optional)
    fetch_labels = True # bool | If true, includes the labels on a subscription/organization/account in the output. Could slow request response time. (optional)
    fetch_capabilities = True # bool | If true, includes the capabilities on a subscription in the output. Could slow request response time. (optional)
    fields = "fields_example" # str | Supplies a comma-separated list of fields to be returned. Fields of sub-structures and of arrays use <structure>.<field> notation. <stucture>.* means all field of a structure Example: For each Subscription to get id, href, plan(id and kind) and labels (all fields)  ``` ocm get subscriptions --parameter fields=id,href,plan.id,plan.kind,labels.* --parameter fetchLabels=true ``` (optional)
    order_by = "orderBy_example" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  ```sql username asc ```  Or in order to retrieve all accounts ordered by username _and_ first name:  ```sql username asc, firstName asc ```  If the parameter isn't provided, or if the value is empty, then no explicit ordering will be applied. (optional)
    labels = "labels_example" # str | Specifies the criteria to filter the subscription resource based on their labels. A label is represented as a `key=value` pair,  ``` labels = \"foo=bar\" ```  and multiple labels are separated by comma,  ``` labels = \"foo=bar,fooz=barz\" ``` (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of subscriptions
        api_response = api_instance.api_accounts_mgmt_v1_subscriptions_get(page=page, size=size, search=search, fetch_accounts=fetch_accounts, fetch_labels=fetch_labels, fetch_capabilities=fetch_capabilities, fields=fields, order_by=order_by, labels=labels)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]
 **fetch_accounts** | **bool**| If true, includes the account reference information in the output. Could slow request response time. | [optional]
 **fetch_labels** | **bool**| If true, includes the labels on a subscription/organization/account in the output. Could slow request response time. | [optional]
 **fetch_capabilities** | **bool**| If true, includes the capabilities on a subscription in the output. Could slow request response time. | [optional]
 **fields** | **str**| Supplies a comma-separated list of fields to be returned. Fields of sub-structures and of arrays use &lt;structure&gt;.&lt;field&gt; notation. &lt;stucture&gt;.* means all field of a structure Example: For each Subscription to get id, href, plan(id and kind) and labels (all fields)  &#x60;&#x60;&#x60; ocm get subscriptions --parameter fields&#x3D;id,href,plan.id,plan.kind,labels.* --parameter fetchLabels&#x3D;true &#x60;&#x60;&#x60; | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  &#x60;&#x60;&#x60;sql username asc &#x60;&#x60;&#x60;  Or in order to retrieve all accounts ordered by username _and_ first name:  &#x60;&#x60;&#x60;sql username asc, firstName asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then no explicit ordering will be applied. | [optional]
 **labels** | **str**| Specifies the criteria to filter the subscription resource based on their labels. A label is represented as a &#x60;key&#x3D;value&#x60; pair,  &#x60;&#x60;&#x60; labels &#x3D; \&quot;foo&#x3D;bar\&quot; &#x60;&#x60;&#x60;  and multiple labels are separated by comma,  &#x60;&#x60;&#x60; labels &#x3D; \&quot;foo&#x3D;bar,fooz&#x3D;barz\&quot; &#x60;&#x60;&#x60; | [optional]

### Return type

[**SubscriptionList**](SubscriptionList.md)

### Authorization

[AccessToken](../README.md#AccessToken), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of subscription objects |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_subscriptions_id_delete**
> api_accounts_mgmt_v1_subscriptions_id_delete(id)

Deletes a subscription by id

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record

    # example passing only required values which don't have defaults set
    try:
        # Deletes a subscription by id
        api_instance.api_accounts_mgmt_v1_subscriptions_id_delete(id)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription deprovisioned by id |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No subscription with specified id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_subscriptions_id_get**
> Subscription api_accounts_mgmt_v1_subscriptions_id_get(id)

Get a subscription by id

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.subscription import Subscription
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    fetch_accounts = True # bool | If true, includes the account reference information in the output. Could slow request response time. (optional)
    fetch_labels = True # bool | If true, includes the labels on a subscription/organization/account in the output. Could slow request response time. (optional)
    fetch_capabilities = True # bool | If true, includes the capabilities on a subscription in the output. Could slow request response time. (optional)
    fetch_cpu_and_socket = True # bool | If true, fetches, from the clusters service, the total numbers of CPU's and sockets under an obligation, and includes in the output. Could slow request response time. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a subscription by id
        api_response = api_instance.api_accounts_mgmt_v1_subscriptions_id_get(id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a subscription by id
        api_response = api_instance.api_accounts_mgmt_v1_subscriptions_id_get(id, fetch_accounts=fetch_accounts, fetch_labels=fetch_labels, fetch_capabilities=fetch_capabilities, fetch_cpu_and_socket=fetch_cpu_and_socket)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **fetch_accounts** | **bool**| If true, includes the account reference information in the output. Could slow request response time. | [optional]
 **fetch_labels** | **bool**| If true, includes the labels on a subscription/organization/account in the output. Could slow request response time. | [optional]
 **fetch_capabilities** | **bool**| If true, includes the capabilities on a subscription in the output. Could slow request response time. | [optional]
 **fetch_cpu_and_socket** | **bool**| If true, fetches, from the clusters service, the total numbers of CPU&#39;s and sockets under an obligation, and includes in the output. Could slow request response time. | [optional]

### Return type

[**Subscription**](Subscription.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription found by id |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No subscription with specified id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_subscriptions_id_labels_get**
> LabelList api_accounts_mgmt_v1_subscriptions_id_labels_get(id)

Returns a list of labels

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.label_list import LabelList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)
    order_by = "orderBy_example" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  ```sql username asc ```  Or in order to retrieve all accounts ordered by username _and_ first name:  ```sql username asc, firstName asc ```  If the parameter isn't provided, or if the value is empty, then no explicit ordering will be applied. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of labels
        api_response = api_instance.api_accounts_mgmt_v1_subscriptions_id_labels_get(id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_id_labels_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of labels
        api_response = api_instance.api_accounts_mgmt_v1_subscriptions_id_labels_get(id, page=page, size=size, search=search, order_by=order_by)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_id_labels_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  &#x60;&#x60;&#x60;sql username asc &#x60;&#x60;&#x60;  Or in order to retrieve all accounts ordered by username _and_ first name:  &#x60;&#x60;&#x60;sql username asc, firstName asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then no explicit ordering will be applied. | [optional]

### Return type

[**LabelList**](LabelList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of label |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_subscriptions_id_labels_key_delete**
> api_accounts_mgmt_v1_subscriptions_id_labels_key_delete(id, key)

Delete a label

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    key = "key_example" # str | The key of the label

    # example passing only required values which don't have defaults set
    try:
        # Delete a label
        api_instance.api_accounts_mgmt_v1_subscriptions_id_labels_key_delete(id, key)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_id_labels_key_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **key** | **str**| The key of the label |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Label successfully deleted |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No label with specified key on specified subscription id exists |  -  |
**500** | An unexpected error occurred deleting the label |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_subscriptions_id_labels_key_get**
> Label api_accounts_mgmt_v1_subscriptions_id_labels_key_get(id, key)

Get subscription labels by label key

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.label import Label
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    key = "key_example" # str | The key of the label

    # example passing only required values which don't have defaults set
    try:
        # Get subscription labels by label key
        api_response = api_instance.api_accounts_mgmt_v1_subscriptions_id_labels_key_get(id, key)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_id_labels_key_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **key** | **str**| The key of the label |

### Return type

[**Label**](Label.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Labels found by key |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No label with specified key on specified subscription id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_subscriptions_id_labels_key_patch**
> Label api_accounts_mgmt_v1_subscriptions_id_labels_key_patch(id, key, label)

Create a new label or update an existing label

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.label import Label
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    key = "key_example" # str | The key of the label
    label = Label(None) # Label | Label data

    # example passing only required values which don't have defaults set
    try:
        # Create a new label or update an existing label
        api_response = api_instance.api_accounts_mgmt_v1_subscriptions_id_labels_key_patch(id, key, label)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_id_labels_key_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **key** | **str**| The key of the label |
 **label** | [**Label**](Label.md)| Label data |

### Return type

[**Label**](Label.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created or updated label successfully |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**409** | Label already exists and cannot be updated |  -  |
**500** | Unexpected error updating subscription label |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_subscriptions_id_labels_post**
> Label api_accounts_mgmt_v1_subscriptions_id_labels_post(id, label)

Create a new label or update an existing label

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.label import Label
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    label = Label(None) # Label | Label data

    # example passing only required values which don't have defaults set
    try:
        # Create a new label or update an existing label
        api_response = api_instance.api_accounts_mgmt_v1_subscriptions_id_labels_post(id, label)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_id_labels_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **label** | [**Label**](Label.md)| Label data |

### Return type

[**Label**](Label.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created or updated label successfully |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | An unexpected error occurred creating the label |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_subscriptions_id_metrics_metric_name_get**
> SubscriptionMetricList api_accounts_mgmt_v1_subscriptions_id_metrics_metric_name_get(id, metric_name)

Get subscription's metrics by metric name

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.subscription_metric_list import SubscriptionMetricList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    metric_name = "metric_name_example" # str | The name of the metric
    search = "search_example" # str | The `search` paramter specifies the PromQL selector. The syntax is defined by Prometheus at https://prometheus.io/docs/prometheus/latest/querying/basics/#time-series-selectors. It only supports simple selections as shown in https://prometheus.io/docs/prometheus/latest/querying/examples/#simple-time-series-selection. For example, in order to retrieve subscription_sync_total with names starting with `managed` and with a channel = `production`:  ``` name=~'managed.*',channel='production' ```  If the parameter isn't provided, or if the value is empty, then all the records will be returned. (optional)
    fields = "fields_example" # str | Supplies a comma-separated list of fields to be returned. Fields of sub-structures and of arrays use <structure>.<field> notation. <stucture>.* means all field of a structure Example: For each Subscription to get id, href, plan(id and kind) and labels (all fields)  ``` ocm get subscriptions --parameter fields=id,href,plan.id,plan.kind,labels.* --parameter fetchLabels=true ``` (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get subscription's metrics by metric name
        api_response = api_instance.api_accounts_mgmt_v1_subscriptions_id_metrics_metric_name_get(id, metric_name)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_id_metrics_metric_name_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get subscription's metrics by metric name
        api_response = api_instance.api_accounts_mgmt_v1_subscriptions_id_metrics_metric_name_get(id, metric_name, search=search, fields=fields)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_id_metrics_metric_name_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **metric_name** | **str**| The name of the metric |
 **search** | **str**| The &#x60;search&#x60; paramter specifies the PromQL selector. The syntax is defined by Prometheus at https://prometheus.io/docs/prometheus/latest/querying/basics/#time-series-selectors. It only supports simple selections as shown in https://prometheus.io/docs/prometheus/latest/querying/examples/#simple-time-series-selection. For example, in order to retrieve subscription_sync_total with names starting with &#x60;managed&#x60; and with a channel &#x3D; &#x60;production&#x60;:  &#x60;&#x60;&#x60; name&#x3D;~&#39;managed.*&#39;,channel&#x3D;&#39;production&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the records will be returned. | [optional]
 **fields** | **str**| Supplies a comma-separated list of fields to be returned. Fields of sub-structures and of arrays use &lt;structure&gt;.&lt;field&gt; notation. &lt;stucture&gt;.* means all field of a structure Example: For each Subscription to get id, href, plan(id and kind) and labels (all fields)  &#x60;&#x60;&#x60; ocm get subscriptions --parameter fields&#x3D;id,href,plan.id,plan.kind,labels.* --parameter fetchLabels&#x3D;true &#x60;&#x60;&#x60; | [optional]

### Return type

[**SubscriptionMetricList**](SubscriptionMetricList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metrics&#39; data |  -  |
**400** | Metric name is invalid |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_subscriptions_id_notify_post**
> api_accounts_mgmt_v1_subscriptions_id_notify_post(id, notification_request)

Notify the owner of a subscription

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.notification_request import NotificationRequest
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    notification_request = NotificationRequest(
        bcc_address="bcc_address_example",
        cluster_id="cluster_id_example",
        cluster_uuid="cluster_uuid_example",
        include_red_hat_associates=True,
        internal_only=True,
        subject="subject_example",
        subscription_id="subscription_id_example",
        template_name="template_name_example",
        template_parameters=[
            TemplateParameter(
                content="content_example",
                name="name_example",
            ),
        ],
    ) # NotificationRequest | The contents of the notification to send to the owner of a subscription in addition to the set of template parameters which are sent automatically ACCOUNT_USERNAME, FIRST_NAME, LAST_NAME, ORGANIZATION_NAME, ORGANIZATION_EXTERNAL_ID

    # example passing only required values which don't have defaults set
    try:
        # Notify the owner of a subscription
        api_instance.api_accounts_mgmt_v1_subscriptions_id_notify_post(id, notification_request)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_id_notify_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **notification_request** | [**NotificationRequest**](NotificationRequest.md)| The contents of the notification to send to the owner of a subscription in addition to the set of template parameters which are sent automatically ACCOUNT_USERNAME, FIRST_NAME, LAST_NAME, ORGANIZATION_NAME, ORGANIZATION_EXTERNAL_ID |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Notification created and queued to be sent soon |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_subscriptions_id_patch**
> Subscription api_accounts_mgmt_v1_subscriptions_id_patch(id, subscription_patch_request)

Update a subscription

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.subscription import Subscription
from account_management_sdk.model.subscription_patch_request import SubscriptionPatchRequest
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    subscription_patch_request = SubscriptionPatchRequest(
        billing_expiration_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        cloud_account_id="cloud_account_id_example",
        cloud_provider_id="cloud_provider_id_example",
        cluster_billing_model="standard",
        cluster_id="cluster_id_example",
        console_url="console_url_example",
        consumer_uuid="consumer_uuid_example",
        cpu_total=1,
        creator_id="creator_id_example",
        display_name="display_name_example",
        external_cluster_id="external_cluster_id_example",
        managed=True,
        organization_id="organization_id_example",
        plan_id="plan_id_example",
        product_bundle="Openshift",
        provenance="provenance_example",
        region_id="region_id_example",
        released=True,
        service_level="L1-L3",
        socket_total=1,
        status="status_example",
        support_level="Eval",
        system_units="Cores/vCPU",
        trial_end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        usage="Production",
    ) # SubscriptionPatchRequest | Updated subscription data

    # example passing only required values which don't have defaults set
    try:
        # Update a subscription
        api_response = api_instance.api_accounts_mgmt_v1_subscriptions_id_patch(id, subscription_patch_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **subscription_patch_request** | [**SubscriptionPatchRequest**](SubscriptionPatchRequest.md)| Updated subscription data |

### Return type

[**Subscription**](Subscription.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription updated successfully |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Not allowed to update subscriptions or the specified field(s) |  -  |
**404** | No subscription with specified id exists |  -  |
**500** | Unexpected error updating subscription |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_subscriptions_id_reserved_resources_get**
> ReservedResourceList api_accounts_mgmt_v1_subscriptions_id_reserved_resources_get(id)

Returns a list of reserved resources

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.reserved_resource_list import ReservedResourceList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)
    order_by = "orderBy_example" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  ```sql username asc ```  Or in order to retrieve all accounts ordered by username _and_ first name:  ```sql username asc, firstName asc ```  If the parameter isn't provided, or if the value is empty, then no explicit ordering will be applied. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of reserved resources
        api_response = api_instance.api_accounts_mgmt_v1_subscriptions_id_reserved_resources_get(id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_id_reserved_resources_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of reserved resources
        api_response = api_instance.api_accounts_mgmt_v1_subscriptions_id_reserved_resources_get(id, page=page, size=size, search=search, order_by=order_by)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_id_reserved_resources_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  &#x60;&#x60;&#x60;sql username asc &#x60;&#x60;&#x60;  Or in order to retrieve all accounts ordered by username _and_ first name:  &#x60;&#x60;&#x60;sql username asc, firstName asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then no explicit ordering will be applied. | [optional]

### Return type

[**ReservedResourceList**](ReservedResourceList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of reserved resource objects |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_subscriptions_id_support_cases_get**
> api_accounts_mgmt_v1_subscriptions_id_support_cases_get(id)

Returns a list of open support creates opened against the external cluster id of this subscrption

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of open support creates opened against the external cluster id of this subscrption
        api_instance.api_accounts_mgmt_v1_subscriptions_id_support_cases_get(id)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_id_support_cases_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of open support creates opened against the external cluster id of this subscrption
        api_instance.api_accounts_mgmt_v1_subscriptions_id_support_cases_get(id, page=page, size=size)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_id_support_cases_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of support cases objects |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_subscriptions_post**
> Subscription api_accounts_mgmt_v1_subscriptions_post(subscription_create_request)

Create a new subscription

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.subscription import Subscription
from account_management_sdk.model.error import Error
from account_management_sdk.model.subscription_create_request import SubscriptionCreateRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    subscription_create_request = SubscriptionCreateRequest(
        cluster_uuid="cluster_uuid_example",
        console_url="console_url_example",
        display_name="display_name_example",
        plan_id="OCP",
        status="Disconnected",
    ) # SubscriptionCreateRequest | Subscription Creation data

    # example passing only required values which don't have defaults set
    try:
        # Create a new subscription
        api_response = api_instance.api_accounts_mgmt_v1_subscriptions_post(subscription_create_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_create_request** | [**SubscriptionCreateRequest**](SubscriptionCreateRequest.md)| Subscription Creation data |

### Return type

[**Subscription**](Subscription.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**409** | Subscription already exists |  -  |
**500** | An unexpected error occurred creating subscription |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_account_id_delete**
> api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_account_id_delete(sub_id, account_id)

Deletes a notification contact by subscription and account id

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    sub_id = "subId_example" # str | The id of subscription
    account_id = "accountId_example" # str | The id of account

    # example passing only required values which don't have defaults set
    try:
        # Deletes a notification contact by subscription and account id
        api_instance.api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_account_id_delete(sub_id, account_id)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_account_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | **str**| The id of subscription |
 **account_id** | **str**| The id of account |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Notification contact deleted by subscription and account id |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No notification contact with specified subscription and account id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_get**
> AccountList api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_get(sub_id)

Returns a list of notification contacts for the given subscription

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.account_list import AccountList
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    sub_id = "subId_example" # str | The id of subscription
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)
    fields = "fields_example" # str | Supplies a comma-separated list of fields to be returned. Fields of sub-structures and of arrays use <structure>.<field> notation. <stucture>.* means all field of a structure Example: For each Subscription to get id, href, plan(id and kind) and labels (all fields)  ``` ocm get subscriptions --parameter fields=id,href,plan.id,plan.kind,labels.* --parameter fetchLabels=true ``` (optional)
    order_by = "orderBy_example" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  ```sql username asc ```  Or in order to retrieve all accounts ordered by username _and_ first name:  ```sql username asc, firstName asc ```  If the parameter isn't provided, or if the value is empty, then no explicit ordering will be applied. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of notification contacts for the given subscription
        api_response = api_instance.api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_get(sub_id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of notification contacts for the given subscription
        api_response = api_instance.api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_get(sub_id, page=page, size=size, search=search, fields=fields, order_by=order_by)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | **str**| The id of subscription |
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]
 **fields** | **str**| Supplies a comma-separated list of fields to be returned. Fields of sub-structures and of arrays use &lt;structure&gt;.&lt;field&gt; notation. &lt;stucture&gt;.* means all field of a structure Example: For each Subscription to get id, href, plan(id and kind) and labels (all fields)  &#x60;&#x60;&#x60; ocm get subscriptions --parameter fields&#x3D;id,href,plan.id,plan.kind,labels.* --parameter fetchLabels&#x3D;true &#x60;&#x60;&#x60; | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  &#x60;&#x60;&#x60;sql username asc &#x60;&#x60;&#x60;  Or in order to retrieve all accounts ordered by username _and_ first name:  &#x60;&#x60;&#x60;sql username asc, firstName asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then no explicit ordering will be applied. | [optional]

### Return type

[**AccountList**](AccountList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of account objects that are notification contacts for this subscription |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_post**
> Account api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_post(sub_id, notification_contact_create_request)

Add an account as a notification contact to this subscription

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.account import Account
from account_management_sdk.model.notification_contact_create_request import NotificationContactCreateRequest
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    sub_id = "subId_example" # str | The id of subscription
    notification_contact_create_request = NotificationContactCreateRequest(
        account_identifier="account_identifier_example",
    ) # NotificationContactCreateRequest | Add a notification contact by an account's username

    # example passing only required values which don't have defaults set
    try:
        # Add an account as a notification contact to this subscription
        api_response = api_instance.api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_post(sub_id, notification_contact_create_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_sub_id_notification_contacts_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | **str**| The id of subscription |
 **notification_contact_create_request** | [**NotificationContactCreateRequest**](NotificationContactCreateRequest.md)| Add a notification contact by an account&#39;s username |

### Return type

[**Account**](Account.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**409** | Notification contact already exists |  -  |
**500** | An unexpected error occurred creating notification contact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_subscriptions_sub_id_reserved_resources_reserved_resource_id_delete**
> api_accounts_mgmt_v1_subscriptions_sub_id_reserved_resources_reserved_resource_id_delete(sub_id, reserved_resource_id)

Delete reserved resources by id

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    sub_id = "subId_example" # str | The id of subscription
    reserved_resource_id = "reservedResourceId_example" # str | The id of reserved resource

    # example passing only required values which don't have defaults set
    try:
        # Delete reserved resources by id
        api_instance.api_accounts_mgmt_v1_subscriptions_sub_id_reserved_resources_reserved_resource_id_delete(sub_id, reserved_resource_id)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_sub_id_reserved_resources_reserved_resource_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | **str**| The id of subscription |
 **reserved_resource_id** | **str**| The id of reserved resource |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Reserved resources deleted by id |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No reserved resources with specified id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_subscriptions_sub_id_reserved_resources_reserved_resource_id_get**
> ReservedResource api_accounts_mgmt_v1_subscriptions_sub_id_reserved_resources_reserved_resource_id_get(sub_id, reserved_resource_id)

Get reserved resources by id

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.reserved_resource import ReservedResource
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    sub_id = "subId_example" # str | The id of subscription
    reserved_resource_id = "reservedResourceId_example" # str | The id of reserved resource

    # example passing only required values which don't have defaults set
    try:
        # Get reserved resources by id
        api_response = api_instance.api_accounts_mgmt_v1_subscriptions_sub_id_reserved_resources_reserved_resource_id_get(sub_id, reserved_resource_id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_sub_id_reserved_resources_reserved_resource_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | **str**| The id of subscription |
 **reserved_resource_id** | **str**| The id of reserved resource |

### Return type

[**ReservedResource**](ReservedResource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reserved resources found by id |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No reserved resources with specified id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_subscriptions_sub_id_reserved_resources_reserved_resource_id_patch**
> ReservedResource api_accounts_mgmt_v1_subscriptions_sub_id_reserved_resources_reserved_resource_id_patch(sub_id, reserved_resource_id, reserved_resource_patch_request)

Update a reserved resource

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.reserved_resource import ReservedResource
from account_management_sdk.model.reserved_resource_patch_request import ReservedResourcePatchRequest
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    sub_id = "subId_example" # str | The id of subscription
    reserved_resource_id = "reservedResourceId_example" # str | The id of reserved resource
    reserved_resource_patch_request = ReservedResourcePatchRequest(
        billing_model="billing_model_example",
    ) # ReservedResourcePatchRequest | Updated reserved resource data

    # example passing only required values which don't have defaults set
    try:
        # Update a reserved resource
        api_response = api_instance.api_accounts_mgmt_v1_subscriptions_sub_id_reserved_resources_reserved_resource_id_patch(sub_id, reserved_resource_id, reserved_resource_patch_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_sub_id_reserved_resources_reserved_resource_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | **str**| The id of subscription |
 **reserved_resource_id** | **str**| The id of reserved resource |
 **reserved_resource_patch_request** | [**ReservedResourcePatchRequest**](ReservedResourcePatchRequest.md)| Updated reserved resource data |

### Return type

[**ReservedResource**](ReservedResource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reserved resources updated successfully |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No reserved resources with specified id exists |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_get**
> SubscriptionRoleBindingList api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_get(sub_id)

Get subscription role bindings

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from account_management_sdk.model.subscription_role_binding_list import SubscriptionRoleBindingList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    sub_id = "subId_example" # str | The id of subscription
    page = 1 # int | Page number of record list when record list exceeds specified page size (optional) if omitted the server will use the default value of 1
    size = 100 # int | Maximum number of records to return (optional) if omitted the server will use the default value of 100
    search = "search_example" # str | Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with `my`:  ```sql username like 'my%' ```  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by `foo=bar`,  ```sql labels.key = 'foo' and labels.value = 'bar' ```  If the parameter isn't provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. (optional)
    order_by = "orderBy_example" # str | Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  ```sql username asc ```  Or in order to retrieve all accounts ordered by username _and_ first name:  ```sql username asc, firstName asc ```  If the parameter isn't provided, or if the value is empty, then no explicit ordering will be applied. (optional)
    fetch_accounts = True # bool | If true, includes the account reference information in the output. Could slow request response time. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get subscription role bindings
        api_response = api_instance.api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_get(sub_id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get subscription role bindings
        api_response = api_instance.api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_get(sub_id, page=page, size=size, search=search, order_by=order_by, fetch_accounts=fetch_accounts)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | **str**| The id of subscription |
 **page** | **int**| Page number of record list when record list exceeds specified page size | [optional] if omitted the server will use the default value of 1
 **size** | **int**| Maximum number of records to return | [optional] if omitted the server will use the default value of 100
 **search** | **str**| Specifies the search criteria. The syntax of this parameter is similar to the syntax of the _where_ clause of an SQL statement, using the names of the json attributes / column names of the account. For example, in order to retrieve all the accounts with a username starting with &#x60;my&#x60;:  &#x60;&#x60;&#x60;sql username like &#39;my%&#39; &#x60;&#x60;&#x60;  The search criteria can also be applied on related resource. For example, in order to retrieve all the subscriptions labeled by &#x60;foo&#x3D;bar&#x60;,  &#x60;&#x60;&#x60;sql labels.key &#x3D; &#39;foo&#39; and labels.value &#x3D; &#39;bar&#39; &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then all the accounts that the user has permission to see will be returned. | [optional]
 **order_by** | **str**| Specifies the order by criteria. The syntax of this parameter is similar to the syntax of the _order by_ clause of an SQL statement, but using the names of the json attributes / column of the account. For example, in order to retrieve all accounts ordered by username:  &#x60;&#x60;&#x60;sql username asc &#x60;&#x60;&#x60;  Or in order to retrieve all accounts ordered by username _and_ first name:  &#x60;&#x60;&#x60;sql username asc, firstName asc &#x60;&#x60;&#x60;  If the parameter isn&#39;t provided, or if the value is empty, then no explicit ordering will be applied. | [optional]
 **fetch_accounts** | **bool**| If true, includes the account reference information in the output. Could slow request response time. | [optional]

### Return type

[**SubscriptionRoleBindingList**](SubscriptionRoleBindingList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription role bindings found, or none exist |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_id_delete**
> api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_id_delete(id, sub_id)

Delete a subscription role binding

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    sub_id = "subId_example" # str | The id of subscription

    # example passing only required values which don't have defaults set
    try:
        # Delete a subscription role binding
        api_instance.api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_id_delete(id, sub_id)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **sub_id** | **str**| The id of subscription |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Subscription role binding successfully deleted |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No Subscription Role Binding with specified Id is accessible |  -  |
**500** | An unexpected error occurred deleting the Subscription Role Binding |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_id_get**
> SubscriptionRoleBinding api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_id_get(id, sub_id)

Get a Subscription Role Binding by id

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.subscription_role_binding import SubscriptionRoleBinding
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | The id of record
    sub_id = "subId_example" # str | The id of subscription

    # example passing only required values which don't have defaults set
    try:
        # Get a Subscription Role Binding by id
        api_response = api_instance.api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_id_get(id, sub_id)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of record |
 **sub_id** | **str**| The id of subscription |

### Return type

[**SubscriptionRoleBinding**](SubscriptionRoleBinding.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription Role Binding found by id |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No Subscription Role Binding with the specified id is accessible |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_post**
> SubscriptionRoleBinding api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_post(sub_id, subscription_role_binding_create_request)

Create a new subscription role binding

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.subscription_role_binding import SubscriptionRoleBinding
from account_management_sdk.model.subscription_role_binding_create_request import SubscriptionRoleBindingCreateRequest
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    sub_id = "subId_example" # str | The id of subscription
    subscription_role_binding_create_request = SubscriptionRoleBindingCreateRequest(
        account_username="account_username_example",
        role_id="role_id_example",
    ) # SubscriptionRoleBindingCreateRequest | Subscription role binding data

    # example passing only required values which don't have defaults set
    try:
        # Create a new subscription role binding
        api_response = api_instance.api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_post(sub_id, subscription_role_binding_create_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_subscriptions_sub_id_role_bindings_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | **str**| The id of subscription |
 **subscription_role_binding_create_request** | [**SubscriptionRoleBindingCreateRequest**](SubscriptionRoleBindingCreateRequest.md)| Subscription role binding data |

### Return type

[**SubscriptionRoleBinding**](SubscriptionRoleBinding.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**409** | Subscription role binding already exists |  -  |
**500** | An unexpected error occurred creating the subscription role binding |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_support_cases_case_id_delete**
> api_accounts_mgmt_v1_support_cases_case_id_delete(case_id)

Delete a support case

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    case_id = "caseId_example" # str | The id of a support case

    # example passing only required values which don't have defaults set
    try:
        # Delete a support case
        api_instance.api_accounts_mgmt_v1_support_cases_case_id_delete(case_id)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_support_cases_case_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| The id of a support case |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Support case successfully deleted |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**404** | No support case with specified case id on specified subscription id exists |  -  |
**405** | Not allowed to close a case that is already closed |  -  |
**500** | An unexpected error occurred deleting the support case |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_support_cases_post**
> SupportCasesCreatedResponse api_accounts_mgmt_v1_support_cases_post(support_cases_request)

create a support case for the subscription

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.support_cases_request import SupportCasesRequest
from account_management_sdk.model.support_cases_created_response import SupportCasesCreatedResponse
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    support_cases_request = SupportCasesRequest(
        account_number="account_number_example",
        case_language="case_language_example",
        cluster_id="cluster_id_example",
        cluster_uuid="cluster_uuid_example",
        contact_sso_name="contact_sso_name_example",
        description="description_example",
        event_stream_id="event_stream_id_example",
        openshift_cluster_id="openshift_cluster_id_example",
        product="OpenShift Container Platform",
        severity="1 (Urgent)",
        subscription_id="subscription_id_example",
        summary="summary_example",
        version="4.10",
    ) # SupportCasesRequest | The contents of the support case to be created

    # example passing only required values which don't have defaults set
    try:
        # create a support case for the subscription
        api_response = api_instance.api_accounts_mgmt_v1_support_cases_post(support_cases_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_support_cases_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **support_cases_request** | [**SupportCasesRequest**](SupportCasesRequest.md)| The contents of the support case to be created |

### Return type

[**SupportCasesCreatedResponse**](SupportCasesCreatedResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Support case created |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_accounts_mgmt_v1_token_authorization_post**
> TokenAuthorizationResponse api_accounts_mgmt_v1_token_authorization_post(token_authorization_request)

Finds the account owner of the provided token

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.token_authorization_response import TokenAuthorizationResponse
from account_management_sdk.model.token_authorization_request import TokenAuthorizationRequest
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    token_authorization_request = TokenAuthorizationRequest(
        authorization_token="authorization_token_example",
    ) # TokenAuthorizationRequest | Token authorization data

    # example passing only required values which don't have defaults set
    try:
        # Finds the account owner of the provided token
        api_response = api_instance.api_accounts_mgmt_v1_token_authorization_post(token_authorization_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_accounts_mgmt_v1_token_authorization_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_authorization_request** | [**TokenAuthorizationRequest**](TokenAuthorizationRequest.md)| Token authorization data |

### Return type

[**TokenAuthorizationResponse**](TokenAuthorizationResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The account belongs to the user with the specified registry credential token |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Registry credential token is invalid |  -  |
**500** | Other token authorization error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorizations_v1_access_review_post**
> AccessReviewResponse api_authorizations_v1_access_review_post(access_review)

Review an account's access to perform an action on a particular resource or resource type

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.access_review_response import AccessReviewResponse
from account_management_sdk.model.access_review import AccessReview
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    access_review = AccessReview(
        account_username="account_username_example",
        action="get",
        cluster_id="cluster_id_example",
        cluster_uuid="cluster_uuid_example",
        organization_id="organization_id_example",
        resource_type="AddOn",
        subscription_id="subscription_id_example",
    ) # AccessReview | Access review data

    # example passing only required values which don't have defaults set
    try:
        # Review an account's access to perform an action on a particular resource or resource type
        api_response = api_instance.api_authorizations_v1_access_review_post(access_review)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_authorizations_v1_access_review_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_review** | [**AccessReview**](AccessReview.md)| Access review data |

### Return type

[**AccessReviewResponse**](AccessReviewResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Review successfully generated |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**422** | Unsupported action, non-existent resource type, or non-existent account |  -  |
**500** | Unexpected error occurred while generating access review |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorizations_v1_capability_review_post**
> CapabilityReview api_authorizations_v1_capability_review_post(capability_review_request)

Review an account's capabilities

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.capability_review import CapabilityReview
from account_management_sdk.model.capability_review_request import CapabilityReviewRequest
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    capability_review_request = CapabilityReviewRequest(
        account_username="account_username_example",
        capability="manage_cluster_admin",
        cluster_id="cluster_id_example",
        organization_id="organization_id_example",
        subscription_id="subscription_id_example",
        type="Cluster",
    ) # CapabilityReviewRequest | Capability review data

    # example passing only required values which don't have defaults set
    try:
        # Review an account's capabilities
        api_response = api_instance.api_authorizations_v1_capability_review_post(capability_review_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_authorizations_v1_capability_review_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **capability_review_request** | [**CapabilityReviewRequest**](CapabilityReviewRequest.md)| Capability review data |

### Return type

[**CapabilityReview**](CapabilityReview.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful review |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform capability reviews |  -  |
**500** | Unexpected error occurred while generating capability review |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorizations_v1_export_control_review_post**
> ExportControlReview api_authorizations_v1_export_control_review_post(export_control_review_request)

Determine whether a user is restricted from downloading Red Hat software based on export control compliance. 

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.export_control_review_request import ExportControlReviewRequest
from account_management_sdk.model.error import Error
from account_management_sdk.model.export_control_review import ExportControlReview
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    export_control_review_request = ExportControlReviewRequest(
        account_username="account_username_example",
        ignore_cache=True,
    ) # ExportControlReviewRequest | Export control review data

    # example passing only required values which don't have defaults set
    try:
        # Determine whether a user is restricted from downloading Red Hat software based on export control compliance. 
        api_response = api_instance.api_authorizations_v1_export_control_review_post(export_control_review_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_authorizations_v1_export_control_review_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_control_review_request** | [**ExportControlReviewRequest**](ExportControlReviewRequest.md)| Export control review data |

### Return type

[**ExportControlReview**](ExportControlReview.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful review |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred while generating access review |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorizations_v1_feature_review_post**
> FeatureReviewResponse api_authorizations_v1_feature_review_post(feature_review)

Review feature to perform an action on it such as toggle a feature on/off

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.feature_review import FeatureReview
from account_management_sdk.model.feature_review_response import FeatureReviewResponse
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    feature_review = FeatureReview(
        account_username="account_username_example",
        feature="feature_example",
        organization_id="organization_id_example",
    ) # FeatureReview | Feature review data

    # example passing only required values which don't have defaults set
    try:
        # Review feature to perform an action on it such as toggle a feature on/off
        api_response = api_instance.api_authorizations_v1_feature_review_post(feature_review)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_authorizations_v1_feature_review_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_review** | [**FeatureReview**](FeatureReview.md)| Feature review data |

### Return type

[**FeatureReviewResponse**](FeatureReviewResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Review successfully generated |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred while generating feature review |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorizations_v1_resource_review_post**
> ResourceReview api_authorizations_v1_resource_review_post(resource_review_request)

Obtain resource ids for resources an account may perform the specified action upon. Resource ids returned as [\"*\"] is shorthand for all ids.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.resource_review_request import ResourceReviewRequest
from account_management_sdk.model.resource_review import ResourceReview
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    resource_review_request = ResourceReviewRequest(
        account_username="account_username_example",
        action="get",
        resource_type="Cluster",
    ) # ResourceReviewRequest | Resource review data
    reduce_cluster_list = True # bool | If true, When returning a list of cluster_ids/cluster_uuids/subscription_ids, if those are already included in one of the organizations provided in organization_ids, do not include it in the list. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Obtain resource ids for resources an account may perform the specified action upon. Resource ids returned as [\"*\"] is shorthand for all ids.
        api_response = api_instance.api_authorizations_v1_resource_review_post(resource_review_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_authorizations_v1_resource_review_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Obtain resource ids for resources an account may perform the specified action upon. Resource ids returned as [\"*\"] is shorthand for all ids.
        api_response = api_instance.api_authorizations_v1_resource_review_post(resource_review_request, reduce_cluster_list=reduce_cluster_list)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_authorizations_v1_resource_review_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_review_request** | [**ResourceReviewRequest**](ResourceReviewRequest.md)| Resource review data |
 **reduce_cluster_list** | **bool**| If true, When returning a list of cluster_ids/cluster_uuids/subscription_ids, if those are already included in one of the organizations provided in organization_ids, do not include it in the list. | [optional]

### Return type

[**ResourceReview**](ResourceReview.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful review |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform resource reviews |  -  |
**422** | Unsupported action or non-existent resource type |  -  |
**500** | Unexpected error occurred while generating access review |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorizations_v1_self_access_review_post**
> AccessReviewResponse api_authorizations_v1_self_access_review_post(self_access_review)

Review your ability to perform an action on a particular resource or resource type

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.self_access_review import SelfAccessReview
from account_management_sdk.model.access_review_response import AccessReviewResponse
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    self_access_review = SelfAccessReview(
        action="get",
        cluster_id="cluster_id_example",
        cluster_uuid="cluster_uuid_example",
        organization_id="organization_id_example",
        resource_type="AddOn",
        subscription_id="subscription_id_example",
    ) # SelfAccessReview | Self access review data

    # example passing only required values which don't have defaults set
    try:
        # Review your ability to perform an action on a particular resource or resource type
        api_response = api_instance.api_authorizations_v1_self_access_review_post(self_access_review)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_authorizations_v1_self_access_review_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **self_access_review** | [**SelfAccessReview**](SelfAccessReview.md)| Self access review data |

### Return type

[**AccessReviewResponse**](AccessReviewResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Review successfully generated |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**422** | Unsupported action or non-existent resource type |  -  |
**500** | Unexpected error occurred while generating access review |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorizations_v1_self_feature_review_post**
> FeatureReviewResponse api_authorizations_v1_self_feature_review_post(self_feature_review)

Review your ability to toggle a feature

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.self_feature_review import SelfFeatureReview
from account_management_sdk.model.feature_review_response import FeatureReviewResponse
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    self_feature_review = SelfFeatureReview(
        feature="feature_example",
    ) # SelfFeatureReview | Self feature review data

    # example passing only required values which don't have defaults set
    try:
        # Review your ability to toggle a feature
        api_response = api_instance.api_authorizations_v1_self_feature_review_post(self_feature_review)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_authorizations_v1_self_feature_review_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **self_feature_review** | [**SelfFeatureReview**](SelfFeatureReview.md)| Self feature review data |

### Return type

[**FeatureReviewResponse**](FeatureReviewResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Review successfully generated |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**500** | Unexpected error occurred while generating feature review |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorizations_v1_self_resource_review_post**
> SelfResourceReview api_authorizations_v1_self_resource_review_post(self_resource_review_request)

Obtain resource ids for resources you may perform the specified action upon. Resource ids returned as [\"*\"] is shorthand for all ids.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.self_resource_review import SelfResourceReview
from account_management_sdk.model.error import Error
from account_management_sdk.model.self_resource_review_request import SelfResourceReviewRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    self_resource_review_request = SelfResourceReviewRequest(
        action="get",
        resource_type="Cluster",
    ) # SelfResourceReviewRequest | Self resource review data
    reduce_cluster_list = True # bool | If true, When returning a list of cluster_ids/cluster_uuids/subscription_ids, if those are already included in one of the organizations provided in organization_ids, do not include it in the list. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Obtain resource ids for resources you may perform the specified action upon. Resource ids returned as [\"*\"] is shorthand for all ids.
        api_response = api_instance.api_authorizations_v1_self_resource_review_post(self_resource_review_request)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_authorizations_v1_self_resource_review_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Obtain resource ids for resources you may perform the specified action upon. Resource ids returned as [\"*\"] is shorthand for all ids.
        api_response = api_instance.api_authorizations_v1_self_resource_review_post(self_resource_review_request, reduce_cluster_list=reduce_cluster_list)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_authorizations_v1_self_resource_review_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **self_resource_review_request** | [**SelfResourceReviewRequest**](SelfResourceReviewRequest.md)| Self resource review data |
 **reduce_cluster_list** | **bool**| If true, When returning a list of cluster_ids/cluster_uuids/subscription_ids, if those are already included in one of the organizations provided in organization_ids, do not include it in the list. | [optional]

### Return type

[**SelfResourceReview**](SelfResourceReview.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful review |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform self resource reviews |  -  |
**422** | Unsupported action or non-existent resource type |  -  |
**500** | Unexpected error occurred while generating access review |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorizations_v1_self_terms_review_post**
> TermsReviewResponse api_authorizations_v1_self_terms_review_post(self_terms_review)

Review your status of Terms

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.self_terms_review import SelfTermsReview
from account_management_sdk.model.terms_review_response import TermsReviewResponse
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    self_terms_review = SelfTermsReview(
        check_optional_terms=True,
        event_code="event_code_example",
        site_code="site_code_example",
    ) # SelfTermsReview | Data to check self terms for

    # example passing only required values which don't have defaults set
    try:
        # Review your status of Terms
        api_response = api_instance.api_authorizations_v1_self_terms_review_post(self_terms_review)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_authorizations_v1_self_terms_review_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **self_terms_review** | [**SelfTermsReview**](SelfTermsReview.md)| Data to check self terms for |

### Return type

[**TermsReviewResponse**](TermsReviewResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Review successfully generated |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**422** | Unsupported action or non-existent resource type |  -  |
**500** | Unexpected error occurred while generating terms review |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_authorizations_v1_terms_review_post**
> TermsReviewResponse api_authorizations_v1_terms_review_post(terms_review)

Review an account's status of Terms

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import account_management_sdk
from account_management_sdk.api import default_api
from account_management_sdk.model.terms_review_response import TermsReviewResponse
from account_management_sdk.model.terms_review import TermsReview
from account_management_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:14321
# See configuration.py for a list of all supported configuration parameters.
configuration = account_management_sdk.Configuration(
    host = "http://localhost:14321"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = account_management_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with account_management_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    terms_review = TermsReview(
        account_username="account_username_example",
        check_optional_terms=True,
        event_code="event_code_example",
        site_code="site_code_example",
    ) # TermsReview | Data to check terms for

    # example passing only required values which don't have defaults set
    try:
        # Review an account's status of Terms
        api_response = api_instance.api_authorizations_v1_terms_review_post(terms_review)
        pprint(api_response)
    except account_management_sdk.ApiException as e:
        print("Exception when calling DefaultApi->api_authorizations_v1_terms_review_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terms_review** | [**TermsReview**](TermsReview.md)| Data to check terms for |

### Return type

[**TermsReviewResponse**](TermsReviewResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Review successfully generated |  -  |
**400** | Validation errors occurred |  -  |
**401** | Auth token is invalid |  -  |
**403** | Unauthorized to perform operation |  -  |
**422** | Unsupported action, non-existent resource type, or non-existent account |  -  |
**500** | Unexpected error occurred while generating terms review |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

