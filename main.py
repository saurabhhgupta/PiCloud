#!/usr/bin/python

import os
import time
import threading
# import paho.mqtt.publish as publish

from mqtt import *
from helper import *
from timestamp import timestamp
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

INTERVAL = 3.0

def measure_cpu():
	temp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
	return (float(temp) / 1000.0)

def measure_gpu():
	temp = os.popen("vcgencmd measure_temp").readline()
	return float((temp.replace("temp=", "").replace("'C", "")))

def display_cpu_temp():
	global INTERVAL
	print(measure_cpu())

def display_gpu_temp():
	global INTERVAL
	print(measure_gpu())

packetized_data = []
def main():
        client = AWSIoTMQTTClient("test_client")
        client.configureEndpoint("ahuv6nrfa9swh-ats.iot.us-east-2.amazonaws.com", 8883)
        client.configureCredentials("AmazonRootCA1.pem", "c4a552c0e6-private.pem.key", "c4a552c0e6-certificate.pem.crt")
        # client.configureOfflinePublishQueueing(-1)
        # client.configureDrainingFrequency(2)
        # client.configureConnectDisconnectTimeout(10)
        # client.configureMQTTOperationTimeout(5)

	# Step 1.
	# threading.Timer(INTERVAL, main).start()
	# packetized_data.append(measure_cpu())
	# print(timestamp(), measure_cpu(), measure_gpu())



        '''
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect(broker, 1883, 60)
	client.loop_start()
        '''

#	client.publish(TOPIC, str(packetized_data))
        client.connect()
        print "connected"
	
        client.subscribe("finalproj/test", 1, "gay")
        #client.publish("finalproj/test", "brandon if you see this, call me a bitch rn", 0)
        client.publish("finalproj/test", str(measure_gpu()), 0)
	print "published"
        client.disconnect()
        # time.sleep(1*60)

if __name__ == '__main__':
	main()
