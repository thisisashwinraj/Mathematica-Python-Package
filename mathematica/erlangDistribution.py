"""
Erlang Distribution
(Also known as Normal Distribution)
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math
from .generalDistribution import Distribution	#Import generalDistribution.py module

class Erlang(Distribution):
	"""
	Erlang distribution class for calculating erlang distribution
	Erlang class inherits from distribution class of generalDistribution.py module

	Notation:
		X ∼ Erlang(k,μ)

	Attributes:
		1. k (shape parameter)
		2. mu (scale parameter)

	Parameters:
		k ∈ {1,2,3,...}
		μ = 1/λ, λ ∈ (0,∞)

	Support:
		x ∈ (0,∞)
	"""	
	def __init__(self,shapeParameter=1,scaleParameter=1):
		#Default value of k = 1
		self.k = shapeParameter
		#Default value of mu = 1
		self.mu = scaleParameter

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
			#λ = 1/μ
			lamda = 1 / self.mu

			#Mean = k/λ
			self.mean = self.k / lamda
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
			self.stdev(float): Standard deviation of the data set

		Raises:
			ZeroDivisionError(string): Raised when division by zero
			ValueError(string): Raised when value error occurs
		"""
		try:
			#λ = 1/μ
			lamda = 1 / self.mu
			#variance = k/λ^2
			variance = self.k / (lamda ** 2)

			#standard deviation = sqrt(variance)
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
		Method to calculate probability density function for erlang distribution
        
		Args:
			x(float): Random variable

		Returns:
			pdf(float): Probability density function for erlang distribution

		Raises:
			ZeroDivisionError(string): Raised when division by zero
			ValueError(string): Raised when value error occurs
		"""
		try:
			#x raised to the power of (k-1)
			powX = self.k - 1
			#e raised to the power of (-x/μ)
			powE = -x / self.mu
			denomDifference = self.k - 1
			"""
				    x^(k-1) e^(-x/μ)
			f(x;k,μ) = -------------------
				       μ^k (k-1)!
			"""
			#Numerator part of erlang's pdf
			pdfNumerator = (x ** powX) * math.exp(powE)

			#Denominator part of erlang's pdf
			pdfDenominator = (self.mu ** self.k) * math.factorial(denomDifference)
			return pdfNumerator / pdfDenominator

		#If division by zero occurs, raise an error
		except ZeroDivisionError as error:	
			raise

		#If value error occurs, raise an error
		except ValueError as error:
			raise

	def __add__(self,other):
		"""
		Method to add together two erlang distributions

		Args:
			other(erlang distribution): Erlang instance

		Returns:
			result(erlang distribution): Sum of erlang distribution
		"""
		result = Erlang()

		#Calculate the shape parameter and scale parameter of the sum of two instances
		result.k = self.k + other.k
		result.mu = self.mu + other.mu

		#Calculate the mean of the two erlang instances
		result.calculate_mean()
		#Calculate the standard deviations of the two erlang instances
		result.calculate_stdev()
		return result

	def __repr__(self):
		"""
		Method to output the characteristics of the erlang instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "Shape Parameter: {}, Scale Parameter: {}, Mean: {}, Standard Deviation: {}".format(self.k,self.mu,self.mean,self.stdev)