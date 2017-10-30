# gpiozero and time are two python libraries we will use
# We are importing the LED() function from gpiozero
# and the sleep() function from time
from gpiozero import LED
from time import sleep

# We set the variable led to correspond to
# GPIO Pin 14 using the LED() function
led1 = LED(14) # Refer to Pin 14 as led1
led2 = LED(15) # Refer to Pin 25 as led2
led3 = LED(18) # Same for 18, 23, 24, 25, and 8
led4 = LED(23)
led5 = LED(24)
led6 = LED(25)
led7 = LED(8)

# This variable stores the amount of time we will delay
delayTime = 1

# This loop runs forever
while True:
    # Turns the LEDs on
    led1.on()
    led2.on()
    led3.on()
    led4.on()
    led5.on()
    led6.on()
    led7.on()
    # Pause for 1 second
    sleep(delayTime)
    # Turn the LEDs off
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    led5.off()
    led6.off()
    led7.off()
    # Pause for 1 second
    sleep(delayTime)
