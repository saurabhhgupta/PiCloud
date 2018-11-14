#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time

# create client instance & connect to localhost
client = mqtt.Client()
client.connect("localhost", 1883, 60)

# publish message to topic/iopi and set pin 1 on bus 1 to ON
client.publish("topic/iopi", "1,1");
time.sleep(2)

# publish message to topic/iopi and set pin 1 on bus 1 to OFF
client.publish("topic/iopi", "1,0");
time.sleep(2)

# publish message to topic/iopi and set pin 1 on bus 2 to ON
client.publish("topic/iopi", "17,1");
time.sleep(2)

# publish message to topic/iopi and set pin 1 on bus 2 to OFF
client.publish("topic/iopi", "17,0");

client.disconnect();
