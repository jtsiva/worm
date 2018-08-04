
class Seek (Object):
	self.A = None
	self.B = None

	def __init__ (self, A, B, C, D, seed):
		"""
		Setup control structures for interpreting new input. Input
		is 1D. Output can be N-dimensional.
		"""
		self.A = A
		self.B = B

	def go(self, newVal):
		"""
		Takes a one dimensional real value and returns an output matrix
		"""
		pass

	def update(self):
		"""
		Force a one-shot change to the next output calculation because we are
		no longer working toward our objective
		"""
		pass