from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT) # Initialize the LED pin (GP25) as an output
     
while True:
    led.value(True)  	# Toggle the LED state on
    sleep(0.5)    		# Wait for 0.5 seconds
    led.value(False)  	# Toggle the LED state off
    sleep(0.5)    		# Wait for 0.5 seconds