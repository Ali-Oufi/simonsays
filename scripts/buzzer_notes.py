import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

buzz_pin = 32

GPIO.setup(buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,1000)

frequencies = [392,440,494,523,587,659,698,784,1]
n = random.randint(0,3)
Buzz.ChangeFrequency(frequencies[0])
Buzz.start(100)
time.sleep(0.5)
Buzz.ChangeFrequency(frequencies[8])
time.sleep(0.125)
Buzz.ChangeFrequency(frequencies[1])
time.sleep(0.5)
Buzz.stop()
