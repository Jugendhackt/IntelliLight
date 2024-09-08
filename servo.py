from servolib import Servo
from time import sleep

# Create a Servo object on pin 0
servo=Servo(pin=0)
state = "off"

def is_on():
    global state
    return state == "on"

def is_off():
    global state
    return state == "off"

def switch_on():
    global state
    servo.move(10)
    #print("on")
    state = "on"

def switch_off():
    global state
    servo.move(0)
    #print("off")
    state = "off"