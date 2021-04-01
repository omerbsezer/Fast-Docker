## App: Binding Volume to the Different Containers

This scenario shows the Docker Volume functionality. 
- Firstly, new volume "test" will be created and binded to the nginx container directory ("mywebserver"). Content will be synchronized.
- Files content ("index.html") will be changed after entering into the container. 
- First container ("mywebserver") will be stopped and removed. Volume ("test") still remains.
- Second container ("mywebserver2") will be created without binding volume to show default page. Second container will be stopped and removed.
- Third container ("mywebserver3") will be created with binding "test" volume. Content of container and volume ("test") will be synchronized. 

### Steps: 

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
- Create a nginx container and bind to volume (-d:detach/running on background, -p:port binding [hostPort]:[containerPort], -v: volume binding [volumeName]:[dockerDirectoryPath]):
```
docker container run --name mywebserver -d -p 80:80 -v test:/usr/share/nginx/html nginx
```
- Step into container:
```
docker container exec -it mywebserver sh
ls
```
- In the container, go to content directory:
```
cd /usr/share/nginx/html
ls
```
- To install "nano" application, update and install nano, in the following order:
```
apt-get update
apt-get install vim nano -y
```
- Open "index.html" and change "Welcome to My Web Site" to "Welcome to My Web Site, This is written using First Container"
```
nano index.html
```
- Open browser to see the result
- Press "CTRL+P+Q" to go out from container to host
- Remove first container and be sure whether it is removed or not: 
```
docker container rm -f mywebserver
docker container ls -a
```
- Create a nginx container without binding to the volume:
```
docker container run --name mywebserver2 -d -p 80:80 nginx
```
- Open browser to see the result (default nginx page)
- Remove second container and be sure whether it is removed or not: 
```
docker container rm -f mywebserver2
docker container ls -a
```
- Create a nginx container with binding to the volume:
```
docker container run --name mywebserver3 -d -p 80:80 -v test:/usr/share/nginx/html nginx
```
- Open browser to see the result (volume syncs with the last container)
- Remove third container and be sure whether it is removed or not: 
```
docker container rm -f mywebserver3
docker container ls -a
```

## App: Mount Binding to the Different Containers
- If you are using Docker Desktop Windows/Mac, go to Docker Desktop Configuration Settings from app /Resources/FileSharing, add your root directory  (e.g. C:/)
- Similar as a volume, but now host path directory is used.

```
docker container run --name mywebserver -d -p 80:80 -v C:\Docker\Webpage:/usr/share/nginx/html nginx
```
- Open browser to see the result (you will see the content of host directory)

