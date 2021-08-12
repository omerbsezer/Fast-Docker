## App: Creating Docker Container to Build C++ on Ubuntu18.04

- In this scenario, we'll create Docker file from scratch that includes Cmake, Git, Python3, Conan, Gcc.
- Create Dockerfile that includes following content: 

```
FROM ubuntu:18.04
WORKDIR /home/project

# Install general dependencies, update, net-tools, iputils-ping, etc.
RUN apt-get update -y && apt-get install net-tools -y && apt-get install iputils-ping -y &&\
	apt-get install python3-distutils -y &&  apt-get install python3-apt -y &&\
	apt-get install sudo wget vim nano -y  
	

# Install python3, pip3, conan, git 
RUN apt-get install -y curl python3.7 python3.7-dev python3.7-distutils &&\
    update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1 &&\
	update-alternatives --set python /usr/bin/python3.7 &&\
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py &&\
	python3.7 get-pip.py &&\
	pip3 install conan &&\
	apt-get install git -y

# Install gcc8
RUN apt install software-properties-common -y &&\
    add-apt-repository ppa:ubuntu-toolchain-r/test -y &&\
	apt install gcc-7 g++-7 gcc-8 g++-8 gcc-9 g++-9 -y &&\
	update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 90 --slave /usr/bin/g++ g++ /usr/bin/g++-9 --slave /usr/bin/gcov gcov /usr/bin/gcov-9 &&\
	update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 80 --slave /usr/bin/g++ g++ /usr/bin/g++-8 --slave /usr/bin/gcov gcov /usr/bin/gcov-8 &&\
	update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 70 --slave /usr/bin/g++ g++ /usr/bin/g++-7 --slave /usr/bin/gcov gcov /usr/bin/gcov-7
   
# Install cmake3.20 
RUN apt-get update &&\
    wget https://github.com/Kitware/CMake/releases/download/v3.20.5/cmake-3.20.5.tar.gz &&\
	tar zxvf cmake-3.20.5.tar.gz &&\
	cd cmake-3.20.5 &&\
	./bootstrap &&\
	make -j4 &&\
	make install &&\
	cmake --version &&\
	cd ..

# Config Conan
RUN pip install conan --upgrade &&\
	conan profile new default --detect &&\
	conan profile show default &&\
	conan profile update settings.compiler=gcc default &&\
	conan profile update settings.compiler.version=8 default &&\
	conan profile update settings.compiler.libcxx=libstdc++11 default &&\
	conan profile update settings.build_type=RelWithDebInfo default &&\
	conan remote list

# Container starts with Bash
CMD bash
```

- Create directory on your C: (e.g. C:\Linux-Project), this directory is used for sharing file between container and host PC.

- Run following command to create Ubuntu environment, it creates 'build-env-ubuntu18' Docker image: 

```
docker image build -t build-env-ubuntu18 .
```

- Run following command to create container from 'build-env-ubuntu18' image, bind mount to 'C:\Linux-Project' directory. Create directory before run: C:\Linux-Project. Copy the project into the C:\Linux-Project.

```
docker container run -it --name con-linux -v C:\Linux-Project:/home/project build-env-ubuntu18 /bin/bash
```

- Go to your to build project (-S: source project path, -B: build project path)

```
cd ProjectName/source
sudo cmake -S /home/project/ProjectName/source -B /home/project/ProjectName/build 
```

- Then go to the build:
```
cd ..
cd build
make -j4
```





