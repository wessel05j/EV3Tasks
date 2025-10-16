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
INNER_BLACK = 10
WHITE = 40
DRIVE = 260
FAST = 260
SLOW = 60

#Entering out while loop that will go untill we cancel the program from the robot
while True:
    #checks the color for each loop
    left_col = left_sensor.reflection()
    right_col = right_sensor.reflection()
    ev3.screen.print(left_col, right_col)
   
    if left_col < BLACK and right_col > WHITE: #This means that the left sensor sees black and the right sensor sees white (going to far to the right)
        if left_col < INNER_BLACK:
            left_motor.run(SLOW/1.5)
            right_motor.run(DRIVE/1.5)
        else:
            right_motor.run(DRIVE-70) 
            left_motor.run(SLOW-20)
        watch.reset() #resets clock since we are not driving right forward
    elif right_col < BLACK and left_col > WHITE: #This means that the right sensor sees black and the left sensor sees white (going to far to the left)
        if right_col < INNER_BLACK:
            right_motor.run(SLOW/1.5)
            left_motor.run(DRIVE/1.5) 
        else:
            right_motor.run(SLOW-20) 
            left_motor.run(DRIVE-70)
        watch.reset() #resets clock since we are not driving right forward    
    else:
        #if there has gone 2 seconds driving forward then the robot will go extra fast
        if watch.time() >= 2000:
            left_motor.run(FAST)
            right_motor.run(FAST)
        else: #If not then just run
            left_motor.run(DRIVE)
            right_motor.run(DRIVE)
    wait(50)
    
            