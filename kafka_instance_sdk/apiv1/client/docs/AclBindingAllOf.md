# AclBindingAllOf

Represents a binding between a resource pattern and an access control entry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | [**AclResourceType**](AclResourceType.md) |  | 
**resource_name** | **str** |  | 
**pattern_type** | [**AclPatternType**](AclPatternType.md) |  | 
**principal** | **str** | Identifies the user or service account to which an ACL entry is bound. The literal prefix value of &#x60;User:&#x60; is required. May be used to specify all users with value &#x60;User:*&#x60;. | 
**operation** | [**AclOperation**](AclOperation.md) |  | 
**permission** | [**AclPermissionType**](AclPermissionType.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


