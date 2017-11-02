# Melody Player

# Plays a melody when a button is pressed.

# Circuit:
# * 8-ohm speaker on pin 5
# * Button connected to pin

import RPi.GPIO as GPIO   #import the GPIO library
from time import sleep    #import the time library

# This function will play each note in your melody
def play_melody():
    # iterate over the notes of the melody:
    for this_note in range(0, 8):
        # to calculate the note duration, take one second
        # divided by the note type.
        # e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.
        note_duration = 1.0/note_durations[this_note]
        play_tone(melody[this_note], note_duration)
        # Space between each note\
        sleep(0.15)

# This function runs for each note in the melody
# inside of the play_melody() function.
# It turns the speaker_pin and and off very quickly to produce a sound wave.
def play_tone(note, duration):
    # If note is 0 don't play it
    if note == 0:
        sleep(duration)
        return
    #in physics, the period (sec/cyc) is the inverse of the frequency (cyc/sec)
    period = 1.0 / note
    #calcuate the time for half of the wave
    delay = period / 2
    #the number of waves to produce is the duration times the frequency
    cycles = int(duration * note)

    #start a loop from 0 to the variable "cycles" calculated above
    for i in range(cycles):
        GPIO.output(speaker_pin, True)   #set speaker_pin to high
        sleep(delay)    #wait with speaker_pin high
        GPIO.output(speaker_pin, False)    #set pin 18 to low
        sleep(delay)    #wait with speaker_pin low
        # play_tone code based off of:
        # http://www.linuxcircle.com/2015/04/12/how-to-play-piezo-buzzer-tunes-on-raspberry-pi-gpio-with-pwm/

speaker_pin = 15
button_pin = 14

button_state = 0

# notes in the melody - these numbers actually control the pitches.
# if you are interested in making music with this circuit, check out:
melody = [523, 294, 330, 349, 392, 0, 494, 523];

# note durations: 4 = quarter note, 8 = eighth note, etc.
# you only need to understand if you are interested in rhythm:
note_durations = [4,8,8,4,4,4,4,4];

# declaring pins as inputs and outputs
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN) # button attached to pin 14
GPIO.setup(speaker_pin, GPIO.OUT) # speaker attached to pin 15

# This will loop forever:
while True:
    # check the current state of the button
    button_state = GPIO.input(button_pin)
    # if the button IS pressed
    if button_state == 1: # 1 = pressed
        play_melody()
    elif button_state == 0: # 0 = NOT pressed
      pass # pass means do nothing
