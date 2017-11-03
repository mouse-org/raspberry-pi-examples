# Nightlight


# Import libraries:
from gpiozero import LightSensor, LED
from time import sleep

# Set pins:
input_pin = 4
led_pin = 14

# Connect pins to functions to use them:
ldr = LightSensor(input_pin)
led = LED(led_pin)

# Start Loop
while True:
	# This fixes the bug of reading full voltage as 0
    if ldr.value == 0:
      print(1.0)
    else:
      print(ldr.value)
      # If the input_pin reads lower than 0.3 turn the light on
      if ldr.value < 0.3:
        led.on()
      else:
        led.off()
    sleep(0.25)