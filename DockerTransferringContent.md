## App: Transferring Content between Host PC and Docker Container

This scenario shows how to transfer content between host and container:
- Copying content from host PC to container
  - Using image file (COPY command)
  - Using bind mount/volume
  - Using cp command into the running container
- Copying content from container to host PC
  - Using cp command from the running container
- Copying content from existed Docker Volume object to host PC
- Copying content from existed Docker Volume object to remote PC

### Copying content from host PC to container

#### Using image file (COPY command)
- Copying app content into the image using the image file (e.g. [FirstImageFirstContainer.md](https://github.com/omerbsezer/Fast-Docker/blob/main/FirstImageFirstContainer.md))
```
FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./index.py
```

#### Using bind mount/volume
- Binding mount and volume: e.g. [DockerVolume.md](https://github.com/omerbsezer/Fast-Docker/blob/main/DockerVolume.md)
- Using '-v [volumeName]:[containerDirectoryPath]' or '-v [hostDirectory]:[containerDirectoryPath]' 

```
docker volume create [volumeName]
docker volume create test
docker container run --name mywebserver3 -d -p 80:80 -v test:/usr/share/nginx/html nginx
docker container run --name mywebserver -d -p 80:80 -v C:\Docker\Webpage:/usr/share/nginx/html nginx
```

#### Using cp command into the running container

```
docker container run --name mywebserver -d -p 80:80 nginx
docker cp "C:\Docker\Webpage" mywebserver:/Webpage
docker cp [hostPath] [containerName]:[containerPath]
```
![image](https://user-images.githubusercontent.com/10358317/113862178-61709480-97a8-11eb-97bd-e7fa078168bb.png)

### Copying content from container to host PC

#### Using cp command from the running container

```
docker container run --name mywebserver -d -p 80:80 nginx
docker cp mywebserver:/usr/share/nginx/html "C:\Docker\Webpage2" 
docker cp [containerName]:[containerPath] [hostPath] 
```

### Copying content from existed Docker Volume object to host PC
- Create a temporary container that is connected to the volume
- Copy the content from container to host PC

```
docker volume create test
docker container run --name mywebserver -d -p 80:80 -v test:/usr/share/nginx/html nginx
docker container create --name temp1 -v test:/temp busybox ('temp1': temporary busybox container which is binded to 'test' volume )
docker cp temp1:/temp "C:\Docker\Webpage3" (copying from temporary container to host PC)
docker cp [containerName]:[containerPath] [hostPath] 
```

![image](https://user-images.githubusercontent.com/10358317/113866155-418f9f80-97ad-11eb-8831-3aad181c94bf.png)

### Copying content from existed Docker Volume object to remote PC
- Creatíng archive to standard output using smallest image 'busybox' (1.23MB)
- SSH to target host and extract files in destination container volume

```
(CONTAINER=myproject_db_1 REMOTE_HOST=newhost DIR=/var/lib/mysql; \
    docker run --rm \
    --volumes-from "$(docker inspect --format={{.Id}} $CONTAINER)" \
    busybox tar -czv --to-stdout $DIR  \
    | ssh $REMOTE_HOST docker run --rm -i \
    --volumes-from "\$(docker inspect --format={{.Id}} $CONTAINER)"\
    busybox tar -xzv \
    )
```
Details: https://medium.com/@bmihelac/copy-docker-container-data-volume-to-another-host-931568bda7fa
