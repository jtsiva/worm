class Trend (Object):
	"""
	We can keep a list of historical important measurements. In this simple 
	case, we only care about differences of	successive measurements
	"""
	self.mem = []
	self.numCells = None
	self.sensitivity = None

	def __init__(self, numCells = 1, sensitivity = .1):
		self.numCells = numCells
		self.sensitivity = sensitivity

	def update(self, newVal):
		"""
		Assumes that you want to maximize value
		"""
		retVal = None
		if len(self.mem) == 0:
			retVal = True
		else:
			if newVal - self.mem[0] < (-1 * self.sensitivity):
				retVal = False
			else:
				retVal = True

			self.mem[0] = newVal

		return retVal



