#!/bin/bash

# enable bluetooth
sudo systemctl start bluetooth

sleep 1

# run the program bluez
echo -e 'power on\nconnect \t \nquit' | bluetoothctl

sleep 1

bluetoothctl power on

bluetoothctl discoverable on

sleep 2

sudo hciconfig hci0 leadv 0

# TODO: Don't forget to add the gyroscope and rfcomm-server in the local.rc file

touch /home/pi/Desktop/done
