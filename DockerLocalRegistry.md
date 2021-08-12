## App: Running Docker Free Local Registry, Tagging Container, Pushing to Local Registry, Pulling From Local Registry

This scenario shows how to run Docker local free registry, tag container, push into the local registry and pull from the registry.

### Steps
- Pull 'Registry' image from Docker Hub:
```
docker image pull registry
```
![image](https://user-images.githubusercontent.com/10358317/113844384-b5717e00-9794-11eb-8b17-13e14fc2cac7.png)

- Run container using 'Registry' image: (-p: port binding [hostPort]:[containerPort], -d: detach mode (running background), -e: change environment variables status)
```
docker container run -d -p 5000:5000 --restart always --name localregistry -e REGISTRY_STORAGE_DELETE_ENABLED=true registry
```

![image](https://user-images.githubusercontent.com/10358317/113854337-0e461400-979f-11eb-9d33-b0eddc9b479f.png)

- Run registry container with binding mount (-v) and without getting error 500 (REGISTRY_VALIDATION_DISABLED=true):
```
docker run -d -p 5000:5000 --restart=always --name registry -v /home/docker_registry:/var/lib/registry -e REGISTRY_STORAGE_DELETE_ENABLED=true -e REGISTRY_VALIDATION_DISABLED=true -e REGISTRY_HTTP_ADDR=0.0.0.0:5000 registry:2
```

- Open a browser: (localregistry runs on 127.0.0.1:5000)
```
http://127.0.0.1:5000/v2/_catalog
```
![image](https://user-images.githubusercontent.com/10358317/113844968-4f392b00-9795-11eb-8c17-8639d518e1af.png)

- To push the image to localregistry, firstly change the name of the image using 'tag', add '127.0.0.1:5000/' as a prefix of the image to push localregistry:
```
docker image tag [sourceImageName] [targetImageName]
```
```
docker image tag alpine 127.0.0.1:5000/alpine:latest (pushing alpine image)
docker image push 127.0.0.1:5000/alpine:latest
```
```
docker image tag busybox 127.0.0.1:5000/busybox:latest
docker image push 127.0.0.1:5000/busybox:latest
```
![image](https://user-images.githubusercontent.com/10358317/113845465-d6869e80-9795-11eb-8c8a-4bab2261e153.png)

- Refresh the browser to see latest status:

![image](https://user-images.githubusercontent.com/10358317/113846436-bf947c00-9796-11eb-8527-d7a0799b3359.png)

- To download from localregistry:
```
docker image pull [imageName]
docker image pull 127.0.0.1:5000/busybox:latest
```

![image](https://user-images.githubusercontent.com/10358317/113855031-d7bcc900-979f-11eb-9610-03d21ab12dd0.png)

- There are different ways of deleting images from localregistry: 
  - using curl DELETE,  (https://betterprogramming.pub/cleanup-your-docker-registry-ef0527673e3a)
  - removing the file from the filesystem,
  - running rm command in the container (I prefer this method, it absolutely works):
  
```
docker exec -it localregistry rm -rf /var/lib/registry/docker/registry/v2/repositories/alpine
docker exec -it localregistry rm -rf /var/lib/registry/docker/registry/v2/repositories/busybox
```
![image](https://user-images.githubusercontent.com/10358317/113854846-a04e1c80-979f-11eb-988d-454cabc91bbe.png)

- After deletion, as expected, when trying pulling image from localregistry, it is not found:

![image](https://user-images.githubusercontent.com/10358317/113855229-16eb1a00-97a0-11eb-93f8-6911557ac502.png)

![image](https://user-images.githubusercontent.com/10358317/113855252-20748200-97a0-11eb-952b-df5efc69eea8.png)

- Docker registy stores both Windows and Linux Container at the same time:
```
docker run -d -p 5000:5000 --restart=always --name registry -v /home/docker_registry:/var/lib/registry -e REGISTRY_STORAGE_DELETE_ENABLED=true -e REGISTRY_VALIDATION_DISABLED=true -e REGISTRY_HTTP_ADDR=0.0.0.0:5000 registry:2
```
- Switch Docker Desktop to Windows Container
- Please add  "IP:5000" in your Docker Desktop (Settings>Docker Engine>"insecure-registries")
- Tagging Image: 
```
docker tag mcr.microsoft.com/windows/nanoserver:1909 {IPofRegistryServer}:5000/windows-nanoserver
```
- Pushing Image: 
```
docker push {IPofRegistryServer}:5000/windows-nanoserver
```
- Browsing: IP:5000/v2/_catalog

![image](https://user-images.githubusercontent.com/10358317/129181056-7a0040ac-cc08-4298-a38d-49c1f0c8d355.png)
