To use github actions to deploy the WEB API on gke, the following steps are required:

1.	Create a new google cloud project (or select the existing one)
2.	Enable the Container registry and Kubernetes Engine API
3.	Create a new GKE cluster (this saves time while performing CI/CD as creating the cluster takes around 6-8 minutes of time)
4.	Create a google cloud service account (if one doesn’t exist)
5.	Add the owner role (IAM) to your service account that you have created above
6.	Create a JSON service account key for the service account (Download this key and store it in your local machine)


Now we have set up the required artifacts on GKE to deploy our application, now the following secrets should be added to our github repository:
* GKE_PROJECT: Google Cloud project ID
* GKE_SA_KEY: the content of the service account JSON file


Following is the workflow of CI pipeline:

1.  Set the following environment variables
     1.	PROJECT_ID: GKE_PROJECT secret
     2. GKE_CLUSTER: The name of the cluster that we created while setting up the cluster on GKE
     3.	GKE_ZONE: Zone (Region) of the cluster (Example: US-Central1)
     4.	IMAGE: The name of the image that we want to use for the docker build
2.	After running the initial formatting and unit tests, now we deploy our application as a service on which integration and load tests would be performed
3.	To deploy our application on GKE cluster, following steps are performed
    1. 	Set up the gcloud CLI
    2.	Get the authorization for docker to store the docker builds
    3.	Get the credentials of GKE cluster to deploy the application
    4.	Build the docker image and push it to google container registry
    5.	Set up the kustomize (this creates the Kubernetes objects based on the kustomization file that we create inside the current directory)
    6.	Deploy the docker image to GKE cluster using the kustomize
4.	Once we have the application up and running, the integration and load test jobs get triggered which tests this application and logs are displayed to the developer on the github actions console.
5.	Once all the jobs finish and logs are displayed, the GKE cluster objects, i.e., deployments, services and jobs are deleted.


The above steps are repeated for the staging environment but this happens whenever the code gets pushed into the master branch.
