import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

light_on = False

while True:
	button_state = GPIO.input(24)
	if button_state == False:
		print("Button Pressed!\n")
		if light_on == True:
			print("Light turning off\n") 
			light_on = False
		else:
			print("Light turning on\n")
			light_on = True
	if light_on == True:
		GPIO.output(18, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(18, GPIO.LOW)
		time.sleep(1)
	else:
		time.sleep(1)
		
