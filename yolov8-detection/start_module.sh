#!/bin/bash

# Debug log: script invocation
echo "[start_module.sh] Invoked at $(date) with args: $@" >> /tmp/yolo_debug.log

# The last argument passed to this script is the path to the socket
SOCKET_PATH="${@: -1}"

# Debug log: socket path
echo "[start_module.sh] SOCKET_PATH resolved to: ${SOCKET_PATH}" >> /tmp/yolo_debug.log

# Ensure the parent directory of SOCKET_PATH exists
SOCKET_DIR="$(dirname "${SOCKET_PATH}")"
if [ ! -d "${SOCKET_DIR}" ]; then
    echo "[start_module.sh] Parent directory ${SOCKET_DIR} does not exist. Creating it." | tee -a /tmp/yolo_debug.log
    mkdir -p "${SOCKET_DIR}"
fi

# Use a different approach for Docker - mount the parent directory instead
CONTAINER_SOCKET_DIR="/tmp/socket_dir"
CONTAINER_SOCKET_PATH="${CONTAINER_SOCKET_DIR}/yolov8_module.sock"

echo "[start_module.sh] Launching docker at $(date)" >> /tmp/yolo_debug.log
exec docker run \
    --rm \
    --ipc=host \
    -v "${SOCKET_DIR}:${CONTAINER_SOCKET_DIR}" \
    sjainapptech/yolov8-detection-module:latest \
    /usr/bin/python3 /app/src/main.py "/tmp/socket_dir/$(basename "${SOCKET_PATH}")"