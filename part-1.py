#!/usr/bin/python

import os
import sched
import time

function_scheduler = sched.scheduler(time.time, time.sleep)

def measure_cpu():
	temp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
	return (float(temp) / 1000.0)

def measure_gpu():
	temp = os.popen("vcgencmd measure_temp").readline()
	return float((temp.replace("temp=", "").replace("'C", "")))

def threaded(scheduler):
	timestamp = time.localtime()
        print (time.strftime("%Y-%m-%d %H:%M:%S", timestamp), measure_cpu(), measure_gpu())
	function_scheduler.enter(5.0, 0, threaded, (scheduler,))

def main():
	global function_scheduler
        function_scheduler.enter(5.0, 0, threaded, (function_scheduler,))
        function_scheduler.run()

if __name__ == '__main__':
	main()
