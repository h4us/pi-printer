import RPi.GPIO as GPIO

from PIL import Image
from thermalprinter import *

import time

lasttime = time.time()
def switch_callback(gpio_pin):
    global lasttime

    print(gpio_pin)
    if time.time() - lasttime > 3:
        with ThermalPrinter(port='/dev/ttyAMA0', baudrate=115200, rtscts=True) as printer:
            # Picture
            printer.feed(3)
            printer.image(Image.open('pcm-logo-vvv.jpg'))
            printer.feed(30)

            # Styles
            printer.out('    P-Code Magazine / 2019')
            printer.feed(3)
        lasttime = time.time()

GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.IN)

GPIO.add_event_detect(20, GPIO.BOTH, bouncetime=100)
GPIO.add_event_callback(20, switch_callback)

try:
    while True:
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
