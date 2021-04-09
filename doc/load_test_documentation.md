# Tool for load testing

Locust is the tool we use for our load test. It is an easy to use, scriptable and scalable performance testing tool. \
We define the behaviour of our users in regular Python code, instead of using a clunky UI or domain specific language. 

## install locust

Install locust using pip: $ pip3 install locust \
Validate your installation and show the Locust version number: $ locust -V 

## write load test with locust

To write the load test, please check locust documentation: https://docs.locust.io/en/stable/writing-a-locustfile.html \
The locust class we use in our locust test is HttpUser class.

# Run load testing

There are many command line options for configuration. check: $ locust --help

## Run locally with web UI (port 8089)

1. Run application locally (both frontend and backend, frontend at localhost:3000, and backend at localhost:5000)
2. open another terminal
3. run: $ locust -f locustfile.py --host http://localhost:3000
4. go to web UI at localhost:8089
5. choose number of total users to simulate: 300; spawn rate(user spawned per second): 2; host: localhost:5000
6. click start swarming button to start our load test.

## Run locally without web UI

1. Run application locally (both frontend and backend, frontend at localhost:3000, and backend at localhost:5000)
2. open another terminal
3. run: $ locust -f locustfile.py --host http://localhost:3000 --users 300 --spawn-rate 2 --run-time 30s --headless

## Run load test locally when application deployed

Same process with run locally without run application process.

## Run load test after deploy both application and load test

1. create dockerfile for loadtest
2. build the dockerfile
3. run doccker image

## Automate load test

write an yaml file to automate the load test, please check deploy load test documentation.

