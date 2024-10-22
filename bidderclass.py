class Bidder:
	"""Data structure used to store & modify auction bidders"""

	def __init__(self, id=0, data_in=[]):
		"""Init instance along with all necessary fields"""

		if len(data_in) == 0:
			self.id = id
			self.name = ""
			self.cart = []

		elif len(data_in) >= 1:
			self.id = data_in[0]
			self.name = data_in[1]
			self.cart = data_in[2]


	def exp(self):
		"""Returns and organized list containing all instance fields"""

		data_out = []

		data_out.insert(0, self.id)
		data_out.insert(1, self.name)
		data_out.insert(2, self.cart)

		return data_out

