# FastAPI Template Paperspace App

## Intro
This is a template FastAPI app that can be run on Paperspace. This is created as a reference for users who are looking to create their own FastAPI app on Paperspace.

The FastAPI app is located in app/main.py. The Dockerfile is used to create an image which was pushed as a public image to [https://hub.docker.com/repository/docker/paperspace/fastapi-template-app/general](paperspace/fastapi-template-app:latest). This image can be deployed to Paperspace using the deployment spec located in paperspace.yaml.

## Project Structure
```
├── Dockerfile
├── requirements.txt
├── paperspace.yaml
├── app
    ├── main.py
    ├── __init__.py
```

[_paperspace.yaml_](paperspace.yaml):
```
apiVersion: latest
enabled: true
name: my-fastapi-app
image: paperspace/fastapi-template-app:latest
port: 80
healthChecks:
  startup:
    path: /
  readiness:
    path: /
  liveness:
    path: /
resources:
  replicas: 1
  instanceType: A4000
  autoscaling:
    enabled: true
    maxReplicas: 2
    metrics:
      - metric: requestDuration
        summary: average
        value: 1.2
      - metric: cpu
        summary: average
        value: 75
```

## Develop locally
- Clone repo to your workspace: `git clone https://github.com/gradient-ai/FastAPI-Template-App.git`
- Make updates to your application (e.g. application files, Dockerfile, requirements.txt)
- Build a new image by running `docker build -t my-image:tag .`
- Push build image to container registry of your choice
- Update the image (containerRegistry) in the paperspace.yaml to point to the new image location in the container registry
- Deploy application by running `pspace up`. Ensure you have the [https://github.com/Paperspace/cli] Paperspace CLI) installed.

## How to deploy
- Download the [https://github.com/Paperspace/cli](Paperspace CLI)
- run `pspace init -t https://github.com/gradient-ai/FastAPI-Template-App`. This will initialize the project locally and clone this GitHub repo as your project template.
- run `pspace up`. This will send the [_paperspace.yaml](paperspace.yaml) to Paperspace to spin up your application.


## Deployment GitHub Action
Use the [https://github.com/Paperspace/deploy-action](Paperspace Deploy GitHub action) to integrate the build/push process with your CI/CD pipeline.

## Additional Information
Find more information about Paperspace apps in our [https://docs.paperspace.com/gradient/deployments](docs).