# Path Agile Development

## Setup on the Pi
All the files needed to make the pi ready for use are located in the ```/other``` folder.

Here you can find multiple ```.wav``` files which are used as the sounds the pi can make based on certain actions. Next to that you can find the ```start-bluetooth-server.sh``` file which is used for turning the bluetooth server on. Also the ```set-audio-to-full.sh``` for turning the audio to 100% in the pi.

There are also two python files. One is for the rfcomm server and the other one is for the gyroscope.

### Steps

- git clone or download to ```/home/pi/Workspace/path-agile-development```.
- Place the following lines in the ```/etc/rc.local``` file.
    - sudo sh /home/pi/Workspace/path-agile-development/set-audio-to-full.sh
    - sudo sh /home/pi/Workspace/path-agile-development/start-bluetooth-server.sh 
    - sudo python /home/pi/Workspace/path-agile-development/gyrovibrate.py & 
    - sudo python /home/pi/Workspace/path-agile-development/rfcomm-server.py &

These files will now be exectuted once the pi starts up. 

## Andoid app
You can find the code for the andoird app in the MainActivity class. 

In the class you can find all the methods that relate to the implemntation of the bluetooth and the commands that are send to the rfcomm server.

For the bluetooth implementation the following library https://github.com/MacroYau/Blue2Serial.
We chose this library because it has clear documentation and not that difficult to implement and will save us time developing the app.
