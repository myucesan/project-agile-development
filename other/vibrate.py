import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)

try:
	while True:
		GPIO.output(16, 1)
		sleep(1)
		GPIO.output(16, 0)
		sleep(1)
except KeyBoardInterrupt:
	GPIO.cleanup()

