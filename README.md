# IntelliLight
*IntelliLight project from Jugendhackt Cologne 2024*


## Description
This will be a module that can be attached to any light switch easily. When there is no one in the room or it's too bright, the light will be turned off.

## ToDo
- [x] Case
  - [ ] Attachement
- [x] RPi Pico Micropython
- [x] Manual Switching
- [x] Lightsensor
- [ ] other stuff ??

## Building te Project

### Setting up the RaspberryPI with Micropython
For this folllow the normal instructions on the Micropython site.

### Connecting the servo
Follow these instructions: https://randomnerdtutorials.com/raspberry-pi-pico-servo-motor-micropython/
**Only connect the servo, don't use the code**

### Connecting the lightsensor
We used these instructions: https://electrocredible.com/raspberry-pi-pico-ldr-photoresistor-light-dark-sensor/
**Also don't use the example code**

### Connect the button
![image](https://github.com/Jugendhackt/IntelliLight/blob/9ee2e0b82cd52101e15f816a604bae7ff2016ba3/images/IMG_20240908_092426254.jpg)
Use this image
![image](https://github.com/Jugendhackt/IntelliLight/blob/2549615bb8719e64efeb6a79cfe6e2e413eaf901/images/Schaltplan.svg)
And this.

### Code
Download the code from our repo and write it to the Pico. to execute it, just run the *main.py* file.
