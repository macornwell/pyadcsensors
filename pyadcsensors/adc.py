import time
import Adafruit_ADS1x15
DEFAULT_GAIN = 1

GAIN_TO_VOLTS = {
    2/3: 6.144,
    1: 4.096,
    2: 2.048,
    4: 1.024,
    8: 0.512,
    16: 0.256,
}


class ADCReader:
    low = 0
    high = 32767
    position = 0

    def __init__(self, position, adc, gain=DEFAULT_GAIN):
        self.adc = adc
        self.gain = gain 
        self.position = position

    def read_raw(self):
        return self.adc.read_adc(self.position, gain=DEFAULT_GAIN)

    def read_volts(self):
        value = self.read_raw()
        voltage = GAIN_TO_VOLTS[self.gain]
        return value * voltage / self.high


class ADS1115Reader(ADCReader):
    """
    An ADC Reader based around the ADS1115
    """

    def __init__(self, position, gain=DEFAULT_GAIN):
        super().__init__(position, Adafruit_ADS1x15.ADS1115(), gain=gain)

