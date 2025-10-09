#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import random
# Initialiser EV3-brikken (hovedenhenten til roboten) 
hjernen = EV3Brick()

# Initialiser motorene på port B og C (venstre og høyre hjul)
venstre_motor = Motor(Port.A)
hoyre_motor = Motor(Port.D)

#kommand for å styre både høyre og venstre motor som 'robot', må ha størrelse og avstand mellom hjul i tilegg.
robot = DriveBase(hoyre_motor, venstre_motor, wheel_diameter=56, axle_track=114)

#sensorene
farge_sensor = ColorSensor(Port.S1)
ultra = UltrasonicSensor(Port.S3)

#definerer 'klokke' for å holde styr på tid 
klokke = StopWatch()

#tilfeldig ting roboten gjør for å 'underholde'
moro = [
    lambda: hjernen.speaker.play_file(SoundFile.HELLO),
    lambda: hjernen.speaker.play_file(SoundFile.HORN_1),
    lambda: hjernen.speaker.play_file(SoundFile.MAGIC_WAND),
    lambda: hjernen.screen.print("Hei der!"),
]

while True:
    # Eksempel på enkel linjefølger
    if farge_sensor.reflection() < 20: # mørkt underlag, dårlig refleksjon/lys 
        venstre_motor.run(200)
        hoyre_motor.run(100)
    else:
        venstre_motor.run(50)
        hoyre_motor.run(300)                                                                     

    #Klokke for å underholde hvert 10 sekund
    if klokke.time() > 10000: # 10 sekunder
        robot.stop()
        random.choice(moro)() # velger en tilfeldig funksjon fra 'moro' listen og kjører den
        wait(1000)
        klokke.reset()

    #Stopper robot da hinderet er nærmere enn 10 cm, og spiller av 'cheering' lyd
    if ultra.distance() < 100:  # 10 cm
        robot.stop()
        hjernen.speaker.play_file(SoundFile.CHEERING)
        wait(1000)
        break

    #funksjon for å stoppe programmet utenom å bruke hinderen (i tilfølge noe går galt)
    if Button.CENTER in hjernen.buttons.pressed():
        break