# Input

# Import libraries:
from gpiozero import LightSensor
from time import sleep

# Set input_pin to be pin 4
input_pin = 4

ldr = LightSensor(input_pin)

while True:
  print(ldr.value)
  sleep(0.25)