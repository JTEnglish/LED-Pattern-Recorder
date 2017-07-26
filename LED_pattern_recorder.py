import RPi.GPIO as GPIO
import time

def record_btn_ISR(pin):
    print(pin)

def main():
    GPIO.setmode(GPIO.BCM)

    # Input Pins for Buttons
    GPIO.setup(4, GPIO.IN) # Record Toggle Button
    GPIO.setup(22, GPIO.IN) # Button for LED 0
    GPIO.setup(27, GPIO.IN) # Button for LED 1
    GPIO.setup(17, GPIO.IN) # Button for LED 2

    # Output Pins for LEDs
    GPIO.setup(6, GPIO.OUT) # Record State Indicator LED
    GPIO.setup(26, GPIO.OUT) # LED 0
    GPIO.setup(19, GPIO.OUT) # LED 1
    GPIO.setup(13, GPIO.OUT) # LED 2

    GPIO.add_event_detect(4, GPIO.FALLING)
    GPIO.add_event_callback(4, record_btn_ISR, 100)

    GPIO.output(6, False)

    pattern = []

    while True:
        for led in pattern:
            GPIO.output(led, True)
            time.sleep(0.5)
            GPIO.output(led, False)
            time.sleep(0.5)

    GPIO.cleanup()

if __name__ == "__main__":
    main()
