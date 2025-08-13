FROM nvcr.io/nvidia/pytorch:25.06-py3

# Set up a working directory
WORKDIR /app


RUN apt-get update && apt-get install -y libgl1


## torch and torchvision are already installed in the base image.


COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt


COPY . .


CMD ["./run.sh"]
