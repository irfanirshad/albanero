
# Docker in 7 easy steps


## What is Docker

A practical way to package software so that it runs on any hardware

**Dockfile** - a blueprint for building a Dockerimage**
**Docker Image** - A template for running dockerimage
**Container** -  a running process


## Installation

Docker Desktop or Docker-CLI

## Dockerfile

Checkout Dockerfile for how to write up one

<!-- - Install dependencies first so they can be cached -->


## How to build an image(after writing a Dockerfile)

### docker build -t albanero/demo-app:1.0

'-t' argument allows you to name your image (a nametag)

## PUSH & PULL DOCKER IMAGES to cloud

### To push image to an image registry

docker push 


### ANother dev would pull it down 
docker pull


## DOCKER ports mapping to machine ports
check out dockerfile for the command to map the above mentioned ..


## HOW TO COMMUNICATE BETWEEN TWO DOCKER IMAGES: VOLUMES

If you want to share data b/w multiple containers and the preferred way to do that is by VOLUMES.

A volume is just a dedicated folder on the host machine. 
Inside this folder, a container can create files that can be re-mounted into future/multiple containers simultaneously and access same set of files . The saved files persist after the containers have been shut down...

TL:DR; A common shared file storage is available across these containers which stick around after the containers have been shut down..


COMMANDS are:

```bash
docker volume create shared-stuff
docker run \
    --mount source=shared-stuff, target=/stuff
```


## DEBUGGING in DOCKER

Use the GUI docker-desktop for rich user experience . Or use ```docker exec <container>```
to get inside of the container and do whatever you want in that environment ..

```docker inspect <container_name>```

### Keep it simple and lightweight: Intro to DOCKER-COMPOSE

Each container should only run one process 
If your app needs more than that, docker has a tool for that called "docker-compose"


Suppose your node app has a seperate mySQL service that also needs a persistent storage

PTO to 'docker-compose.yml' to see how we write up one


**Build and Run**
```
docker-compose up -d
```

## Other docker commands

Install an image on the fly
```
docker run -t -d --name firstcontainer_name alpine
<!-- should return back a container ID  -->
```

To get inside of a container
```
docker exec -it firstcontainer_name sh
<!-- OR -->
docker exec -it firstcontainer_name bash
```

### DOcker-compose MISC

github.com/docker/awesome-compose/


### DOcker networks

Two containers talking to each other through a network

Journey from docker-network to my localhost machine Wifi.
![url: https://www.youtube.com/watch?v=OU6xOM0SE4o]

A goof watch^ . Watch it fully later and repeat it 2-3 times on intervals to really hammer down internal networking concepts.  

### Others


- need only first 2 chars of a container image to reference it ... 

Images is the template where you can spin up many containers 

Containers are instances of these images..think of it like this way...

Logs:

```docker-compose logs
```


