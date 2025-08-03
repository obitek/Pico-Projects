
# analog-inputs
from machine import Pin, ADC
from time import sleep

# configure adc pin
pot = ADC(Pin(26))

# while loop
if __name__ == "__main__":
    while True:
        pot_value = pot.read_u16() # read value, 0 - 65535 across voltage range 0.0V - 3.3V
        pot_volts = pot_value / 65536 * 3.3
        print(f"Potentiomter Reading: {pot_volts} V")
        sleep(0.2)
