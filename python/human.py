class Human:

	def say_hello(self, name=None):

		if name is not None:
			print 'Hello ' + name
		else:
			print 'Hello'


obj = Human()

obj.say_hello()


obj.say_hello("Sankar")
