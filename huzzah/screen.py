import board
import bitbangio as io
#import analogio

import adafruit_ssd1306

from ucollections import namedtuple

# setup OLED FeatherWing in I2C mode
i2c = io.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
#adc = analogio.AnalogIn(board.ADC)


class Screen:
    '''
    Screen: display various text screens on the OLED FeatherWing
        * name: displays name and a tagline for work
        * email: displays an email address split at the @ symbol
        * mobile: displays a mobile number in Australian or International format
        * voltage: displays the current voltage on the BAT pin
          (to estimate remaining LiPo battery life)
    '''

    def __init__(self, jobs):
        # Display taglines as initial screen for selection via hardware input
        oled.fill(0)
        oled.text('A: %s' % jobs.a, 0, 0)
        oled.text('B: %s' % jobs.b, 0, 8)
        oled.text('C: %s' % jobs.c, 0, 16)
        oled.show()

    def name(self, name, job):
        # Display name and tagline
        nameText = self.__centreText(name)
        jobText = self.__centreText(job)

        oled.fill(0)
        oled.text(self.__generateUnderscore(nameText.text),
                   nameText.spacing, 6)
        oled.text(nameText.text, nameText.spacing, 0)
        oled.text(jobText.text, jobText.spacing, 24)
        oled.show()

    def email(self, email):
        # Display email, split and carry to newline at the @ symbol
        if len(email) > 16:
            string = email.split('@')
            line1 = '%s%s' % (string[0], '@')
            line2 = '%s%s' % (' ', string[1])

        oled.fill(0)
        oled.text('email:', 0, 0)
        if len(email) > 16:
            oled.text(line1, 0, 16)
            oled.text(line2, 0, 24)
        else:
            oled.text(email, 0, 16)
        oled.show()

    def mobile(self, number, international):
        # Display mobile number, international boolean determines string format
        mobile = '%s' % number

        if not international:
            mobile = '0%s' % mobile
            mobile = list(mobile)
            mobile.insert(4, ' ')
            mobile.insert(8, ' ')
            mobile = ''.join(mobile)
        else:
            mobile = '+61%s' % mobile

        oled.fill(0)
        oled.text('mobile:', 0, 0)
        oled.text(mobile, 0, 16)
        oled.show()

    '''
    def voltage(self, analog):
        # Display current BAT pin voltage to estimate remaining LiPo battery life,
        # analog boolean determines whether or not to display analog reading.
        # R1 and R2 values of resistors used to scale voltage to under 1V.
        CF = .9 ** -3  # >5V reading as {0,999} scaled to .9V by voltage divider
        R1 = 15000  # R1, 15kΩ
        R2 = 3300  # R2, 3k3Ω

        def voltageRead(Vout, R1, R2):
            # Calculate V_in using the ideal voltage formula:
            #                Z_2
            #     V_out = --------- . V_in
            #             Z_1 + Z_2
            #   => V_in = V_out / (Z_2 / (Z_1 + Z_2))
            Vin = Vout / (R2 / (R1 + R2))
            return Vin

        if (analog):
            aline = 0:w
            vline = 8
        else:
            vline = 0

        reading = adc.value()
        oled.fill(0)
        if (analog):
            oled.text('ADC:         %s' % reading, 0, aline)
        oled.text('Voltage:   %.2fV' %
                   voltageRead((reading * CF), R1, R2), 0, vline)
        oled.show()
    '''

    # private methods

    def __centreText(self, string):
        '''
        Generate a string with corrent indentation values to centre text
        '''
        text = namedtuple("text", "text spacing")
        spacing = (16 - len(string)) * 4
        if spacing < 0:
            spacing = 0
        result = text(string, spacing)

        return result

    def __generateUnderscore(self, text):
        '''
        Generate a string of '-' characters = to the length of a given string
        '''
        underscore = []
        for count in range(0, len(text)):
            underscore.append('-')
        result = ''.join(underscore)

        return result

