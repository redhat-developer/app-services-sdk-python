#!/usr/bin/env bash

# generates an API client for the given OpenAPI spec file
generate_sdk() {
    local oas_file_name=$1
    local output_path=$2
    local package_name=$3
     
    echo "Validating OpenAPI ${oas_file_name}"
    npx @openapitools/openapi-generator-cli validate -i "$oas_file_name"

    echo "Generating source code based on ${oas_file_name}"

    # remove old generated models
    rm -Rf $OUTPUT_PATH

    echo "Generating SDK"
    npx @openapitools/openapi-generator-cli generate -g python -i\
        $oas_file_name -o $output_path \
        --package-name="$package_name" \
        --ignore-file-override=.openapi-generator-ignore \
        --template-dir .github/templates \
        --package-name=$package_name

}

OPENAPI_FILENAME="openapi/kas-fleet-manager.yaml"
PACKAGE_NAME="rhoas_kafka_mgmt_sdk"
OUTPUT_PATH="sdks/kafka_mgmt_sdk/apiv1/client"

generate_sdk $OPENAPI_FILENAME $OUTPUT_PATH $PACKAGE_NAME

OPENAPI_FILENAME="openapi/srs-fleet-manager.json"
PACKAGE_NAME="rhoas_service_registry_mgmt_sdk"
OUTPUT_PATH="sdks/registry_management_sdk/apiv1/client"

generate_sdk $OPENAPI_FILENAME $OUTPUT_PATH $PACKAGE_NAME

OPENAPI_FILENAME="openapi/connector_mgmt.yaml"
PACKAGE_NAME="rhoas_connector_mgmt_sdk"
OUTPUT_PATH="sdks/connector_management_sdk/apiv1/client"

generate_sdk $OPENAPI_FILENAME $OUTPUT_PATH $PACKAGE_NAME

OPENAPI_FILENAME="openapi/kafka-admin-rest.yaml"
PACKAGE_NAME="rhoas_kafka_instance_sdk"
OUTPUT_PATH="sdks/kafka_instance_sdk/apiv1/client"

generate_sdk $OPENAPI_FILENAME $OUTPUT_PATH $PACKAGE_NAME

OPENAPI_FILENAME="openapi/ams.json"
PATCH_FILE="openapi/ams.patch" 
PACKAGE_NAME="rhoas_account_mgmt_sdk"
OUTPUT_PATH="sdks/account_management_sdk/apiv1/client"

patch $OPENAPI_FILENAME < $PATCH_FILE

npx @openapitools/openapi-generator-cli generate -g python -i \
    "$OPENAPI_FILENAME" -o "$OUTPUT_PATH" \
    --template-dir .github/templates \
    --package-name="${PACKAGE_NAME}" \
    --ignore-file-override=./packages/account-management-sdk/.openapi-generator-ignore 

git checkout -- $OPENAPI_FILENAME


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

echo "Removing invalid datetime definitions"
sed -i '' 's/date-time/utc-date/' registry-instance.json

cd ..

OPENAPI_FILENAME="openapi/registry-instance.json"
PACKAGE_NAME="rhoas_registry_instance_sdk"
OUTPUT_PATH="sdks/registry_instance_sdk/apiv1/client"

generate_sdk $OPENAPI_FILENAME $OUTPUT_PATH $PACKAGE_NAME

OPENAPI_FILENAME="openapi/smartevents_mgmt.yaml"
PACKAGE_NAME="rhoas_smart_events_mgmt_sdk"
OUTPUT_PATH="sdks/smart_events_management_sdk/apiv1/client"

rm -Rf $OUTPUT_PATH/model $OUTPUT_PATH/api
npx @openapitools/openapi-generator-cli generate -g python -i \
    "$OPENAPI_FILENAME" -o "$OUTPUT_PATH" \
    --template-dir .github/templates \
    --package-name="${PACKAGE_NAME}" \
    --remove-operation-id-prefix \
    --ignore-file-override=.openapi-generator-ignore


