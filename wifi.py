ionimport network
import utime
import SETTINGS

'''
references:
https://datasheets.raspberrypi.com/picow/connecting-to-the-internet-with-pico-w.pdf
'''
class Wifi():
    """Class for Wifi connection"""
    def __init__(self, lan = SETTINGS.wifi, pw = SETTINGS.pw):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(lan, pw)

        while not wlan.isconnected() and wlan.status() >= 0:
          print("Waiting to connect:")
          utime.sleep(5)

        print(wlan.ifconfig())


