#!/usr/bin/python

import os
import time
import threading
import paho.mqtt.client as mqtt

INTERVAL = 3.0

def measure_cpu():
	temp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
	return (float(temp) / 1000.0)

def measure_gpu():
	temp = os.popen("vcgencmd measure_temp").readline()
	return float((temp.replace("temp=", "").replace("'C", "")))

def display_temps():
	global INTERVAL
	threading.Timer(INTERVAL, display_temps).start()
	print("CPU temperature:", measure_cpu())
	print("GPU temperature:", measure_gpu())

def main():
	display_temps()

if __name__ == '__main__':
	main()