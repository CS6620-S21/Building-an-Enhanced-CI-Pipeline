# Building CI/CD/CT for API Project Proposal

#### Team Members: Ankita Mahapatra, Yaqin Zhou, Yiqian Deng, Yashwanthreddy Beeravolu, Rahul Guin

#### Mentors: Ata Turk, Prajna Bhaskar, James Colley, Surya Jayanthi, Panat Taranat, Yan Chen


# 1. Vision and Goals of the Project:

A CI/CD pipeline that can be used for API development has already been developed by a team (Panat Taranat, Yan Chen, Mella Liang, Peter Wang, Kaito Yamagishi). They have used an example of a URL shortener API as a demonstration of the pipeline, though the pipeline will work with most Python APIs. The pipeline will allow incremental changes to be developed, tested, verified, and deployed in an automated manner.  The project currently supports unit testing only during the integration phase and deployment in OpenShift only.
 
We will be adding the functionality of integration testing during CI and deployment in Kubernetes only. Following core DevOps principles will allow the project team to strive for continuous improvement with minimal downtime, and to respond quickly to customer feedback and insights.


Important goals include:
- Fully automated setup, deployment and testing. The entire process for a developer to make changes to the codebase should require as little manual interaction as possible. Same with someone who is looking to use our repo as a GitHub template for their own project.
- Unit tests and Integration tests can be written and integrated into the pipeline on GitHub.
- Integration tests will be performed on Kubernetes.



## 2. Users/Personas of the Project:

Andy is a user of the CI/CD/CT pipeline with an existing project. Andy already has a simple Flask webapp on a GitHub repo. Andy has written some unit tests and integration tests and wants to deploy his app onto Kubernetes. He reads the documentation for our CI/CD/CT pipeline, grabs the CLI tool from npm, and uses our CLI tool to quickly setup GitHub Actions workflows. Now, whenever Andy makes commits to this repo, the code will go through unit tests and integration tests. If the tests have passed, the code will be deployed on Kubernetes, serving users of his webapp with the latest version.

Brian is a user starting from scratch. Brian can grab our CLI tool from npm. The tool will guide him through the process of setting up and deploying his webapp. As he develops, he can add tests (both unit and integration tests) and the tool can regenerate the workflow yaml files as needed. This allows Brian to perform test driven development on the cloud as early as possible.




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

---------------------------------------------------------------------------------------------
PENDING IMAGE (Check with the previous team)


In the diagram, when developers make any changes in the code and the commits are pushed to GitHub, GitHub Actions triggers the CI workflow. It builds the project with the changed contents, formats code, runs unit and integration tests with pytest and selenium (or cypress), and then provides results of the tests in the pull request.

If the changes introduce errors, the developer can go back to debugging. If there are no errors from the tests, it is deployed to Kubernetes. Once it gets deployed, integration and stress testing will take place and check marks will appear on the GitHub Actions page if the tests have passed.

