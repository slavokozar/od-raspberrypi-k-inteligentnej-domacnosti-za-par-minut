import RPi.GPIO as GPIO ## Import GPIO library
from Classes.SIPO import *

GPIO.setmode(GPIO.BOARD)

GPIO.setup(37, GPIO.OUT)

for i in range(10):
	GPIO.output(37,True)
	time.sleep(0.5) 
	GPIO.output(37, False)
	time.sleep(0.5)

GPIO.cleanup()


