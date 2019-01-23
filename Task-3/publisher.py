#!/usr/bin/env python
import rospy from std_msgs.msg 
import String
import serial #Serial imported for Serial communication
import time 
 
ArduinoSerial = serial.Serial('COM5',9600) #open the same port as arduino
time.sleep(2) #communication establishing delay

def talker():

    pub = rospy.Publisher('temperature', String, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        data = ArduinoSerial.readline() #read the serial data and print it as line
        rospy.loginfo(data)
        pub.publish(data)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass