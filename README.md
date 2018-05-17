# Path Agile Development

## Setup on the Pi
All the files needed to make the pi ready for use are located in the ```/other``` folder.

Here you can find multiple ```.wav``` files which are used as the sounds the pi can make based on certain actions. Next to that you can find the ```start-bluetooth-server.sh``` file which is used for turning the bluetooth server on. Also the ```set-audio-to-full.sh``` for turning the audio to 100% in the pi.

There are also two python files. One is for the rfcomm server and the other one is for the gyroscope.

### Steps

- git clone or download to ```/home/pi/Workspace/path-agile-development```.
- Place the following lines in the ```/etc/rc.local``` file.
    - 
    
That is it. The pi is now ready to use with the android app.