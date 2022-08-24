# RecordAllOf

An individual record consumed from a topic or produced to a topic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Record value | 
**partition** | **int** | The record&#39;s partition within the topic | [optional] 
**offset** | **int** | The record&#39;s offset within the topic partition | [optional] [readonly] 
**timestamp** | **datetime** | Timestamp associated with the record. The type is indicated by &#x60;timestampType&#x60;. When producing a record, this value will be used as the record&#39;s &#x60;CREATE_TIME&#x60;. | [optional] 
**timestamp_type** | **str** | Type of timestamp associated with the record | [optional] [readonly] 
**headers** | **{str: (str,)}** | Record headers, key/value pairs | [optional] 
**key** | **str** | Record key | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


