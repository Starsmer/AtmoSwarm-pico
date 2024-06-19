from mqtt.simple import MQTTClient
from SETTINGS import ID, BROKER

class Publisher:
    
    def __init__(self):
        #CLIENT_ID = ID #ubinascii.hexlify(machine.unique_id())
        self.TOPIC = f"{ID}-Temp"

        print(f"Begin connection with MQTT Broker :: {BROKER}")
        self.Client = MQTTClient(ID, BROKER, keepalive=10)
        #self.Client.set_callback(sub_cb)
        #self.Client.connect()
        print(f"Connected to MQTT Broker :: {BROKER}")


    def push(self, msg):
        self.Client.connect()
        msg = msg.encode()
        self.Client.publish(self.TOPIC, msg)
        self.Client.disconnect()        
        
