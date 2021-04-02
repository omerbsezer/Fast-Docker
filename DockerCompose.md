## App: Docker Compose and Creating WordPress Container Depends on MySql Container

This scenario shows how to run multiple Docker containers using docker-compose.yml file. 
After running containers, it is shown how: 
- to step (enter) into container, 
- to install binary packages into container, 
- to see ethernet interfaces
- to send ping packet to see the connection of the containers.

### Steps
- Create "example" directory on your Desktop.
- Create "docker-compose.yml" in "example" directory.
- Copy below and paste into "docker-compose.yml" (2 containers are created namely: mydatabase, mywordpress. mydata is volume object that binds to container, environment variables are basically defined, new bridge network is created) 
(Normally, credentials are not defined this way, just example. Docker secret is used to define credentials, safety way)

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

- Open terminal where "docker-compose.yml" is. Run following command:
```
docker-compose up -d
```
![image](https://user-images.githubusercontent.com/10358317/113313590-ae1d2100-930b-11eb-965b-f8638cef16b6.png)

- Run on terminal to see list of containers: 
```
docker container ls -a
```
![image](https://user-images.githubusercontent.com/10358317/113410555-00198180-93b4-11eb-8784-8b561b5afb21.png)


- Open Browser (127.0.0.1) to see result:

![image](https://user-images.githubusercontent.com/10358317/113315210-58e20f00-930d-11eb-972e-67c6885404bb.png)

- If you want, you can enter one of the containers and ping to another container to see the connection between both containers. They are connected to each other via bridge "mynet".
- Run on terminal to see list of containers: 
```
docker container ls -a
```
- You can see the names of the containers. You should create “docker-compose.yml” under “example” directory. Docker-compose creates containers and adds names according to path (without using docker-compose, if user does not enter name for container, docker assigns random name to the container). For example, your container names are "example_mywordpress_1", "example_mydatabase_1". Container name is important when you want to enter the container (like below).
- Run on terminal to step into container:
```
docker exec -it example_mywordpress_1 sh
```
- Now you are in the container if you see "#". When you run "ifconfig" and "ping", these binaries are not found in the container. But we can update and install these binaries into this container.
- Run on terminal to update OS in the container:
```
apt-get update
```
- Run on terminal to install net-tools (ifconfig) in the container:
```
apt-get install net-tools
```
- Run on terminal to install iputils-ping (ping) in the container:
```
apt-get install iputils-ping
```
![image](https://user-images.githubusercontent.com/10358317/113315939-1cfb7980-930e-11eb-8996-f7f23ae87781.png)

- Run on terminal to see the IP of current container. It could be "172.19.0.3":
```
ifconfig
```
- Run on terminal to send ping to another container (“example_mydatabase_1”):
```
ping 172.19.0.2
```
![image](https://user-images.githubusercontent.com/10358317/113315708-dad23800-930d-11eb-97a3-4bee7ab1fed1.png)

- Press CTRL+C to stop ping.
- Press CTRL+P+Q to go out of the container to host terminal.
- Run on terminal to stop and remove containers:
```
docker-compose down
```
![image](https://user-images.githubusercontent.com/10358317/113316439-9f843900-930e-11eb-8e34-4fce7460eaae.png)

