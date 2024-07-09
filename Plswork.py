import RPi.GPIO as GPIO
import os
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin for the switch
switch_pin = 17

# Set up the GPIO pin as an input with a pull-up resistor
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    print("Waiting for the switch to be pressed...")
    # Wait for the switch to be pressed (GPIO goes LOW)
    GPIO.wait_for_edge(switch_pin, GPIO.FALLING)
    
    print("Switch pressed! Shutting down...")
    # Add a small delay to debounce the switch
    time.sleep(0.2)

    # Execute the shutdown command
    os.system("sudo shutdown -h now")

except KeyboardInterrupt:
    # Clean up GPIO settings if the script is interrupted
    GPIO.cleanup()

GPIO.cleanup()
