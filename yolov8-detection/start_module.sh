#!/bin/bash

# The last argument passed to this script is the path to the socket
# Viam provides this automatically
SOCKET_PATH="${@: -1}"

# Run the docker container without GPU for initial testing
# --rm: Automatically remove the container when it exits.
# --ipc=host: Use the host's shared memory.
# -v ${SOCKET_PATH}:/tmp/module.sock: Mount the Viam socket into the container.
exec docker run \
    --rm \
    --ipc=host \
    -v ${SOCKET_PATH}:/tmp/module.sock \
    sjainapptech/yolov8-detection-module:latest \
    /usr/bin/python3 /app/src/main.py --socket-path /tmp/module.sock