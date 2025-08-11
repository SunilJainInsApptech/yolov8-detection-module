#!/bin/bash


# Debug log: script invocation
echo "[start_module.sh] Invoked at $(date) with args: $@" >> /tmp/yolo_debug.log

# The last argument passed to this script is the path to the socket
# Viam provides this automatically
SOCKET_PATH="${@: -1}"

# Debug log: socket path
echo "[start_module.sh] SOCKET_PATH resolved to: ${SOCKET_PATH}" >> /tmp/yolo_debug.log


# Ensure the parent directory of SOCKET_PATH exists
SOCKET_DIR="$(dirname \"${SOCKET_PATH}\")"
if [ ! -d "${SOCKET_DIR}" ]; then
    echo "[start_module.sh] Parent directory ${SOCKET_DIR} does not exist. Creating it." | tee -a /tmp/yolo_debug.log
    mkdir -p "${SOCKET_DIR}"
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
    /usr/bin/python3 /app/src/main.py /tmp/yolov8_module.sock