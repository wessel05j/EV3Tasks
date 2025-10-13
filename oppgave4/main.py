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


BLACK = 20
WHITE = 50
DRIVE = 300
SWING_DRIVE = 50

driving_left = False
driving_right = False
came_back = True




while True:
    #Functions
    left_col = left_sensor.reflection()
    right_col = right_sensor.reflection()

    if left_col < BLACK and right_col > WHITE: #This means that the left sensor sees black and the right sensor sees white (going to far to the right)
        came_back = False
        driving_left = True
        right_motor.run(DRIVE)
        left_motor.run(SWING_DRIVE)
        if right_col > WHITE and left_col > WHITE:
            came_back = True
            driving_left = False
    elif right_col < BLACK and left_col > WHITE: #This means that the right sensor sees black and the left sensor sees white (going to far to the left)
        came_back = False
        driving_right = True
        right_motor.run(SWING_DRIVE)
        left_motor.run(DRIVE)
        if right_col > WHITE and left_col > WHITE:
            came_back = True
            driving_right = False
    elif right_col > WHITE and right_col > WHITE: #Then the only other thing that can happen is if the robot is in line, so both sensors see white
        if came_back:
            right_motor.run(DRIVE)
            left_motor.run(DRIVE)
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
                