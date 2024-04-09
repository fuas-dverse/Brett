# Deployment Agents
In the sixth semester at Fontys, we are creating a group project called [Dverse,](https://fuas-dverse.github.io/) The main goal of this project is to create a system where different agents can work together. Our individual is creating one or more of those agents that can complete tasks in the group project's system. To get a better understanding of what actually is needed to create such an agent, we created a design challenge research question with multiple sub questions. This research paper will be written to search for the answer to a sub question.

# Table of contents
- [[#Research|Research]]
- [[#Context|Context]]
- [[#Library|Library]]
	- [[#Library#Available product analysis|Available product analysis]]
- [[#Workshop|Workshop]]
	- [[#Workshop#Prototyping|Prototyping]]


## Research
How can we deploy a Dockerized Flask application and to what service?

## Context
For the individual project, we are creating agents that needs to be implemented in the Group project. To access these bots, we need to deploy them to a certain service. This becomes an API that can be accessed all over the internet and especially in the group project. 

There are many ways to deploy a certain API, but what are the good and bad ways. That is what I am going to find out now.

## Library
### Available product analysis
To answer this question, I first will ask a question to Perplexity AI, which is an AI that can search the web and summarize the found articles into one complete answer.

- **Prompt:** Methods to deploy a Docker Container
- **Answer:** [complete answer](https://www.perplexity.ai/search/Services-to-deploy-A1wLV86ZRRyc4oPTp7irog)
	- Google Cloud Run (free tier available)
	- Heroku (free tier available)
	- Azure App Service (free Linux-only tier available)
	- DigitalOcean (affordable Docker hosting options)
	- AWS (with pay-as-you-go pricing)

Now I know a bit about the services to where to deploy to like: Azure, AWS and DigitalOcean. I know from school we get free credits on Azure. So in our case, Azure is going to be a good first option in order to use it for free (but Azure overall a good option).

- **Prompt:** Methods to deploy a docker container: Development and Operations (DevOps)
- **Answer:** [complete answer](https://www.perplexity.ai/search/methods-to-deploy-zVhPbIWIRQGb4KRGN9F9tg)
	- In summary, the key methods for deploying Docker containers in a DevOps environment include containerization, image versioning and registry, deployment automation, CI/CD integration, consistency across environments, rollback and versioning, and resource efficiency.

Now we know that the deployment is going to happen thought a Pipeline using CI/CD. I already used it many times before, and already thought it was going to be a good option. For the next question, we want to know: How can we deploy a Docker Container to Azure using the CI/CD?

- **Prompt:** How can we deploy a Docker Container to Azure using the CI/CD? 
- **Answer:** [complete answer](https://www.perplexity.ai/search/How-can-we-bjuXUB5vTAq.ZMR68V9zLQ)
	- The key steps are as following:
		1. Build and push the Docker image to an Azure Container Registry.
		2. Create an Azure Web App for Containers.
		3. Deploy the Docker container to the Azure Web App using the CI/CD pipeline.
	- Possible tutorials:
		- https://www.youtube.com/watch?v=H5hs4LreRS0
		- https://learn.microsoft.com/en-us/azure/app-service/deploy-ci-cd-custom-container?tabs=acr&pivots=container-linux

So, now I know a bit about where and how we are going to deploy our Dockerized Flask Applications to Azure. In order to make this work. I need to make a prototype to find out how the CI/CD is going to work in Azure.

## Workshop
### Prototyping




