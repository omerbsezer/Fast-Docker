# Fast-Docker
This repo aims to cover Docker details (Dockerfile, Image, Container, Commands, Volumes, Docker-Compose, Networks, Swarm, Stack), example usage scenarios (applications) in a nutshell.

**Keywords:** Docker Image, Dockerfile, Containerization, Docker-Compose File, Swarm

**NOTE: This tutorial is only for education purpose. All related references are listed at the end of the file.**

# Quick Look 
- [App: Creating First Docker Image and Container using Docker File](https://github.com/omerbsezer/Fast-Docker/blob/main/FirstImageFirstContainer.md)
- [App: Binding Volume to the Different Containers](https://github.com/omerbsezer/Fast-Docker/blob/main/DockerVolume.md)
- [App: Binding Mount to Container](https://github.com/omerbsezer/Fast-Docker/blob/main/DockerVolume.md#app_mount)
- [App: Docker Compose and Creating WordPress Container depends on MySql Container]()
- [App: Docker Swarm using PlayWithDocker, Creating Swarm Cluster: 3 x WordPress Containers and 1 x MySql Container]()
- [App: Copying Docker Volume Content to Host PC]()
- [App: Updating Docker Swarm Service]()
- [App: Creating New Network Switch and (Dis)Connecting Containers]()
- [Docker Commands Cheatsheet](https://github.com/omerbsezer/Fast-Docker/blob/main/DockerCommandCheatSheet.md)

# Table of Contents
- [Motivation](#motivation)
    - [Needs](#needs)
    - [Benefits](#benefits)
    - [Problems Docker does not solve](#problems)
- [What is Docker?](#whatIsDocker)
    - [Architecture](#architecture)
    - [Installation](#installation)
    - [Docker Engine (Deamon, REST API, CLI)](#engine)
    - [Docker Registry and Docker Hub](#registry)
    - [Docker Command Structure](#command)
    - [Docker Volumes/Bind Mounts](#volume)
    - [Docker Network](#network)
    - [Docker Log](#log)
    - [Docker Stats/Memory-CPU Limitations](#stats)
    - [Docker File](#file)
    - [Docker Image](#image)
    - [Docker Container](#container)
    - [Docker Compose](#compose)
    - [Docker Swarm](#swarm)
    - [Docker Stack](#stack)
- [Play With Docker](#playWithDocker)
- [Docker Commands Cheatsheet](#cheatsheet)
- [References](#references)

## Motivation <a name="motivation"></a>
Why should we use Docker? "Docker changed the way applications used to build and ship. It has completely revolutionized the containerization world." (Ref:ItNext)

### Needs <a name="needs"></a>
- Installing all dependencies, setting up new environment for SW (time consuming every time to install environment for testing ) 
- We want to run our apps on different platforms (Ubuntu, Windows, Raspberry Pi).
    - Question in our mind: What if, it does not run on a different OS?
- CI/CD Integration Testing: We can handle unit testing, component testing with Jenkins. What if integration testing? 
    - Extending Chain: Jenkins- Docker Image - Docker Container - Automatic testing
- Are our SW products portable to carry on different PC easily? (especially in development & testing phase)


### Benefits <a name="benefits"></a>

- NOT needed to install dependencies/SWs again & again
- Enables to run on different OS, different platforms
- Enables consistent environment
- Enables more efficient use of system resources
- Easy to use and maintain
- Efficient use of the system resources
- Isolate SW components
- Enables faster software delivery cycles
- Containers give us instant application portability.
- Enables developers to easily pack, ship, and run any application as a lightweight, portable, self-sufficient container
- Microservice Architecture (Monolithic Apps to MicroService Architecture, e.g. [Cloud Native App](https://docs.microsoft.com/en-us/dotnet/architecture/cloud-native/introduction))

(Ref: Infoworld)

### Problems Docker does not solve<a name="problems"></a>
- NOT fix your security issues
- NOT turn applications magically into microservices
- Docker isn’t a substitute for virtual machines

(Ref: Infoworld)

## What is Docker?  <a name="whatIsDocker"></a>
- Docker is a tool that reduces the gap between Development/Deployment phase of a software development cycle.
- Docker is like VM but it has more features than VMs (no kernel, only small app and file systems, portable)
    - On Linux Kernel (2000s) two features are added (these features support Docker):
        - Namespaces: Isolate process.
        - Control Groups: Resource usage (CPU, Memory) isolation and limitation for each process. 
- Without Docker, each VM consumes 30% resources (Memory, CPU)

![image](https://user-images.githubusercontent.com/10358317/113183089-ef51fa00-9253-11eb-9ade-771905ce8ebd.png) (Ref: Docker.com)

### Architecture  <a name="architecture"></a>

![image](https://user-images.githubusercontent.com/10358317/113183210-0db7f580-9254-11eb-9716-0de635f3cbdf.png) (Ref: Docker.com)


### Installation  <a name="installation"></a>

- Linux: Docker Engine
    - https://docs.docker.com/engine/install/ubuntu/
- Windows: Docker Desktop for Windows 
    - WSL: Windows Subsystem for Linux, 
    - WSL2: virtualization through a highly optimized subset of Hyper-V to run the kernel and distributions, better than WLS.
        - https://docs.docker.com/docker-for-windows/install/
- Mac-OS: Docker Desktop for Mac
    - https://docs.docker.com/docker-for-mac/install/

### Docker Engine (Deamon, REST API, CLI)  <a name="engine"></a>
- There are mainly 3 components in the Docker Engine:
    - Server is the docker daemon named docker daemon. Creates and manages docker images, containers, networks, etc.
    - Rest API instructs docker daemon what to do.
    - Command Line Interface (CLI) is the client used to enter docker commands.

![image](https://user-images.githubusercontent.com/10358317/113183406-45bf3880-9254-11eb-8d13-e68c83f3d349.png) (Ref: Docker.com)

### Docker Registry and Docker Hub  <a name="registry"></a>

- https://hub.docker.com/

![image](https://user-images.githubusercontent.com/10358317/113183434-4eb00a00-9254-11eb-9275-9b1ccf705d5b.png) 


### Docker Command Structure  <a name="command"></a>

- docker [ManagementCommand] [Command] 

```
docker container ls -a
docker image ls
docker volume ls
docker network ls
docker container rm -f [containerName or containerID]
```

![image](https://user-images.githubusercontent.com/10358317/113183615-81f29900-9254-11eb-8695-360680931866.png)

![image](https://user-images.githubusercontent.com/10358317/113183721-9fbffe00-9254-11eb-9841-79bf037db34a.png)

### Docker Container  <a name="container"></a>

![image](https://user-images.githubusercontent.com/10358317/113183556-730be680-9254-11eb-8bdd-84c5cf5b86c6.png)

- When we create the container from image, in every container, there is an application that is set to run by default app. 
    - When this app runs, container runs.
    - When this default app finished/stopped, container stopped. 
- There could be more than one app in docker image (such as: sh, ls, basic commands)
- When the Docker container is started, it is allowed that a single application is configured to run automatically

```
docker container run --name mywebserver -d -p 80:80 -v test:/usr/share/nginx/html nginx
docker container ls -a
docker image pull alpine
docker image push alpine
docker image build -t hello . (run this command where “Dockerfile” is)
(PS: image file name MUST be “Dockerfile”, no extension)
docker save -o hello.tar test/hello
docker load -i <path to docker image tar file>
docker load -i .\hello.tar
```

Goto: [App: Creating First Docker Image and Container using Docker File](https://github.com/omerbsezer/Fast-Docker/blob/main/FirstImageFirstContainer.md)

### Docker Container: Life Cycle

![image](https://user-images.githubusercontent.com/10358317/113186436-f67b0700-9257-11eb-9b2e-41ccf056e88b.png)

```
e.g. [imageName]=alpine, busybox, nginx, ubuntu, etc.
docker image pull [imageName]
docker container run [imageName]
docker container start [containerId or containerName]
docker container stop [containerId or containerName]
docker container pause [containerId or containerName]
docker container unpause [containerId or containerName]
```

### Docker Container: Union File System  <a name="container-filesystem"></a>

- Images are R/O.
- When containers are created, new R/W thin layer is created.

![image](https://user-images.githubusercontent.com/10358317/113183883-d8f86e00-9254-11eb-994b-30c17fe9429b.png)

### Docker Volumes: Why Volumes needed?
- Persistence
- e.g. Create log file in the container. When it is killed, log file also killed. So we use Volumes!

![image](https://user-images.githubusercontent.com/10358317/113184189-2d035280-9255-11eb-9409-578ad1f2bd4b.png)

### Docker Volumes/Bind Mounts  <a name="volume"></a>

- Volumes and Bind Mounts used for logs, inputs, outputs, etc..
- When volumes bind to directory in the container, this directory and volume are synchronised.

```
docker volume create [volumeName]
docker volume create test
docker container run --name [containerName] -v [volumeName]:[pathInContainer] [imageName]
docker container run --name c1 -v test:/app alpine
```
Goto: [App: Binding Volume to the Different Containers](https://github.com/omerbsezer/Fast-Docker/blob/main/DockerVolume.md)

#### Bind Mount
```
docker container run --name [containerName] -v [pathInHost]:[pathInContainer] [imageName]
docker container run --name c1 -v C:\test:/app alpine
```
![image](https://user-images.githubusercontent.com/10358317/113184347-57eda680-9255-11eb-811c-9f55efd11deb.png) (Ref: Docker.com)

Goto: [App: Binding Mount to Container](https://github.com/omerbsezer/Fast-Docker/blob/main/DockerVolume.md#app_mount)

### Docker Network <a name="network"></a>
- Docker containers work like VMs.
- Every Docker containers have network connections
- Docker Network Drivers:
    - None
    - Bridge
    - Host
    - Macvlan
    - Overlay
    
#### Docker Network: Bridge
- Default Network Driver: Bridge (--net bridge)

```
docker network create [networkName]
docker network create bridge1
docker container run --name [containerName] --net [networkName] [imageName] 
docker container run --name c1 --net bridge1 alpine sh
docker network inspect bridge1
docker container run --name c2 --net bridge1 alpine sh
docker network connect bridge1 c2
docker network inspect bridge1
docker network disconnect bridge1 c2
```

![image](https://user-images.githubusercontent.com/10358317/113184949-1b6e7a80-9256-11eb-9a0c-fe5c62404a06.png) (Ref: Docker.com)

#### Docker Network: Host
- Containers reach host network interfaces (--net host)

```
docker container run --name [containerName] --net [networkName] [imageName] 
docker container run --name c1 --net host alpine sh
```

![image](https://user-images.githubusercontent.com/10358317/113185061-43f67480-9256-11eb-9b94-83735ce980ce.png) (Ref: Docker.com)

#### Docker Network: MacVlan
- Each Container have own MAC interface (--net macvlan)

![image](https://user-images.githubusercontent.com/10358317/113185105-52dd2700-9256-11eb-84f2-ef1880eb4f4c.png) (Ref: Docker.com)

#### Docker Network: Overlay 
- Containers which work on different PC/host, can work like same network (--net overlay)

![image](https://user-images.githubusercontent.com/10358317/113185192-6e483200-9256-11eb-8cb4-d8aa170d1a1e.png) (Ref: Docker.com)

### Docker Log  <a name="log"></a>

- Docker Logs show /dev/stdout, /dev/stderror

```
docker logs --details [containerName]
```

![image](https://user-images.githubusercontent.com/10358317/113289697-d8151a00-92f0-11eb-86e6-6280c4bf2e77.png)


### Docker Stats/Memory-CPU Limitations  <a name="stats"></a>

![image](https://user-images.githubusercontent.com/10358317/113289735-e9f6bd00-92f0-11eb-940b-13113a5a5da2.png)

![image](https://user-images.githubusercontent.com/10358317/113289755-efec9e00-92f0-11eb-9f49-333a4608c523.png)

![image](https://user-images.githubusercontent.com/10358317/113289773-f5e27f00-92f0-11eb-8c4f-2db75f17baeb.png)


### Docker Enviroment Variables  <a name="variables"></a>

![image](https://user-images.githubusercontent.com/10358317/113289974-40fc9200-92f1-11eb-9f12-1125ec32eabf.png)


### Docker File  <a name="file"></a>

![image](https://user-images.githubusercontent.com/10358317/113185932-54f3b580-9257-11eb-9f50-0d18512a0c40.png)

#### Sample Docker Files

```
FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./index.py
```

```
FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install default-jre -y
WORKDIR /myapp
COPY /myapp .
CMD ["java","hello"]
```

### Docker Image  <a name="image"></a>

- Create Image using Dockerfile
```
docker image build -t hello . (run this command where “Dockerfile” is)
(PS: image file name MUST be “Dockerfile”, no extension)
docker image pull [imageName]
docker image push [imageName]
docker image tag [imageOldName] [imageNewName]
(PS: If you want to push DockerHub, [imageNewName]=[username]/[imageName]:[version])
docker save -o hello.tar test/hello
docker load -i <path to docker image tar file>
docker load -i .\hello.tar
```

![image](https://user-images.githubusercontent.com/10358317/113186047-748ade00-9257-11eb-9c1c-1604d53523e8.png)

Goto: [App: Creating First Docker Image and Container using Docker File](https://github.com/omerbsezer/Fast-Docker/blob/main/FirstImageFirstContainer.md)

### Docker Compose  <a name="compose"></a>
- Define and run multi-container applications with Docker.
- Easy to create Docker components using one file: Docker-Compose file
- It is yaml file that defines components: services, volumes, networks, secrets
- Sample "docker-compose.yml" file: 

```
version: "3.8"

services:
  mydatabase:
    image: mysql:5.7
    restart: always
    volumes: 
      - mydata:/var/lib/mysql
    environment: 
      MYSQL_ROOT_PASSWORD: somewordpress
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress
    networks:
      - mynet
  mywordpress:
    image: wordpress:latest
    depends_on: 
      - mydatabase
    restart: always
    ports:
      - "80:80"
      - "443:443"
    environment: 
      WORDPRESS_DB_HOST: mydatabase:3306
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress
    networks:
      - mynet
volumes:
  mydata: {}
networks:
  mynet:
    driver: bridge
```

- After saving file as "docker-compose.yml", run following commands where docker-compose file is, to create containers, volumes, networks:
```
docker-compose up -d
docker-compose down
```
Goto: [App: Docker Compose and Creating WordPress Container depends on MySql Container]()

### Docker Swarm  <a name="swarm"></a>

One of the Container Orchestration tool: 
- Automating and scheduling the 
    - deployment, 
    - management, 
    - scaling, and
    - networking of containers
- Container Orchestration tools:
    - Docker Swarm,
    - Kubernetes,
    - Mesos

![image](https://user-images.githubusercontent.com/10358317/113186661-3b06a280-9258-11eb-9bb8-3ad38d3c55fb.png)

### Docker Stack  <a name="stack"></a>
- With Docker Stack, multiple services can be created with one-file.
- It is like Docker-Compose file but it has more features than Docker-compose file: update_config, replicas.
- But it is running on when Docker Swarm mode is activated.
- Network must be overlay.

```
docker service create --name testservice --replicas=5 -p 8080:80 nginx
docker service ps testservice
docker service scale testservice=10
docker service inspect testservice
```

![image](https://user-images.githubusercontent.com/10358317/113303356-4a8df600-9301-11eb-9114-38872ca01f29.png)

Goto: [App: Docker Swarm using PlayWithDocker, Creating Swarm Cluster: 3 x WordPress Containers and 1 x MySql Container]()

## Play With Docker  <a name="playWithDocker"></a>

![image](https://user-images.githubusercontent.com/10358317/113187037-ae101900-9258-11eb-9789-781ca2f6a464.png)

## Docker Commands Cheatsheet <a name="cheatsheet"></a>

Goto: [Docker Commands Cheatsheet](https://github.com/omerbsezer/Fast-Docker/blob/main/DockerCommandCheatSheet.md)

## References  <a name="references"></a>
- [Docker.com](https://www.docker.com/)
- [Infoworld](https://www.infoworld.com/article/3310941/why-you-should-use-docker-and-containers.html)
- [ItNext](https://itnext.io/getting-started-with-docker-facts-you-should-know-d000e5815598)
