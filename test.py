from simpili import GPIO
from time import sleep

sleep(2)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUTPUT)

while True:
    GPIO.write(13, GPIO.HIGH)
    sleep(1)
    GPIO.write(13, GPIO.LOW)
    sleep(1)