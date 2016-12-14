class Car(object):
	@staticmethod
	def factory(type):
		if type == 'Racecar':
			return Racecar()
		else:
			return Van()
		assert 0, "Bad creation: " + type

	# factory = staticmethod(factory)

class Racecar(Car):
	def drive(self): print "Racecar driving"

class Van(Car):
	def drive(self): print "Van driving"

#Create obj using factory
obj = Car.factory("Racecar")
obj.drive()
		