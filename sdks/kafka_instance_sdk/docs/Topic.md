# Topic


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the object. Not supported for all object kinds. | [optional] 
**kind** | **str** |  | [optional] [readonly] 
**href** | **str** | Link path to request the object. Not supported for all object kinds. | [optional] 
**name** | **str** | The name of the topic. | [optional] 
**is_internal** | **bool** |  | [optional] 
**partitions** | [**[Partition]**](Partition.md) | Partitions for this topic. | [optional] 
**config** | [**[ConfigEntry]**](ConfigEntry.md) | Topic configuration entry. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


