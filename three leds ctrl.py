from machine import Pin
from time import sleep

led1 = Pin("LED", Pin.OUT)
led2 = Pin(15, Pin.OUT)
led3 = Pin(14, Pin.OUT)

def ledToggle():
    led1.value(1) # turn ON onboard led
    sleep(1)      # wait for a second
    led1.value(0) # turn OFF onboard led 
    sleep(1)      # wait for 1 second
    
    led2.value(1)
    sleep(1)
    led2.value(0)
    sleep(1)
    
    led3.value(1)
    sleep(1)
    led3.value(0)
    sleep(1)

while True:
    ledToggle()
