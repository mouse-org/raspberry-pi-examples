# gpiozero and time are two python libraries we will use
# We are importing the LED() function from gpiozero
# and the sleep() function from time
from gpiozero import LED
from time import sleep

# We set the variable led to correspond to
# GPIO Pin 14 using the LED() function
led_pin_1 = LED(14) # Refer to Pin 14 as led1
led_pin_2 = LED(15) # Refer to Pin 25 as led2
led_pin_3 = LED(18) # Same for 18, 23, 24, 25, and 8
led_pin_4 = LED(23)
led_pin_5 = LED(24)
led_pin_6 = LED(25)
led_pin_7 = LED(8)

# This variable stores the amount of time we will delay
delay_time = 1

# This loop runs forever
while True:
    # Turns the LEDs on
    led_pin_1.on()
    led_pin_2.off()
    led_pin_3.on()
    led_pin_4.off()
    led_pin_5.on()
    led_pin_6.off()
    led_pin_7.on()
    # Pause for 1 second
    sleep(delay_time)
    # Turn the LEDs off
    led_pin_1.off()
    led_pin_2.on()
    led_pin_3.off()
    led_pin_4.on()
    led_pin_5.off()
    led_pin_6.on()
    led_pin_7.off()
    # Pause for 1 second
    sleep(delay_time)
