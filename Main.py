import time
import machine
from temp import Temp
from SETTINGS import ID, INTERVAL
from publisher import Publisher

last_publish = 30
publish_interval = INTERVAL

def reset():
   '''Reset device'''
    print("Resetting...")
    time.sleep(5)
    machine.reset()
    

def main():
   '''main loop'''
    P = Publisher()
    T = Temp()
    while True:
            # Non-blocking wait for message
            # mqttClient.check_msg()
            global last_publish
            if (time.time() - last_publish) >= publish_interval or not last_publish:
                temp = T.get_temp()
                P.push(str(round(temp,2)))
                print(temp, last_publish - time.time())
                last_publish = time.time()

            time.sleep(10)


if __name__ == "__main__":
    T = Temp()
    while True:
        try:
            main()
        except OSError as e:
            print("Error: " + str(e))
            main()  #reset()
