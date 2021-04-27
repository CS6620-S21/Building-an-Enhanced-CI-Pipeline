# getting base image ubuntu
FROM ubuntu:18.04

# install
RUN apt-get update && apt-get install -y build-essential \
    python3 \
    python3-dev \
    python3-pip 
   

RUN apt-get clean

# make working directory
RUN mkdir /loadTest

# Declare the working directory insde continer
WORKDIR /loadTest

# Copy everything in test folder to container
COPY . /loadTest

# port
EXPOSE 8089
# EXPOSE 5000

# install load test requirements
RUN pip3 install locust


# run load test
ENTRYPOINT [ "locust" ,"-f","locustfile.py","--host", "http://gke-test-staging-service-backend/", "--users", "300", "--spawn-rate", "2", "--run-time", "30s", "--headless"]


# docker run --hostname standalone -e ATTACKED_HOST=http://34.102.157.148/  -p 8089:8089 24d8dabbd6db

