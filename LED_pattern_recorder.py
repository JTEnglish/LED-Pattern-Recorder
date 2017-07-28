import RPi.GPIO as GPIO
import time

RECORD_ON = False
LED_PATTERN = []

def btn_ISR(pin):
	global RECORD_ON
	global LED_PATTERN
	if pin == 4:
		if RECORD_ON:
			RECORD_ON = False
			GPIO.output(6, True)
		else:
			RECORD_ON = True
			LED_PATTERN = []
			GPIO.output(6, False)
	else:
		if RECORD_ON:
			if pin == 25:
				LED_PATTERN.append(26)
			elif pin == 24:
				LED_PATTERN.append(19)
			elif pin == 23:
				LED_PATTERN.append(13)

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
	GPIO.add_event_detect(22, GPIO.FALLING, callback=btn_ISR, bouncetime = 100)
	GPIO.add_event_detect(27, GPIO.FALLING, callback=btn_ISR, bouncetime = 100)
	GPIO.add_event_detect(17, GPIO.FALLING, callback=btn_ISR, bouncetime = 100)

	try:
	    while True:
	            for led in LED_PATTERN:
	                GPIO.output(led, True)
	                time.sleep(0.5)
	                GPIO.output(led, False)
	                time.sleep(0.5)
	finally:
		GPIO.cleanup()

if __name__ == "__main__":
    main()
