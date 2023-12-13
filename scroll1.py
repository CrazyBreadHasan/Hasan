import RPi.GPIO as GPIO
import drivers
from time import sleep

# Load the driver and set it to "display"
display = drivers.Lcd()

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set the pin number for the backlight
backlight_pin = 18

# Set the pin as output
GPIO.setup(backlight_pin, GPIO.OUT)

# Create a PWM object with a frequency of 100 Hz
pwm = GPIO.PWM(backlight_pin, 100)

# Start the PWM with a duty cycle of 0 (off)
pwm.start(0)

# Set the backlight color to green
display.backlight(display.GREEN)

# Loop through different duty cycles to change the brightness
try:
    while True:
        # Increase the brightness from 0 to 100
        for dc in range(0, 101, 5):
            pwm.ChangeDutyCycle(dc)
            sleep(0.1)
        # Decrease the brightness from 100 to 0
        for dc in range(100, -1, -5):
            pwm.ChangeDutyCycle(dc)
            sleep(0.1)
except KeyboardInterrupt:
    # Stop the PWM and clean up the GPIO
    pwm.stop()
    GPIO.cleanup()