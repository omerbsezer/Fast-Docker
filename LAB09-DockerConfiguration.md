## LAB-09: Docker Configuration (Proxy, Registry)

This scenario shows how to configure local PC Docker app for corporate proxy and pulling image from local registries.

### Proxy Configuration

#### Linux Configuration

- If the Docker PC is the behind the corporate proxy, proxy settings should be configured.
- No_proxy should be added if local registries (nexus, docker registry) are used.

```
sudo mkdir -p /etc/systemd/system/docker.service.d
cd /etc/systemd/system/docker.service.d/
sudo touch http-proxy.conf
sudo nano http-proxy.conf
```

- Proxy IP should be added:
```
# copy and paste in the file:
[Service] 
Environment="HTTP_PROXY=http://192.x.x.x:3128"
Environment="HTTPS_PROXY=http://192.x.x.x:3128"
Environment="NO_PROXY=localhost,192.168.1.0/16,<RegistryIPorDNS>" 
```

```
sudo systemctl daemon-reload
sudo systemctl restart docker
sudo systemctl show --property=Environment docker
```

#### Windows Configuration

- Powershell with admin rights:
```
[Environment]::SetEnvironmentVariable("HTTP_PROXY", "http://192.x.x.x:3128", [EnvironmentVariableTarget]::Machine)
[Environment]::SetEnvironmentVariable("HTTPS_PROXY", "http://192.x.x.x:3128", [EnvironmentVariableTarget]::Machine)
[Environment]::SetEnvironmentVariable("NO_PROXY", "192.168.*.*, *192.168.*.*,  172.24.*.*, 172.25.*.*, 10.*.*.*, localhost, 127.0.0.1, 0.0.0.0/8, <RegistryIPorDNS>", [EnvironmentVariableTarget]::Machine)
Restart-Service docker
```

### Registry Configuration

#### Linux Configuration
- Nexus or Docker Registry IP  should be added to "insecure-registries".

```
cd /etc/docker
sudo touch daemon.json
sudo nano daemon.json
# in the file, paste:
{
        "exec-opts": ["native.cgroupdriver=systemd"],
        "insecure-registries": ["192.x.x.x", "192.x.x.x:5000"],
        "dns": [ "192.x.x.x", "8.8.8.8" ]
}
sudo systemctl restart docker
```

#### Windows Configuration
- Create Daemon.json file is in the following directory: C:\ProgramData\docker\config\daemon.json

```
# daemon.json, copy and paste:
{ 
"insecure-registries": ["192.x.x.x:5000"],
"dns": [ "192.x.x.x", "8.8.8.8" ]
}
```

- Run to restart docker service:
```
Restart-Service -Name docker
```
