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

topic = "picloud/test"
TIME_INTERVAL = 5.0
SLEEP_INTERVAL = 1.0
function_scheduler = sched.scheduler(time.time, time.sleep)
packet = {}

def measure_cpu():
	temp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
	return (float(temp) / 1000.0)

def measure_gpu():
	temp = os.popen("vcgencmd measure_temp").readline()
	return float((temp.replace("temp=", "").replace("'C", "")))

def fahrenheit_to_celsius(value):
        return ((value - 32) * 5.0/9.0)

def celsius_to_fahrenheit(value):
        return ((9.0/5.0 * value) + 32)

def threaded(scheduler, client, connection_count):
	global packet
        connection_count += 1

	client.connect()
	print "[{}] Connecting client... done.".format(connection_count)

	timestamp = time.localtime()
        packet["timestamp"] =  time.strftime("%Y-%m-%d %H:%M:%S", timestamp)
	packet["CPU"] = measure_cpu()
	packet["GPU"] = measure_gpu()
	send_packet = json.dumps(packet)

	client.publish(topic, send_packet, 0)
	print "[{}] Publishing... done.".format(connection_count)

	function_scheduler.enter(TIME_INTERVAL, SLEEP_INTERVAL, threaded, (scheduler, client, connection_count))

	client.disconnect()
	print "[{}] Disconnecting client... done.".format(connection_count)

def main():
	global function_scheduler
	connection_count = 0

	print "Starting PiCloud."
	print "Creating client... done."
        client = AWSIoTMQTTClient("PiCloudy")
        print "Configuring endpoint... done."
	client.configureEndpoint("ahuv6nrfa9swh-ats.iot.us-west-2.amazonaws.com", 8883)
        print "Configuring credentials... done."
	client.configureCredentials("AmazonRootCA1.pem", "Certificates/3fb5119996-private.pem.key", "Certificates/3fb5119996-certificate.pem.crt")

        function_scheduler.enter(TIME_INTERVAL, SLEEP_INTERVAL, threaded, (function_scheduler, client, connection_count))
        function_scheduler.run()

if __name__ == '__main__':
	main()
