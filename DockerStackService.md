## App: Docker Swarm using PlayWithDocker, Creating Swarm Cluster: 3 x WordPress Containers and 1 x MySql Container

This scenario shows how to run multi-containers in the cluster using the Docker Stack file by creating a service in Docker Swarm. It goes following:
- Creating Docker Swarm Cluster (2 Manager Nodes, 3 Worker Nodes) using [PlayWithDocker](https://labs.play-with-docker.com/)
- Copying docker-compose.yml file into the Manager node to create Docker Service
- Creating Docker Service and showing the service's details
- Going to one of the Worker Node, stepping into the container, showing the connection using ping.
- Removing one of the containers in the Worker Node and showing the recreation by Docker Service.
- Stopping and removing all containers in the Docker Service.

#### Note
```
In server, these ports should be opened: (These ports are opened in PlayWithDocker, not needed to open ports)
- TCP port 2377 (Cluster management)
- TCP - UDP port 7946 (Communication between nodes)
- UDP port 4789 (Overlay network) 
```

### Step

- Go to [PlayWithDocker](https://labs.play-with-docker.com/) and login (you have to DockerHub user)
- Create 5 x Instances
- Initialize Docker Swarm: (Copy-KeyCombination: CTRL+Insert, Paste-KeyCombination: Shift+Insert)

```
docker swarm init --advertise-addr [ManagerNodeIP]
docker swarm init --advertise-addr 192.168.0.18 
```

![image](https://user-images.githubusercontent.com/10358317/113690887-2d27a600-96cc-11eb-8431-0fb89ee1fdfb.png)


- Paste command which appears after init. Swarm Cluster into 3 Instances:
```
docker swarm join --token SWMTKN-1-1cfvch2ygu5h0ga357dte1i53ukbigei8qd0uyw93gcegogb3z-eebewiqny6obn9vcoxmdb4moq 192.168.0.18:2377
```
![image](https://user-images.githubusercontent.com/10358317/113691250-855ea800-96cc-11eb-8016-52074a201272.png)

- Run on the terminal to add second Manager Node into Swarm Cluster:
```
docker swarm join-token manager
```
- Paste command which appears after join-token manager command into the remained instance: 
```
Example token (it will be different in different session)
docker swarm join --token SWMTKN-1-23a47kkzf1hp8j7a51tx0fsc4hj1tprqi3kx04zfm0djf8ozr4-eqcsf6huttmugjf4yu4yoyrxd 192.168.0.13:2377
```
- Run on the terminal to show cluster (Manager:2, Worker:3):
```
docker node ls
```
![image](https://user-images.githubusercontent.com/10358317/113691538-cf478e00-96cc-11eb-9d67-4a80509b7082.png)

- Copy the following "docker-compose.yml" content:
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
    deploy:
      replicas: 3
      update_config:
        parallelism: 2
        delay: 5s
        order: stop-first
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
  mydata:

networks:
  mynet:
    driver: overlay
```

- On the leader Manager Node, create "docker-compose.yml" file, paste the content using "Shift+Insert":

```
cat > docker-compose.yml
(After pasting the content of the Docker-compose.yml, press "Enter" and "CTRL+D" to save the file and click "Editor" to see the content of the docker-compose.yml)
```

![image](https://user-images.githubusercontent.com/10358317/113691837-2f3e3480-96cd-11eb-8463-0bf9bae8ec50.png)


- Start Docker Service using docker-compose.yml file:
```
docker stack deploy --compose-file docker-compose.yml firststack
```

![image](https://user-images.githubusercontent.com/10358317/113692058-6ca2c200-96cd-11eb-8a6c-6e7db4932b20.png)

- "firststack" service is started and 3 x WordPress containers are created and 1 x MySql container is created. Click "80" port to see "WordPress" Container Service:

![image](https://user-images.githubusercontent.com/10358317/113692398-cd31ff00-96cd-11eb-8469-acd0697c5e1f.png)

![image](https://user-images.githubusercontent.com/10358317/113692502-e3d85600-96cd-11eb-8984-0b4a08b0df83.png)


- Run on the terminal to see details of stack: 
```
docker stack ls 
```
![image](https://user-images.githubusercontent.com/10358317/113692693-15512180-96ce-11eb-835d-f8c6a96bcda7.png)

- Run on the terminal to see containers: 
```
docker stack services firststack
```
![image](https://user-images.githubusercontent.com/10358317/113693036-724cd780-96ce-11eb-925e-0e0736e96cdd.png)

- Run on the terminal to see on which nodes which containers run: 
```
docker stack ps firststack
```
![image](https://user-images.githubusercontent.com/10358317/113693389-d8395f00-96ce-11eb-85e3-13c3334b7eac.png)

- Go to Node5 and run on the terminal to see the running container, connected network and networks' details:
```
docker container ls -a
docker network ls 
docker network inspect firststack_mynet
```
![image](https://user-images.githubusercontent.com/10358317/113694959-a45f3900-96d0-11eb-95f5-8e79cbdafcf8.png)

- Run on the terminal to enter into container:
```
docker exec -it [containerID] sh
docker exec -it aeb sh 
docker container exec -it aeb sh
```

- Run on the terminal to update, install net-tools (ifconfig), iputils-ping (ping) and to see the Ethernet interfaces (ifconfig) and connection of other containers (ping):
```
apt-get update
apt-get install net-tools
apt-get install iputils-ping -y
ifconfig
ping 10.0.1.2
ping 10.0.1.3
```
![image](https://user-images.githubusercontent.com/10358317/113695846-9d84f600-96d1-11eb-8ff5-a65188ea4bb5.png)

- Go to Node5 and stop containers which are running on Node5 twice times:
```
docker container ls -a
docker container stop aeb
docker container ls -a (after stopping container, automatically created by docker service using docker-compose.yml)
docker container ls b7f
docker container ls -a
```
![image](https://user-images.githubusercontent.com/10358317/113697092-0c168380-96d3-11eb-99f7-f4db1ea846e9.png)

- Go to Node1 (ManagerNode) to see docker containers' status. On Node5, the 'WordPress' container is stopped and created twice times. This works with Docker Service using docker-compose.yml:
```
docker stack ps firststack
```
![image](https://user-images.githubusercontent.com/10358317/113697229-35cfaa80-96d3-11eb-922d-19d2bf0bb2f4.png)

- Run on the terminal to stop and remove containers in Docker Service:
```
docker stack rm firststack
docker stack ps firststack
```
![image](https://user-images.githubusercontent.com/10358317/113697847-0ff6d580-96d4-11eb-870e-aaa1059ffe37.png)

