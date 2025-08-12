#!/bin/bash

# Viam documented pattern: mount the socket's parent directory at the same path, pass all args
SOCKET_DIR=$(dirname "$1")

echo "[start_module.sh] Launching docker at $(date) with socket dir: $SOCKET_DIR and args: $@" >> /tmp/yolo_debug.log

exec docker run \
    --rm \
    -v "$SOCKET_DIR:$SOCKET_DIR" \
    sjainapptech/yolov8-detection-module:latest \
    /usr/bin/python3 /app/src/main.py "$@"