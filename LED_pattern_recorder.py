import RPi.GPIO as GPIO
import time

RECORD_ON = False
LED_PATTERN = []

def record_btn_ISR(pin):
#	print('Record Button ISR Called')
	if GPIO.input(18):
		global RECORD_ON
		if not RECORD_ON:
			print('Recording Started')
			RECORD_ON = True
			GPIO.output(6, True)
			record_pattern()
		else:
			print('Recording Stopped')
			RECORD_ON = False
			GPIO.output(6, False)
	
def record_pattern():
	global LED_PATTERN
	LED_PATTERN = []
	while RECORD_ON:
		if GPIO.input(25):
			print('Button 0 Recorded')
			LED_PATTERN.append(26)
		elif GPIO.input(24):
			print('Button 1 Recorded')
			LED_PATTERN.append(19)
		elif GPIO.input(23):
			print('Button 2 Recorded')
			LED_PATTERN.append(13)
		time.sleep(0.2)

def main():
    GPIO.setmode(GPIO.BCM)

    # Input Pins for Buttons
    GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Record Toggle Button
    GPIO.setup(22, GPIO.IN) # Button for LED 0
    GPIO.setup(27, GPIO.IN) # Button for LED 1
    GPIO.setup(17, GPIO.IN) # Button for LED 2

    # Output Pins for LEDs
    GPIO.setup(18, GPIO.OUT) # Record State Indicator LED
    GPIO.setup(25, GPIO.OUT) # LED 0
    GPIO.setup(24, GPIO.OUT) # LED 1
    GPIO.setup(23, GPIO.OUT) # LED 2

    GPIO.add_event_detect(4, GPIO.FALLING, callback=record_btn_ISR, bouncetime = 100)
    #GPIO.add_event_callback(4, record_btn_ISR)

    #GPIO.output(6, False)

    while True:
        #try:
            for led in LED_PATTERN:
                GPIO.output(led, True)
                time.sleep(0.5)
                GPIO.output(led, False)
                time.sleep(0.5)
        #finally:
            #GPIO.cleanup()

if __name__ == "__main__":
    main()
