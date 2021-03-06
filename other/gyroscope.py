#!/usr/bin/python
import smbus
import math
import time
import pygame

pygame.mixer.init()
woohoo = pygame.mixer.Sound("/home/pi/Workspace/path-agile-development/other/woohoo.wav")
wow = pygame.mixer.Sound("/home/pi/Workspace/path-agile-development/other/wow.wav")

# Register
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(reg):
    return bus.read_byte_data(address, reg)

def read_word(reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address, reg+1)
    value = (h << 8) + l
    return value

def read_word_2c(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

bus = smbus.SMBus(1)
address = 0x68

bus.write_byte_data(address, power_mgmt_1, 0)

print "gyroscope"
print "--------"

while True:

    time.sleep(1)

    gyroscope_xout = read_word_2c(0x43)
    gyroscope_yout = read_word_2c(0x45)
    gyroscope_zout = read_word_2c(0x47)

    acceleration_xout = read_word_2c(0x3b)
    acceleration_yout = read_word_2c(0x3d)
    acceleration_zout = read_word_2c(0x3f)

    acceleration_xout_scaling = acceleration_xout / 16384.0
    acceleration_yout_scaling = acceleration_yout / 16384.0
    acceleration_zout_scaling = acceleration_zout / 16384.0

    x_value =  get_x_rotation(acceleration_xout_scaling, acceleration_yout_scaling, acceleration_zout_scaling)
    y_value =  get_y_rotation(acceleration_xout_scaling, acceleration_yout_scaling, acceleration_zout_scaling)

    print x_value
    print y_value

    if x_value > 10 && x_value < 20:
	    wohoo.play()
	elif x_value > -20 && x_value < 10:
	    wow.play()
	time.sleep(5)
