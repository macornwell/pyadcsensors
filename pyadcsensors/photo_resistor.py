import time
from adc import ADCReader
import RPi.GPIO as GPIO 

class PhotoResistor:
    """
    A component that can determine if there is light.
    """

    def __init__(self, adc_reader=None):
        self.__adc_reader = adc_reader or ADCReader(0)

    def read_volts(self):
        return self.__adc_reader.read_volts()

class PhotoResistorAnalysis:

    def __init__(self):
        pass

    def is_dark(self, ground_resistor, value_in_volts):
        """
        Determines if a photoresistor reading is seeing darkness.
        """




def main():
    device = PhotoResistor()
    lines = []
    try:
        while True:
            volts = device.read_volts()
            print('Volts: ', volts)
            time.sleep(1)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
