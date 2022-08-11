# RootTypeForRegistry

Service Registry instance in a multi-tenant deployment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | [**RegistryStatusValue**](RegistryStatusValue.md) |  | 
**name** | **str** | User-defined Registry instance name. Does not have to be unique. | 
**owner** | **str** | Registry instance owner. | 
**created_at** | **datetime** | ISO 8601 UTC timestamp. | 
**updated_at** | **datetime** | ISO 8601 UTC timestamp. | 
**instance_type** | [**RegistryInstanceTypeValue**](RegistryInstanceTypeValue.md) |  | 
**registry_url** | **str** |  | [optional] 
**browser_url** | **str** |  | [optional] 
**registry_deployment_id** | **int** | Identifier of a multi-tenant deployment, where this Service Registry instance resides. | [optional] 
**description** | **str** | Description of the Registry instance. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


