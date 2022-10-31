"""
Log Logistic Distribution
(Also known as Fisk Distribution)
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math
from numpy import sin	#Import sin() method from Numpy module
from .generalDistribution import Distribution	#Import generalDistribution.py module

class LogLogistic(Distribution):
	"""
	Log logistic distribution class for calculating log logistic distribution
	Log logistic class inherits from distribution class of generalDistribution.py module

	Notation:
		X ∼ LogLogistic(α,β)

	Attributes:
		1. a (scale parameter, a>0)
		2. b (shape parameter, b>0)

	Parameters:
		α > 0 location
		β > 0 scale

	Support:
		x ∈ [0,∞)
	"""
	def __init__(self,scaleParameter=1,shapeParameter=1):
		#Default value of a = 1
		self.a = scaleParameter
		#Default value of b = 1
		self.b = shapeParameter

		Distribution.__init__(self,self.calculate_mean(),self.calculate_stdev())

	def calculate_mean(self):
		"""
		Method to calculate the mean
		
		Args:
			none

		Returns:
			self.mean(float): Mean of the input dataset

		Raises:
			ZeroDivisionError(string): Raised when division by zero
			ValueError(string): Raised when value error occurs
		"""
		#Numerator of the mean
		avgNumerator = (self.a * math.pi) / self.b
		#Denominator of the mean
		avgDenominator = sin(math.pi / self.b)

		try:
			if (self.b > 1):
				"""
					  απ / β
				Mean = ------------, if β>1, else undefined
					 sin(π/β)
				"""
				self.mean = avgNumerator / avgDenominator
				return self.mean

			else:
				return "Undefined"

		#If division by zero occurs, raise an error
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
			if(self.b > 2):
				#Using p = π/β for convenience
				p = math.pi / self.b

				#Variance = α^2(2β/sin2β - β^2/sin^2(β)), β >2
				variance = (self.a ** 2) * ((2 * p) / sin(2 * p) - (p ** 2) / (sin(p) ** 2))

				#Standard deviation = sqrt(variance)
				self.stdev = math.sqrt(variance)
				return self.stdev

			else:
				return "Undefined"

		#If division by zero occurs, raise an error
		except ZeroDivisionError as error:	
			raise

		#If value error occurs, raise an error
		except ValueError as error:
			raise

	def pdf(self,x):
		"""
		Method to calculate probability density function for log logistic distribution
        
		Args:
			x(float): Random variable

		Returns:
			pdf(float): Probability density function for log logistic distribution

		Raises:
			ZeroDivisionError(string): Raised when division by zero
			ValueError(string): Raised when value error occurs
		"""
		try:
			#Numerator of the pdf expression
			pdfNumerator = (self.b / self.a) * ((x / self.a)**(self.b - 1))
			#Denominator of the pdf expression
			pdfDenominator = (1 + ((x / self.a) ** self.b)) ** 2
			"""				  
				    (β/α) (x/α)^(β-1)
			f(x;α,β) = -------------------
				    ((1 + (x/α)^β)^2)
			"""
			return pdfNumerator / pdfDenominator

		#If division by zero occurs, raise an error
		except ZeroDivisionError as error:	
			raise

		#If value error occurs, raise an error
		except ValueError as error:
			raise

	def __repr__(self):
		"""
		Method to output the characteristics of the log logistic instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "α: {}, β: {}, Mean: {}, Standard Deviation: {}".format(self.a,self.b,self.mean,self.stdev)