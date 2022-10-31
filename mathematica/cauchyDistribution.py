"""
Cauchy Distribution
(Also known as Lorentz distribution, Cauchy–Lorentz distribution, Lorentz(ian) function, or Breit–Wigner distribution)
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math
from .generalDistribution import Distribution 	#Import generalDistribution.py module

class Cauchy(Distribution):
	"""
	Cauchy distribution class for calculating cauchy distribution
	Cauchy class inherits from distribution class of generalDistribution.py module

	Notation:
		X ~ Cauchy(x0,γ)

	Attributes:
		none

	Parameters:
		x0 location(real)
		γ>0 scale (real)

	Support:
		x ∈ (-∞,+∞)
	"""	
	def __init__(self):
		Distribution.__init__(self,self.calculate_mean(),self.calculate_stdev())

	def calculate_mean(self):
		"""
		Method to calculate the mean of the input dataset

		Args:
			none

		Returns:
			output(string): Mean is not defined for cauchy distribution
		"""
		return "Undefined"

	def calculate_stdev(self):
		"""
		Method to calculate the standard deviation of the input dataset
		
		Args:
			none

		Returns:
			output(string): Standard deviation is not defined for Cauchy Distribution
		"""
		return "Undefined"

	def pdf(self,x,scaleParameter=1,locationParameter=0):
		"""
		Method to calculate probability density function for cauchy distribution
        
		Args:
			x(float): Random variable
			scaleParameter(float) = Scale Parameter (x0)
			locationParameter(float) = Location Parameter (γ)

		Returns:
			pdf(float): Probability density function for cauchy distribution
		"""
		#Default value of s = 1
		s = scaleParameter
		#Default value of t = 0
		t = locationParameter

		try:
			"""
						1
			f(x;x0,γ) = ------------------------
				    π γ [1 + ((x - x0)/γ)^2]
			"""
			pdfDenominator = (s * math.pi) * (1 + ((x - t) / (s ** 2)))
			return 1 / pdfDenominator

		#If division by zero occurs, raise an error
		except ZeroDivisionError as error:	
			raise

	def __repr__(self):
		"""
		Method to output the characteristics of the cauchy instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "mean: undefined, standard deviation: undefined"