#!/bin/bash

# The last argument passed to this script is the path to the socket
# Viam provides this automatically
SOCKET_PATH="${@: -1}"

# Run the docker container with flags recommended by NVIDIA for PyTorch
# --rm: Automatically remove the container when it exits.
# --ipc=host: Use the host's shared memory.
# --runtime=nvidia: Use the NVIDIA container runtime to pass the GPU into the container.
# --privileged: Grant the container extended privileges to access host devices (like the GPU).
# -v ${SOCKET_PATH}:/tmp/module.sock: Mount the Viam socket into the container.
exec docker run \
    --rm \
    --ipc=host \
    --runtime=nvidia \
    --privileged \
    -v ${SOCKET_PATH}:/tmp/module.sock \
    sjainapptech/yolov8-detection-module:latest \
    /usr/bin/python3 /app/src/main.py --socket-path /tmp/module.sock