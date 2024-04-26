# [[Code research - Kubernetes]]
Before we start with deploying our Kubernetes cluster. We need to have a API created. In my case I am going to use Python with Flask because we use it for the group project as well. So lets create a simple API endpoint first:

```python
from flask import Flask, request, jsonify  
  
app = Flask(__name__)  
  
  
@app.route('/', methods=['GET', 'POST'])  
def chat():  
    return jsonify({"response": "Hi I am an API"})  
  
  
if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=5001, debug=True)
```

I added a Dockerfile with it:

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
  
# Run app.py when the container launches  
CMD ["python", "main.py"]
```

As you can see, I use the command `pip install --no-cache-dir -r requirements.txt`. So there needs to be a requirements.txt file. 
# Setup development cluster
1. create a registry
```shell
k3d registry create dverse --port 5001
```

2. Create k3d cluster
```shell
k3d cluster create dverse --servers 1 --agents 1 --port 9080:80@loadbalancer --registry-use dverse:5001
```

3. Check if the cluster is running
```bash
kubectl get nodes
```

The result should be like this:

![[Screenshot 2024-04-26 at 09.12.16.png]]

# Deploy API to kubernetes
### Build API docker image
Go into your API project and build your docker image here.

```shell
docker build -t localhost:5001/api:v0.1 .
```

### Push API docker image
Then you should push your Docker Image by running:

```shell
docker push localhost:5001/api:v0.1
```

### Deploy your Kubernetes deployment
1. First I need to create a deployment.yml file. And place this in the root of your directory.

```yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
  labels:
    app: api
spec:
  replicas: 1
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
      - name: api
        image: k3d-fontys:5000/api:v0.1
        ports:
        - containerPort: 3000
        resources:
          limits:
            memory: 512Mi
            cpu: "1"
```

2. Then we need to deploy the image to our Kubernetes Cluster.
```shell
kubectl apply -f deployment.yml
```

3. Check if your deployment has been created
```shell
kubectl get deployments
```

4. Than we need to port forward our pod, you can get your pod by running 
```shell
kubectl get pods
```

5. Actually port forward your pod
```shell
kubectl port-forward api-5676b48bbb-s5cv5 3000
```

# Deploy Kubernetes Service
First we need to create a service.yml:
```yml
apiVersion: v1
kind: Service
metadata:
  name: api-service
spec:
  selector:
    app: api
  ports:
    - protocol: TCP
      port: 80
      targetPort: 3000
```

To expose our API we first. need to create a service. We can do this with the following command:

```shell
kubectl apply -f service.yml
```

# Deploy Kubernetes Ingress
First we need to create a ingress.yml file.
```yml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: api-ingress
spec:
  rules:
  - host: api.localhost
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: api-service
            port:
              number: 80
```

After that you need to app
```shell
kubectl apply -f ingress.yml
```

In the end we need to port forward the application again using:
```shell
kubectl port-forward api-578bd5bbcb-djhjl 5001
```

Now you can visit the endpoint `api.localhost:5001` and see the following:
![[Screenshot 2024-04-26 at 10.08.53.png]]

# Testing
Now the exiting opart begins, we are going to test the application using Load Testing from K6. I create an account on www.grafana.net. In here I created a new project. Grafana is a cloud service that shows functions as a dashboard where you can see you test results.

1. Download the K6 CLI from this url: https://k6.io/docs/get-started/installation/. 

2. In Grafana you need to authorize the K6 with Grafana. Running the following command:
```shell
`k6 login cloud --token <YOUR_KEY_HERE>`
```

3. Than you can create your test script called `test.js`: 
```js
import http from 'k6/http';  
import { sleep } from 'k6';  
  
export const options = {  
  vus: 10,  
  duration: '10s',  
  cloud: {  
    // Project: Default project  
    // Test runs with the same name groups test runs together.    
    name: 'Test (26/04/2024-10:29:12)'  
  }  
};  
  
export default function() {  
  http.get('http://localhost:5001/');  
  sleep(0.0001);  
}
```

This test runs for 10s and after every 0.0001 second, it generates a new request. Now you need to run the test:

4. Run the test locally but send the data to the cloud
```shell
k6 run --out cloud test.js
```

What this does, it runs the test locally. But it sends the data to the cloud, in our example the cloud is Grafana. When you have runned the commad it gives you this output:

![[Screenshot 2024-04-26 at 11.02.50.png]]

And this results in the following results in the Grafana dashboard:

![[Screenshot 2024-04-26 at 11.04.01.png]]

# Conclusion
So what we have done now. We create a simple API in Python using Flask. We Dockerized this application. After that we created our own Kubernetes Cluster using K3D. We deployed it, created a service and an ingress in order to get eternal access from the cluster. 

And in the end, we tested the application using a load balance test using Grafana as our dashboard insights and k6 as our CLI to run the tests.