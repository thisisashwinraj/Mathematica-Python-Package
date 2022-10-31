"""
Lévy Distribution
(Special case of the Inverse-Gamma Distribution)
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math
from .generalDistribution import Distribution	#Import generalDistribution.py module

class Levy(Distribution):
	"""
	Lévy distribution class for calculating lévy distribution
	Lévy class inherits from distribution class of generalDistribution.py module

	Notation:
		X ∼ Lévy(c,μ)

	Attributes:
		1. a (location parameter, x≥a)
		2. c (scale parameter, c>0)

	Parameters:
		μ location
		c > 0 scale

	Support:
		x ∈ [μ,∞)
	"""
	def __init__(self,scaleParameter=1,locationParameter=2):
		#Default value of c = 1
		self.c = scaleParameter
		#Default value of a = 2
		self.a = locationParameter

		Distribution.__init__(self,self.calculate_mean(),self.calculate_stdev())

	def calculate_mean(self):
		"""
		Method to calculate the mean
		
		Args:
			none

		Returns:
			self.mean(float): Mean of the input dataset
		"""
		#Mean value of a lévy distribution is infinity
		self.mean = "∞"
		return self.mean

	def calculate_stdev(self):
		"""
		Method to calculate the standard deviation
        
		Args: 
			none
        
		Returns: 
			self.stdev(float): Standard deviation of the data set
		"""
		#Standard deviation of a lévy distribution is infinity
		self.stdev = "∞"
		return self.stdev

	def pdf(self,x):
		"""
		Method to calculate probability density function for lévy distribution
        
		Args:
			x(float): Random variable

		Returns:
			pdf(float): Probability density function for lévy distribution

		Raises:
			ZeroDivisionError(string): Raised when division by zero
			ValueError(string): Raised when value error occurs
		"""
		try:
			#Exponent with base e = -(c/2(x-μ))
			powE = (-1.0 * self.c) / (2 * (x - self.a))

			#Numerator of the operand2
			operand2Numerator = math.exp(powE)
			#Denominator of the operand2
			operand2Denominator = (x - self.a) ** (3 / 2)
			"""
						 -(c/2(x-μ))
						e
			f(x;μ,c) = √(c/2π) --------------
					    (x-μ)^(3/2)
			"""
			operand1 = math.sqrt(self.c / (2 * math.pi))
			operand2 = operand2Numerator / operand2Denominator
			return operand1 * operand2

		#If division by zero occurs, raise an error
		except ZeroDivisionError as error:	
			raise

		#If value error occurs, raise an error
		except ValueError as error:
			raise

	def __add__(self,other):
		"""
		Method to add together two lévy distributions with equal p
        
		Args:
			other(lévy distribution): Lévy instance
            
		Returns:
			result(lévy distribution): Sum of lévy distribution
		"""
		result = Levy()

		#Calculate the scale parameter of the sum of two instances
		result.c = self.c + other.c
		#Calculate the location parameter of the sum of two instances
		result.a = self.a + other.a

		#Calculate the mean of the two lévy instances
		result.calculate_mean()
		#Calculate the standard deviation of the two lévy instances
		result.calculate_stdev()
		return result

	def __repr__(self):
		"""
		Method to output the characteristics of the lévy instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "c: {}, μ: {}, Mean: {}, Standard Deviation: {}".format(self.c,self.a,self.mean,self.stdev)