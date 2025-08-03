
from machine import Pin
from time import sleep
import random as rdm

led = Pin("LED", Pin.OUT) # led = Pin(25, Pin.OUT)
count = 6

def ToggleLed():
    led.toggle()  # Toggle the LED state (on/off)
    sleep(0.5)    # Wait for 0.5 seconds

while True:
    rm = rdm.randint(1, 10)
    print(f"\n")
    val = int(input("Enter a value: "))
    print(f"Random value: {rm}")
    if rm == val:
        while count > 0:
            print(f"count down = {count}")
            for i in range(4):
                ToggleLed()
            count -= 1
    else:
        count = 6



