## App: Binding Volume to the Different Containers

This scenario shows the Docker-Volume functionality. 
- Firstly, a new volume "test" will be created and connected to the Nginx container directory ("mywebserver"). Content will be synchronized.
- Files content ("index.html") will be changed after entering into the container. 
- First container ("mywebserver") will be stopped and removed. Volume ("test") still remains.
- Second container ("mywebserver2") will be created without binding volume to show the default page. The second container will be stopped and removed.
- Third container ("mywebserver3") will be created with binding "test" volume. Content of container and volume ("test") will be synchronized. 

### Steps: 

- Create a directory (“Webpage”) on your Desktop.
- Create a file ("index.html" in "Webpage" directory) that contains the following:

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
- Enter into the container:
```
docker container exec -it mywebserver sh
ls
```
- In the container, go to the content directory:
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
- Open a browser to see the result.
- Press "CTRL+P+Q" to go out from container to host.
- Remove the first container and be sure whether it is removed or not: 
```
docker container rm -f mywebserver
docker container ls -a
```
- Create an Nginx container without binding to the volume:
```
docker container run --name mywebserver2 -d -p 80:80 nginx
```
- Open the browser to see the result (default Nginx page)
- Remove the second container and be sure whether it is removed or not: 
```
docker container rm -f mywebserver2
docker container ls -a
```
- Create an Nginx container with binding to the volume:
```
docker container run --name mywebserver3 -d -p 80:80 -v test:/usr/share/nginx/html nginx
```
- Open the browser to see the result (volume syncs with the last container)
- Remove the third container and be sure whether it is removed or not: 
```
docker container rm -f mywebserver3
docker container ls -a
```

## App: Mount Binding to the Different Containers <a name="app_mount"></a>
- If you are using Docker Desktop Windows/Mac, go to Docker Desktop Configuration Settings from app /Resources/FileSharing, add your root directory  (e.g. C:/). 

![image](https://user-images.githubusercontent.com/10358317/113410473-bdf04000-93b3-11eb-82fd-e2bcd508bebe.png)

- Similar to the Docker-Volume object, but now the host PC's file path directory is used to bind the container's file path. Hence, while developing/testing your application, you can change the content instantly. When host directory content is updated, the container directory is also updated right away, and vice-versa.
- Create a directory (“Webpage”) on your Desktop.
- Create a file ("index.html" in "Webpage" directory) that contains the following:

```
<center>
<h1>Welcome to My Web Site</h1>
</center>
``` 
```
docker container run --name mywebserver -d -p 80:80 -v C:\Docker\Webpage:/usr/share/nginx/html nginx
```
- Open the browser to see the result (you will see the content of the host directory). Change the content of the host directory ('index.html') to see the changes.

![image](https://user-images.githubusercontent.com/10358317/114019691-005fc400-986f-11eb-9737-6e3f5659d6ef.png)

