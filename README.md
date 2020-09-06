# avrcompile
This is used to launch a webserver that is capable of compiling the arduino ino files using rest api.

# Pre requisites
Install Python 3 and pip3 (This code was tested on Python 3.8.2)
on Ubuntu: 
```
apt install python3
apt install python3-pip
```
Install Flask (This code was tested on Flask 1.1.2)
```
pip3 install flask
```

# Usage
Clone the code and launch 
```
git clone https://github.com/suriyanath/avrcompile
cd avrcompile
chmod 777 Run.sh
./Run.sh
```
To run in background even on ssh exit use below command:
```
nohup ./Run.sh 2>1 &
```
Internally this Flask webserver uses arduino-cli from Arduino.


# READY to use DOCKER Image
```
docker run -d -it -p 5000:5000 suriyanath/ubuntucompiler:1.0 
```
Source: https://hub.docker.com/repository/docker/suriyanath/ubuntucompiler
