import time

class PhotoResistor:
    """
    A component that can determine if there is light.
    """

    def __init__(self, adc_reader=None):
        self.__adc_reader = adc_reader

    def read_volts(self):
        return self.__adc_reader.read_volts()
