
from machine import Pin
from time import sleep
import random as rdm

led = Pin("LED", Pin.OUT) # led = Pin(25, Pin.OUT)
led_count = 6
count_down = 3

def ToggleLed():
    led.toggle()  # Toggle the LED state (on/off)
    sleep(0.5)    # Wait for 0.5 seconds

while True:
    rm = rdm.randint(1, 10)
    print(f"\n")
    val = int(input("Enter a value: "))
    print(f"Random value: {rm}")

    if rm == val:
        while led_count > 0:
            print(f"LED count = {led_count}")
            for i in range(4):
                ToggleLed()
            led_count -= 1
        led_count = 6
        count_down = 3

    else:
        print(f"You have {count_down} attempts left!")
        count_down -= 1
        if count_down < 0:
            count_down = 3
            print(f"You have exhausted you chances! NEXT CLIENT PLS!")



