# Semi-Autonomous RC-Car
## Bates Short Term 2017 
## Brad Rutkin, Matt Kalt, Priyanka Takle, Reed Feldman 
 
# Description 
Our project used a Raspberry Pi 3 to make a semi-autonomous RC-Car. In this project we used a standard RC car that was bought online for about $20. Using our Raspberry Pi, a HC-SR04 sensor, a L298-D chip, a Pi can and some python our car was able to drive straight and come to a stop if it sensed an object in front of it. This documentation will give a step by step guide to building our car. At the end of the documentation we will talk about the obstacles we faced, and how we overcame (most of) them.  
 
# List of Parts 
 
8GB MicroSD Card w/ NOOBS 2.0: $9.95
Raspberry Pi Model B: $39.95
L298D Chip: $2.95
Breadboard: $5.95
Raspberry Pi Camera Module V2 8 Megapixel,1080p: $29.88
HC-SR04 sensor: $2.99
M/M and F/F wires: $8.90
RC Car: $28.99
External USB Power Supply:  $14.95
 
Total: $144.51
 
# Programs/Packages Required 
 
OpenCV
Python 
 
## Step by Step
This tutorial assumes your Raspberry Pi has Noobs downloaded, and wifi. Because we were on the closed Bates Network we had to wait two days to get our Pi online. 
 
# Your Car
The best place to start is to take your car apart. You can buy an expensive car made for the Pi, but if you are like us, buy a cheaper car and take notes and pictures when you take the car apart. Label all screws and pieces.  This step consists of rewiring the car, including detaching the the chip/radio receiver that was already inside the car.   We go into more detail on configuration below.  
 
Tutorial: http://www.instructables.com/id/Raspberry-Pi-2-WiFi-RC-Car/
 
 
![img_3615](https://cloud.githubusercontent.com/assets/18706242/26501842/b9f05d38-4208-11e7-93b8-b7718303dac1.jpg)
 
You want to make sure you have two DC motors. One to go back and forward, and one to go left and right. Each motor should have two wires going into it to control each direction.
 
 
# L298D chip
Connect your power supply to the L298D chip along with the two motors. Make sure you mark down which is motor A and which is motor B.  The L298D chip has input/output for each motor.  We used online tutorials for configuration(see below).  You can use the GPIO on the PI to connect the L298D chip to the Pi.  Basically the configuration of this chip has 4 components.  The Pi, the L298D chip, battery pack for powering motors, and the two DC motors.  We connected these components as such.  
 
Tutorial: http://geextor.com/2016/11/20/driving-a-dc-motor-with-raspberry-pi/
 
![img_3634](https://cloud.githubusercontent.com/assets/18706242/26502098/7bbee510-4209-11e7-992c-b0be6dd04dd8.jpg)

 
# HC-SR04 Sensor
Using a breadboard, connect the sensor to the Pi. Make sure the wires are connected accurately based on the the GPIO numbers in the Pi and the positions on the breadboard, as errors in this wiring can cause the sensor to overheat and break.   When setting up our GPIO pins it is important to be consistent.  One can either use GPIO.Board or GPIO.BCM.  We chose to use gpio.board and use the physical pin numbers rather than the GPIO numbers.  
 
Tutorial: https://www.raspberrypi.org/learning/physical-computing-with-python/distance/
 
![img_0503 1](https://cloud.githubusercontent.com/assets/18706242/26502210/e6b46e12-4209-11e7-94ae-0512b7fa37a8.jpg)

 
# Programming
 
You can use python to turn on specific GPIO pins, sleep and shut the pin off. This allows you to control specific wires and specific motor functions via the keyboard. We had a function for forward, back,  left and right. Our autonomous driving function was called drive. It would scan the environment using the HC-sr04 sensor, if it saw nothing for 30 cm it would run forward motor for .5 seconds, then scan again. If it saw something it would reverse for .1 seconds (just enough to stop the car). It would perform 15 scans and actions (straight or stop) before the program would end. It could do more than 15 actions but we wanted to perform shorter tests. 
 
Next, we using the raspberry pi camera and OpenCV to allow the car to ‘see’.  Using an xml file with hundreds of postive and negative sample of stop signs  The way image recognition works is we first need to "train" a classifier, like we would with any machine learning algorithm. To do this, we gathered a  massive set of images of what we're looking to detect.   In our case it’s stop signs.  To do this, we wrote code that analyzes each picture and either says: “ yes this picture contains a stop sign” or “no this picture does not contain a stop sign”.  At this point, training is done.  When we placed an image of a stop sign in front of our car and executed our script, our result was as follows:
 
![result1](https://cloud.githubusercontent.com/assets/18706242/26502148/a1110d02-4209-11e7-93ac-17512ce232b6.jpg)
 
At this point, our car could detect objects using a distance sensor and see stop signs using a pi camera.  If either were detected, our car would stop and stay put until either were removed.  
 
Link to our xml file: https://github.com/mbasilyan/Stop-Sign-Detection
To install openCV: http://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/
 
# Challenges
In class designed to last only 5 weeks this was a large task to take on. There is a learning curve to operating a Raspberry Pi which made starting the project difficult. None of us had ever worked with the Pi before so between shopping, planning and learning it took us about two weeks before we could really get started. That meant we only had about three weeks for the car.
 
Our first challenge was just working with the car. More expensive RC-Cars have better documentation and can be taken apart more easily to allow for customization. To limit expenses we had to buy a cheaper car, take it apart and reverse engineer it back together. There was no tutorial or documentation for this. We had to take notes, carefully label pieces and work together to get all the motors out. Once the motors were out we had to rebuild the car. This lead to another issue.
 
All the tutorials online were slightly different. In our daily logs you can see just how many tutorials we used. We constantly pieced them together to try new things. Just getting the motors to be controlled by the Pi was a challenge. It took a lot of guess and check attempts but we finally found that the L298D chip works best. Because the wiring was new to us we constantly burned wires. We even had hardware issues. We lost 1 SD card that was probably fried due to poor wiring.
 
Once we had the motors attached to the Pi we spent almost two days putting the car and its gears back together. We overcame this challenge but just guessing and checking. We consistently had to try new things throughout this project and we consistently failed. Eventually the car was pieced together again. 
 
Installing OpenCV was an extremely time consuming process and there was no way of making sure each step of the installation process was successful. We were able to install the program in about 2 and a half hours, but once the program was installed we were not able to import it from python. After a lot of troubleshooting, we determined that this was because we did not bind OpenCV to python (via the sudo apt-get install python-opencv command). Because it took us so long to be able to import OpenCV from python, we were limited in the amount of time we had to work on the stop sign detection aspect of the car. 
 
We needed more time. Our time constraint did not allow us to perfect any aspect of our car. We had a working car that could only drive straight and stop on its own. We never had time to add in turns or to allow it to use the Pi-Cam to stop the car. We did get the camera to recognize stop signs, but this function was never added into the driving program. 

# Final Car:  Check out our Youtube video for more details and clips of our working car:


![img_0512 1](https://cloud.githubusercontent.com/assets/18706242/26502365/94d6262a-420a-11e7-8a1c-c0d63a0b181c.jpg)



![img_0513 1](https://cloud.githubusercontent.com/assets/18706242/26502360/8eb28db0-420a-11e7-925c-a4a50755db65.jpg)



