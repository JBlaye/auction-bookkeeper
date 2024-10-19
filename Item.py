class Item:
	"""Data structure used to store & modify auction items"""

	def __init__(self, id):
		"""Init instance along with all necessary attributes"""

		self.id = id
		self.name = ""
		self.donator = ""
		self.est_val = 0.0
		self.price = 0.0


	def exp(self):
		"""Returns an organized list containing all instance attributes"""

		data_out = []

		data_out.insert(0, self.id)
		data_out.insert(1, self.name)
		data_out.insert(2, self.donator)
		data_out.insert(3, self.est_val)
		data_out.insert(4, self.price)

		return data_out


	def imp(self, data_in):
		"""Takes in an organized list and populates instance attributes"""

		self.id = data_in[0]
		self.name = data_in[1]
		self.donator = data_in[2]
		self.est_val = data_in[3]
		self.price = data_in[4]

		return

