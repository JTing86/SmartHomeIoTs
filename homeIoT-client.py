import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import serial
import json

Broker = "192.168.0.196" #JT-BlackBox
sub_topic = "homeIoT/lock/test"
pub_topic = "homeIoT/sensor/test"

time.sleep(2)

###################### MQTT Connection ####################

#when connecting to mqtt:
def on_connect(client, usrData, flags, rc):
    client.subscribe(sub_topic)
    print("Connected with result code" + str(rc))
    

#when receiving a message:
def on_message(client, usrData, msg):
    message=str(msg.payload)
    print(msg.topic+" "+message)
    
    
client=mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(Broker)
client.loop_start()

while True:
    client.publish(pub_topic, "test from homeIoT") #data need to be something
    time.sleep(60)