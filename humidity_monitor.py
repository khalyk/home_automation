#!/usr/bin/python

import pigpio
import ouimeaux
import time
import DHT22
from ouimeaux.environment import Environment

INTERVAL=60

# what GPIO is the DHT22/AM2302 plugged into?
GPIO=4

# name of WeMo switch that dehumidifier is plugged into
WEMO="Bedroom"

pi = pigpio.pi()
s = DHT22.sensor(pi, GPIO)

r = 0

next_reading = time.time()

# scan environment and discover WeMo switch
env = Environment()
env.start()
env.discover(10)

while True:
    r += 1
    s.trigger()
    time.sleep(0.2)
    print("{} {} {} {:3.2f} {} {} {} {}".format(
        r, s.humidity(), s.temperature(), s.staleness(),
        s.bad_checksum(), s.short_message(), s.missing_message(),
        s.sensor_resets()))
    if (s.humidity() >= 50):
        print "High humidity level detected, turning on dehumidifer..."
        switch.on()
    if (s.humidity() <= 45):
        print "Humidity level normal, turning off dehumidifier..."
        switch.off()
    next_reading += INTERVAL
    time.sleep(next_reading-time.time()) # Overall INTERVAL second polling.

s.cancel()
pi.stop()
