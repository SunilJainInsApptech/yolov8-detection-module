
FROM nvcr.io/nvidia/pytorch:25.06-py3
ENV PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:128
ENV CUDA_LAUNCH_BLOCKING=1
ENV TORCH_USE_CUDA_DSA=1

# Debugging: Enable CUDA kernel error reporting and CUDA DSA
ENV CUDA_LAUNCH_BLOCKING=1
ENV TORCH_USE_CUDA_DSA=1

# Set up a working directory
WORKDIR /app


RUN apt-get update && apt-get install -y libgl1


## torch and torchvision are already installed in the base image.


COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt


COPY . .


CMD ["./run.sh"]
