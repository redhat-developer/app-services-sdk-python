# Partition

Kafka topic partition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partition** | **int** | The partition id, unique among partitions of the same topic | 
**replicas** | [**[Node]**](Node.md) | List of replicas for the partition | [optional] 
**isr** | [**[Node]**](Node.md) | List in-sync replicas for this partition. | [optional] 
**leader** | [**PartitionLeader**](PartitionLeader.md) |  | [optional] 
**id** | **int** | Unique id for the partition (deprecated, use &#x60;partition&#x60; instead) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


