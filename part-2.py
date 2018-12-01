#!/usr/bin/python

import os
import sched
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

from mqtt import *


broker = "192.168.0.22"
topic = "picloud/test"
function_scheduler = sched.scheduler(time.time, time.sleep)

def measure_cpu():
	temp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
	return (float(temp) / 1000.0)

def measure_gpu():
	temp = os.popen("vcgencmd measure_temp").readline()
	return float((temp.replace("temp=", "").replace("'C", "")))

def threaded(scheduler, client):
	timestamp = time.localtime()
        packet = (time.strftime("%Y-%m-%d %H:%M:%S", timestamp), measure_cpu(), measure_gpu())

	client.connect(broker, 1883, 60)
	client.publish(topic, str(packet))
	print packet
	client.disconnect()

	function_scheduler.enter(5.0, 0, threaded, (scheduler, client))

def main():
	global function_scheduler

	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message

        function_scheduler.enter(5.0, 0, threaded, (function_scheduler, client))
        function_scheduler.run()

if __name__ == '__main__':
	main()
