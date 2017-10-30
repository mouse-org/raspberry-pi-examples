# gpiozero and time are two python libraries we will use
# We are importing the LED() function from gpiozero and the sleep() function from time
from gpiozero import LED
from time import sleep

# We set the variable led to correspond to GPIO Pin 14 using the LED() function
led = LED(14)

# This loop runs forever
while True:
    # Turns the LED on
    led.on()
    # Pause for 1 second
    sleep(1)
    # Turn the LED off
    led.off()
    # Puase for 1 second
    sleep(1)
