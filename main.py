from servo import *
from lightsensor import *
from button import *
import time

try:
    while True:
        if is_on():
            if is_pressed():
                print("button pressed, switching off")
                switch_off()
            if got_bright():
                print("gone bright, switching off")
                switch_off()
        elif is_off():
            if is_pressed():
                print("button pressed, switching on")
                switch_on()
            if got_dark():
                print("gone dark, switching on")
                switch_on()
        time.sleep(.1)
except KeyboardInterrupt:
    stop_servo()
    print("program interrupted by user")