# RegistryStatusValue

\"accepted\": Registry status when accepted for processing.  \"provisioning\": Registry status when provisioning a new instance.  \"ready\": Registry status when ready for use.  \"failed\": Registry status when the provisioning failed. When removing a Registry instance in this state, the status transitions directly to \"deleting\".   \"deprovision\": Registry status when accepted for deprovisioning.  \"deleting\": Registry status when deprovisioning. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | \&quot;accepted\&quot;: Registry status when accepted for processing.  \&quot;provisioning\&quot;: Registry status when provisioning a new instance.  \&quot;ready\&quot;: Registry status when ready for use.  \&quot;failed\&quot;: Registry status when the provisioning failed. When removing a Registry instance in this state, the status transitions directly to \&quot;deleting\&quot;.   \&quot;deprovision\&quot;: Registry status when accepted for deprovisioning.  \&quot;deleting\&quot;: Registry status when deprovisioning.  |  must be one of ["accepted", "provisioning", "ready", "failed", "deprovision", "deleting", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


