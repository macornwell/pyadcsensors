import time
import re
from datetime import datetime


class WaterFlowPrinter:
    __number_re = re.compile(r'(?P<tens>\d)\.(?P<ones>\d)')

    def print_value(self, value):
        match = self.__number_re.match(str(value))
        tens = int(match.groups('tens')[0]) * 10 * 2
        ones = int(match.groups('ones')[0]) *2
        to_print = ''
        for i in range(0, tens + ones):
            to_print += '-'
        print(to_print)


class YFS403:
    __milliliters_per_pulse = 2.25
    __pulses_per_liter = 450
    __zero = re.compile(r'^((0.00)|(4.096))')
    __window = re.compile(r'(?P<data>\d\.\d\d\d)')

    def __init__(self, adc_reader)
        self.__adc_reader = adc_reader

    def read_raw(self):
        return self.__adc_reader.read_volts()

    def monitor_hertz(self, average_time_in_seconds=1):
        values = self.__monitor_values(average_time_in_seconds)
        pulses = self.__calculate_pulses(values)
        return pulses / average_time_in_seconds

    def __monitor_values(self, length_in_seconds):
        end = time.time() + length_in_seconds 
        values = []
        while time.time() < end:
            value = self.__adc_reader.read_volts()
            values.append(value)
        return values

    def __calculate_pulses(self, values):
        pulses = 0
        current_pulse_value = 0.00
        going_up = True
        previous_was_zero = False
        # We are trying to find peaks. The value increases until it hits a top
        # then goes backwards. When we find those, those are pulses.
        for val in values:
            val = float(self.__window.match(str(val)).groups('data')[0])
            is_zero = self.__zero.match(str(val))
            if is_zero:
                #current_pulse_value = val
                continue
                if previous_was_zero:
                    # Just skipping entirely
                    continue
                previous_was_zero = True
            # It's now going down.
            if val < current_pulse_value:
                # If it was going up, but now its down, its a peak
                if going_up:
                    going_up = False
                    pulses += 1
                    print('val: {0}'.format(val))
                    print('cur: {0}'.format(current_pulse_value))
                else:
                    # Do nothing. We're riding our way down.
                    pass
                pass
            else:
                # It was going down, but now its turned around.
                if not going_up:
                    going_up = True
                else:
                    # Do nothing. Its still going up.
                    pass
            previous_was_zero = is_zero
            current_pulse_value = val
        return pulses

    def calculate_liters_per_hour(self, hertz):
        return self.calculate_liters_per_minute(hertz) * 60

    def calculate_liters_per_minute(self, hertz):
        return hertz / 7.5

    def calculate_liters_per_second(self, hertz):
        return self.calculate_liters_per_minute(hertz) / 60

    def calculate_gallons_per_minute(self, hertz):
        lph = self.calculate_liters_per_minute(hertz)
        return lph / 3.78541
