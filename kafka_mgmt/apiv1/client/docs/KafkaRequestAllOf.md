# KafkaRequestAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multi_az** | **bool** |  | 
**reauthentication_enabled** | **bool** |  | 
**status** | **str** | Values: [accepted, preparing, provisioning, ready, failed, deprovision, deleting]  | [optional] 
**cloud_provider** | **str** | Name of Cloud used to deploy. For example AWS | [optional] 
**region** | **str** | Values will be regions of specific cloud provider. For example: us-east-1 for AWS | [optional] 
**owner** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**bootstrap_server_host** | **str** |  | [optional] 
**admin_api_server_url** | **str** | The kafka admin server url to perform kafka admin operations e.g acl management etc. The value will be available when the Kafka has been fully provisioned i.e it reaches a &#39;ready&#39; state | [optional] 
**created_at** | **datetime** |  | [optional] 
**expires_at** | **datetime, none_type** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**failed_reason** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 
**instance_type_name** | **str** | This field is now deprecated, please use the /api/kafkas_mgmt/v1/instance_types/{cloud_provider}/{cloud_region} endpoint to retrieve the field instead. | [optional] 
**kafka_storage_size** | **str** | Maximum data storage available to this Kafka. This is now deprecated, please use max_data_retention_size instead. | [optional] 
**max_data_retention_size** | [**SupportedKafkaSizeBytesValueItem**](SupportedKafkaSizeBytesValueItem.md) |  | [optional] 
**browser_url** | **str** |  | [optional] 
**size_id** | **str** |  | [optional] 
**ingress_throughput_per_sec** | **str** | This field is now deprecated, please use the /api/kafkas_mgmt/v1/instance_types/{cloud_provider}/{cloud_region} endpoint to retrieve the field instead. | [optional] 
**egress_throughput_per_sec** | **str** | This field is now deprecated, please use the /api/kafkas_mgmt/v1/instance_types/{cloud_provider}/{cloud_region} endpoint to retrieve the field instead. | [optional] 
**total_max_connections** | **int** | This field is now deprecated, please use the /api/kafkas_mgmt/v1/instance_types/{cloud_provider}/{cloud_region} endpoint to retrieve the field instead. | [optional] 
**max_partitions** | **int** | This field is now deprecated, please use the /api/kafkas_mgmt/v1/instance_types/{cloud_provider}/{cloud_region} endpoint to retrieve the field instead. | [optional] 
**max_data_retention_period** | **str** | This field is now deprecated, please use the /api/kafkas_mgmt/v1/instance_types/{cloud_provider}/{cloud_region} endpoint to retrieve the field instead. | [optional] 
**max_connection_attempts_per_sec** | **int** | This field is now deprecated, please use the /api/kafkas_mgmt/v1/instance_types/{cloud_provider}/{cloud_region} endpoint to retrieve the field instead. | [optional] 
**billing_cloud_account_id** | **str** |  | [optional] 
**marketplace** | **str** |  | [optional] 
**billing_model** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


