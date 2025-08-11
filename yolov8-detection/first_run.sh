#!/usr/bin/env bash

# Pull the docker image from the registry
docker pull sjainapptech/yolov8-detection-module:latest

cat << EOF
-------------------------------------
The setup script ran successfully!
-------------------------------------
EOF

# Exit with a success code
exit 0
