from machine import Pin
from time import sleep

ledPins = ['LED', 14, 15]                     # Define your pins properly
leds = [Pin(pin, Pin.OUT) for pin in ledPins] # Create a list to store Pin objects

def ledToggle():
    for led in leds:
        led.toggle()
        sleep(1)
        led.toggle()
        sleep(1)

while True:
    ledToggle()
