import Seek
import Trend
import Sense

class Runner (Object):

	def __init__ (self, seek, trend, sense):
		self.seek = seek
		self.trend = trend
		self.sense = sense
		#Generate initial conditions based on seed?
		self.initial = None

	def go (self):
		state = initial
		while 1000:
			sample = self.sense.update(state)
			if not self.trend(sample):
				self.seek.update()

			state = self.seek(sample)
		