"""
F Distribution
(Also known as Snedecor's F Distribution or the Fisher–Snedecor Distribution)
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math
from .generalDistribution import Distribution	#Import generalDistribution.py module

class F(Distribution):
	"""
	F distribution class for calculating F distribution
	F class inherits from distribution class of generalDistribution.py module

	Notation:
		X ∼ F(d1,d2)

	Attributes:
		1. d1 (degree of freedom)
		2. d2 (degree of freedom)

	Parameters:
		d1,d2 > 0 deg. of freedom

	Support:
		x ∈ (0,+∞), if d1 = 1
		x ∈ [0,+∞), otherwise
	"""
	def __init__(self,degreeOfFreedomD1=4,degreeOfFreedomD2=4):
		#Default value of d1 = 4
		self.d1 = degreeOfFreedomD1
		#Default value of d2 = 4
		self.d2 = degreeOfFreedomD2

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
		"""
		try:
			"""
				  d2
			mean = --------, for d2>2
				d2 - 2
			"""
			self.mean = self.d2 / (self.d2 - 2)
			return self.mean

		#If division by zero occurs, raise an error
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
			ValueError(string): Raised when value error occurs
		"""
		try:
			#Numerator of the variance
			varNumerator = (2 * (self.d2) ** 2) * (self.d1 + self.d2 - 2)
			#Denominator of the variance
			varDenominator = (self.d1 * ((self.d2 - 2) ** 2) * (self.d2 - 4))
			"""
				     2d2^(2) (d1+d2-2)
			Variance = ---------------------, for d2>4
				    d1(d2-2)^(2) (d2-4)
			"""
			variance = varNumerator / varDenominator

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
		Method to calculate probability density function for F distribution
        
		Args:
			x(float): Random variable

		Returns:
			pdf(float): Probability density function for F distribution

		Raises:
			ZeroDivisionError(string): Raised when division by zero
			ValueError(string): Raised when value error occurs
		"""
		try:
			#Numerator of the pdf
			pdfNumerator = math.gamma((self.d1 + self.d2) / 2) * ((self.d1 / self.d2) ** (self.d1 / 2)) * (x ** ((self.d1 / 2) - 1))
			#Denominator of the pdf
			pdfDenominator = math.gamma(self.d1 / 2) * math.gamma(self.d2 / 2) * (1 + ((self.d1 * x) / self.d2)) ** ((self.d1 + self.d2) / 2)
			"""
					Γ(d1+d2 / 2) (d1/d2)^(d1/2) x^(d1/2 - 1)
			f(x;d1,d2) = ----------------------------------------------, x>0
					Γ(d1/2) Γ(d2/2) (1 + d1x/d2)^(d1+d2 / 2)
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
		Method to output the characteristics of the F instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "d1: {}, d2: {}, Mean: {}, Standard Deviation: {}".format(self.d1,self.d2,self.mean,self.stdev)