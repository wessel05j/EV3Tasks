#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Initialisering
ev3 = EV3Brick()
venstre_motor = Motor(Port.C)
hoyre_motor = Motor(Port.B)
start_stopp_sensor = TouchSensor(Port.S1)
ultralyd_sensor = UltrasonicSensor(Port.S2)

driving = False
ev3.speaker.say("Ready")    

# Hovedløkke
while True:
    # Sjekk knapper
    pressed = ev3.buttons.pressed()
    
    if start_stopp_sensor.pressed(): 
        driving = not driving
        if driving == True:
            ev3.speaker.say("Exercise 2")
        else:
            venstre_motor.stop()
            hoyre_motor.stop()
            ev3.speaker.say("Exercise done")
            break
        
        wait(300)
    
    # Kjør eller stopp
    if driving:
        if ultralyd_sensor.distance() < 300:
            # Hindring oppdaget - stopp umiddelbart
            venstre_motor.stop()
            hoyre_motor.stop()
            wait(100)
            
            # Sving 90 grader til venstre (høyre motor fremover, venstre motor bakover)
            venstre_motor.run_time(-600, 800)  # Venstre motor bakover - økt tid for 90 grader
            hoyre_motor.run_time(600, 800)     # Høyre motor fremover - økt tid for 90 grader
            wait(900)  # Vent til svingen er ferdig
            
            
            # Nå er veien fri - fortsett fremover
            
        else:
            # Kjør rett frem - ingen hindring
            venstre_motor.run(500)
            hoyre_motor.run(500)
    else:
        # Stopp motorene når ikke i kjøremodus
        venstre_motor.stop()
        hoyre_motor.stop()

    
    wait(50)
