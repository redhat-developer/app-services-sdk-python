# ConnectorTypeAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the connector type. | [optional] 
**version** | **str** | Version of the connector type. | [optional] 
**channels** | [**[Channel]**](Channel.md) | Channels of the connector type. | [optional] 
**description** | **str** | A description of the connector. | [optional] 
**icon_href** | **str** | URL to an icon of the connector. | [optional] 
**labels** | **[str]** | Labels used to categorize the connector | [optional] 
**featured_rank** | **int** | Ranking for featured connectors | [optional] 
**capabilities** | **[str]** | The capabilities supported by the conenctor | [optional] 
**schema** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | A json schema that can be used to validate a ConnectorRequest connector field. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


