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

left_motor = Motor(Port.C)
left_sensor = ColorSensor(Port.S4).reflection()

right_motor = Motor(Port.B)
right_sensor = ColorSensor(Port.S1).reflection()
program = True
BLACK = 20
WHITE = 60

driving_left = False
driving_right = False
came_back = True


#Functions
def Drive(): #This function drives the machine
    global driving_left
    global driving_right
    if left_sensor <= BLACK and right_sensor >= WHITE: #This means that the left sensor sees black and the right sensor sees white (going to far to the right)
        came_back = False
        driving_left = True
        right_motor.run(300)
        left_motor.run(50)
        if right_sensor >= WHITE and left_sensor >= WHITE:
            came_back = True
            driving_left = False
    elif right_sensor <= BLACK and left_sensor >= WHITE: #tHIS MEANS THAT THE RIGHT SENSOR sees black and the left sensor sees white (going to far to the left)
        came_back = False
        driving_right = True
        right_motor.run(50)
        left_motor.run(300)
        if right_sensor >= WHITE and left_sensor >= WHITE:
            came_back = True
            driving_right = False
    else: #Then the only other thing that can happen is if the robot is in line, so both sensors see white
        if came_back:
            right_motor.run(400)
            left_motor.run(400)
            ev3.screen.print("Forward")
        else:
            if driving_left:
                ev3.screen.print("You went too far out left")
                ev3.speaker.say("You went too far out left")
            elif driving_right:
                ev3.screen.print("You went too far out right")
                ev3.speaker.say("You went too far out right")
            else:
                ev3.screen.print("Logic error")
                ev3.speaker.say("Logic errort")
            

def Finder(): #This functions finds back to the line upon having lost it
    ...

def Intersection(): #This function will properly handle the intersection in the course
    ...

while program: #while our program is true
    Drive()