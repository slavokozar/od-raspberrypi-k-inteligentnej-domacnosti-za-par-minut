import RPi.GPIO as GPIO ## Import GPIO library
from Classes.SIPO import *

GPIO.setmode(GPIO.BOARD)

sipo = SIPO(3,7,5)
data = [1,1,1,1,1,0,1,0];

sipo.write(data);


GPIO.cleanup()
