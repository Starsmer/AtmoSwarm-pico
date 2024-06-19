import machine
from wifi import Wifi

class Temp:
    """Class for retrieving on-board Temporature sensor data"""
    def __init__(self):
        self.sensor = machine.ADC(4)
        self.conv_factor = 3.3 / (65336)

    def get_temp(self):
        """Returns temp reading in F"""
        reading = self.sensor.read_u16() * self.conv_factor
        temp = 27 - (reading - 0.706) / 0.001721
        fahr = temp * 9/5 + 32
        return fahr


if __name__ == '__main__':
    Wifi(env.wifi, env.pw)
    T = Temp()
    while True:
        print(T.get_temp(), end = "\r")
        utime.sleep(1)
        led.toggle
        utime.sleep(1)

