#!/usr/bin/python

import os
import time
import threading
import json
import sched

from mqtt import *
from helper import *
from timestamp import timestamp
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

TIME_INTERVAL = 5.0
SLEEP_INTERVAL = 1.0
s = sched.scheduler(time.time, time.sleep)
temperatures = {}

def measure_cpu():
	temp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
	return (float(temp) / 1000.0)

def measure_gpu():
	temp = os.popen("vcgencmd measure_temp").readline()
	return float((temp.replace("temp=", "").replace("'C", "")))

def measure_both(sc, client):
	global temperatures

	client.connect()
	print "connect client... done."

	temperatures["CPU"] = measure_cpu()
	temperatures["GPU"] = measure_gpu()
#	send_packet = (measure_cpu(), measure_gpu())
	json_send_packet = json.dumps(temperatures)

	client.publish("picloud/test", json_send_packet, 0)
	print "publishing... done."

	s.enter(TIME_INTERVAL, SLEEP_INTERVAL, measure_both, (sc, client))

	client.disconnect()
	print "disconnect client... done."

def main():
	global s
	print "create client... done."
        client = AWSIoTMQTTClient("PiCloudy")
        print "configuring endpoint... done."
	client.configureEndpoint("ahuv6nrfa9swh-ats.iot.us-west-2.amazonaws.com", 8883)
        print "configure credentials... done."
	client.configureCredentials("AmazonRootCA1.pem", "Certificates/3fb5119996-private.pem.key", "Certificates/3fb5119996-certificate.pem.crt")

        s.enter(TIME_INTERVAL, SLEEP_INTERVAL, measure_both, (s, client))
	s.run()

if __name__ == '__main__':
	main()
