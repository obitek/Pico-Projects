import machine
import sys

led = machine.Pin(25, machine.Pin.OUT)  # Onboard LED for Raspberry Pi Pico

while True:
    command = sys.stdin.read(1)  # Read 1 character from serial input
    if command == "1":
        led.value(1)
        print("LED ON")
    elif command == "0":
        led.value(0)
        print("LED OFF")
