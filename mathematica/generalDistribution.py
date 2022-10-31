"""
General Distribution
(General parent class for to act as a base class)
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

class Distribution:
	"""
	Generic Distribution class for calculating probability distribution
	Attributes:
		1. mean
		2. stdev
		3. data
	"""
	def __init__(self,mu=0,sigma=1):
		#Mean value of the distribution
		self.mean = mu
		#Sandard deviation of the distribution
		self.stdev = sigma
		#List of floats extracted from input file
		self.data = []

	
	def read_data_file(self,file_name):
		"""
		Method to read data from a txt file(file_name) and store in self.data.
		The txt file should have one number (float) per line.

		Args:
			Name of the file to read data from.

		Returns:
			No return value
		"""
		with open(file_name) as file:
		#file_name: name of the txt file to read data from
			data_list = []
			#Returns one line from the file
			line = file.readline()

			while line:
				#Add data to the list
				data_list.append(int(line))
				line = file.readline()

		#Close the file
		file.close()
		#store the data in the class attribute
		self.data = data_list