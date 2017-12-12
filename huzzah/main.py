# import network
# import webrepl

import machine

from time import sleep
from ucollections import namedtuple

from constants import *
from screen import Screen

'''
# WiFi details if required
SSID = ''
PASSWD = ''
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWD)
'''

# digital input pins for the FeatherWing input buttons on the Feather HUZZAH
buttonA = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
buttonB = machine.Pin(16, machine.Pin.IN)  # pin 16 has a 100kΩ pullup
buttonC = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)

'''
variable declarations
'''
modulo = 0  # buttonC increment counter
delay = 0.5  # built-in delay between readings

'''
"void"() {} setup
'''
# set up MicroPython web REPL if wifi is configured
if SSID:
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    webrepl.start()

screen = Screen(JOBS)
tag = None

# wait for initial input to determine tagline and email
while not tag:
    # inputs are pulled up, value False when triggered.
    if not buttonA.value():
        tag = JOBS.a
        email = EMAILS.a
    elif not buttonB.value():
        tag = JOBS.b
        email = EMAILS.b
    elif not buttonC.value():
        tag = JOBS.c
        email = EMAILS.c

screen.name(NAME, tag)
sleep(1)

'''
"main"() {} loop
'''
while True:
    # inputs are pulled up, value False when triggered.
    if not buttonA.value():
        screen.voltage(False)
        sleep(2)

    if not buttonC.value():
        modulo += 1
        sleep(delay)

    # cycle through screens using modular arithmetic in Z_n where n = 3,
    # expandable by increasing n
    n = 3
    if (modulo % n == 0):
        screen.name(NAME, tag)
    elif (modulo % n == 1):
        screen.email(email)
    elif (modulo % n == 2):
        screen.mobile(NUMBER, INTERNATIONAL)
