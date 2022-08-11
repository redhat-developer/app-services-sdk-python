# ConnectorNamespace

A connector namespace

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**resource_version** | **int** |  | 
**cluster_id** | **str** |  | 
**tenant** | [**ConnectorNamespaceTenant**](ConnectorNamespaceTenant.md) |  | 
**status** | [**ConnectorNamespaceStatus**](ConnectorNamespaceStatus.md) |  | 
**kind** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**modified_at** | **datetime** |  | [optional] 
**annotations** | **{str: (str,)}** |  | [optional] 
**quota** | [**ConnectorNamespaceQuota**](ConnectorNamespaceQuota.md) |  | [optional] 
**expiration** | **str** | Namespace expiration timestamp in RFC 3339 format | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


