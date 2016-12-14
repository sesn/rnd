class Car:
	__maxspeed = 0
	__name = ""

	def __init__(self):
		self.__name = "Supercar"
		self.__maxspeed = 200
		self.__updateSoftware()

	def drive(self):
		print str(self.__name) + "driving with speed of " + str(self.__maxspeed)

	def __updateSoftware(self):
		print 'Updating software'


redCar = Car()
redCar.drive()
redCar.__maxspeed = 10
redCar.drive()