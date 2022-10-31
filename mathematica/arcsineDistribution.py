"""
Arcsine Distribution
Arbitrary Bounded Support
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math
from .generalDistribution import Distribution	#Import generalDistribution.py module

class Arcsine(Distribution):
	"""
	Arcsine distribution class for calculating arcsine distribution
	Arcsine class inherits from distribution class of generalDistribution.py module

	Notation:
		X ~ Arcsine()

	Attributes:
		none

	Parameters:
		none

	Support:
		x ∈ [0,1]
	"""
	def __init__(self):
		#No attributes
		Distribution.__init__(self,self.calculate_mean(),self.calculate_stdev())

	def calculate_mean(self):
		"""
		Method to calculate the mean
        
		Args: 
			none
        
		Returns: 
			self.mean(float): Mean of the data set
		"""
		self.mean = 1 / 2
		return self.mean

	def calculate_stdev(self):
		"""
		Method to calculate the standard deviation
        
		Args: 
			none
        
		Returns: 
			self.stdev(float): Standard deviation of the data set
		"""
		#Variance = 1/8
		self.stdev = math.sqrt(1 / 8)
		return self.stdev

	def pdf(self,x):
		"""
		Method to calculate probability density function for arcsine distribution
        
		Args:
			x(float): Random variable

		Returns:
			pdf(float): Probability density function for arcsine distribution

		Raises:
			ZeroDivisionError(string): Raised when division by zero
			ValueError(string): Raised when negative number passed for square root
		"""
		try:
			part = math.sqrt(x * (1 - x))
			"""
				     1
			f(x) = -------------
				π √(x(1-x))
			"""
			return 1 / (math.pi * part)

		#If divided by zero, raise an error
		except ZeroDivisionError as error:
			raise

		#If negative number passed for square root, raise an error
		except ValueError as error:
			raise

	def __repr__(self):
		"""
		Method to output the characteristics of the arcsine instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "mean: {}, standard deviation: {}".format(self.mean,self.stdev)

class BoundedArcsine(Distribution):
	"""
	Arcsine distribution class for calculating arcsine distribution
	Arcsine class inherits from distribution class of generalDistribution.py module

	Notation:
		X ~ Arcsin(a,b)

	Attributes:
		1. abcissa (x-coordinate of the bounded region)
		2. ordinate (y-coordinate of the bounded region)

	Parameters:
		-∞ < a < b < ∞

	Support:
		x ∈ [a,b]
	"""
	def __init__(self,abcissa=0,ordinate=1):
		#Default value of a = 0
		self.a = abcissa
		#Default value of b = 1
		self.b = ordinate

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
		return self.mean

	def calculate_stdev(self):
		"""
		Method to calculate the standard deviation

		Args: 
			none
        
		Returns: 
			self.stdev(float): Standard deviation of the data set
		"""
		variance = ((self.b - self.a) ** 2) / 8
		"""
        		(b-a)^(2)
		Mean = -----------
        		    2
		"""
		#Standard deviation = sqrt(variance)
		self.stdev = math.sqrt(variance)
		return self.stdev

	def pdf(self,x):
		"""
		Method to calculate probability density function for arcsine distribution
        
		Args:
			x(float): Random variable

		Returns:
			pdf(float): Probability density function for arcsine distribution

		Raises:
			ZeroDivisionError(string): Raised when division by zero
			ValueError(string): Raised when negative number passed for square root
		"""
		try:
			part = math.sqrt((x - self.a) * (self.b - x))
			"""
					  1
			f(x;a,b) = ---------------, a ≤ x ≤ b
				    π √(x-a)(b-x)
			"""
			return 1 / (math.pi * part)

		#If divided by zero, raise an error
		except ZeroDivisionError as error:
			raise

		#If negative number passed for square root, raise an error
		except ValueError as error:
			raise

	def __repr__(self):
		"""
		Method to output the characteristics of the exponential instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "a:{}, b:{}, Mean:{}, Standard Deviation:{}".format(self.a,self.b,self.mean,self.stdev)