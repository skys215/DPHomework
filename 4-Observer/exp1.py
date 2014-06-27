class Observer:
	def response(self):
		pass
	

class GeekObserver(Observer):
	def response(self):
		print 'Open browser, get it from tmall!'
	
class NormalObserver(Observer):
	def response(self):
		print 'Goto Apple Shop queue a line and buy it!'
	
	
class Subject:
	def __init__(self):
		self.observers={}

	def attach(self,name,obs):
		self.observers[name]=obs

	def detach(self,name):
		del self.observers[name]

	def notify(self):
		for obs in self.observers:
			self.observers[obs].response()
	

class IPhone5Subject(Subject):

	def arrived(self):
		print 'iPhone5 has arrived'
		self.notify()

geek=GeekObserver()
nrml=NormalObserver()

iphone=IPhone5Subject()
iphone.attach('geek',geek)
iphone.attach('normal',nrml)

iphone.arrived()
