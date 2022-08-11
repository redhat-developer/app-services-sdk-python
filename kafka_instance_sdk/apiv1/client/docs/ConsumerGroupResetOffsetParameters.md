# ConsumerGroupResetOffsetParameters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | [**OffsetType**](OffsetType.md) |  | 
**value** | **str** | Value associated with the given &#x60;offset&#x60;. Not used for &#x60;offset&#x60; values &#x60;earliest&#x60; and &#x60;latest&#x60;. When &#x60;offset&#x60; is &#x60;timestamp&#x60; then &#x60;value&#x60; must be a valid timestamp representing the point in time to reset the consumer group. When &#x60;offset&#x60; is &#x60;absolute&#x60; then &#x60;value&#x60; must be the integer offset to which the consumer group will be reset. | [optional] 
**topics** | [**[TopicsToResetOffset]**](TopicsToResetOffset.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


