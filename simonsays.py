import RPi.GPIO as GPIO
import LEDRGB as LED
import time
import random
from getpass import getpass

colors = ['R','Y','G','B']
sounds = [262,392,591,880]
list_color = [ ]
list_sound = [ ]
sequence = ""
guess = ""

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
buzz_pin = 32

GPIO.setup(buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,1000)

R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)

def play_list(listc,lists):
    for x in range(0,len(listc)):
        LED.setColor(listc[x])
        Buzz.ChangeFrequency(lists[x])
        Buzz.start(50)
        time.sleep(0.25)
        LED.noColor()
        Buzz.stop()
        time.sleep(0.25)

def append_list():
    n = random.randint(0,3)
    list_color.append(colors[n])
    list_sound.append(sounds[n])

def turn_off():
    LED.setColor('R')    
    Buzz.ChangeFrequency(3520)
    Buzz.start(50)
    time.sleep(2)
    LED.destroy()
    Buzz.stop()

def validate_guess():
    guess = getpass("Guess the color sequence (ex: rygbb): \n").upper()
    sequence= ''.join(list_color)
    if not (len(sequence) == len(guess)):
        print "Your sequence does not contain the same number of colors as shown."
        print "The correct sequence is: ", sequence
        print "The sequence you put is: ", guess
        print "Game Over"
        turn_off()
        exit()
    if not (sequence == guess):
        print "Wrong color sequence"
        print "The correct sequence is: ", sequence
        print "The sequence you put is: ", guess
        print "Game Over"
        turn_off()
        exit()
    print "Correct sequence"

if __name__ == '__main__':
    try:
        while True: 
            append_list()
            play_list(list_color,list_sound)
            validate_guess()
    except KeyboardInterrupt:
        GPIO.setwarnings(False)        
        turn_off()
        print '\nGood Bye'
