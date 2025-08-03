# libraries
from machine import Pin, PWM
from time import sleep

# configure PWM on gp15
servo = PWM(Pin(15))
# set frequency
servo.freq(50)       

def set_angle(angle):
    duty = int((angle/180) * 8000 + 1000)
    servo.duty_u16(int(duty * 65535 / 2000))
    
while True:
    # rotates in one direction
    for i in range(0,181, 10):
        set_angle(i)
        sleep(0.1)
        
    # rotates in the opposite direction  
    for j in range(180, -1, -10):
        set_angle(j)
        sleep(0.1)