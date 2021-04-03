<h3>Steps to setup a Google Cloud account and deploying a web application on Google Cloud Kubernetes Engine:</h3>

Pods: Kubernetes represents applications as Pods, which are scalable units holding one or more containers. The Pod is the smallest deployable unit in Kubernetes. Usually, you deploy Pods as a set of replicas that can be scaled and distributed together across your cluster. One way to deploy a set of replicas is through a Kubernetes Deployment.

- Create a Google Cloud account.
- Once the account is created, visit the Kubernetes Engine page in the Google Cloud Console.
- Create a new project by entering a name for the project 
- Wait for the API and related services to be enabled. This can take several minutes.

<h4>There are two ways to access your project:</h4>
- Option A: Using Cloud Shell (Google) which comes preinstalled with the gcloud, docker, and kubectl command-line tools. You do not need to install these command lines.  

- Option B: Use command-line tools locally  
      - Install the Cloud SDK, which includes the gcloud command-line tool.  
      - Using the gcloud command line tool, install the Kubernetes command-line tool. kubectl is used to communicate with Kubernetes, which is the cluster orchestration system of GKE clusters: gcloud components install kubectl  
      - Install Docker Community Edition (CE) on your workstation. You use this to build a container image for the application.  
      - Install the Git source control tool to fetch the sample application from GitHub.  


     
**Before deploying your web application to GKE, you must package the application source code as a Docker image.**
- To build a Docker image, you need source code and a Dockerfile. A Dockerfile contains instructions on how the image is built.

1. Download the source code and dockerfile and access the path.  
   Eg: 
      `git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples`
      `cd kubernetes-engine-samples/hello-app`
      
 2. Set the PROJECT_ID environment variable to your Google Cloud project ID (PROJECT_ID). The PROJECT_ID variable associates the container image with your project's Container Registry.       
    Eg:
       `export PROJECT_ID=PROJECT_ID`
 
 3. Confirm that the PROJECT_ID environment variable has the correct value:  
    Eg: 
       `echo $PROJECT_ID`
       
  4. Build and tag the Docker image for your app:  
     Eg: 
        `docker build -t gcr.io/${PROJECT_ID}/hello-app:v1 .`
    
    NOTE: This command instructs Docker to build the image using the Dockerfile in the current directory and tag it with a name, such as gcr.io/my-project/hello-app:v1. The gcr.io prefix refers to Container Registry, where the image is hosted. Running this command does not upload the image.   
    
  5. Run the `docker images` command to verify the build was successful.   
     Eg: 
        `docker images`
   
 **The next step would be to push the Docker image to Container Registy. The container image to a registry must be uploaded so that the GKE cluster 
 can download and run the container image.**
   
 1. Enable the Container Registry API for the Google Cloud project you are working on:    
    Eg: 
       gcloud services enable containerregistry.googleapis.com

 2. Configure the Docker command-line tool to authenticate to Container Registry:  
    Eg:
       gcloud auth configure-docker

3. Push the Docker image that you just built to Container Registry:  
    Eg: 
       docker push gcr.io/${PROJECT_ID}/hello-app:v1
       
**After pushing the Docker image to Container Registry, you will create a [GKE cluster](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture)
 A GKE cluster consists of a pool of Compute Engine VM instances running Kubernetes, the open source cluster orchestration system that powers GKE.**
 
1. Set your project ID option for `gcloud` tool:   
   Eg: 
      `gcloud config set project $PROJECT_ID`

2. Set your zone or region. Depending on the mode of operation that you choose to use in GKE, specify a default zone or region. If you use the Standard mode, your cluster is zonal (for this tutorial), so set your default compute zone. If you use the Autopilot mode, your cluster is regional, so set your default compute region. Choose the zone or region that is closest to you.
  
   Standard cluster, such as us-west1-a:  
   Eg: 
      `gcloud config set compute/zone COMPUTE_ZONE`

   Autopilot cluster, such as us-west1:  
   Eg: 
    `gcloud config set compute/region COMPUTE_REGION`
    
 3. Create a cluster by specifying the name of the cluster.  
    Eg:
       `gcloud container clusters create hello-cluster`
    
    NOTE: It takes a few minutes for your GKE cluster to be created and health-checked.   
 
 4. Once the command finishes, you can see the cluster's three noded (created by default) by running the below commands:    
    `kubectl get nodes`
    
**Once the cluster is ready, you can go ahead and deploy the application to GKE. You will create replicas(pods) for deployment
One Deployment Pod contains only one container (the docker image of your application).**  
NOTE: You also create a HorizontalPodAutoscaler resource that scales the number of Pods from 3 to a number between 1 and 5, based on CPU load.

1. Ensure that you are connected to your GKE cluster.   
   Eg: 
      `gcloud container clusters get-credentials hello-cluster --zone COMPUTE_ZONE`
      
2. Create a kubernetes Deployment for your web application Docker image.  
   Eg: 
      `kubectl create deployment hello-app --image=gcr.io/${PROJECT_ID}/hello-app:v1`
      
3. Set the baseline number of Deployment replicas to 2  
   Eg: 
      `kubectl scale deployment hello-app --replicas=2`
 
 4. To see the Pods created, run the following command:  
    `kubectl get pods`
    
 **Now that the pods are working, you need to expose the web application to the internet.**  
 While Pods do have individually-assigned IP addresses, those IPs can only be reached from inside your cluster.
 
You need a way to   
    1) Group Pods together into one static hostname   
    2) Expose a group of Pods outside the cluster, to the internet.
    
This can be achieved by using ["Kubernetes Services"](https://kubernetes.io/docs/concepts/services-networking/service/)    
Services group Pods into one static IP address, reachable from any Pod inside the cluster. GKE also assigns a DNS hostname to that static IP.

The default Service type in GKE is called ClusterIP, where the Service gets an IP address reachable only from inside the cluster. To expose a Kubernetes Service outside the cluster, create a Service of type "LoadBalancer". This type of Service spawns an External Load Balancer IP for a set of Pods, reachable through the internet.

Using Cloud Shell:  
1. Use the `kubectl expose` command to generate a Kubernetes Service for your application deployment.  
   Eg: 
      `kubectl expose deployment hello-app --name=hello-app-service --type=LoadBalancer --port 80 --target-port 8080`
      
    NOTE: Here, the --port flag specifies the port number configured on the Load Balancer, and the --target-port flag specifies the port number that the hello-app container is listening on.
    
2. Run the following command to get the details of the service created:  
   `kubectl get service`
   
   NOTE:  It might take a few minutes for the Load Balancer to be provisioned. Until the Load Balancer is provisioned, you might see a <pending> IP address.
   
3. Copy the external IP address to the clipboard and access your application through a web browser.   

**To avoid incurring charges to your Google Cloud account for the resources used, either delete the project that contains the resources or keep th project and delete individual resources.**   

1. Delete the Service:   
   `kubectl delete service [SERVICE_NAME]`
   
2. Delete the cluster:  
   `gcloud container clusters delete [CLUSTER_NAME] --zone [COMPUTE_ZONE]`
   
3. Delete container images:   
   `gcloud container images delete gcr.io/${PROJECT_ID}/hello-app:v1  --force-delete-tags --quiet`
   `gcloud container images delete gcr.io/${PROJECT_ID}/hello-app:v2  --force-delete-tags --quiet`
   
 
 
 
 
