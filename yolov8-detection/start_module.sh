#!/bin/bash

# The last argument passed to this script is the path to the socket
# Viam provides this automatically
SOCKET_PATH="${@: -1}"

# Run the docker container
# --runtime=nvidia: This uses the NVIDIA container runtime to pass the GPU into the container.
# -v /path/to/your/models:/models: This is an example of how you could mount a model directory
#    from the host into the container. You would need to create this directory on your robot
#    and place your .pt file there. Then, in the Viam config, you would set the
#    "model_location" attribute to "/models/your_model.pt".
# -v ${SOCKET_PATH}:/tmp/module.sock: This mounts the Viam socket into the container
# The final part is the image name and the command to run inside it, passing the socket path.
exec docker run \
    --runtime=nvidia \
    -v ${SOCKET_PATH}:/tmp/module.sock \
    sjainapptech/yolov8-detection-module:latest \
    /usr/bin/python3 /app/src/main.py --socket-path /tmp/module.sock
