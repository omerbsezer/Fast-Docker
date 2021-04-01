## App2: Binding Volume to the Different Containers

This scenario shows the Docker Volume functionality. 
- Firstly, new volume "test" will be created and binded to the nginx container directory ("mywebserver"). Content will be synchronized.
- Files content ("index.html") will be changed after entering into the container. 
- First container ("mywebserver") will be stopped and removed. Volume ("test") still remains.
- Second container ("mywebserver2") will be created without binding volume to show default page. Second container will be stopped and removed.
- Third container ("mywebserver3") will be created with binding "test" volume. Content of container and volume ("test") will be synchronized. 

Steps: 

- Create directory (“Webpage”) on your Desktop.
- Create file ("index.html" in "Webpage" directory) which contains following:
```
<center>
<h1>Welcome to My Web Site</h1>
</center>
```
- Open terminal and run:
```
docker volume create test
```
- Create a nginx container and bind to volume:
```
docker container run --name mywebserver -d -p 80:80 -v test:/usr/share/nginx/html nginx
```
-
