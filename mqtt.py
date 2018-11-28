from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

import time
# import paho.mqtt.client as mqtt
# import paho.mqtt.publish as publish

broker = "ahuv6nrfa9swh-ats.iot.us-east-2.amazonaws.com"
TOPIC = "finalproj/test"

def on_connect(client, userdata, flags, rc):
	print("Connected with result code " + str(rc))
	client.subscribe(TOPIC)

def on_message(client, userdata, msg):
	message = str(msg.payload)
	print(msg.topic + " " + message)

def on_publish(mosq, obj, mid):
	print("mid: " + str(mid))
