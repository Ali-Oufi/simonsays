import RPi.GPIO as GPIO
import LEDRGB as LED
import time
import random

colors = ['R', 'G', 'B', 'Y']

R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)
GPIO.setwarnings(False)

def rand_color():
    while True:
        n = random.randint(0,3)
        LED.setColor(colors[n])
        time.sleep(0.5)

def turn_off():
    LED.destroy()

if __name__ == '__main__':
    try:
        rand_color()
    except KeyboardInterrupt:
        GPIO.setwarnings(False)        
        turn_off()
        print '\nGood Bye'
