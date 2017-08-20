import time
from datetime import datetime

TOTALLY_DRY = 0.09
DRY = 0.10
MOIST = 1.50
TOTALLY_WET = 2.5

STATES = {
        TOTALLY_DRY : 'Very Dry',
        DRY : 'Dry',
        MOIST : 'Moist',
        TOTALLY_WET : 'Wet',
}

class VegetronixSMS:
    """
    A vegetronix soil moisture sensor.
    """
    def __init__(self, adc_reader):
        self.__adc_reader = adc_reader

    def read_volts():
        return self.__adc_reader.read_volts()

    def read():
        value = self.read_volts()
        if value <= TOTALLY_DRY:
            return STATES[TOTALLY_DRY]
        if value < MOIST:
            return STATES[DRY]
        if value < TOTALLY_WET:
            return STATES[MOIST]
        return STATES[TOTALLY_WET]
