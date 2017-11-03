# Input

# Import libraries:
from gpiozero import LightSensor
from time import sleep

# Set input_pin to be pin 4
sensor_pin = 4

ldr = LightSensor(sensor_pin)

# Start loop:
while True:
  print(ldr.value)
  sleep(0.25)