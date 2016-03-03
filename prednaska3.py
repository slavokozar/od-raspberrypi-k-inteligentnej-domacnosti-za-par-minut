import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us 
from Classes.ADC import *

GPIO.setmode(GPIO.BOARD)
adc = ADC(33,31,35);

print(adc.read())

GPIO.cleanup()
