FROM ubuntu:18.04


RUN apt-get update && apt-get install -y build-essential \
    python3 \
    python3-dev \
    python3-pip

RUN apt-get clean


# Make working directory
RUN mkdir /var/tmp/env_test


# Declare the working directory inside container
WORKDIR /var/tmp/env_test


# Copy the project files into the container
COPY . /var/tmp/env_test


# Install Python requirements
RUN pip3 install -r /var/tmp/env_test/requirements.txt


# Make the selenium_test.py file executable
# RUN chmod +x /var/tmp/selenium_test/selenium_test.py
ENTRYPOINT [ "python3" ]
CMD [ "scheduler.py" ]