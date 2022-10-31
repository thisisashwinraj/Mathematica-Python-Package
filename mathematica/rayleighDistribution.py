"""
Rayleigh Distribution
(Special case of the Weibull distribution with scale parameter of 2)
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math
from .generalDistribution import Distribution	#Import generalDistribution.py module

class Rayleigh(Distribution):
	"""
	Rayleigh distribution class for calculating rayleigh distribution
	Rayleigh class inherits from distribution class of generalDistribution.py module

	Notation:
		X ∼ Ray(σ)

	Attributes:
		1. scaleParameter

	Parameters:
		scale: σ > 0

	Support:
		x ∈ [0,∞)
	"""
	def __init__(self,scaleParameter=1):
		#Default value of sigma = 1
		self.sigma = scaleParameter

		Distribution.__init__(self,self.calculate_mean(),self.calculate_stdev())

	def calculate_mean(self):
		"""
		Method to calculate the mean
		
		Args:
			none

		Returns:
			self.mean(float): Mean of the input dataset
		"""
		part = math.pi / 2
		"""
			    π
		Mean = σ √(---)
			    2
		"""
		self.mean = self.sigma * math.sqrt(part)
		return self.mean

	def calculate_stdev(self):
		"""
		Method to calculate the standard deviation
		
		Args:
			none

		Returns:
			self.stdev(float): Standard deviation of the input dataset

		Raises:
        	ValueError(string): Raised when value error occurs
		"""
		try:
			"""
				    4 - π
			Variance = ------- σ^(2)
				      2
			"""
			variance = ((4 - math.pi) / 2) * (self.sigma) ** 2

			#Standard deviation = sqrt(variance)
			self.stdev = math.sqrt(variance)
			return self.stdev

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
			powE = (-1.0 * (x ** 2)) / (2 * (self.sigma) ** 2)

			#Splitting the pdf expression into two parts for convenience
			pdfOperandOne = x / (self.sigma) ** 2
			pdfOperandTwo = math.exp(powE)
			"""
				    x
			f(x;σ) = ------ e^(-x^(2) / 2σ^(2)), x ≥ 0
				  σ^(2)
			"""
			pdf = pdfOperandOne * pdfOperandTwo
			return pdf

		#If division by zero occurs, raise an error
		except ZeroDivisionError as error:	
			raise

		#If value error occurs, raise an error
		except ValueError as error:
			raise

	def __repr__(self):
		"""
		Method to output the characteristics of the rayleigh instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "σ:{}, Mean:{}, Standard Deviation:{}".format(self.sigma,self.mean,self.stdev)