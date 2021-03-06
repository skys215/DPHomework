class Light:
	def on(self):
		print 'Light\'s on'
	
	def off(self):
		print 'Light\'s off'

class Commands:
	def __init__(self):
		pass
	
	def execute(self):
		pass
	

class LightsOnCommand(Commands):
	def __init__(self,light):
		self.light=light
	
	def execute(self):
		self.light.on()

class LightsOffCommand(Commands):
	def __init__(self, light):
		self.light=light

	def execute(self):
		self.light.off()
	

class Switch:
	def __init__( self, cmd ):
		self.command = cmd
	
	def do(self):
		self.command.execute()


l=Light()
onCmd = LightsOnCommand( l )
offCmd = LightsOffCommand( l )

swtOn = Switch( onCmd )
swtOn.do()

swtOff = Switch( offCmd )
swtOff.do()
	

