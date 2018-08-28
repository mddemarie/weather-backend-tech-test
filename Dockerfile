FROM ubuntu:16.04

RUN apt-get update
RUN apt-get update && apt-get install -y \
    curl \
    git \
    python3 \
    python3-dev

# Create app folder + set correct permission
RUN mkdir -p /app/web
WORKDIR /app

# Install pip3
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | /usr/bin/python3
RUN pip install --upgrade pip

# Add requirements + install
ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

EXPOSE 8001

CMD python3