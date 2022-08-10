# CloudRegion

Description of a region of a cloud provider.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | [**[RegionCapacityListItem]**](RegionCapacityListItem.md) | Indicates whether there is capacity left per instance type | 
**enabled** | **bool** | Whether the region is enabled for deploying an OSD cluster. | defaults to False
**kind** | **str** | Indicates the type of this object. Will be &#39;CloudRegion&#39;. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**display_name** | **str** | Name of the region for display purposes, for example &#x60;N. Virginia&#x60;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


