#this is the script that runs the motors
#from pythonprogramming.net
from stop import find_stop
import RPi.GPIO as GPIO
import time
from time import sleep

### distance

import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)

#set GPIO Pins
GPIO_TRIGGER = 37
GPIO_ECHO = 35

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance
###


GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

def forward(x):
        GPIO.setup(13, GPIO.OUT)
        GPIO.output(13, GPIO.HIGH)
        sleep(x)
        GPIO.output(13, GPIO.LOW)

def reverse(x):
        GPIO.setup(15, GPIO.OUT)
        GPIO.output(15, GPIO.HIGH)
        sleep(x)
        GPIO.output(15, GPIO.LOW)

def left(x):
        GPIO.setup(7, GPIO.OUT)
        GPIO.output(7, GPIO.HIGH)
        sleep(x)
        GPIO.output(7, GPIO.LOW)

def right(x):
        GPIO.setup(11, GPIO.OUT)
        GPIO.output(11, GPIO.HIGH)
        sleep(x)
        GPIO.output(11, GPIO.LOW)


def drive():
        count = 0
        while count < 15:
                x = distance()
                y = find_stop()
                if x > 50:
                        forward(.5)
                        print(x)
                        count += .5
                        print(count,"GO")

#               attempt at adding openCV  
                x = distance()
                y = find_stop()
                if x > 50:
                        forward(.5)
                        print(x)
                        count += .5
                        print(count,"GO")

#               attempt at adding openCV        
#               if len(stops)>0:
#                       reverse(.1)     
                else:
                        print(x, "STOP")
                        count += .5
                        reverse(.1)


drive()



