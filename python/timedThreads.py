from threading import *

def hello():
	print 'Hello World'

# create thread
t = Timer(10.0, hello)

# start thread after 10 seconds
t.start()
