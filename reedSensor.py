
# Reed sensor / switch example for Raspberry Pi Pico with serial debug
from machine import Pin
from utime import sleep

reedPin = Pin(14, Pin.IN, Pin.PULL_UP) # Configure GPIO14 as input with internal pull-up resistor
onboardLed = Pin("LED", Pin.OUT)       # Use onboard LED (GPIO25)

while True:
    reed_state = reedPin.value()       # extract reed sensor state
    if reed_state == 0:                # Reed switch is closed (magnet near)
        onboardLed.high()
        print("Magnet detected: Reed switch CLOSED. LED ON.")
    else:                              # Reed switch is open
        onboardLed.low()
        print("No magnet: Reed switch OPEN. LED OFF.")
    sleep(1)

    