from machine import Pin

button_pin = Pin(1, Pin.IN, Pin.PULL_UP)
button_state = 1

def is_pressed():
    global button_state
    button = button_pin.value()
    if button == button_state:
        return False
    if button == 0:
        button_state = 0
        return True
    else:
        button_state = 1
        return False