#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


 
#Creating our variables
ev3 = EV3Brick()

left_motor = Motor(Port.A)
left_sensor = ColorSensor(Port.S1)
right_motor = Motor(Port.D)
right_sensor = ColorSensor(Port.S4)
watch = StopWatch()


BLACK = 30
WHITE = 50
DRIVE = 250
FAST = 300
SWING_DRIVE = 40
SWING_DRIVE_FAST = 100

#Entering out while loop that will go untill we cancel the program from the robot
while True:
    #checks the color for each loop
    left_col = left_sensor.reflection()
    right_col = right_sensor.reflection()

    if left_col < BLACK and right_col > WHITE: #This means that the left sensor sees black and the right sensor sees white (going to far to the right)
        right_motor.run(SWING_DRIVE_FAST) #right motor drives fast to swing left
        left_motor.run(SWING_DRIVE)
        watch.reset() #resets clock since we are not driving right forward
    elif right_col < BLACK and left_col > WHITE: #This means that the right sensor sees black and the left sensor sees white (going to far to the left)
        right_motor.run(SWING_DRIVE)
        left_motor.run(SWING_DRIVE_FAST) #left motor drivest fast to swing right
        watch.reset() #resets clock since we are not driving right forward    
    else:
        #if there has gone 2 seconds driving forward then the robot will go extra fast
        if watch.time() >= 2000:
            left_motor.run(FAST)
            right_motor.run(FAST)
        else: #If not then just run
            left_motor.run(DRIVE)
            right_motor.run(DRIVE)
        
    
            