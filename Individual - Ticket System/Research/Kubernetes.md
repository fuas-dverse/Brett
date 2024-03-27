# Table of contents
[Context](#Context)
[In short, what is Kubernetes?](#In%20short,%20what%20is%20Kubernetes?)
[How it works](#How%20it%20works)
[Keywords and their meanings](#Keywords%20and%20their%20meanings)
[Example](#Example)
[Playground](#Playground)
# Context
The project will utilize numerous Docker containers. Those Docker containers need to be managed by some sort of service. That is where Kubernetes comes in. 

# In short, what is Kubernetes?
Kubernetes is a tool for managing and automating containerized workloads in the cloud. Imagine you have an orchestra, think of each individual musician as a Docker container. To create beautiful music, we need a conductor to manage musicians and set the tempo. The conductor represents Kubernetes, and all the musicians represent Docker containers.


# How it works
A system deployed on Kubernetes is organized into a structure known as a cluster. At the heart of this architecture is the control plane, which functions as the cluster's brain. It is responsible for managing the cluster's state and operations, primarily through the API server. This server handles both internal and external requests to manage and orchestrate the containerized applications within the cluster.

Central to the operation of the control plane is a distributed key-value store named `etcd`. This database securely stores critical data related to the cluster's state and configuration, ensuring that the cluster operates smoothly and cohesively.

Within a Kubernetes cluster, the workload is distributed across one or more worker machines, known as nodes. Each node is an essential component of the cluster, hosting the containerized applications and providing the necessary computational resources to run them.

A key element of each node is the kubelet, an agent that runs on every node in the cluster. The kubelet's main job is to ensure that containers are running in a Pod as expected. It communicates with the control plane to receive commands and workload assignments, and then executes these instructions, ensuring that the specified containers are running and healthy.

Kubernetes excels in managing application scalability. When the demand on a containerized application increases, Kubernetes can automatically scale the application to meet the demand. This is achieved by either adding more Pods to distribute the workload more effectively or by adjusting the resources allocated to existing Pods. Additionally, Kubernetes can scale the cluster itself by adding more nodes, thereby increasing the cluster's overall computational resources and capacity.

This dynamic scaling capability ensures that applications remain responsive and available, even as demand fluctuates, without requiring manual intervention from the operations team. By automating these complex tasks, Kubernetes enables organizations to deploy and manage containerized applications at scale efficiently.

# Keywords and their meanings
To better understand how Kubernetes works, it's important to familiarize yourself with some key terms and their definitions:

- **`Cluster`**: A collection of nodes along with the control plane that manages them. Clusters are the foundational infrastructure on which Kubernetes deploys and manages containerized applications.
- **``Control Plane (also known as Master)``**: The set of components that act as the "brain" of the Kubernetes cluster. It makes global decisions about the cluster (e.g., scheduling), as well as detecting and responding to cluster events (e.g., starting a new pod when a deployment's replicas field is unsatisfied).
- **``Node``**: A worker machine in Kubernetes, which can be either a physical or a virtual machine, depending on the cluster. Each node has the services necessary to run Pods and is managed by the control plane.
- **``Pod``**: The smallest deployable unit created and managed by Kubernetes. A Pod is a group of one or more containers, with shared storage/network resources, and a specification for how to run the containers.
- **``Kubelet``**: An agent that runs on each node in the cluster. It ensures that containers are running in a Pod.
- **``etcd``**: A consistent and highly-available key value store used as Kubernetes' backing store for all cluster data.
- **``API Server``**: The central management entity of Kubernetes that exposes the Kubernetes API. It is the front-end for the Kubernetes control plane.
- **``Deployment``**: A declaration that describes a desired state for a set of Pods and ReplicaSets. Kubernetes works to maintain that state (e.g., maintaining a certain number of replicas of a pod running at any given time).
- **``Service``**: An abstraction which defines a logical set of Pods and a policy by which to access them. Services enable a loose coupling between dependent Pods.
- **``ReplicaSet``**: Ensures that a specified number of pod replicas are running at any given time. It's often used to guarantee the availability of a specified number of identical Pods.

# Example
To demonstrate deploying two Python containers on Kubernetes, we'll first need a simple Python application. For the sake of this example, let's assume we have a basic Python web server using Flask for each container, with each serving content on different ports. Below is a simple outline of what the Python application might look like, followed by the Kubernetes YAML configuration to deploy two replicas of this container.

### Python application
**`app.py`**
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Python container 1!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Dockerfile
**`Dockerfile`**
```Dockerfile
# Use an official Python runtime as a parent image  
FROM python:3.12-alpine  
  
# Set the working directory in the container  
WORKDIR /app  
  
# Copy the current directory contents into the container at /app  
COPY . .  
  
# Install any needed packages specified in requirements.txt  
RUN pip install --no-cache-dir -r requirements.txt  
  
# Make port 5001 available to the world outside this container  
EXPOSE 5001  

# Define environment variable 
ENV NAME World
  
# Run app.py when the container launches  
CMD ["python", "agent.py"]
```

### Kubernetes Deployment YAML

**`deployment.yml`**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-app-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: python-app
  template:
    metadata:
      labels:
        app: python-app
    spec:
      containers:
      - name: python-app
        image: <your-docker-image>
        ports:
        - containerPort: 5000

```

### Running Kubernetes
Before you can run Kubernetes you need to install it. You can follow this tutorial for up to date versions:
- https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/

To apply this configuration to your Kubernetes cluster, save it to a file and use the command 
```bash
kubectl apply -f deployment.yaml
```

## Playground
To get to know more about kubernetes, you can use the following demo called `minikube`. You can follow this tutorial to learn develop for kubernetes.
- https://minikube.sigs.k8s.io/docs/start/

# Sources
- https://kubernetes.io/
- https://www.youtube.com/watch?v=PziYflu8cB8
- https://minikube.sigs.k8s.io/docs/start/