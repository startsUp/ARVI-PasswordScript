import serial #Serial imported for Serial communication
import time 
 
ArduinoSerial = serial.Serial('COM5',9600) #open the same port as arduino
time.sleep(2) #communication establishing delay

print ArduinoSerial.readline() #read the serial data and print it as line
print "Enter 1 to turn led on, and 0 to turn it off"
while 1: #Do this forever

    var = raw_input() #get input from use
    if (var == '1'): #if the value is 1
        ArduinoSerial.write('1') #send 1
        print ("LED turned ON")
        time.sleep(1)
    
    if (var == '0'): #if the value is 0
        ArduinoSerial.write('0') #send 0
        print ("LED turned OFF")
        time.sleep(1)