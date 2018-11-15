#!/usr/bin/python

import os
import time
import threading
import paho.mqtt.publish as publish

from helper import *
from timestamp import timestamp

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

def main():
	# Step 1.
	threading.Timer(INTERVAL, main).start()
	print(timestamp(), measure_cpu(), measure_gpu())

if __name__ == '__main__':
	main()
