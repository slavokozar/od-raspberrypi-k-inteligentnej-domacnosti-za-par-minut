import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'

class SIPO():
        def __init__ (self,data,clk,ltch):

                self.SIPO_DAT = data
                self.SIPO_CLK = clk
                self.SIPO_LTC = ltch
             
                GPIO.setup(self.SIPO_DAT, GPIO.OUT)
                GPIO.setup(self.SIPO_CLK, GPIO.OUT)
                GPIO.setup(self.SIPO_LTC, GPIO.OUT)

                GPIO.output(self.SIPO_DAT, False)
                GPIO.output(self.SIPO_CLK, False)
                GPIO.output(self.SIPO_LTC, False)
                
        def write(self,data):
                
                for i in range(0, len(data)):
                        self.writeBite(data[i])

                time.sleep(0.001)
                GPIO.output(self.SIPO_LTC, False)


                time.sleep(0.001)
                GPIO.output(self.SIPO_LTC, True)
                

                        
        def writeBite(self,bite):
                GPIO.output(self.SIPO_DAT, (bite == 1))
                
                time.sleep(0.001) 
                GPIO.output(self.SIPO_CLK, True)
                
                time.sleep(0.001)
                GPIO.output(self.SIPO_CLK, False)