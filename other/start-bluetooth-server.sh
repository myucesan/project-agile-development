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

# TODO: Add gyroscope, Add rfcomm-server

touch /home/pi/Desktop/done
