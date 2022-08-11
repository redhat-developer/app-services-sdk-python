# ConnectorNamespaceMeta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**modified_at** | **datetime** |  | [optional] 
**name** | **str** | Namespace name must match pattern &#x60;^(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])?$&#x60;, or it may be empty to be auto-generated. | [optional] 
**annotations** | **{str: (str,)}** |  | [optional] 
**resource_version** | **int** |  | [optional] 
**quota** | [**ConnectorNamespaceQuota**](ConnectorNamespaceQuota.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


