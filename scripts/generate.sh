#!/usr/bin/env bash

# generates an API client for the given OpenAPI spec file
generate_sdk() {
    local oas_file_name=$1
    local output_path=$2
    local package_name=$3
    local package_version=$4
     
    echo "Validating OpenAPI ${oas_file_name}"
    npx @openapitools/openapi-generator-cli validate -i "$oas_file_name"

    echo "Generating source code based on ${oas_file_name}"

    # remove old generated models
    rm -Rf $OUTPUT_PATH

    additional_properties=packageVersion="$package_version"

    echo "Generating SDK"
    npx @openapitools/openapi-generator-cli generate -g python -i\
        $oas_file_name -o $output_path \
        --package-name="$package_name" \
        --ignore-file-override=.openapi-generator-ignore \
        --template-dir './scripts/templates' \
        --package-name=$package_name
}

npx @openapitools/openapi-generator-cli version-manager set 6.0.1

OPENAPI_FILENAME="openapi/kas-fleet-manager.yaml"
PACKAGE_NAME="rhoas_kafka_mgmt_sdk"
OUTPUT_PATH="sdks/kafka_mgmt_sdk"

generate_sdk $OPENAPI_FILENAME $OUTPUT_PATH $PACKAGE_NAME $PACKAGE_VERSION

OPENAPI_FILENAME="openapi/srs-fleet-manager.json"
PACKAGE_NAME="rhoas_service_registry_mgmt_sdk"
OUTPUT_PATH="sdks/registry_mgmt_sdk"

generate_sdk $OPENAPI_FILENAME $OUTPUT_PATH $PACKAGE_NAME $PACKAGE_VERSION

OPENAPI_FILENAME="openapi/connector_mgmt.yaml"
PACKAGE_NAME="rhoas_connector_mgmt_sdk"
OUTPUT_PATH="sdks/connector_mgmt_sdk"

generate_sdk $OPENAPI_FILENAME $OUTPUT_PATH $PACKAGE_NAME

OPENAPI_FILENAME="openapi/kafka-admin-rest.yaml"
PACKAGE_NAME="rhoas_kafka_instance_sdk"
OUTPUT_PATH="sdks/kafka_instance_sdk"

generate_sdk $OPENAPI_FILENAME $OUTPUT_PATH $PACKAGE_NAME

echo "generating registry instance SDK "

cd openapi
echo "Removing codegen "
cat registry-instance.json | jq 'del(.paths."x-codegen-contextRoot")' > registry-instance-tmp.json
mv -f registry-instance-tmp.json registry-instance.json

echo "Ensuring only single tag is created "
cat registry-instance.json | jq 'walk( if type == "object" and has("tags") 
       then .tags |= select(.[0])
       else . end )' > registry-instance-tmp.json
mv -f registry-instance-tmp.json registry-instance.json

echo "removing invalid datetime definitions"
sed -i '' 's/date-time/utc-date/' registry-instance.json

cd ..

OPENAPI_FILENAME="openapi/registry-instance.json"
PACKAGE_NAME="rhoas_registry_instance_sdk"
OUTPUT_PATH="sdks/registry_instance_sdk"

generate_sdk $OPENAPI_FILENAME $OUTPUT_PATH $PACKAGE_NAME

OPENAPI_FILENAME="openapi/smartevents_mgmt.yaml"
PACKAGE_NAME="rhoas_smart_events_mgmt_sdk"
OUTPUT_PATH="sdks/smart_events_mgmt_sdk"

rm -rf $OUTPUT_PATH/model $OUTPUT_PATH/api
generate_sdk $OPENAPI_FILENAME $OUTPUT_PATH $PACKAGE_NAME

OPENAPI_FILENAME="openapi/service-accounts.yaml"
PACKAGE_NAME="rhoas_service_accounts_mgmt_sdk"
OUTPUT_PATH="sdks/service_accounts_mgmt_sdk"

generate_sdk $OPENAPI_FILENAME $OUTPUT_PATH $PACKAGE_NAME