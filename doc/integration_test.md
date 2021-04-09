# Integration test

Integration testing is the phase in software testing in which individual software modules are combined and tested as a group.

In this part, we will deploy the app on K8s, run selenium test on k8s and collect the log.

To learn how to write selenium test with Python, here is the link of document:
https://selenium-python.readthedocs.io/index.html

## Deploy the app on K8s
Please visit other docs.

## Run selenium test on k8s
1. Write the docker file to run the test.
```Dockerfile
FROM ubuntu:18.04


RUN apt-get update && apt-get install -y build-essential \
    wget \
    python3 \
    python3-dev \
    python3-pip \
    firefox


RUN apt-get clean


# Make working directory
RUN mkdir /var/tmp/selenium_test


# Declare the working directory inside container
WORKDIR /var/tmp/selenium_test


# Copy the project files into the container
COPY . /var/tmp/selenium_test


# Get the geckodriver binary for Firefox and decompress the tar
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-linux64.tar.gz
RUN tar -xvzf /var/tmp/selenium_test/geckodriver-v0.28.0-linux64.tar.gz


# Move the geckodriver binary into the $PATH and delete the tar file.
RUN mv /var/tmp/selenium_test/geckodriver /usr/local/bin/
RUN rm -rf /var/tmp/selenium_test/geckodriver-v0.28.0-linux64.tar.gz


# Install Python requirements
RUN pip3 install -r /var/tmp/selenium_test/requirements.txt


# Make the selenium_test.py file executable
# RUN chmod +x /var/tmp/selenium_test/selenium_test.py
ENTRYPOINT [ "python3" ]
CMD [ "selenium_test.py" ]
```

2. Get the service name of the app we deployed and visit http://service-name/ when you run selenium test.
3. Run selenium test as a job on K8s:
- Write a config file to set up the job.
- Set the backoffLimit as 0 in order to get the failed warning.

```yml
apiVersion: batch/v1
kind: Job
metadata:
  # Unique key of the Job instance
  name: gke-test-selenium
spec:
  template:
    metadata:
      name: gke-test-selenium
    spec:
      containers:
      - name: gke-test-selenium
        image: gcr.io/PROJECT_ID/selenium/IMAGE:TAG
        resources:
          requests:
            cpu: 100m
            memory: 100Mi
      # Do not restart containers after they exit
      restartPolicy: Never
  # of retries before marking as failed.
  backoffLimit: 0
```
- Put the config yml file in the kustomization.yml.
```yml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
- config.yml
```

4. Run the job using Github actions
- Follow the docs of deploy the app using github action.

5. Get the warning and send back the trace.
- Run your test on K8s without this action first and get the container's initalizing time and total running time.
- Set a proper time in the timeout of waiting for job complete and failed.
- Set a proper time in the timeout of ContainersReady.

```yaml
    - name: Selenium_test log
      run: |-
        pods=$(kubectl get pods --selector=job-name=gke-test-selenium --output=jsonpath='{.items[*].metadata.name}')
        kubectl wait --for=condition=complete job/gke-test-selenium --timeout=360s &
        completion_pid=$!
        kubectl wait --for=condition=failed job/gke-test-selenium --timeout=360s && exit 1 &
        failure_pid=$! 
        kubectl wait --for=condition=ContainersReady pods/$pods --timeout=240s
        kubectl logs --follow job/gke-test-selenium
        wait -n $completion_pid $failure_pid
        exit_code=$?
        exit $exit_code
```



