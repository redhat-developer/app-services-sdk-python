#!/usr/bin/env bash

publish_sdks() {
    local sdk_path=$1

    echo "Building python package"
    python $sdk_path/setup.py \
        build --build-base $sdk_path \
        egg_info --egg-base $sdk_path \
        bdist_wheel --dist-dir $sdk_path/dist

    echo "Validating python package"
    twine check "$sdk_path/dist/*"

    echo "Publishing python package"
    twine upload -r testpypi "$sdk_path/dist/*"
}

SDK_PATH="sdks/connector_management_sdk/apiv1/client"
publish_sdks $SDK_PATH

SDK_PATH="sdks/kafka_instance_sdk/apiv1/client"
publish_sdks $SDK_PATH

SDK_PATH="sdks/kafka_mgmt_sdk/apiv1/client"
publish_sdks $SDK_PATH

SDK_PATH="sdks/registry_management_sdk/apiv1/client"
publish_sdks $SDK_PATH

SDK_PATH="sdks/smart_events_management_sdk/apiv1/client"
publish_sdks $SDK_PATH

SDK_PATH="sdks/account_management_sdk/apiv1/client"
publish_sdks $SDK_PATH