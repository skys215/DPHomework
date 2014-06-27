class Context:
	def __init__(self):
		self.strategy=None
	
	def setStrategy(self, strat):
		self.strategy=strat
	
	def algorithm(self):
		self.strategy.algorithm()

class Strategy:
	def algorithm(self):
		pass

class BubbleSortStrat(Strategy):
	def algorithm(self):
		print 'bubble sort'
	
class QuickSortStrat(Strategy):
	def algorithm(self):
		print 'quick sort'

c=Context()
c.setStrategy(BubbleSortStrat())
c.algorithm()

c.setStrategy(QuickSortStrat())
c.algorithm()

