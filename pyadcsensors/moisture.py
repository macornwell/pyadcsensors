import time
from datetime import datetime
from adc import ADCReader

DRY = 0.09
WET = 2.5

def print_value(value):
    print('{0} - {1}'.format(datetime.now().strftime('%Y%m%d-%H%M%S'), value))
    if value > WET:
        print('Totally Wet.')
    elif value <= DRY:
        print('Totally Dry')


def main():
    while True:
        adc = ADCReader(0)
        value = adc.read_volts()
        print_value(value)
        time.sleep(2)


if __name__ == '__main__':
    main()
