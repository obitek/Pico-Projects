
from machine import Pin
from time import sleep

ledPins = ['LED', 14, 15]
leds = [Pin(pin, Pin.OUT) for pin in ledPins]

def ledToggle():
    leds[0].high()
    sleep(1)
    leds[0].low()
    sleep(1)

    leds[1].high()
    sleep(1)
    leds[1].low()
    sleep(1)

    leds[2].high()
    sleep(1)
    leds[2].low()
    sleep(1)

while True:
    ledToggle()
