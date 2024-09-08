from machine import ADC
import time
adc = ADC(28)
threshold = 750

light_state = ""

def get_light():
    value = adc.read_u16()
    if value < threshold:
        return "dark"
    elif value >= threshold:
        return "bright"

def got_dark():
    global light_state
    light = get_light()
    if light == light_state:
        return False
    if light == "dark":
        light_state = "dark"
        return True
    else:
        light_state = "bright"
        return False

def got_bright():
    global light_state
    light = get_light()
    if light == light_state:
        return False
    if light == "dark":
        light_state = "dark"
        return False
    else:
        light_state = "bright"
        return True