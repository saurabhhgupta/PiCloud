import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

broker = "192.168.0.22"
TOPIC = "picloud/final"

def on_connect(client, userdata, flags, rc):
	print("Connected with result code " + str(rc))
	client.subscribe(TOPIC)

def on_message(client, userdata, msg):
	message = str(msg.payload)
	print(msg.topic + " " + message)

def on_publish(mosq, obj, mid):
	print("mid: " + str(mid))
