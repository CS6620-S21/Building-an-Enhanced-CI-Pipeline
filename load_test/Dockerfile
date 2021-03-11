# getting base image ubuntu
FROM ubuntu:18.04
# FROM locustio/locust
# RUN pip3 install python3

# runs my image into container
# RUN apt-get update -y
# RUN apt install python3 -y
# RUN apt install python3-pip -y
# RUN python -m pip install --upgrade pip
# RUN apt-get install locust -y

RUN apt-get update && apt-get install -y build-essential \
    python3 \
    python3-dev \
    python3-pip 
    # locust


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
# RUN pip3 install -r /loadTest/requirements.txt
RUN pip3 install locust


# run load test
# RUN chmod +x /loadTest/locust -f locustfile.py --host http://localhost:5000/ --users 50 --spawn-rate 2
ENTRYPOINT [ "locust" ]

# CMD [ "locustfile.py" ]

# docker run --hostname standalone -e ATTACKED_HOST=http://35.239.70.253:80 -p 8089:8089 24d8dabbd6db
