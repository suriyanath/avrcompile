# avrcompile
This is used to launch a webserver that is capable of compiling the arduino ino files using rest api.

# Pre requisites
Install Python 3 and pip3 (This code was tested on Python 3.8.2)
on Ubuntu (for fedora based OS it will be with yum package manager): 
```
apt install python3
apt install python3-pip
```
Install Flask (This code was tested on Flask 1.1.2)
```
pip3 install flask
```

# Run Server
Clone the code and launch 
```
git clone https://github.com/suriyanath/avrcompile.git
cd avrcompile
chmod 777 Run.sh
./Run.sh
```
To run in background even on ssh exit use below command:
```
nohup ./Run.sh 2>1 &
```
Internally this Flask webserver uses arduino-cli from Arduino.

# Usage
Test URL:
```
GET : http://host:5000/test
```
Compiler usage:
```
POST: http://host:5000/ 
      BODY (form-data): key: board, value: uno | key: file, value: xxxx.ino
```

# READY to use DOCKER Image
```
docker run -d -it -p 5000:5000 suriyanath/ubuntucompiler:1.0 
```
Source: https://hub.docker.com/repository/docker/suriyanath/ubuntucompiler


# Launch the compiler server in a laptop without internet usage
```
nmcli device wifi hotspot con-name my-hotspot ssid my-hotspot band bg password secretpassword
```
Connect to the WIFI hotspot "my-hotspot" in android smartphone with password "secretpassword". Then use ifconfig command to find the ip address of wifi interface, in my case interface name is wlp7s0 and IP address is 10.42.0.1 as shown below,
```
wlp7s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.42.0.1  netmask 255.255.255.0  broadcast 10.42.0.255
        inet6 fe80::9201:4egf:fed2:912  prefixlen 64  scopeid 0x20<link>
        ether 90:00:4e:d2:07:13  txqueuelen 1000  (Ethernet)
        RX packets 472455  bytes 560402276 (560.4 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 241045  bytes 69396555 (69.3 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
Thus the host URL is - http://10.42.0.1:5000 
