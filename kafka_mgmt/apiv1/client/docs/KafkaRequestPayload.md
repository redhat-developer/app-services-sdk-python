# KafkaRequestPayload

Schema for the request body sent to /kafkas POST

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Kafka cluster. It must consist of lower-case alphanumeric characters or &#39;-&#39;, start with an alphabetic character, and end with an alphanumeric character, and can not be longer than 32 characters. | 
**cloud_provider** | **str** | The cloud provider where the Kafka cluster will be created in | [optional] 
**region** | **str** | The region where the Kafka cluster will be created in | [optional] 
**reauthentication_enabled** | **bool, none_type** | Whether connection reauthentication is enabled or not. If set to true, connection reauthentication on the Kafka instance will be required every 5 minutes. The default value is true | [optional] 
**plan** | **str** | kafka plan in a format of &lt;instance_type&gt;.&lt;size_id&gt; | [optional] 
**billing_cloud_account_id** | **str, none_type** | cloud account id used to purchase the instance | [optional] 
**marketplace** | **str, none_type** | marketplace where the instance is purchased on | [optional] 
**billing_model** | **str, none_type** | billing model to use | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


