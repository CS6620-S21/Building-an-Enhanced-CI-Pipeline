# Building CI/CD/CT for API Project Proposal

#### Team Members: Ankita Mahapatra, Yaqin Zhou, Yiqian Deng, Yashwanthreddy Beeravolu, Rahul Guin

#### Mentors: Ata Turk, Prajna Bhaskar, James Colley, Surya Jayanthi, Panat Taranat, Yan Chen


## 1. Vision and Goals of the Project:

A CI/CD pipeline that can be used for API development has already been developed by a team (Panat Taranat, Yan Chen, Mella Liang, Peter Wang, Kaito Yamagishi). They have used an example of a URL shortener API as a demonstration of the pipeline, though the pipeline will work with most Python APIs. The pipeline will allow incremental changes to be developed, tested, verified, and deployed in an automated manner.  The project currently supports unit testing only during the integration phase and deployment in OpenShift only.
 
 
During the CI, once the unit tests gets done, the k8s build gets triggered, integration and load testing gets started in the application testing environment, if the application passes the tests, the code is now ready to merge to the master branch.

During the CD process, when the developer/operator decides to push the code to staging environment, the k8s build is triggered and the integration/load tests run on the application and once it passes, the code changes are now succesfully pushed to the staging environment.

Once the above steps are done, the code changes will be pushed to the production.

Now, the application in the production environment will be tested continuosly using the testing tools.

Important goals include:
- Fully automated setup, deployment and testing. The entire process for a developer to make changes to the codebase should require as little manual interaction as possible. Same with someone who is looking to use our repo as a GitHub template for their own project.
- Unit tests can be written and integrated into the pipeline on GitHub.
- Integration tests will be performed on Kubernetes.
- Creating different environments duirng different phases and testing the code changes appropriately.


## 2. Users/Personas of the Project:

Andy is a user of the CI/CD/CT pipeline with an existing project. Andy already has a simple Flask webapp on a GitHub repo. Andy has written some unit tests and integration tests and wants to deploy his app onto Kubernetes. He reads the documentation for our CI/CD/CT pipeline, grabs the CLI tool from npm, and uses our CLI tool to quickly setup GitHub Actions workflows. Now, whenever Andy makes commits to this repo, the code will go through unit tests and integration tests. If the tests have passed, the code will be tested on the staging envionment, and then deployed to production environment, serving users of his webapp with the latest version while being continuously tested.

Brian plays the role of an operator who is responsible for deploying the changes in the code to different environments like, staging and production and can use the CD pipeline to deploy changes in the respective environments once the tests pass.



## 3. Scope and Features of the Project:

#### Already implemented:
- Allow adding and running of unit tests in CI
- Easy installation and configuration of the pipeline, can be customized to different projects
- Failed builds and tests will alert developers

#### In-Scope Features:
- Allow adding and running of integration tests (Selenium) and Load tests (using Locust) in CI and after deployment to Kubernetes
- The API being developed should have high availability, a failed test should not bring down the service
- Every commit or pull-request by a developer will go through CI/CD/CT pipeline, must pass all tests before being deployed
- Ensure the security of secrets and sensitive data/tokens in the pipeline
- Allow deployment on Kubernetes only after unit tests and integration tests pass.  

#### Out-of-Scope Features (not delivered as part of MVP):
- Provide interface to view the logs of continuous testing in production environment

## 4. Design Decision
#### The system components of the architectural design is as follows:
- GitHub Actions for unit, integration and load testing and deployment
- Selenium for performing integration tests
- Locust for performing load tests
- Documentation for guiding users to set up GitHub Actions workflow yaml files and view logs
- Kubernetes Actions to deploy from GitHub
- Kubernetes on GCP for hosting production app and testing environment (integration, load)

#### Main Decision
- Why we choose GCP: 
  - Kubernetes was originally designed by Google and GKE has the best support for K8s.
  - GKE provides a lot of tools to help us deploy app directly from GCP and it's more intuitive to use.
  - We can easily find the docs of Deploying to Google Kubernetes Engine using github actions.
- Why use documentation instead of CLI tools:
  - Flexibility. As this is an open source project, if other developer wants to use our pipeline, he can take our doc as a reference and write his own config files to deploy and automatically run other tests
  - we don’t have enough time to develop the CLI tools as we have at least 17 yaml files in total, and we decide to put more time in viewing the logs in continuous testing part.


#### Architecture Diagram
<img src="https://i.ibb.co/1929yJj/CI-CD-CT.png" alt="CI-CD-CT" border="0">

In the diagram, when developers make any changes in the code and the commits are pushed to GitHub, GitHub Actions triggers the CI workflow. It builds the project with the changed contents, formats check, runs unit and integration tests with Pytest and selenium (or cypress), and then provides results of the tests in the pull request.

If the changes introduce errors, the developer can go back to debugging. If there are no errors from the tests, it is deployed to Kubernetes. Once it gets deployed, integration and load testing will take place and checkmarks will appear on the GitHub Actions page if the tests have passed.

