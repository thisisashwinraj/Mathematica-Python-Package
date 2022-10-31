"""
Exponential Distribution
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math
from .generalDistribution import Distribution	#import generalDistribution.py module

class Exponential(Distribution):
	"""
	Exponential distribution class for calculating exponential distribution
	Exponential class inherits from distribution class of generalDistribution.py module

	Notation:
		X ~ Exp(λ)

	Attributes:
		1. lamda (rate parameter)

	Parameters:
		λ > 0, rate, or inverse scale

	Support:
		x ∈ [0,∞)
	"""
	def __init__(self,rateParameter = 1):
		#Default value of lamda = 1
		self.lamda = rateParameter

		Distribution.__init__(self,self.calculate_mean(),self.calculate_stdev())

	def calculate_mean(self):
		"""
		Method to calculate the mean
        
		Args: 
			none
        
		Returns: 
			self.mean(float): Mean of the data set

		Raises:
			ZeroDivisionError(string): Raised when division by zero
		"""
		try:
			#Mean = 1/λ
			self.mean = 1.0 * (1 / self.lamda)
			return self.mean

		#If divided by zero, raise an error
		except ZeroDivisionError as error:
			raise

	def calculate_stdev(self):
		"""
		Method to calculate the standard deviation
        
		Args: 
			none
        
		Returns: 
			self.stdev(float): Standard deviation of the data set

		Raises:
			ZeroDivisionError(string): Raised when division by zero
		"""
		try:
			#Standard deviation = 1/λ
			self.stdev = 1.0 * (1 / self.lamda)
			return self.stdev
			
		#If divided by zero, raise an error
		except ZeroDivisionError as error:	
			raise

	def pdf(self,x):
		"""
		Method to calculate probability density function for exponential distribution

		Args:
			x(float): Random variable

		Returns:
			self.lamda(float): Probability density function for exponential distribution
		"""
		#For random variable less than zero
		if x < 0:
			return 0

		#Otherwise,
		else:
			power = -1.0 * self.lamda * x
			"""
			f(x;λ) = λ e^(-λ/x)
			"""
			return self.lamda * math.exp(power)

	def __add__(self,other):
		"""
		Method to add together two exponential distributions with equal p
        
		Args:
			other(exponential distribution): Exponential instance
            
		Returns:
			result(exponential distribution): Sum of eponential distribution
		"""
		result = Exponential()

		#Calculate the sum of the rate parameter of the two exponential instances
		result.lamda = self.lamda + other.lamda
		
		#Calculate the mean and standard deviation of the result
		result.calculate_mean()
		result.calculate_stdev()
		return result

	def __repr__(self):
		"""
		Method to output the characteristics of the exponential instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "lamda: {}, mean: {}, standard deviation: {}".format(self.lamda,self.mean,self.stdev)