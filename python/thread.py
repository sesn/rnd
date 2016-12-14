import threading

class MyThread(threading.Thread):
	"""docstring for MyThread"""
	def __init__(self, x):
		super(MyThread, self).__init__()
		self.__x = x

	def run(self):
		print str(self.__x)

for x in xrange(10):
	MyThread(x).start()
