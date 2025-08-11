#!/bin/bash


# Debug log: script invocation
echo "[start_module.sh] Invoked at $(date) with args: $@" >> /tmp/yolo_debug.log

# The last argument passed to this script is the path to the socket
# Viam provides this automatically
SOCKET_PATH="${@: -1}"

# Debug log: socket path
echo "[start_module.sh] SOCKET_PATH resolved to: ${SOCKET_PATH}" >> /tmp/yolo_debug.log

# Check if SOCKET_PATH exists and is a socket file
if [ ! -S "${SOCKET_PATH}" ]; then
    echo "[start_module.sh] ERROR: SOCKET_PATH ${SOCKET_PATH} does not exist or is not a socket file. Exiting." | tee -a /tmp/yolo_debug.log
    exit 1
fi

# Run the docker container without GPU for initial testing
# --rm: Automatically remove the container when it exits.
# --ipc=host: Use the host's shared memory.
# -v ${SOCKET_PATH}:/tmp/yolov8_module.sock: Mount the Viam socket into the container.
echo "[start_module.sh] Launching docker at $(date)" >> /tmp/yolo_debug.log
exec docker run \
    --rm \
    --ipc=host \
    -v ${SOCKET_PATH}:/tmp/yolov8_module.sock \
    sjainapptech/yolov8-detection-module:latest \
    /usr/bin/python3 /app/src/main.py --socket-path /tmp/yolov8_module.sock