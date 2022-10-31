"""
T Distribution
(Also known as Student's t-Distribution)
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math
from .generalDistribution import Distribution	#Import generalDistribution.py module

class T(Distribution):
	"""
	T distribution class for calculating T distribution
	T class inherits from distribution class of generalDistribution.py module

	Notation:
		X ∼ T(v)

	Attributes:
		1. v (degree of freedom)

	Parameters:
		v > 0 degree of freedom (real)

	Support:
		x ∈ (-∞,∞)
	"""
	def __init__(self,degreeOfFreedom=4):
		#Default value of v = 4
		self.v = degreeOfFreedom

		Distribution.__init__(self,self.calculate_mean(),self.calculate_stdev())

	def calculate_mean(self):
		"""
		Method to calculate the mean
		
		Args:
			none

		Returns:
			self.mean(float/string): Mean of the input dataset
		"""
		#For v>1
		if(self.v > 1):
			self.mean = 0

		#Otherwise undefined
		else:
			self.mean = "Undefined"
		
		return self.mean

	def calculate_stdev(self):
		"""
		Method to calculate the standard deviation
        
		Args: 
			none
        
		Returns: 
			self.stdev(float/string): Standard deviation of the data set
		"""
		#For v>2
		if(self.v > 2):
			variance = self.v / (self.v - 2)
			#Standard deviation = sqrt(variance)
			self.stdev = math.sqrt(variance)

		#For 1<v<=2
		elif(self.v > 1 and self.v<=2):
			self.stdev = "∞"

		#Otherwise undefined
		else:
			self.stdev = "Undefined"

		return self.stdev

	def pdf(self,x):
		"""
		Method to calculate probability density function for T distribution
        
		Args:
			x(float): Random variable

		Returns:
			pdf(float): Probability density function for T distribution

		Raises:
			ZeroDivisionError(string): Raised when division by zero
			ValueError(string): Raised when value error occurs
		"""
		try:
			#Numerator part of operandOne
			partOneNumerator = math.gamma((self.v + 1) / 2)
			#Denominator part of operandTwo
			partOneDenominator = math.sqrt(self.v * math.pi) * math.gamma(self.v / 2)

			#Operand two raised to the power powPartTwo
			powPartTwo = -1.0 * ((self.v + 1) / 2)
			"""
				  Γ(v+1 / 2)		  -(v+1 / 2)
			f(x;v) = ------------ (1+(x^(2)/v))
				  √vπ Γ(v/2)
			"""
			#Operand one of the pdf expression
			operandOne = partOneNumerator / partOneDenominator
			#Operand two of the pdf expression
			operandTwo = (1 + ((x ** 2) / self.v)) ** powPartTwo
			return operandOne * operandTwo

		#If division by zero occurs, raise an error
		except ZeroDivisionError as error:	
			raise

		#If value error occurs, raise an error
		except ValueError as error:
			raise

	def __repr__(self):
		"""
		Method to output the characteristics of the F instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "v: {}, Mean: {}, Standard Deviation: {}".format(self.v,self.mean,self.stdev)