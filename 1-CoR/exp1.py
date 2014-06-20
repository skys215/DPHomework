import math
class VendingMachine:
	def __init__( self, ten, five, two, one ):
		self.yuan10 = ten
		self.yuan5  = five
		self.yuan2  = two
		self.yuan1  = one
		self.totalPrice = 0
		self.changes    = 0
		self.handlers   = []
	
	def put( self, money ):
		print 'U put %d dollars into the vending machine'% money
		self.changes = money
	
	def buy( self, price ):
		print 'U R gonna buy something costs %d dollar'% price
		self.totalPrice = price
	
	def change( self ):
		self.changes -= self.totalPrice
		print 'the machine need to change %d to U'% self.changes
		for handler in self.handlers:
			handler(self )
	
	def add_handler( self, handler ):
		self.handlers.append( handler )


def change10( VM ):
	tens = math.floor(VM.changes/10) 
	if tens <=0:
		return

	VM.yuan10   -= tens
	VM.changes -= tens * 10
	print '10:', tens

def change5( VM ):
	fives = math.floor(VM.changes/5)
	if fives <=0:
		return

	VM.yuan5    -= fives
	VM.changes -= fives * 5
	print '5:', fives

def change2( VM ):
	twos = math.floor( VM.changes / 2 )
	if twos <=0:
		return
	
	VM.yuan2    -= twos
	VM.changes -= twos * 2
	print '2:', twos

def change1( VM ):
	ones = math.floor(VM.changes)
	if ones <=0:
		return
	
	VM.yuan1    -= ones
	VM.changes -= ones 
	print '1:', ones



handlers = [ change10, change5, change2, change1 ]
vm = VendingMachine( 3, 6, 4, 8 )

for handler in handlers:
	vm.add_handler( handler )

vm.put(28)
vm.buy(12)
vm.change()
