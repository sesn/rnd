from threading import *
import time

def handleClient1():
	while(True):
		print "Waiting for the client 1..."
		time.sleep(5) # wait 5 seconds

def handleClient2():
	while(True):
		print "Waiting for the client 2..."
		time.sleep(5) # wait for 5 seconds

t = Timer(5.0, handleClient1)
t2 = Timer(3.0, handleClient2)

t.start()
t2.start()