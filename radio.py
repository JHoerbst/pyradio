#!/usr/bin/env python

import mpyg321.mpyg321
import subprocess
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

on = 0
off_counter = 0

while True:
    time.sleep(0.05)
    if GPIO.input(5) == GPIO.HIGH:
        if on == 0:
            on = 1
            subprocess.Popen("mpg321 http://orf-live.ors-shoutcast.at/fm4-q2a",shell=True)
    else:
        off_counter += 1
        if off_counter == 5:
            if on == 1: 
               subprocess.Popen("killall mpg321",shell=True)
            on = 0
            off_counter = 0

