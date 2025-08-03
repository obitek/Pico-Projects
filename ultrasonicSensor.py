
from machine import Pin, time_pulse_us
import utime

tPin = Pin(2, Pin.OUT)
ePin = Pin(3, Pin.IN)

def get_Distance():
    tPin.low()
    utime.sleep_us(2)
    tPin.high()
    utime.sleep_us(10)
    tPin.low()
    
    t = time_pulse_us(ePin, 1, 30000)
    if t < 0:
        print('Out of range!')
        return None
    return (t / 2) / 29.1

while True:
    d_cm = get_Distance()
    #d_cm = 0
    #n = 20
    #for i in range(n):
    #    d_cm += get_Distance()
    #d_cm /= n
    if d_cm:
        print("Distance: {:.2f} cm".format(d_cm))
    utime.sleep(1)
    