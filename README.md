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
- Allow adding and running of integration tests (Either Selenium or Cypress tests) in CI and after deployment to Kubernetes
- The API being developed should have high availability, a failed test should not bring down the service
- Every commit or pull-request by a developer will go through CI/CD/CT pipeline, must pass all tests before being deployed
- Ensure the security of secrets and sensitive data/tokens in the pipeline
- Allow deployment on Kubernetes only after unit tests and integration tests pass. 

#### Out-of-Scope Features (not delivered as part of MVP):
- Backwards compatibility with Jenkins
- The URL shortener API is a demonstration, so extensive development or design of the shortener API is not in scope
- Support for other Web APIs (other languages)

## 4. Solution Concept
#### The system components of the architectural design is as follows:
- GitHub Actions for unit and integration testing and deployment
- CLI tool for setting up GitHub Actions workflow yaml files and viewing logs
- Kubernetes Actions to deploy from GitHub
- Docker for containerizing web app
- Kubernetes on AWS/GCP/MOC for hosting production app and testing environment (integration, load/stress)

Majority of our code will be in the CLI tool for generating GitHub Action workflow files.
Development of the CLI tool is being done at [https://github.com/CS6620-S21/Building-an-Enhanced-CI-Pipeline](https://github.com/CS6620-S21/Building-an-Enhanced-CI-Pipeline)

#### Architecture Diagram
<img src="https://i.ibb.co/4YGkMQ3/CI-CD-CT.png" alt="CI-CD-CT" border="0">

In the diagram, when developers make any changes in the code and the commits are pushed to GitHub, GitHub Actions triggers the CI workflow. It builds the project with the changed contents, formats code, runs unit and integration tests with pytest and selenium (or cypress), and then provides results of the tests in the pull request.

If the changes introduce errors, the developer can go back to debugging. If there are no errors from the tests, it is deployed to Kubernetes. Once it gets deployed, integration and stress testing will take place and check marks will appear on the GitHub Actions page if the tests have passed.

The change is ready to be reviewed by another team member as a pull request. When the team member approves the changes, the code will be deployed to the production server hosted on AWS/GCP/MOC using Kubernetes.
  
We will be developing unit tests and end-to-end API integration tests alongside the development of the URL shortener. These tests will allow us to verify the proper function of various system components, such as backend and frontend.

## 5. Acceptance Criteria
Minimum acceptance criteria is a enhanced CI/CD/CT pipeline for an API developed and tested with our example URL shortener API. It will detect all commits and pull requests in a GitHub repository, and run the pipeline defined by our GitHub actions configurations. This will build a docker image and deploy the changes to a running production server with no stoppage.
- Add integration test in CI pipeline
- Create a staging environment to perform application testing
- Any code that does not build or passes tests will not make it to production
- Make sure that application on production environment gets tested continuously

## 6. Release Planning
Release 1 (Deadline: Feb 23, Demo1: Feb 26)
- Write selenium tests for the Flask application and test them manually
- Configure the previous code base and deploy a code change to OpenShift
  
Release 2 (Deadline: Mar 9, Demo2: Mar 12)
- Create the application testing environment for CI pipleine
- Automate the integration tests using Selenium/cypress in CI pipeline
  
Release 3 (Deadline: Mar 23, Demo3: Mar 26)
- Creating the staging environment in CD pipeline
- Automate the integration tests using Selenium/cypress in CD pipeline
  
Release 4 (Deadline: Apr 6, Demo4: Apr 9) 
- Create the production envrionment for continuous testing
- Perform continuous testing
  
Release 5 (Deadline: end of semester)
- Complete documentation and make sure every part is functional, stable, and verified
- Final video
