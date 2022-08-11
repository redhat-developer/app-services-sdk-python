# SupportedKafkaSize

Supported Kafka Size

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of this Kafka instance size. | [optional] 
**display_name** | **str** | Display name of this Kafka instance size. | [optional] 
**ingress_throughput_per_sec** | **SupportedKafkaSizeBytesValueItem** |  | [optional] 
**egress_throughput_per_sec** | **SupportedKafkaSizeBytesValueItem** |  | [optional] 
**total_max_connections** | **int** | Maximum amount of total connections available to this Kafka instance size. | [optional] 
**max_data_retention_size** | **SupportedKafkaSizeBytesValueItem** |  | [optional] 
**max_partitions** | **int** | Maximum amount of total partitions available to this Kafka instance size. | [optional] 
**max_data_retention_period** | **str** | Maximum data retention period available to this Kafka instance size. | [optional] 
**max_connection_attempts_per_sec** | **int** | Maximium connection attempts per second available to this Kafka instance size. | [optional] 
**max_message_size** | **SupportedKafkaSizeBytesValueItem** |  | [optional] 
**min_in_sync_replicas** | **int** | Minimum number of in-sync replicas. | [optional] 
**replication_factor** | **int** | Replication factor available to this Kafka instance size. | [optional] 
**supported_az_modes** | **[str]** | List of Availability Zone modes that this Kafka instance size supports. The possible values are \&quot;single\&quot;, \&quot;multi\&quot;. | [optional] 
**lifespan_seconds** | **int, none_type** | The limit lifespan of the kafka instance in seconds. If not specified then the instance never expires. | [optional] 
**quota_consumed** | **int** | Quota consumed by this Kafka instance size. | [optional] 
**quota_type** | **str** | Quota type used by this Kafka instance size. | [optional] 
**capacity_consumed** | **int** | Data plane cluster capacity consumed by this Kafka instance size. | [optional] 
**maturity_status** | **str** | Maturity level of the size. Can be \&quot;stable\&quot; or \&quot;preview\&quot;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


