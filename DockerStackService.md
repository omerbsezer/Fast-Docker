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
