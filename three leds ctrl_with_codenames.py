
from machine import Pin
from time import sleep

led1 = Pin("LED", Pin.OUT)
led2 = Pin(15, Pin.OUT)
led3 = Pin(14, Pin.OUT)

def ledToggle(codeName):
    if codeName.lower() == 'timi':
        for i in range(3):
            led1.high() # turn ON onboard led
            sleep(1)      # wait for a second
            led1.low() # turn OFF onboard led 
            sleep(1)      # wait for 1 second
    elif codeName.lower() =='obii':
        for i in range(3):
            led2.high() # turn led 2
            sleep(1)      # wait for a second
            led2.low() # turn OFF led 
            sleep(1)      # wait for 1 second
    elif codeName.lower() == 'abbey':
        for i in range(3):
            led3.high() # turn led 3
            sleep(1)      # wait for a second
            led3.low() # turn OFF led 
            sleep(1)      # wait for 1 second

while True:
    x = input('Enter a word or type 'exit' to quit: ')
    if x.lower() == 'exit':
        break
    ledToggle(x)

