from rtttl import RTTTL
from machine import Pin, PWM
import songs
import time

speaker_pin = Pin(19, Pin.OUT)  # Speaker is connected to this pin

# Initialize input/output pins
pwm = PWM(speaker_pin, freq=20000, duty=0) # create and configure in one go


def play_tone(freq, msec):
#    print('freq = {:6.1f} msec = {:6.1f}'.format(freq, msec))
    if freq > 0:
        pwm.freq(int(freq))     # Set frequency
        pwm.duty(512)           # 50% duty cycle
        time.sleep(msec*0.001)  # Play for a number of msec
        pwm.duty(0)             # Stop playing
        time.sleep(0.05)        # Delay 50 ms between notes

tune = RTTTL(Songs.find('Entertainer'))

for freq, msec in tune.notes():
    play_tone(freq, msec)
