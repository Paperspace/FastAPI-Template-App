# Run a FastAPI app on Paperspace

## Intro

This is a template for users looking to deploy their own FastAPI app on Paperspace.

- The [FastAPI](https://fastapi.tiangolo.com/lo/) app code is located in `app/main.py`
- The Dockerfile is used to create an image which was pushed as a public image to [paperspace/fastapi-template-app:2023-06-14](https://hub.docker.com/repository/docker/paperspace/fastapi-template-app/general)
- The above image can be deployed to Paperspace using the [app config](https://docs-next.paperspace.com/deploying/app-config) located at `paperspace.yaml`

## Project Structure

```
├── Dockerfile
├── requirements.txt
├── paperspace.yaml
├── app
    ├── main.py
```

## Develop locally

- Install the [Paperspace CLI](https://docs-next.paperspace.com/cli) `curl -fsSL https://paperspace.com/install.sh | sh`
- Initialize the app `pspace init paperspace-fastapi -t Paperspace/FastAPI-Template-App`. This will create an app locally, clone this GitHub repo as your app template, and remotely link your app to Paperspace so you can add [secrets](https://docs-next.paperspace.com/secrets) and collaborators.
- Make updates to your application (e.g. application files, Dockerfile, requirements.txt)
- Build a new image by running `docker build -t my-image:tag .`
- Push image to the container registry of your choice by running `docker push my-image:tag`
- Update the app config at `paperspace.yaml` with the location of your new image
- Deploy your application on Paperspace by running [`pspace up`](https://docs-next.paperspace.com/cli/up).

## How to deploy

- Install the [Paperspace CLI](https://docs-next.paperspace.com/cli) `curl -fsSL https://paperspace.com/install.sh | sh`
- Run [`pspace up`](https://docs-next.paperspace.com/cli/up) to deploy your app on Paperspace. This will send the app config at [paperspace.yaml)(paperspace.yaml) to Paperspace, which will spin up your application.
- Once the application is in a ready state, you can send a request to the base endpoint using the application URL provided in the [Paperspace dashboard](https://https://dashboard.paperspace.com/) or outputted from the `pspace up` CLI command.

## Simplify your deployment workflow with GitHub Actions

Use the [Paperspace Deploy Action](https://github.com/Paperspace/deploy-action) to integrate a build/push process into your CI/CD pipeline.

## Documentation

Learn more about Paperspace apps at our [documentation site](https://docs-next.paperspace.com/apps).
