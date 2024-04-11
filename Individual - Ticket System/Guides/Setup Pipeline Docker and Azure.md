# [[Setup Pipeline Docker and Azure]]

# Table of contents
- [[#Introduction|Introduction]]
- [[#Requirements|Requirements]]
- [[#Setup|Setup]]
- [[#Testing|Testing]]

## Introduction
This document is going to help you with setting up CI/CD for building, pushing and deploying a Docker Container to Azure. This tutorial is based on the GitHub pipeline, so if you want to use Gitlab. You have to check their documentation in order to use their Pipeline.

## Requirements
Before you can start creating the Pipeline, you need to have some things configured in Azure. We need to have some resources created in order to deploy your Docker Container. 

What you need to create in Azure:
1. A Resource Group (if you don't have any)
2. A Container Registry
3. A App Service (Web App) if you want to create a API / Frontend

![image](https://github.com/fuas-dverse/DVerse-UI/assets/111641213/b6ad684a-82e8-4846-8e62-5317c344e24e)

Some extra stuff:
1. GitHub account with access to Github Actions
2. A GitHub Repository that contains the code you want to deploy
3. A Dockerized Container that is ready to be deployed

## Setup
For automating deployment to Azure, we need to create a GitHub Action. This Action needs to be created inside the workflow directory inside the .GitHub directory.

1. Create a folder called: `.github/workflows`

In this folder, are all the Actions. When pushing something to Gitlab, all the files in this workflows directory are being checked. If you tell the file to be triggered, it will be. That is where the Pipeline starts to run.

2. Create a file with a logic name: `PushAzureContainerRegistry.GoogleSearchAgent.yml`

After creating the file, you need to add some code to it in order to actually do something. There are some required things that need to be in the file. We are going to add them first:

3. Add the required things
```yml
name: Build, Push and Deploy to Azure

on:
  push:
    branches:
      - main

jobs:
  build_and_push:
```

Each of the required things have their own purpose. I will describe them below:
- **Name**: The name of your Pipeline / Github Action.
- **On**: On tells this Action needs to be triggered based on your configuration. In this case, it is **triggered** every time something is pushes to the `main` branch.
- **Jobs**: The jobs section is used to define certain jobs that it should run. Such as building, pushing, testing and more.

So what is next? We need to configure the Jobs:

4. Add different types of Jobs:
```yml
name: Build, Push and Deploy to Azure

on:
  push:
    branches:
      - main

jobs:
  build_and_push:
    runs-on: ubuntu-latest
    defaults:
      run:
        shell: bash
        working-directory: GoogleSearchAgent
    steps:
      - uses: actions/checkout@v2

      - uses: azure/docker-login@v1
        with:
          login-server: dversegooglesearchagent.azurecr.io
          username: ${{ secrets.REGISTRY_USERNAME }}
          password: ${{ secrets.REGISTRY_PASSWORD }}

      - name: Build and Push Docker image
        run: |
          docker build -t dversegooglesearchagent.azurecr.io/myapp:${{ github.sha }} .
          docker push dversegooglesearchagent.azurecr.io/myapp:${{ github.sha }}
  
```

As you can see, it does a lot, but it actually makes sense. In one step, you need to login Azure. This required 2 secrets: `REGISTRY_USERNAME` and `REGISTRY_PASSWORD`. You can get these secrets from the Container Registry in Azure under the tab Access Keys. There are 2 steps you need to take in order to login using the Pipeline. Go to your Azure Container Registry and copy your username and password.

- Get the username and password from Azure
![image](https://github.com/fuas-dverse/ticket-system-agent/assets/111641213/9a8ae06c-885a-4fe8-9bc2-7aa0e9fc4789)

- Create 2 GitHub Secrets in your repository settings. You can do this under Settings -> Security -> Secrets and Variables -> Actions -> Repository Secrets. Paste the copied username and password here. That should be it.
![image](https://github.com/fuas-dverse/ticket-system-agent/assets/111641213/455c9ee9-e740-420f-b1e0-25ab91457489)


After the login had completed. You can see there are 2 commands that you already know if you have experience with Docker. It builds the image and after that it pushes the image to Azure Container Registry. Then it should look like this inside GitHub:

![image](https://github.com/fuas-dverse/ticket-system-agent/assets/111641213/6e3b8b30-572c-4fc4-9d0c-f03b2c4935ff)


After we build and pushed the Docker Container to Azure Container Registry. It is not available and accessible on the web. That is where the Azure App Services comes in. The Azure App Service can be connected to the Azure Container Registry, this can be done in the Azure Portal, or also using the CI/CD. 

5. Add a new Job to the Pipeline that deploys the Container to the App Service
```yml
name: Build, Push and Deploy to Azure  
  
env:  
  AZURE_WEBAPP_NAME: DVerseGoogleSearchAgent  
  
on:  
  push:  
    paths:  
      - GoogleSearchAgent/**  
    branches:  
      - main  
  
permissions:  
  contents: read  
  
jobs:  
  build_and_push:  
    runs-on: ubuntu-latest  
    defaults:  
      run:  
        shell: bash  
        working-directory: GoogleSearchAgent  
    steps:  
      - uses: actions/checkout@v2  
  
      - uses: azure/docker-login@v1  
        with:  
          login-server: dversegooglesearchagent.azurecr.io  
          username: ${{ secrets.REGISTRY_USERNAME }}  
          password: ${{ secrets.REGISTRY_PASSWORD }}  
  
      - name: Build and Push Docker image  
        run: |  
          docker build -t dversegooglesearchagent.azurecr.io/myapp:${{ github.sha }} .  
          docker push dversegooglesearchagent.azurecr.io/myapp:${{ github.sha }}  
  
  deploy:  
    permissions:  
      contents: none  
    runs-on: ubuntu-latest  
    needs: build_and_push  
  
    steps:  
  
      - name: Deploy to Azure Web App  
        id: deploy-to-webapp  
        uses: azure/webapps-deploy@v2  
        with:  
          app-name: ${{ env.AZURE_WEBAPP_NAME }}  
          publish-profile: ${{ secrets.GOOGLE_SEARCH_AGENT_AZURE_PUBLISH_PROFILE }}  
          images: 'dversegooglesearchagent.azurecr.io/myapp:${{ github.sha }}'
```

Here you can see the last step for the deployment of the Container Registry. The step is called `deploy`, it has a property called `needs` with the content `build_and_push`. The first job that we created earlier is called like this. What this does, it waits for the `build_and_push` job to be finished. When that job is finished, it starts this one.

Then on top of the file there is a new added env variable called `AZURE_WEBAPP_NAME`. This is the name of the Azure App Service. You require this one in order to deploy to the correct Azure App Service. After that, you have the `publish-profile`. You need to have the `publish-profile` setup as secret in GitHub.

You need to download the publish profile in your Azure App Service dashboard. As you can see on the picture below on the right.

![DownloadPublishProfile](https://github.com/fuas-dverse/Brett/assets/111641213/7f2111dc-fb2c-4261-bdb0-fe8f7c13a01a)

Than you need the content of this file and add it to your GitHub Secrets as you already did with the username and password.

![image](https://github.com/fuas-dverse/ticket-system-agent/assets/111641213/6ec3ce4a-819c-42e5-9399-f00a66a94745)

And in the end, you have the command:
```yml
    images: 'dversegooglesearchagent.azurecr.io/myapp:${{ github.sha }}'
```

This specifies the latest image of your Azure Container Registry, and this means that now you have deployed the just earlier pushed image to the Azure App Service.

You can now visit the URL of your Azure App Service and that is it!!

## Testing
**TODO: Add the test phase in the CI/CD**

