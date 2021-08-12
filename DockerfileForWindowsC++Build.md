## App: Creating Docker Container using Dockerfile to Build C++ on Windows with Visual Studio Compiler

- In this scenario, we'll create Docker file from scratch that includes Visual Studio Compiler (VS2019Community), Python, Choco, Conan, Cmake, Git.
- Please in your PC, release minimum 20GB-25GB of diskspace (because base image of Win-Server-Core with .Net is ~12GB). 
- Switch to your Docker Desktop to Windows Containers
- Create Dockerfile that includes following content: 

```
# escape=`

# Use the latest Windows Server Core image with .NET Framework 4.8. for Visual Studio
FROM mcr.microsoft.com/dotnet/framework/sdk:4.8-windowsservercore-ltsc2019

ENV VS160COMNTOOLS C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\Tools

WORKDIR C:\init

# Restore the default Windows shell for correct batch processing.
SHELL ["cmd", "/S", "/C"]

# install choco (win package manager like apt-get)
RUN @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

# install python3.9
RUN choco install -y python3 `
    && set PATH=%PATH%;C:\Python39\

# install VS2019 community for compiler
RUN choco install -y visualstudio2019community 

# install conan
RUN pip3 install conan

# config conan
RUN conan profile new default --detect `
    && conan profile show default `
	&& conan profile update settings.build_type=RelWithDebInfo default `
	&& conan remote list

# install cmake
RUN choco install cmake -y `
    && set PATH=%PATH%;C:\Program Files\CMake\bin\
    
# install git    
RUN choco install git -y `
    && set PATH=%PATH%;C:\Program Files\Git\bin\
    
# run.bat includes visualstudio2019-workload-nativedesktop, cmake, msbuild 
COPY run.bat .

# start run.bat when container started
CMD C:\init\run.bat && cmd.exe
```

- Before building image, create "run.bat" file to continue to install remaining part and configuration, it also starts building solution:

```
@ECHO OFF

ECHO Starting installation of the visualstudio2019-workload-nativedesktop!
choco install -y visualstudio2019-workload-nativedesktop
ECHO Congratulations! visualstudio2019-workload-nativedesktop was installed successfully.

set PATH=%PATH%;C:\Program Files\CMake\bin\
ECHO Cmake added into Path!

cmake -S C:\Project\ProjectName\source -B C:\Project\ProjectName\build
ECHO Project .sln file created!

cd C:\Project\ProjectName\build
"C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Current\Bin\msbuild.exe" projectName.sln /property:Configuration=RelWithDebInfo
ECHO Project builded!
```

- Create directory on your C: (e.g. C:\Win-Project), this directory is used for sharing file between container and host PC.

- Run following command to create Windows environment, it creates 'build-env-windows' Docker image: 

```
docker image build -t build-env-windows -m 2GB .
```

- Run following command to create container from 'build-env-windows' image, bind mount to 'C:\Win-Project' directory. Create directory before run: C:\Win-Project. Copy the project into the C:\Win-Project.

```
docker container run -it --name con-win -v C:\Win-Project:C:\Project build-env-windows
```
