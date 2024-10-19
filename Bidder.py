class Bidder:
	"""Data structure used to store & modify auction bidders"""

	def __init__(self, id):
		"""Init instance along with all necessary attributes"""

		self.id = id
		self.name = ""
		self.cart = []


	def exp(self):
		"""Returns and organized list containing all instance attributes"""

		data_out = []

		data_out.insert(0, self.id)
		data_out.insert(1, self.name)
		data_out.insert(2, self.cart)

		return data_out


	def imp(self, data_in):
		"""Takes in an organized list and populates instance attributes"""

		self.id = data_in[0]
		self.name = data_in[1]
		self.cart = data_in[2]

		return