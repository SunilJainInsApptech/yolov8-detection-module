# Start from the official NVIDIA PyTorch container, which includes CUDA
FROM nvcr.io/nvidia/pytorch:25.06-py3

# Set up a working directory
WORKDIR /app

# Install system dependencies required by OpenCV
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# By using the NVIDIA container, we assume torch and torchvision are already installed.
# Your requirements.txt should NOT include torch or torchvision.
# It should only include things like:
# viam-sdk
# ultralytics
# pillow
# numpy
# opencv-python

# Copy the requirements file and install your specific dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of your module's source code
COPY . .

# The command that will be run when the container starts
# This should point to your module's entrypoint script
CMD ["./run.sh"]
