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