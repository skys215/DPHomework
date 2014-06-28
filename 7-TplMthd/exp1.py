class GoSomewhere:
	def __init__(self,comeFrom,dest):
		self.origin=comeFrom
		self.destination=dest

	def go(self):
		self.leave()
		self.transportation()
		self.arrive()
	
	def leave(self):
		print 'leaving %s'%self.origin
	
	def transportation(self):
		print 'I walked to %s'%self.destination
	
	def arrive(self):
		print 'I arrived %s'%self.destination
	
class GoSomewhereByBus(GoSomewhere):
	def transportation(self):
		print 'I\'m in the bus to %s'%self.destination
	
class GoSomewhereByMetro(GoSomewhere):
	def transportation(self):
		print 'I\'m in the metro to %s'%self.destination
	
trip=GoSomewhereByMetro('home','school')
trip.go()

