#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Initialiser EV3-brikken (hovedenheten til roboten)
ev3 = EV3Brick()

# Initialiser motorene på port B og C (venstre og høyre hjul)
venstre_motor = Motor(Port.C)
hoyre_motor = Motor(Port.B)

# Initialiser sensorer
trykk_sensor = TouchSensor(Port.S1)  # Trykksensor for start/stopp
ultralyd_sensor = UltrasonicSensor(Port.S4)  # Ultralydsensor for hindringer

# Vis "Exercise 2" på LCD-skjermen
ev3.screen.print("Exercise 2")

# Vent på at trykksensor blir trykket for å starte
while not trykk_sensor.pressed():
    wait(10)

# Si "Exercise 2" og start gressklipping
ev3.speaker.say("Exercise 2")
wait(1000)

# Hovedløkke for gressklipping
kjoerer = True
while kjoerer:
    # Sjekk om trykksensor er trykket for å stoppe
    if trykk_sensor.pressed():
        kjoerer = False
        break
    
    # Sjekk avstand til hindringer (under 30 cm = hindring)
    if ultralyd_sensor.distance() < 300:  # 300 mm = 30 cm
        # Stopp motorene
        venstre_motor.stop()
        hoyre_motor.stop()
        wait(500)
        
        # Rygge litt
        venstre_motor.run_angle(400, -200, Stop.BRAKE, False)
        hoyre_motor.run_angle(400, -200, Stop.BRAKE, True)
        
        # Sving til høyre for å unngå hindringen
        venstre_motor.run_angle(400, 300, Stop.BRAKE, False)
        hoyre_motor.run_angle(400, -300, Stop.BRAKE, True)
    else:
        # Kjør frem med konstant hastighet
        venstre_motor.run(200)
        hoyre_motor.run(200)
    
    wait(50)  # Kort pause før neste sjekk

# Stopp motorene
venstre_motor.stop()
hoyre_motor.stop()

# Si "Exercise done" og avslutt
ev3.speaker.say("Exercise done")
ev3.screen.print("Exercise done")
