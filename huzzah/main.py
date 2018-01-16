#import network
#import webrepl

import board
import digitalio

from time import sleep
from ucollections import namedtuple

from screen import Screen

NAME=''

jobs = namedtuple('jobs', 'a b c')
JOBS = jobs(a='', b='', c='')
emails = namedtuple('emails', 'a b c')
EMAILS = emails(a='', b='', c='')

NUMBER = 0
INTERNATIONAL = True

# WiFi details if required
#SSID = ''
#PASSWD = ''
#wlan = network.WLAN(network.STA_IF)
#wlan.active(True)
#wlan.connect(SSID, PASSWD)

# digital input pins for the FeatherWing input buttons on the Feather HUZZAH
buttonA = digitalio.DigitalInOut(board.GPIO0)
buttonB = digitalio.DigitalInOut(board.GPIO16)
buttonC = digitalio.DigitalInOut(board.GPIO2)
'''
variable declarations
'''
modulo = 0  # buttonC increment counter
delay = 0.5  # built-in delay between readings

'''
"void"() {} setup
'''
# set up MicroPython web REPL if wifi is configured
#if SSID:
#    wlan = network.WLAN(network.STA_IF)
#    wlan.active(True)
#    webrepl.start()

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
    #if not buttonB.value():
    #    screen.voltage(False)
    #    sleep(2)

    if not buttonA.value():
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
