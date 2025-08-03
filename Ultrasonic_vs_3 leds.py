
from machine import Pin, time_pulse_us
import utime

tPin = Pin(2, Pin.OUT)
ePin = Pin(3, Pin.IN)

ledPins = ['LED', 14, 15]                     
leds = [Pin(pin, Pin.OUT) for pin in ledPins] 

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

def ledFunc(n):
    leds[n].high()
    utime.sleep(1)
    leds[n].low()
    utime.sleep(1)

while True:
    d_cm = get_Distance()
    #d_cm = 0
    #n = 20
    #for i in range(n):
    #    d_cm += get_Distance()
    #d_cm /= n
    if int(d_cm) <= 50:
        ledFunc(0)
        
    elif int(d_cm) <= 100:
        print("Distance: {:.2f} cm".format(d_cm))
        for i in range(2):
            ledFunc(i)
            
    elif int(d_cm) > 100:
        print("Distance: {:.2f} cm".format(d_cm))
        for i in range(3):
            ledFunc(i)
            
    utime.sleep(0.1)
    
