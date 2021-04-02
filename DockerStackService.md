## App: Docker Swarm using PlayWithDocker, Creating Swarm Cluster: 3 x WordPress Containers and 1 x MySql Container

This scenario shows how to run multi-containers in cluster using Docker Stack file by creating service in Docker Swarm. It goes following:
- Creating Docker Swarm Cluster (2 Manager Nodes, 3 Worker Nodes) using [PlayWithDocker](https://labs.play-with-docker.com/)
- Copying docker-compose.yml file into the Manager node to create Docker Service
- Creating Docker Service and showing the service's details
- Going to one of the Worker Node, stepping into the container, showing the connection using ping.
- Removing one of the container in the Worker Node and showing the recreation by Docker Service
-
- Scaling the Docker Service
- Updating all containers using Docker Service 

### Step

- Go to [PlayWithDocker](https://labs.play-with-docker.com/) and login (you have to DockerHub user)
- Create 5 x Instances

![image](https://user-images.githubusercontent.com/10358317/113414275-edf01100-93bc-11eb-92cb-c64b63882ea9.png)

- Initialize Docker Swarm: (Copy-KeyCombination: CTRL+Insert, Paste-KeyCombination: Shift+Insert)
```
docker swarm init --advertise-addr [ManagerNodeIP]
docker swarm init --advertise-addr 192.168.0.13 
```
![image](https://user-images.githubusercontent.com/10358317/113414610-aae26d80-93bd-11eb-8358-a4790583b3b5.png)

- Paste command which appears after init. Swarm Cluster into 3 Instances:
```
docker swarm join --token SWMTKN-1-23a47kkzf1hp8j7a51tx0fsc4hj1tprqi3kx04zfm0djf8ozr4-b1hlyzy46syd04n5e8qdtdjlz 192.168.0.13:2377
```
![image](https://user-images.githubusercontent.com/10358317/113415691-0ada1380-93c0-11eb-8f1d-11da8c29eab2.png)

- Run terminal to add second Manager Node into Swarm Cluster:
```
docker swarm join-token manager
```
- Paste command which appears after join-token manager command into remained instance: 
```
Example token (it will be different in different session)
docker swarm join --token SWMTKN-1-23a47kkzf1hp8j7a51tx0fsc4hj1tprqi3kx04zfm0djf8ozr4-eqcsf6huttmugjf4yu4yoyrxd 192.168.0.13:2377
```
- Run on terminal to show cluster (Manager:2, Worker:3):
```
docker node ls
```
![image](https://user-images.githubusercontent.com/10358317/113415443-8091af80-93bf-11eb-8454-a2f3341d81a0.png)

- Copy 


