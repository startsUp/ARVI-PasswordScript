import serial #Serial imported for Serial communication
import time 
 
ArduinoSerial = serial.Serial('COM5',9600) #open the same port as arduino
time.sleep(2) #communication establishing delay

while 1: #Do this forever
    print "Temperature data recieved"
    print ArduinoSerial.readline() #read the serial data and print it as line
    time.sleep(2)