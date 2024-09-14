# Cloud-Native DevOps Project (Part 3 of 5)

## Background

Our University Library is a cornerstone of academic resources, aims to enhance
accessibility to educational materials through an advanced online platform. You
has been asked to develop a cloud-native microservices architecture to support the
library’s diverse user base and streamline deployment processes. This project is
divided into 5 parts as follows:

<table>
    <tr>
        <th>No.</th>
        <th>Title</th>
        <th>Task</th>
    </tr>
    <tr class="highlight">
        <td>1</td><td>Deploying Microservice with PostgreSQL on Render</td><td>Task 4.2P</td>
    </tr>
    <tr>
        <td>2</td><td>Containerizing Microservices with Docker and Deploying to Local Kubernetes</td><td>Task 6.2P</td>
    </tr>
    <tr>
        <td>3</td><td>Containerizing Microservices with Docker and Deploying to Azure Managed Kubernetes</td><td>Task 7.2P</td>
    </tr>
    <tr>
        <td>4</td><td> Infrastructure as Code with Terraform</td><td>Task 8.2C</td>
    </tr>
    <tr>
        <td>5</td><td>CI/CD with Github Actions using Terraform</td><td>Task 9.2D</td>
    </tr>
</table>

By end of this project, you will gain a comprehensive understanding of essential DevOps practices and cloud-native application deployment techniques. More specifically, you will be able to do following:

1. Create Dockerfiles to containerize application and define the runtime environment.
2. Develop Kubernetes YAML files (deployment.yaml and service.yaml) to deploy and manage their microservice on Azure managed Kubernetes cluster.
3. Write Terraform scripts (main.tf, variables.tf, outputs.tf, provider.tf) to provision Azure infrastructure.
4. Deploy Azure Kubernetes Service (AKS) and integrate PostgreSQL for data storage.
5. Configure GitHub Actions workflows to automate the CI/CD pipeline.
6. Apply theoretical knowledge to real-world scenarios, enhancing their understanding of cloud computing and DevOps principles.

## Task
In this task, you are continuing work from the previous project, focusing on
Dockerizing the book_catalog and inventory_management microservices and
deploying it to Azure Managed Kubernetes. By the end of this project, you will gain
hands-on experience in setting up and managing containerized applications to
Azure Container Registry and host them on Azure Kubernetes Service.
### Steps

1. Create account on [Render](http://render.com/) using GitHub if you dont have one yet.
2. Create PostgreSQL database instance on [Render](http://render.com/).
3. Once database is created, copy the __External Database URL__ in notepad for future use.
4. Ensure your Dockerfile is correctly set up.
5. Run the following command to start the application : `docker-compose up`
6. Ensure you have a deployment.yaml file to define how your application will be deployed on Kubernetes.
7. Update the DATABASE_URL value in deployments.yml, docker-compose.yml, config.py, database.py files with the External Database URL. Also update the container registry url in deployment.yml file.
8. Use `kubectl apply -f deployments.yaml` to deploy your application to the Kubernetes cluster.
9. To ensure our deployments are running, use this command `kubectl get deployments`.
10. To ensure our pods are running, use this command `kubectl get pods`.
11. If the pod is not running we have to check the logs for errors, To check the logs use this command `kubectl logs pod-name`.
12. To verify the service is up and running, use this command `kubectl get services`.
13. To access the application, If we are using a cloud provider, find the external IP of the node. So to access the application open a browser and
navigate to `http://<NodeIP>/docs` url in browser. Check different endpoints via Swagger Docs such as `create new book`, `get all book`, and `delete book`.

