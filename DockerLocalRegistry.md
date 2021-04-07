## App: Running Docker Free Local Registry, Tagging Container, Pushing to Local Registry, Pulling From Local Registry

This scenario shows how to run Docker local free registry, to tag container, to push into local registry and to pull from registry.

### Steps
- Pull 'Registry' image from Docker Hub:
```
docker image pull registry
```
![image](https://user-images.githubusercontent.com/10358317/113844384-b5717e00-9794-11eb-8b17-13e14fc2cac7.png)

- Run container using 'Registry' image: (-p: port binding [hostPort]:[containerPort], -d: detach mode (running background))
```
docker container run -d -p 5000:5000 --restart always --name localregistry registry
```
![image](https://user-images.githubusercontent.com/10358317/113844611-f49fcf00-9794-11eb-94a1-9e6a899ef118.png)

- Open browser: (localregistry runs on 127.0.0.1:5000)
```
http://127.0.0.1:5000/v2/_catalog
```
![image](https://user-images.githubusercontent.com/10358317/113844968-4f392b00-9795-11eb-8c17-8639d518e1af.png)

- To push image to localregistry, firstly change the name of image using 'tag', add '127.0.0.1:5000/' as prefix of the image to push localregistry:
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

