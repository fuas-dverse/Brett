
# How can we deploy a Dockerized Flask application and to what service

# Table of contents


## Context
For the individual project, we need to create some agents to be used in the group project. Our group project is based on a pair of collaborating bots that can communicate with each other to solve or help the user with a certain task. In order to make this accessible, we need to have the agents created for the individual project deployed and accessed for the outside world.

In order to do this, we need to use DevOps to automate this process. This needs to be done with the CI/CD, but the place to deploy it to has not been defined yet. That will be found out in the research.

## Structure
I'm going to use the "Realize as an expert" strategy from the DOT Framework in order to get to the correct answer. Besides that, I need to try stuff if it works. In this strategy, I predefined some methods I am going to use for this research.
**Library:**
- Literature Study
- Available product analysis
**Workshop:**
- Prototyping
**Showroom:**
- Static program analysis

*During the research, it can be possible that some of these methods are not useful for this research.*

## Literature study

### Introduction
For the literature study, I need to get to know which services are available for deployment. It focuses on methodologies, tools, and platforms relevant to deploying Dockerized Flask applications.

### Methodology
I am going to read thought articles, documentations and studies on Docker, Flask Applications and deployment services. This can be done with searching on Google using the following keywords:
- Docker
- Flask
- Deployment
- Cloud services
- Containerization

### Literature Review
**Docker and Flask:**
To understand what Docker and Flask are, I am going to break it down a bit.
- **Docker:** Docker is a platform that allows developers to package applications into containers—standardized executable components combining application source code with the operating system (OS) libraries and dependencies required to run that code in any environment. This simplification ensures that the application runs smoothly and consistently across different computing environments, from development to production.
- **Flask:** Flask is a lightweight and flexible micro web framework for Python, designed to make it easy to develop web applications quickly and with a minimal amount of code. It provides tools, libraries, and technologies that allow developers to build a web application as a single-page application, RESTful services, or other complex web services with ease.

**Deployment Strategies:**
There are many options to deploy an application nowadays. For this project I already know that I want to use the CI/CD pipeline in order to keep it in my own control. But what other options are there:
- **CI/CD**: It stands for Continuous Integration/Continuous Delivery or Continuous Deployment. It's a method used in software development that emphasizes short, frequent updates to code. This approach is key to modern development practices, particularly in agile development. Here's a breakdown of the components:
	- **Continuous Integration (CI):** This is the practice of frequently integrating code changes into a shared repository, preferably multiple times a day. Each integration is automatically verified by building the project and running automated tests. This helps detect integration errors, conflicts, and other issues early.
	- **Continuous Delivery (CD):** Extending CI, Continuous Delivery automates the delivery of the code to a staging or production environment after the build stage. It ensures that the code is always in a deployable state, facilitating frequent releases with minimal manual intervention.
	- **Continuous Deployment:** While often used interchangeably with Continuous Delivery, Continuous Deployment goes one step further by automating the release of the code to production, so that it can be used by customers. It's Continuous Delivery without manual steps in the release process.

**Services for Deployment:**
When it comes down to services for deployments, I found some of the most used services:
- **[Heroku](https://www.heroku.com/pricing)**: A good option if you want to pay, because it is not free
- **[Azure](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart)**: One of the most used, and good for deploying docker containers, there is a fee we can use as Fontys Students
- **[AWS](https://aws.amazon.com/getting-started/hands-on/deploy-docker-containers/)**: Also a good option, it is almost free around $0.004 / hour

### Discussion
#### Heroku
**Advantages:**
- **Easy to Use:** One of the best things about Heroku is how easy it is to get things up and running. If you're working on a project, and you've got it all containerized with Docker, deploying it on Heroku is a breeze. It's perfect for developers who'd rather spend their time building cool stuff than worrying about the nitty-gritty of servers and infrastructure.
- **Developer-Friendly:** It's packed with features and tools that make life easier, like being able to push updates straight from GitHub without a hitch.
- **Heroku CLI and Dashboard:** Managing your projects is super easy with Heroku's tools. Whether you're deploying, scaling up, or just checking on your app's status, it's all made simple.

**Disadvantages:**
- **Cost:** Starting out, Heroku's ease of use is fantastic, but as your project grows, so can the costs. Those dynos (Heroku's version of lightweight containers) might not feel so light on your wallet as your app scales.
- **Limited Control:** Heroku abstracts much of the underlying infrastructure, which is great for simplicity but can be a limitation for applications requiring fine-tuned configurations or specific optimizations.

#### Azure
**Advantages:**
- **Integration with Microsoft Products:** If your organization already uses Microsoft products, Azure offers excellent integration, particularly with tools like Active Directory and Visual Studio.
- **Hybrid Cloud Capabilities:** Azure provides strong support for hybrid cloud configurations, allowing businesses to integrate on-premises servers with cloud instances seamlessly.
- **Scalability and Flexibility:** Azure's infrastructure is designed to scale, offering a range of services that can be tailored to specific needs, from virtual machines to Kubernetes services for container orchestration.
- **Pricing:** the pricing of Azure is normally pretty high for some services. But because as a Fontys student, we get some credits each year. This way the disadvantage can be converted in my advantage because of the credits.

**Disadvantages:**
- **Complexity:** Azure's comprehensive suite of services and capabilities can be overwhelming, particularly for smaller teams or projects where simplicity is a priority.

#### AWS
**Advantages:**
- **Market Leader:** AWS is the largest cloud services provider, offering a vast array of services that cater to nearly any cloud computing need, from simple hosting to machine learning and beyond.
- **Scalability and Performance:** AWS provides robust scalability options for Docker containers through services like ECS (Elastic Container Service) and EKS (Elastic Kubernetes Service), ensuring high performance even under heavy load.
- **Rich Feature Set:** Offers a comprehensive set of tools for monitoring, security, and management, making it suitable for complex applications and large-scale deployments.

**Disadvantages:**
- **Learning Curve:** The breadth of AWS services and options can be daunting for newcomers. Mastering AWS can take significant time and effort.
- **Cost Management:** While AWS offers cost-effective solutions for various scales, managing costs effectively requires understanding the pricing model and actively monitoring usage, which can be complex.

### Conclusion
In conclusion, all of these services are good. They all offer a various amount of options to deploy a Docker container. AWS is the market leader, but Azure has the option to do it all for free because I am a Fontys student. So for now, my number one option goes to Azure.