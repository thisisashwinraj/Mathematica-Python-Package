"""
Laplace Distribution
(Also known as Double Exponential Distribution)
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math
from .generalDistribution import Distribution	#Import generalDistribution.py module

class Laplace(Distribution):
	"""
	Laplace distribution class for calculating laplace distribution
	Laplace class inherits from distribution class of generalDistribution.py module

	Notation:
		X ∼ Laplace(μ,β)

	Attributes:
		1. mu (location parameter)
		2. b (scale parameter)

	Parameters:
		μ location (real)
		β > 0 scale (real)

	Support:
		ℝ
	"""
	def __init__(self,locationParameter=0,scaleParameter=1):
		#Default value of mu = 0
		self.mu = locationParameter
		#Default value of b = 1
		self.b = scaleParameter

		Distribution.__init__(self,self.calculate_mean(),self.calculate_stdev())

	def calculate_mean(self):
		"""
		Method to calculate the mean
		
		Args:
			none

		Returns:
			self.mean(float): Mean of the input dataset
		"""
		#Mean value = location parameter
		self.mean = self.mu
		return self.mean

	def calculate_stdev(self):
		"""
		Method to calculate the standard deviation
        
		Args: 
			none
        
		Returns: 
			self.stdev(float): Standard deviation of the data set
		"""
		#Variance = 2β^(2)
		variance = 2 * (self.b)**2
		#Standard deviation = sqrt(variance)
		self.stdev = math.sqrt(variance)
		return self.stdev

	def pdf(self,x):
		"""
		Method to calculate probability density function for laplace distribution
        
		Args:
			x(float): Random variable

		Returns:
			pdf(float): Probability density function for laplace distribution

		Raises:
			ZeroDivisionError(string): Raised when division by zero
			ValueError(string): Raised when value error occurs
		"""
		try:
			numDifference = x - self.mu

			#Upadte value of numDifference = |x - μ|
			if(numDifference < 0):
				numDifference = -1 * numDifference

			#powE = -|x-μ| / β
			powE = (-1 * numDifference) / self.b
			"""
				     1	 -|x-μ| / β
			f(x;μ,β) = ----- e
				    2 β
			"""
			#Numerator of the pdf expression
			pdfNumerator = math.exp(powE)
			#Denominator of the pdf expression
			pdfDenominator = 2 * self.b

			return pdfNumerator / pdfDenominator

		#If division by zero occurs, raise an error
		except ZeroDivisionError as error:	
			raise

		#If value error occurs, raise an error
		except ValueError as error:
			raise

	def __add__(self,other):
		"""
		Method to add together two laplace distributions with equal p
        
		Args:
			other(laplace distribution): Laplace instance
            
		Returns:
			result(laplace distribution): Sum of laplace distribution
		"""
		result = Laplace()
		#Calculate the location parameter of the sum of two instances
		result.mu = self.mu + other.mu
		#Calculate the scale parameter of the sum of two instances
		result.b = self.b + other.b

		#Calculate the mean of the two laplace instances
		result.calculate_mean()
		#Calculate the standard deviation of the two laplace instances
		result.calculate_stdev()
		return result

	def __repr__(self):
		"""
		Method to output the characteristics of the laplace instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "μ: {}, β: {}, Mean: {}, Standard Deviation: {}".format(self.mu,self.b,self.mean,self.stdev)