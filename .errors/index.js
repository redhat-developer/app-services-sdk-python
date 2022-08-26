module.exports ={
    kafka: {
        definition: require("./errors_kafka_mgmt.json"),
        file: "sdks/kafka_mgmt_sdk/errors.py"
    },
    srs:  {
        definition: require("./errors_srs_mgmt.json"),
        file: "sdks/registry_mgmt_sdk/errors.py"
    },
    connector: {
        definition: require("./errors_connector_mgmt.json"),
        file: "sdks/connector_mgmt_sdk/errors.py"
    }, 
    kafkainstance: {
        definition: require("./errors_kafka_instance.json"),
        file: "sdks/kafka_instance_sdk/errors.py"
    }, 
}

