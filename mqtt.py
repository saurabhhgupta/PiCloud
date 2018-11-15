import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

broker = "xxx.xxx.x.xxx"
sub_topic = "picloud/recv"
pub_topic = "picloud/send"

def on_connect(client, userdata, flags, rc):
	print("Connected with result code " + str(rc))
	client.subscribe(sub_topic)

def on_message(client, userdata, msg):
	message = str(msg.payload)
	print(msg.topic + " " + message)
	# display_sensehat(message)

def on_publish(mosq, obj, mid):
	print("mid: " + str(mid))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, 1883, 60)
client.loop_start()

while True:
	# packetize everything into an array
	PACKETIZED_DATA = []
	client.publish(pub_topic, str(PACKETIZED_DATA))
	time.sleep(1*60)
