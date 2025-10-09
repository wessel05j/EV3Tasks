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

left_motor = Motor(Port.D)
left_sensor = ColorSensor(Port.S1).color()

right_motor = Motor(Port.D)
right_sensor = ColorSensor(Port.S4).color()
program = True
SPEED = 300
SWING_SPEED = 50

driving_left = False
driving_right = False
came_back = True


#Functions
def Drive(): #This function drives the machine
    global driving_left
    global driving_right

    if left_sensor == Color.BLACK and right_sensor == Color.WHITE: # left sees black, right sees white (too far to the right)
        came_back = False
        driving_left = True
        right_motor.run(SPEED)
        left_motor.run(SWING_SPEED)
        if right_sensor == Color.WHITE and left_sensor == Color.WHITE:
            came_back = True
            driving_left = False
    elif right_sensor == Color.BLACK and left_sensor == Color.WHITE: # right sees black, left sees white (too far to the left)
        came_back = False
        driving_right = True
        right_motor.run(SWING_SPEED)
        left_motor.run(SPEED)
        if right_sensor == Color.WHITE and left_sensor == Color.WHITE:
            came_back = True
            driving_right = False
    elif left_sensor == Color.RED or right_sensor == Color.RED: # if either sensor sees red
        ...
    else: #Then the only other thing that can happen is if the robot is in line, so both sensors see white
        if came_back:
            right_motor.run(SPEED)
            left_motor.run(SPEED)
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
            


while program: #while our program is true
    wait(2000) #Waits 2 seconds before starting
    Drive()