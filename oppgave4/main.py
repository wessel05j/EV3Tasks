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
DRIVE = 200
SWING_DRIVE = 100

def kjør_forbi_kryss():
    left_motor.run(DRIVE)
    right_motor.run(DRIVE)
    wait(1000)  # kjør rett frem i 1 sekund


while True:
    left_col = left_sensor.reflection()
    right_col = right_sensor.reflection()

    if left_col < BLACK and right_col > WHITE: #This means that the left sensor sees black and the right sensor sees white (going to far to the right)
        right_motor.run(DRIVE)
        left_motor.run(SWING_DRIVE)
    elif right_col < BLACK and left_col > WHITE: #This means that the right sensor sees black and the left sensor sees white (going to far to the left)
        right_motor.run(SWING_DRIVE)
        left_motor.run(DRIVE)    
    elif left_col < BLACK and right_col < BLACK:
        kjør_forbi_kryss()
    else:
        left_motor.run(DRIVE)
        right_motor.run(DRIVE)
    
            