"""
Reciprocal Distribution
(Also known as the Log-Uniform distribution)
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math
from .generalDistribution import Distribution	#Import generalDistribution.py module

class Reciprocal(Distribution):
	"""
	Reciprocal distribution class for calculating reciprocal distribution
	Reciprocal class inherits from distribution class of generalDistribution.py module

	Notation:
		ln(X) ∼ U(ln(a),ln(b))

	Attributes:
		1. lowerBound
		2. upperBound

	Parameters:
		0 < a < b
		a,b ∈ ℝ

	Support:
		[a,b]
	"""
	def __init__(self,lowerBound=1,upperBound=1):
		#Default value of a = 1 
		self.a = lowerBound
		#Default value of b = 1
		self.b = upperBound

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
		try:
			#Split the expression to calculate mean into two parts for convenience
			avgNumerator = self.b - self.a
			avgDenominator = math.log(float(self.b / self.a))
			"""
				 b - a
			Mean = ---------
				ln(b/a)
			"""
			self.mean = avgNumerator / avgDenominator
			return self.mean

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
			self.stdev(float): Standard deviation of the input dataset

		Raises:
			ZeroDivisionError(string): Raised when division by zero
			ValueError(string): Raised when value error occurs
		"""
		try:
			#Split the expression to calculate variance into two parts for convenience
			varNumerator = (self.b ** 2) - (self.a ** 2)
			varDenominator = 2 * math.log(float(self.b / self.a))
			"""
				    b^(2) - a^(2)       b - a
			Variance = --------------- - (---------)^(2)
				      2 ln(b/a)	       ln(b/a)
			"""
			variance = (varNumerator / varDenominator) - (self.mean ** 2)

			#Standard deviation = sqrt(variance)
			self.stdev = math.sqrt(variance)
			return self.stdev

		#If division by zero occurs, raise an error
		except ZeroDivisionError as error:	
			raise

		#If value error occurs, raise an error
		except ValueError as error:
			raise

	def pdf(self,x):
		"""
		Method to calculate probability density function for reciprocal distribution
        
		Args:
			x(float): Random variable

		Returns:
			pdf(float): Probability density function for reciprocal distribution

		Raises:
			ZeroDivisionError(string): Raised when division by zero
			ValueError(string): Raised when value error occurs
		"""
		try:
			"""
					1
			f(x;a,b) = -----------, for a ≤ x ≤ b and, a > 0
				    x ln(b/a)
			"""
			return 1 / (x * math.log(float(self.b / self.a)))

		#If division by zero occurs, raise an error
		except ZeroDivisionError as error:	
			raise

		#If value error occurs, raise an error
		except ValueError as error:
			raise

	def __repr__(self):
		"""
		Method to output the characteristics of the reciprocal instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "a:{}, b:{}, Mean:{}, Standard Deviation:{}".format(self.a,self.b,self.mean,self.stdev)