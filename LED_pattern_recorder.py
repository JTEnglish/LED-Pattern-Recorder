import RPi.GPIO as GPIO
import time

RECORD_ON = False
LED_PATTERN = [26, 19, 13]
NEW_PATTERN = []

def btn_ISR(pin):
	global RECORD_ON
	global LED_PATTERN
	global NEW_PATTERN
	if pin == 4:
		if RECORD_ON:
			RECORD_ON = False
			if len(NEW_PATTERN) > 0:
				LED_PATTERN = NEW_PATTERN
		else:
			RECORD_ON = True
			LED_PATTERN = []
			NEW_PATTERN = []
		GPIO.output(6, RECORD_ON)
		print('Record:', RECORD_ON)
		
		if not RECORD_ON:
			LED_loop()
	else:
		if RECORD_ON:
			if pin == 25:
				NEW_PATTERN.append(26)
			elif pin == 24:
				NEW_PATTERN.append(19)
			elif pin == 23:
				NEW_PATTERN.append(13)
			print('New Pattern:', NEW_PATTERN)

def LED_loop():
	for led in LED_PATTERN:
		GPIO.output(led, True)
		time.sleep(0.5)
		GPIO.output(led, False)
		time.sleep(0.5)

def main():
	GPIO.setmode(GPIO.BCM)

	# Input Pins for Buttons
	GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Record Toggle Button
	GPIO.setup(25, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Button for LED 0
	GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Button for LED 1
	GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Button for LED 2

	# Output Pins for LEDs
	GPIO.setup(6, GPIO.OUT) # Record State Indicator LED
	GPIO.setup(26, GPIO.OUT) # LED 0
	GPIO.setup(19, GPIO.OUT) # LED 1
	GPIO.setup(13, GPIO.OUT) # LED 2

	# Add ISR Button Events
	GPIO.add_event_detect(4, GPIO.FALLING, callback=btn_ISR, bouncetime = 100)
	GPIO.add_event_detect(25, GPIO.FALLING, callback=btn_ISR, bouncetime = 100)
	GPIO.add_event_detect(24, GPIO.FALLING, callback=btn_ISR, bouncetime = 100)
	GPIO.add_event_detect(23, GPIO.FALLING, callback=btn_ISR, bouncetime = 100)

	try:
		while True:
			pass
	finally:
		GPIO.cleanup()

if __name__ == "__main__":
    main()
