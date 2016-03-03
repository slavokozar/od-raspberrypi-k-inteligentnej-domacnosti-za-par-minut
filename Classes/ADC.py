import RPi.GPIO as GPIO ## Import GPIO library
import time

class ADC():
        def __init__ (self,dat,clk,cs):

                self.ADC_DAT = dat
                self.ADC_CLK = clk
                self.ADC_CS = cs
             
                GPIO.setup(self.ADC_DAT, GPIO.IN)
                GPIO.setup(self.ADC_CLK, GPIO.OUT)
                GPIO.setup(self.ADC_CS, GPIO.OUT)

                GPIO.output(self.ADC_CLK, False)
                GPIO.output(self.ADC_CS, True)
                
        def read(self):
                value=[0 for i in range(8)]

                GPIO.output(self.ADC_CS, False)
                time.sleep(0.001)

                for i in range(0, 8):
                        self.readBite()

                GPIO.output(self.ADC_CS, True)
                time.sleep(0.01)
                
                GPIO.output(self.ADC_CS, False)
                time.sleep(0.001)

                for i in range(0, 8):
                        value[7-i] = self.readBite()
                
                GPIO.output(self.ADC_CS, True)
                print(value)
                
                result = 0;
                b = 1; 
                for i in range(0, 8):
                        result = result + value[i]*b;
                        b = b*2;
                                                
                return result;
                        
        def readBite(self):
                GPIO.output(self.ADC_CLK, True)
                time.sleep(0.001)
                
                bite = GPIO.input(self.ADC_DAT);

                GPIO.output(self.ADC_CLK, False)
                time.sleep(0.001)

                return bite