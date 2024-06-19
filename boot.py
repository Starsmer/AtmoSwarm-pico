#  runs main loop on boot
import network, utime, machine
from wifi import Wifi
import Main

Wifi()

if __name__ == '__main__':
    Main.main()
