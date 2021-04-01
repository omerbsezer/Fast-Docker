# Fast-Docker
This repo aims to cover Docker details (Dockerfile, Image, Container, Commands, Volumes, Docker-Compose, Networks, Swarm, Stack), example usage in a nutshell.

**Keywords:** Docker Image, Dockerfile, Containerization, Docker-Compose File, Swarm

**NOTE: This tutorial is only for education purpose. All related references are listed at the end of the file.**

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
- [Usage Scenarios](#scenario)
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

![image](https://user-images.githubusercontent.com/10358317/113183089-ef51fa00-9253-11eb-9ade-771905ce8ebd.png)

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

![image](https://user-images.githubusercontent.com/10358317/113183406-45bf3880-9254-11eb-8d13-e68c83f3d349.png)

### Docker Registry and Docker Hub  <a name="registry"></a>

- https://hub.docker.com/

![image](https://user-images.githubusercontent.com/10358317/113183434-4eb00a00-9254-11eb-9275-9b1ccf705d5b.png)


### Docker Command Structure  <a name="command"></a>

- docker [ManagementCommand] [Command] 

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
docker container run nginx
```
[App1: Creating First Docker Image and Container using Docker File](https://github.com/omerbsezer/Fast-Docker/blob/main/FirstImageFirstContainer.md)

### Docker Container: Life Cycle

![image](https://user-images.githubusercontent.com/10358317/113186436-f67b0700-9257-11eb-9b2e-41ccf056e88b.png)

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

docker volume create volumeName

![image](https://user-images.githubusercontent.com/10358317/113184347-57eda680-9255-11eb-811c-9f55efd11deb.png)

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
- Default Network Driver: Bridge

![image](https://user-images.githubusercontent.com/10358317/113184949-1b6e7a80-9256-11eb-9a0c-fe5c62404a06.png)

#### Docker Network: Host
- Containers reach host network interfaces

![image](https://user-images.githubusercontent.com/10358317/113185061-43f67480-9256-11eb-9b94-83735ce980ce.png)

#### Docker Network: MacVlan
- Each Container have own MAC interface

![image](https://user-images.githubusercontent.com/10358317/113185105-52dd2700-9256-11eb-84f2-ef1880eb4f4c.png)

#### Docker Network: Overlay
- Containers which work on different PC/host, can work like same network

![image](https://user-images.githubusercontent.com/10358317/113185192-6e483200-9256-11eb-8cb4-d8aa170d1a1e.png)

### Docker Log  <a name="log"></a>

### Docker Stats/Memory-CPU Limitations  <a name="stats"></a>

### Docker File  <a name="file"></a>

![image](https://user-images.githubusercontent.com/10358317/113185932-54f3b580-9257-11eb-9f50-0d18512a0c40.png)



### Docker Image  <a name="image"></a>

![image](https://user-images.githubusercontent.com/10358317/113186047-748ade00-9257-11eb-9c1c-1604d53523e8.png)


### Docker Compose  <a name="compose"></a>

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

## Play With Docker  <a name="playWithDocker"></a>

![image](https://user-images.githubusercontent.com/10358317/113187037-ae101900-9258-11eb-9789-781ca2f6a464.png)


## Usage Scenarios  <a name="scenario"></a>

## Docker Commands Cheatsheet <a name="cheatsheet"></a>

#### first try
```docker run hello-world
docker info
docker version
docker --help
```

#### listing (ls=listing)
```docker images ls
docker container ls -a
docker volume ls
docker network ls
docker container ps -a
docker ps
```

#### image pull from, push to registry
```docker image pull alpine
docker image push alpine
```
#### creating and entering container (--name=name of new container, -it=interactive mode, sh=shell)
```
docker container run -it --name c1 omerbsezer/sample-java-app sh
```
#### start, stop container (30e=containerID)
```
docker container start 30e    
docker container stop 30e
```
#### entering container (8aa=containerID, webserv=containerName, sh=shell)
```docker container exec -it webserv sh
docker container run --name c1 -it busybox sh  #create and enter in 
docker exec -it 8aa sh
```

#### local registry running (d=detach mode, p:portBinding)
```
docker container run -d -p 5000:5000 --restart always --name localregistry registry
```

#### port binding, background running ## (d=detach mode, p:portBinding)
```
docker container run --name nginxcontainer -d -p 8080:80 nginx
```

#### volume (v:volume host:container)
```
docker container run --name ng2 -d -p 8080:80 -v test1:/usr/share/nginx/html nginx
```

#### copy container to host (cp:copy)
```
docker cp ng2:/test12 C:\Users\oesezer\Desktop\sampleBindMount
```

#### copying from volume, creating new temp. container
```docker run -d -v hello:/hello --name c1 busybox
docker cp c1:/hello ./
```
#### container erasing (rm:remove, f:force, prune: delete all)
```docker container prune
docker container rm -f 123
```
#### creating new bridge (network) (net=network)
```docker network create bridge1
docker network inspect bridge1
docker container run -it -d --name webserver --net bridge1 omerbsezer/sample-web-php sh
docker container run -it -d --name webdb --net bridge1 omerbsezer/sample-web-mysql sh
docker network inspect bridge1
```
#### creating new bridge (custom subnet, mask and ip range) and connecting
```docker network create --driver=bridge --subnet=10.10.0.0/16 --ip-range=10.10.10.0/24 --gateway=10.10.10.10 bridge2
docker network inspect bridge2
docker container run -dit --name webserver2 omerbsezer/sample-web-php
docker container run -dit --name webdb2 omerbsezer/sample-web-mysql
docker network connect bridge2 webserver2
docker network connect bridge2 webdb2
docker network inspect bridge2
```
#### image tagging and pushing
```docker image tag mysql:5 test:latest
docker image push test:latest
```
#### image build (-t: tagging image name)
```docker image build -t hello . (run this command where “Dockerfile” is)
(PS: image file name MUST be “Dockerfile”, no extension)
```
#### image save and load (t=tag, i=input, o=output)
```docker save -o <path for created tar file> <image name>
docker save -o merhaba.tar deneme/merhaba
docker load -i <path to docker image tar file>
docker load -i .\merhaba.tar
```
#### env, copy from container to host 
```docker container run --net host tdfnext/hwservice
ENV USER="space"
docker container run -d -d p 80:80 --name hd2 -e USER="Omer" hello-world
docker cp host_path:/usr/src/app .
```
#### multistage image File ##
```FROM mcr.microsoft.com/java/jdk:8-zulu-alpine AS compiler
COPY --from=compiler /usr/src/app . 
COPY --from=nginx:latest /usr/src/app .
```
#### using ARG (ARG=argument is only used while creating image, difference from ENV: env is reachable from container)
```ARG VERSION
ADD https://www.python.org/ftp/python/${VERSION}/Python-${VERSION}.tgz .
docker image build -t x1 --build-arg VERSION=3.7.1 .
docker image build -t x1 --build-arg VERSION=3.8.1 .
```
#### creating Image from Container (-c: CMD)
```docker commit con1 dockerUserName/con1:latest
docker commit -c 'CMD ["java","app"]' con1 dockerUserName/con1:second
docker image inspect dockerUserName/con1:secon
```
#### docker-compose commands (run this command where “docker-compose.yml” is)
```docker-compose up -d
docker-compose ps
docker container ls -a
docker-compose down  
docker-compose config
docker-compose images
docker-compose logs
docker-compose exec websrv ls -al
docker-compose build
```
#### docker swarm commmunication
```In server, these ports should be opened:
- TCP port 2377 (Cluster management)
- TCP - UDP port 7946 (Communication between nodes)
- UDP port 4789 (Overlay network) 
```
#### creating docker swarm: binding manager and worker nodes (test it with docker play with creating instances on docker play environment)
```(PS1: To login PlayWithDocker, you must sign up Docker Hub to use PlayWithDocker)
(PS2: On PlayWithDocker Paste: Shift+Insert, Copy: CTRL+Insert)
docker swarm init --advertise-addr 192.168.0.13 (after choosing manager node, run this command to initialize swarm, IP is the master node’s IP)
	
(after running command above, following writings appear on master PC to add worker PCs)
	Swarm initialized: current node (u4tqju429dcmggxmw29ll8nls) is now a manager.
	To add a worker to this swarm, run the following command:
docker swarm join --token SWMTKN-1 5qbi2uydkawpcuo9rcp4quytr37z1 pzob5ss66o821br09h7x9-3jrqc08scyetlxg9iyhck25u1 192.168.0.13:2377
To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.

(run following command on worker nodes)
docker swarm join --token SWMTKN-1 5qbi2uydkawpcuo9rcp4quytr37z1 pzob5ss66o821br09h7x9-3jrqc08scyetlxg9iyhck25u1 192.168.0.13:2377

(if you want to add more manager nodes to swarm cluster, run following command on manager PC to take manager token from master PC)
docker swarm join-token manager

(after running command above, following writings appear on master PC to add manager PCs)
	To add a manager to this swarm, run the following command:
docker swarm join --token SWMTKN-1 5qbi2uydkawpcuo9rcp4quytr37z 1pzob5ss66o821br09h7x9-3bv78968l9qdfza68979np715 192.168.0.13:2377
	This node joined a swarm as a manager

(run following command on manager nodes)
docker swarm join --token SWMTKN-1 5qbi2uydkawpcuo9rcp4quytr37z 1pzob5ss66o821br09h7x9-3bv78968l9qdfza68979np715 192.168.0.13:2377
```
#### list managers and workers on swarm
```
docker node ls 
```
#### docker service, ls
```(run these commands on manager nodes)
docker service (to see docker service help)
docker service create --name test --replicas=5 -p 8080:80 nginx 
docker service ps test (shows containers, which containers run on which PC)
docker service ls   (list service, shows service detail)
docker service logs test
docker service scale test=3   (desired state 3 replica)
docker service rm test
docker service create --name glb --mode=global nginx
```
#### create overlay network
```docker network create -d overlay over-net   (creating overlay network)
docker service create --name webserv --network over-net -p 8080:80 --replicas=3 omerbsezer/sample-web-php
docker service create --name db --network over-net omerbsezer/sample-web-mysql
```
#### update service, rollback (update containers)
```docker service update --help
docker service update -d --update-delay 5s --update-parallelism 2 --image omerbsezer/sample-web-php:v2 websrv (when updating images with version2, updating from 2 parallel branches)
docker service ps websrv
docker service rollback -d websrv (rollback to last status of websrv)
```
#### secret (to work with secrets, swarm mode must be active)
```notepad username.txt (create username.txt that include username)
notepad password.txt (create password.txt that include password) 
docker secret create username .\username.txt (create username secret object)
docker secret create password .\password.txt
docker secret inspect password
docker secret ls
docker service create -d --name secrettest --secret username --secret password omerbsezer/sample-web-php
docker service ps secrettest
docker ps
docker exec -it c4c sh
(when we are in the container, we can reach and see secrets at “/run/secrets”)
(when new password is needed, new password file must be created again)
echo "password222" | docker secret create password2
docker service update --secret-rm password --secret-add password2 secrettest (password is removed, new password2 object is added)
```
#### docker stack (stack is like compose, but run-on swarm)(deploy, replica, update-config definitions are added to define Docker Stack file)
```docker stack (to see stack help)
docker stack deploy -c docker-compose.yml firststack
docker stack ls 
docker stack services firststack
docker stack ps firststack
```

## References  <a name="references"></a>
- [Docker.com](https://www.docker.com/)
- [Infoworld](https://www.infoworld.com/article/3310941/why-you-should-use-docker-and-containers.html)
- [ItNext](https://itnext.io/getting-started-with-docker-facts-you-should-know-d000e5815598)