The change is ready to be reviewed by another team member as a pull request. When the team member approves the changes, the code will be deployed to the staging environment automatically. In this staging environment, all testing will be performed exactly like what will happen in the production environment. When all testing passed, developers/operators can deploy code to the production environment server hosted on GCP using Kubernetes by clicking the release button on Github.

After the application deploys to the production environment, it will automatically set up a continuous test environment and the test will run regularly. Also, we can optionally set up the EFK stack(Elasticsearch - Fluentd - Kibana) to generate logs and developers can view loggings.



## 5. Acceptance Criteria
Minimum acceptance criteria is a enhanced CI/CD/CT pipeline for an API developed and tested with our example URL shortener API. It will detect all commits and pull requests in a GitHub repository, and run the pipeline defined by our GitHub actions configurations. This will build a docker image and deploy the changes to a running production server with no stoppage.
- Add integration tests and laod tests in CI pipeline
- Create a staging environment to perform application testing
- Any code that does not build or passes tests will not make it to production
- Make sure that application on production environment gets tested continuously

## 6. Release Planning
Release 1 (Deadline: Feb 23, Demo1: Feb 26)
- Configure the previous code base and deploy a code change to OpenShift
  
Release 2 (Deadline: Mar 9, Demo2: Mar 12)
- Manually run integration test and load test on our application
- Set up the CI pipeline
- Automate deployment of the flask app on kubernetes GCP
- Deploy the integration test on Kubernetes GCP
  
Release 3 (Deadline: Mar 23, Demo3: Mar 26)
- Automate the integration tests (Selenium) and load tests (Locust) in CI pipeline
- Creating and setting up the staging environment in CD pipeline
- Deploy and automate deployment of the application on Google Kubernetes Engine
  
Release 4 (Deadline: Apr 6, Demo4: Apr 9)
- Optimize the CI pipeline
- Set up the production environment in CD pipeline
- Deploy and continuously run the tests in production environment
- Write documentation for everything we did so far
  
Release 5 (Deadline: end of semester)
- Make sure every part is functional, stable, and verified
- Provide an user interface to display test logs
- Final video, update readme and documentation

## 7. Sprint demos and presentations

- [Sprint 1 presentation](https://drive.google.com/file/d/1lyJXW9O5FHLuR44W96lfd_3f_qhILI5b/view?usp=sharing)
- [Sprint 2 presentation](https://drive.google.com/file/d/1KEYMqCRR8AGZ9b5MrpuiLmRe5J2mXfeS/view?usp=sharing)
- [Sprint 3 presentation](https://drive.google.com/file/d/1xEKhIZ2uhDqj5PfDZ5nrKpJwAgoEFW9s/view?usp=sharing)
- [Sprint 4 presentation](https://docs.google.com/presentation/d/1fHEegSYMZsdt-Ul8VIxIynwMLov-aXxr9S4_0v5TO1o/edit?usp=sharing)
- [Sprint 5 presentation](https://docs.google.com/presentation/d/1oNZRTOz_ps-EAe3LhqLtEJ22-iSNdZdcVpYAo6TOknM/edit?usp=sharing)

- Sprint 1 Demo (no video)
- [Sprint 2 Demo](https://www.youtube.com/watch?v=zqCeR8jRPFQ)
- [Sprint 3 Demo](https://www.youtube.com/watch?v=hKFIRhfNkq0)
- [Sprint 4 Demo](https://www.youtube.com/watch?v=INccY-tMers)
- [Sprint 5 Demo](https://drive.google.com/file/d/1Wn1a1hcznkqhosTIVBZ-vVxG5oJFNZQ3/view)

## 8. Other repositories


- https://github.com/yachinz/cicdct_react_frontend


## 9. Run application guide
- Install virtual env on your local machine
  - Windows User: python -m venv env
  - Mac User: python3 -m venv env
- Enable virtual env
  - Windows User: source venv_pc
  - Mac User: source venv_unix
- Install dependencies
  - Windows User: pip install -r requirements.txt
  - Mac User: pip3 install -r requirements.txt
- Run Flask App
  - Windows User: python app.py
  - Mac User: python3 app.py
- OR run Flask App via Docker Container (docker installed)
  - docker build -t flaskapp:latest .
  - docker run -it -p 5000:5000 flaskapp
  - Optional: docker run -it -d -p 5000:5000 flaskapp (automatically runs in background)
- Flask app runs on http://localhost:5000/


## 10. Documentation
* [Integration test documentation](/doc/integration_test.md)
* [Load test documentation](/doc/load_test_documentation.md)
* [GKE setup documentation](/doc/gke_setup_deployment_manual.md)
* [CI pipeline documentation](/doc/CI_pipeline_documentation.MD)
* [APScheduler documentation](/doc/apscheduler.md)
* [Logging-Fluentd-Elasticsearch-Kibana](/doc/logging-fluentd-elasticsearch-kibana.md)
