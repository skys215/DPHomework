class Iterator:
	def __init__(self, itr):
		self.itrObject = itr
		self.currentPosition = 0
		self.length = itr.__len__()
	
	def first(self):
		self.currentPosition = 0
	
	def next(self):
		self.currentPosition = (self.currentPosition+1)%self.length
	
	def hasNext(self):
		return self.currentPosition+1 < self.length
	
	def currentItem(self):
		return self.itrObject[self.currentPosition]
	
l=['a','b','c']
itrList = Iterator(l)

itrList.next()
print itrList.currentItem()

itrList.next()
print itrList.currentItem()

print itrList.hasNext()

itrList.first()
print itrList.currentItem()
