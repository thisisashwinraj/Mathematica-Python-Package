"""
Inverse Gaussian Distribution
(Also known as Wald Distribution or Normal-Inverse Gaussian Distribution)
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math
from .generalDistribution import Distribution	#Import generalDistribution.py module

class InverseGaussian(Distribution):
	"""
	Inverse gaussian distribution class for calculating inverse gaussian distribution
	Inverse gaussian class inherits from distribution class of generalDistribution.py module

	Notation:
		X ∼ IG(μ,λ)

	Attributes:
		1. μ (location parameter, μ>0)
		2. λ (scale parameter, λ>0)

	Parameters:
		μ >0
		λ > 0

	Support:
		x ∈ (0,∞)
	"""

	def __init__(self,locationParameter=1,scaleParameter=1):
		#Default value of mu = 1
		self.mu = locationParameter
		#Default value of lamda = 1
		self.lamda = scaleParameter

		Distribution.__init__(self,self.calculate_mean(),self.calculate_stdev())

	def calculate_mean(self):
		"""
		Method to calculate the mean
		
		Args:
			none

		Returns:
			self.mean(float): Mean of the input dataset
		"""
		#Mean value of an inverse gaussian distribution is the same as the value of μ
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
		#Variance = μ^(3) / λ
		variance = (self.mu ** 3) / self.lamda

		#Standard deviation = sqrt(variance) 
		self.stdev = math.sqrt(variance)
		return self.stdev

	def pdf(self,x):
		"""
		Method to calculate probability density function for inverse gaussian distribution
        
		Args:
			x(float): Random variable

		Returns:
			pdf(float): Probability density function for inverse gaussian distribution

		Raises:
			ZeroDivisionError(string): Raised when division by zero
			ValueError(string): Raised when value error occurs
		"""
		try:
			#Splitting the expression to calculate pdf for convenience
			powNumerator = -1.0 * self.lamda * ((x - self.mu) ** 2)
			powDenominator = 2 * (self.mu ** 2) * x

			partOne = self.lamda / (2 * math.pi * (x ** 3))
			powE = powNumerator / powDenominator
			"""
					 λ		λ (x-μ)^(2)
			f(x;μ,λ) = √(---------) exp[- --------------]
				     2 π x^(3)		 2 μ^(2) x
			"""
			operand1 = math.sqrt(partOne)
			operand2 = math.exp(powE)
			return operand1 * operand2

		#If division by zero occurs, raise an error
		except ZeroDivisionError as error:	
			raise

		#If value error occurs, raise an error
		except ValueError as error:
			raise

	def __repr__(self):
		"""
		Method to output the characteristics of the inverse gaussian instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "μ: {}, λ: {}, Mean: {}, Standard Deviation: {}".format(self.mu,self.lamda,self.mean,self.stdev)