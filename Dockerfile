FROM ubuntu:20.04

WORKDIR /app

RUN apt update && apt install -y python3 python3-distutils wget

RUN apt install -y python3-pip
# Python dependencies
COPY requirements.txt ./
RUN pip3 --no-cache-dir install -r requirements.txt

COPY . ./

ENTRYPOINT [ "python3", "-u", "transform.py" ]