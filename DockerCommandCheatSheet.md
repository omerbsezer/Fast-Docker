## Docker Commands Cheatsheet

#### first try
```
docker run hello-world
docker info
docker version
docker --help
```
#### listing (ls=listing)
```
docker images ls
docker container ls -a
docker volume ls
docker network ls
docker container ps -a
docker ps
```
#### image pull from, push to registry
```
docker image pull alpine
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
```
docker container exec -it webserv sh
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
```
docker run -d -v hello:/hello --name c1 busybox
docker cp c1:/hello ./
```
#### container erasing (rm:remove, f:force, prune: delete all)
```
docker container prune
docker container rm -f 123
```
#### creating new bridge (network) (net=network)
```
docker network create bridge1
docker network inspect bridge1
docker container run -it -d --name webserver --net bridge1 omerbsezer/sample-web-php sh
docker container run -it -d --name webdb --net bridge1 omerbsezer/sample-web-mysql sh
docker network inspect bridge1
```
#### creating new bridge (custom subnet, mask and ip range) and connecting
```
docker network create --driver=bridge --subnet=10.10.0.0/16 --ip-range=10.10.10.0/24 --gateway=10.10.10.10 bridge2
docker network inspect bridge2
docker container run -dit --name webserver2 omerbsezer/sample-web-php
docker container run -dit --name webdb2 omerbsezer/sample-web-mysql
docker network connect bridge2 webserver2
docker network connect bridge2 webdb2
docker network inspect bridge2
```
#### image tagging and pushing
```
docker image tag mysql:5 test:latest
docker image push test:latest
```
#### image build (-t: tagging image name)
```
docker image build -t hello . (run this command where “Dockerfile” is)
(PS: image file name MUST be “Dockerfile”, no extension)
```
#### image save and load (t=tag, i=input, o=output)
```
docker save -o <path for created tar file> <image name>
docker save -o [imageName].tar [imageName]
docker load -i <path to docker image tar file>
docker load -i .\[imageName].tar
```
#### env, copy from container to host 
```
docker container run --net host [imageName]
ENV USER="space"
docker container run -d -d p 80:80 --name hd2 -e USER="UserName" [imageName]
docker cp host_path:/usr/src/app .
```
#### multistage image File ##
```
FROM mcr.microsoft.com/java/jdk:8-zulu-alpine AS compiler
COPY --from=compiler /usr/src/app . 
COPY --from=nginx:latest /usr/src/app .
```
#### using ARG (ARG=argument is only used while creating image, difference from ENV: env is reachable from container)
```
ARG VERSION
ADD https://www.python.org/ftp/python/${VERSION}/Python-${VERSION}.tgz .
docker image build -t x1 --build-arg VERSION=3.7.1 .
docker image build -t x1 --build-arg VERSION=3.8.1 .
```
#### creating Image from Container (-c: CMD)
```
docker commit con1 dockerUserName/con1:latest
docker commit -c 'CMD ["java","app"]' con1 dockerUserName/con1:second
docker image inspect dockerUserName/con1:secon
```
#### docker-compose commands (run this command where “docker-compose.yml” is)
```
docker-compose up -d
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
```
In server, these ports should be opened:
- TCP port 2377 (Cluster management)
- TCP - UDP port 7946 (Communication between nodes)
- UDP port 4789 (Overlay network) 
```
#### creating docker swarm: binding manager and worker nodes (test it with docker play with creating instances on docker play environment)
```
(PS1: To login PlayWithDocker, you must sign up Docker Hub to use PlayWithDocker)
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
```
(run these commands on manager nodes)
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
```
docker network create -d overlay over-net   (creating overlay network)
docker service create --name webserv --network over-net -p 8080:80 --replicas=3 omerbsezer/sample-web-php
docker service create --name db --network over-net omerbsezer/sample-web-mysql
```
#### update service, rollback (update containers)
```
docker service update --help
docker service update -d --update-delay 5s --update-parallelism 2 --image omerbsezer/sample-web-php:v2 websrv (when updating images with version2, updating from 2 parallel branches)
docker service ps websrv
docker service rollback -d websrv (rollback to last status of websrv)
```
#### secret (to work with secrets, swarm mode must be active)
```
notepad or nano username.txt (create username.txt that include username)
notepad or nano password.txt (create password.txt that include password) 
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
```
docker stack (to see stack help)
docker stack deploy -c docker-compose.yml firststack
docker stack ls 
docker stack services firststack
docker stack ps firststack
```
