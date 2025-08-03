from machine import Pin
#import time
from time import sleep

btn = Pin(15, Pin.IN, Pin.PULL_UP) 
led = Pin(25, Pin.OUT)

while True:
    if btn.value() == 0:  		# Button pressed (LOW state)
        print("Button Pressed")	# Print "Button Pressed" on the shell
        led.toggle()			# Toggle LED (on/off)
    #time.sleep(0.1)  			# Debounce delay
    sleep(0.1)					# Debounce delay