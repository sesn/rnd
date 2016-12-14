class User:
	name = ""

	def __init__(self, name):
		self.name = name

	def printName(self):
		print "Name = " + self.name



class Programmer(User):

	def __init__(self, name):
		self.name = name

	def doPython(self):
		print "Programming Python"

sankar = User("Sankar")
sankar.printName()

chandan = Programmer("Chandan")
chandan.printName()
chandan.doPython()