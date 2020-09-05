# avrcompile
This is used to launch a webserver that is capable of compiling the arduino ino files using rest api.

# Pre requisites
Install Python 3 (This code was tested on Python 3.8.2)
Install Flask (This code was tested on Flask 1.1.2)

# Usage
Clone the code and launch "./Run.sh"
To run in background even on ssh exit use "nohup ./Run.sh 2>1 &"

Internally this Flask webserver uses arduino-cli from Arduino.
