from machine import Pin
from time import sleep

# Initialize the Onboard LED pin (GP25 of 'LED') as an output
led = Pin(25, Pin.OUT)

# Blink the LED in a loop
def ToggleState():
    led.toggle()  # Toggle the LED state (on/off)
    sleep(0.5)    # Wait for 0.5 seconds

# repeat process forever
while True:
    ToggleState()
