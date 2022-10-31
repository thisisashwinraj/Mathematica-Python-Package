"""
Weibull Distribution
(Also known as Normal Distribution)
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math
from .generalDistribution import Distribution	#Import generalDistribution.py module

class Weibull(Distribution):
	"""
	Weibull distribution class for calculating weibull distribution
	Weibull class inherits from distribution class of generalDistribution.py module

	Notation:
		X ∼ Weibull(λ,k)

	Attributes:
		1. λ (scale parameter)
		2. k (shape parameter)

	Parameters:
		λ ∈ (0,+∞)
		k ∈ (0,+∞)

	Support:
		x ∈ (0,+∞)
	"""	
	def __init__(self,scaleParameter=1,shapeParameter=1):
		#Default vale of lamda = 1
		self.lamda = scaleParameter
		#Default value of k = 1
		self.k = shapeParameter

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
			ValueError(string): Raised when value error occurs
		"""
		try:
			gammaMean = 1 + (1 / self.k)
			"""
					1
			Mean = λ Γ(1 + ---)
					k
			"""
			self.mean = self.lamda * math.gamma(gammaMean)
			return self.mean

		#If value error occurs, raise an error
		except ZeroDivisionError as error:	
			raise

		#If value error occurs, raise an error
		except ValueError as error:
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
			ValueError(string): Raised when value error occurs
		"""
		try:
			gammaVar1 = 1 + (2 / self.k)
			gammaVar2 = 1 + (1 / self.k)
			"""
						 2	       1
			Variance = λ^(2) [Γ(1 + ---) - (Γ(1 + ---))^(2)]
						 k	       k
			"""
			variance = (self.lamda ** 2) * (math.gamma(gammaVar1) - (math.gamma(gammaVar2)) ** 2)

			#Standard deviation = sqrt(variance)
			self.stdev = math.sqrt(variance)
			return self.stdev

		#If value error occurs, raise an error
		except ZeroDivisionError as error:	
			raise

		#If value error occurs, raise an error
		except ValueError as error:
			raise

	def pdf(self,x):
		"""
		Method to calculate probability density function for weibull distribution

		Args:
			x(float): Random variable

		Returns:
			pdf(float): Probability density function for weibull distribution

		Raises:
			ZeroDivisionError(string): Raised when division by zero
			ValueError(string): Raised when value error occurs
		"""
		try:
			if (x >= 0):
				powE = -1 * ((x / self.lamda) ** self.k)
				"""
					    k	  x 		-(x/λ)^(k)
				f(x;λ,k) = --- ((---)^(k - 1)) e, for x ≥  0
					    λ	  λ
				"""
				pdf = (self.k / self.lamda) * ((x / self.lamda) ** (self.k - 1)) * math.exp(powE)

			else:
				"""
				f(x;λ,k) = 0, for x < 0
				"""
				pdf = 0

			return pdf

		#If value error occurs, raise an error
		except ZeroDivisionError as error:	
			raise

		#If value error occurs, raise an error
		except ValueError as error:
			raise

	def __repr__(self):
		"""
		Method to output the characteristics of the weibull instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "Scale Parameter:{}, Shape Parameter:{}, Mean:{}, Standard Deviation:{}".format(self.lamda,self.k,self.mean,self.stdev)