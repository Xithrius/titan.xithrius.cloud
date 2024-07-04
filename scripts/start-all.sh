#!/usr/bin/env bash

REPO_DIR="$(dirname "$(readlink -f "$0")")/.."

pushd ${REPO_DIR}

for file in "services"/*; do
    if [ -f "${file}" ]; then
        if [[ "${file}" == *.docker-compose.yml ]]; then
            echo "Starting compose file ${file}..."
            docker-compose -f ${file} up -d
        fi
    fi
done

popd
