class Person:
	def __init__(self,mood):
		self.mood=mood;

	def laugh(self):
		self.mood.laugh()

	def cry(self):
		self.mood.cry()
	
	def setMood(self, mood):
		self.mood=mood

class Mood:
	def laugh(self):
		pass
	def cry(self):
		pass

class HappyMood(Mood):
	def laugh(self):
		print 'Ha ha ha!'

class SadMood(Mood):
	def cry(self):
		print 'Sniff sniff'

p=Person(HappyMood())
p.laugh()
p.cry()

p.setMood(SadMood())
p.laugh()
p.cry()

