# RHOAS SDK for Python

Python packages and API clients for Red Had OpenShift Application Services (RHOAS) 

[Check us out on GitHub](https://github.com/redhat-developer/app-services-sdk-python)

## Prequisites

- [Python 3.9](https://docs.python.org/3/) or above
- [pip](https://pypi.org/project/pip/) for installing packages

## Installation

Install the RHOAS SDK with the pip package installer:

```shell
$ python3 -m pip install rhoas-sdks
```

## Management SDKs

> NOTE: Some of these APIs are under development and may sometimes cause backwards-incompatible changes.

All packages are now available and can be accessed by just importing them as shown below:


| API                       | Status | Package                                                                                                                                                         |
| :------------------------ | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| KafkaManagement           | beta   | `import python rhoas_kafka_mgmt_sdk`          |
| ServiceRegistryManagement  | alpha   | `import rhoas_service_registry_mgmt_sdk`         |
| ConnectorManagement       | alpha  | `import rhoas_connector_mgmt_sdk`  |

 
 ## Instances SDKs

| API              | Status | Package                                                                                                                                                                               |
| ---------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| KafkaInstance    | beta   | `import rhoas_kafka_instance_sdk`|
| RegistryInstance | beta   | `import rhoas_registry_instance_sdk` |


## Documentation

[Documentation](./docs)

## Examples

[Examples](./examples)

## Contributing

Contributions are welcome. See [CONTRIBUTING](CONTRIBUTING.md) for details.
