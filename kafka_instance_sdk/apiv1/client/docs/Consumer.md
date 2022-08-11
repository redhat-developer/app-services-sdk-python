# Consumer

A Kafka consumer is responsible for reading records from one or more topics and one or more partitions of a topic.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | Unique identifier for the consumer group to which this consumer belongs. | 
**topic** | **str** | The unique topic name to which this consumer belongs | 
**partition** | **int** | The partition number to which this consumer group is assigned to. | 
**offset** | **int** | Offset denotes the position of the consumer in a partition. | 
**lag** | **int** | Offset Lag is the delta between the last produced message and the last consumer&#39;s committed offset. | 
**log_end_offset** | **int** | The log end offset is the offset of the last message written to a log. | [optional] 
**member_id** | **str** | The member ID is a unique identifier given to a consumer by the coordinator upon initially joining the group. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


