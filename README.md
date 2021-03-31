# Fast-Docker
This repo aims to cover Docker details (Dockerfile, Image, Container, Commands, Volumes, Docker-Compose, Networks, Swarm, Stack), example usage in a nutshell.

**Keywords:** Docker Image, Dockerfile, Containerization, Docker-Compose File, Swarm

**NOTE: This tutorial is only for education purpose. All related references are listed at the end of the file.**

# Table of Contents
- [Motivation](#motivation)
    - [Needs](#needs)
    - [Benefits](#benefits)
- [What is Docker](#whatIsDocker)
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
Why shoul we use Docker?

### Needs <a name="needs"></a>
- Installing all dependencies, setting up new environment for SWs (time consuming every time to install environment for testing ) 
    - e.g. TDFNext Hw Service, EthSec, Xpad code on Linux/Win
- We want to run our apps on different platforms (Ubuntu, Windows, Raspberry Pi).
    - Question in our mind: What if, it does not run on a different OS?
- CI/CD Integration Testing: We can handle unit testing, component testing with Jenkins. Integration Testing? 
    - It could be possible to encounter complex problems because of the lacking integration testing. We can avoid it with automatic integration testing (Extending Chain: Jenkins-Docker Image-Container-Automatic testing).  
- Are our SW products portable to carry on different PC easily? (especially in development & testing phase)
- Microservice Architecture

### Benefits <a name="benefits"></a>

- NOT needed to install dependencies/SWs again & again
- Enables to run on different OS, different platforms
- Enables consistent environment
- Easy to use and maintain
- Efficient use of the system resources
- Isolate SW components
- Enable Automatic Integration Testing (CI/CD)
- Containers give us instant application portability.
- Enables developers to easily pack, ship, and run any application as a lightweight, portable, self-sufficient container

## What is Docker  <a name="whatIsDocker"></a>
- Docker is a tool that reduces the gap between Development/Deployment phase of a software development cycle.
- Docker is like VM but it has more features than VMs (no kernel, only small app and file systems, portable)
    - On Linux Kernel (2000s) two features are added (these features support Docker):
        - Namespaces: Isolate process.
        - Control Groups: Resource usage (CPU, Memory) isolation and limitation for each process. 
- Without Docker, each VM consumes 30% resources (Memory, CPU)

![image](https://user-images.githubusercontent.com/10358317/113183089-ef51fa00-9253-11eb-9ade-771905ce8ebd.png)

### Architecture  <a name="architecture"></a>

![image](https://user-images.githubusercontent.com/10358317/113183210-0db7f580-9254-11eb-9716-0de635f3cbdf.png)


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

- docker ManagementCommand Command 

![image](https://user-images.githubusercontent.com/10358317/113183615-81f29900-9254-11eb-8695-360680931866.png)

![image](https://user-images.githubusercontent.com/10358317/113183721-9fbffe00-9254-11eb-9841-79bf037db34a.png)

### Docker Container  <a name="container"></a>

![image](https://user-images.githubusercontent.com/10358317/113183556-730be680-9254-11eb-8bdd-84c5cf5b86c6.png)

- When we create the container from image, in every container, there is an application that is set to run by default app. 
    - When this app runs, container runs.
    - When this default app finished/stopped, container stopped. 
- There could be more than one app in docker image (such as: sh, ls, basic commands)
- When the Docker container is started, it is allowed that a single application is configured to run automatically

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

### Docker Stack  <a name="stack"></a>

## Play With Docker  <a name="playWithDocker"></a>

## Usage Scenarios  <a name="scenario"></a>

## Docker Commands Cheatsheet <a name="cheatsheet"></a>

## References  <a name="references"></a>
   
