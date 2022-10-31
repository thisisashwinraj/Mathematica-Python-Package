"""
Uniform Distribution
(Also known as Rectangular Distribution)
"""
#Author: Ashwin Raj <rajashwin733@gmail.com>
#License: GNU General Public License v3.0

import math
from .generalDistribution import Distribution 	#Import generalDistribution.py module

class Uniform(Distribution):
	"""
	Uniform distribution class for calculating uniform distribution
	Uniform class inherits from distribution class of generalDistribution.py module

	Notation:
		Unif(a,b)
    
	Attributes:
		1. a (location parameter)
		2. b (scale parameter)

	Parameters:
		-∞ < a < b < ∞

	Support:
		x ∈ [a,b]
	"""
	def __init__(self,locationParam=0,scaleParam=1):
		#Default value of a = 0
		self.a = locationParam
		#Default value of b = 1
		self.b = scaleParam

		Distribution.__init__(self,self.calculate_mean(),self.calculate_stdev())

	def calculate_mean(self):
		"""
		Method to calculate the mean
        
		Args: 
			none
        
		Returns: 
			self.mean(float): Mean of the data set
		"""
		self.mean = (self.a + self.b) / 2
		"""
			  1
		Mean = -------
			a + b
		"""
		return self.mean

	def calculate_stdev(self):
		"""
		Method to calculate the standard deviation
        
		Args: 
			none
        
		Returns: 
			self.stdev(float): Standard deviation of the data set
		"""
		variance = ((self.b - self.a)**2) / 12
		"""
			    (b - a)^(2)
		Variance = -------------
				12
		"""
		self.stdev = math.sqrt(variance)
		return self.stdev

	def replace_stats_with_data(self):
		"""
		Method to calculate p and n from the data set
        
		Args: 
			none
        
		Returns: 
			self.a(float): Value of a
			self.b(float): Value of b    
		"""
		self.a = min(self.data)	#max value in the data file
		self.b = max(self.data)	#min value in the data file

		#Calculate mean and standard deviation
		self.mean = self.calculate_mean()
		self.stdev = self.calculate_stdev()
		return self.a, self.b

	def pdf(self,x):
		"""
		Method to calculate probability density function for uniform distribution
        
		Args:
			x(float): Random variable

		Returns:
			pdf(float): Probability density function for uniform distribution
		"""
		#For random variable ranging between a and b
		if(x < self.a or x > self.b):
			return 0

		#Otherwise
		else:
			"""
				      1
			f(x;a,b) = -------
				    b - a
			"""
			return 1 / (self.b - self.a)

	def __add__(self,other):
		"""
		Method to add together two uniform distributions with equal p
        
		Args:
			other(uniform distribution): Uniform instance
            
		Returns:
			result(uniform distribution): Sum of uniform distribution
		"""
		result = Uniform()

		result.a = self.a + other.a
		result.b = self.b + other.b

		#Calculate the mean of the two uniform instances
		result.calculate_mean()
		#Calculate the standard deviations of the two uniform instances
		result.calculate_stdev()

		return result

	def __repr__(self):
		"""
		Method to output the characteristics of the uniform instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "a: {}, b: {}, mean: {}, standard deviation: {}".format(self.a,self.b,self.mean,self.stdev)