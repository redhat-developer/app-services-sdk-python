# TopicSettings

The settings that are applicable to this topic. This includes partitions, configuration information, and number of replicas.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_partitions** | **int** | Number of partitions for this topic. If not specified, the default for new topics is &#x60;1&#x60;. Number of partitions may not be reduced when updating existing topics | [optional] 
**config** | [**[ConfigEntry]**](ConfigEntry.md) | Topic configuration entries. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


