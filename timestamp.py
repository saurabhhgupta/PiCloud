import time

def timestamp():
	timestamp = time.gmtime()
	return time.strftime("%Y-%m-%d %H:%M:%S", timestamp)
