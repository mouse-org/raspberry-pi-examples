# Nightlight


# Import libraries:
from gpiozero import LightSensor, LED
from time import sleep

# Set pins:
sensor_pin = 4
led_pin = 14

# Connect pins to functions to use them:
ldr = LightSensor(sensor_pin)
led = LED(led_pin)
# If your led is always on try making this number lower.
# If your led is not turning on, try making this number higher.
threshold = 0.7

# Start Loop
while True:
	# This fixes the bug of reading full voltage as 0
    if ldr.value == 0:
      print(1.0)
    else:
      print(ldr.value)
      # If the input_pin reads lower than the threshold turn the light on
      if ldr.value < threshold:
        led.on()
      else:
        led.off()
    # Pause for a fraction of a second.
    # The Raspberry Pi will check the value 400 times per second.
    sleep(0.0025)
