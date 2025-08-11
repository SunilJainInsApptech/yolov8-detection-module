#!/bin/bash

# The last argument passed to this script is the path to the socket
# Viam provides this automatically
SOCKET_PATH="${@: -1}"

# Run the docker container with flags recommended by NVIDIA for PyTorch
# --gpus all: Exposes all available GPUs to the container.
# --ipc=host: Use the host's shared memory, crucial for multi-process data loading in PyTorch.
# --ulimit...: Increase memory limits for performance.
# --runtime=nvidia: This uses the NVIDIA container runtime to pass the GPU into the container.
# -v ${SOCKET_PATH}:/tmp/module.sock: This mounts the Viam socket into the container
# The final part is the image name and the command to run inside it, passing the socket path.
exec docker run \
    --gpus all \
    --ipc=host \
    --ulimit memlock=-1 \
    --ulimit stack=67108864 \
    --runtime=nvidia \
    -v ${SOCKET_PATH}:/tmp/module.sock \
    sjainapptech/yolov8-detection-module:latest \
    /usr/bin/python3 /app/src/main.py --socket-path /tmp/module.sock
