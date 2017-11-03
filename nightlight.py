from gpiozero import LightSensor, LED
from time import sleep
ldr = LightSensor(4)  # alter if using a different pin
led = LED(14)
while True:
    if ldr.value == 0:
      print(1.0)
    else:
      print(ldr.value)
      if ldr.value < 0.3:
        led.on()
      else:
        led.off()
    sleep(0.25)