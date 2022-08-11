module.exports ={
    kafka: {
        definition: require("./errors_kafka_mgmt.json"),
        file: "sdks/kafka_management_sdk/apiv1/errors.ts"
    },
    srs:  {
        definition: require("./errors_srs_mgmt.json"),
        file: "sdks/registry_management_sdk/apiv1/errors.ts"
    },
    // connector: {
    //     definition: require("./errors_connector_mgmt.json"),
    //     file: "connector_management_sdk/apiv1/errors.ts"
    // }, 
    // kafkainstance: {
    //     definition: require("./errors_kafka_instance.json"),
    //     file: "kafka_instance_sdk/apiv1/errors.ts"
    // }, 
}

