"""
Yule Simon Distribution
(Also known as Yule distribution)
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math
from .generalDistribution import Distribution	#Import generalDistribution.py module

class YuleSimon(Distribution):
	"""
	Yule Simon distribution class for calculating yule simon distribution
	Yule Simon class inherits from distribution class of generalDistribution.py module

	Notation:
		X ∼ Yule(ρ)

	Attributes:
		1. shape parameter

	Parameters:
		ρ > 0 shape(real)

	Support:
		k ∈ {1,2,...}
	"""
	def __init__(self,shapeParameter=1):
		#Default value of rho = 1
		self.rho = shapeParameter

		Distribution.__init__(self,self.calculate_mean(),self.calculate_stdev())

	def calculate_mean(self):
		"""
		Method to calculate the mean
		
		Args:
			none

		Returns:
			self.mean(float/string): Mean of the input dataset
		"""
		#For ρ > 1
		if (self.rho > 1):
			"""
				 ρ
			Mean = -----, for ρ>1
				ρ-1
			"""
			self.mean = self.rho / (self.rho - 1)

		#Otherwise
		else:
			self.mean = "Undefined"
		
		return self.mean

	def calculate_stdev(self):
		"""
		Method to calculate the standard deviation
		
		Args:
			none

		Returns:
			self.stdev(float/string): Standard deviation of the input dataset
		"""
		#For ρ > 2
		if (self.rho > 2):
			"""
					 ρ^(2)
			Variance = ----------------
				   (ρ-1)^(2) (ρ-2)
			"""
			variance = (self.rho ** 2) / (((self.rho - 1)**2) * (self.rho - 2))
			#Standard deviation = sqrt(variance)
			self.stdev = math.sqrt(variance)

		#Otherwise
		else:
			self.stdev = "Undefined"
		return self.stdev

	def pdf(self,x):
		"""
		Method to calculate probability density function for yule simon distribution
        
		Args:
			x(float): Random variable

		Returns:
			pdf(float): Probability density function for yule simon distribution

		Raises:
			ZeroDivisionError(string): Raised when division by zero
			ValueError(string): Raised when value error occurs
		"""
		try:
			#Splitting the pdf expression for convenience
			pdfNumerator = self.rho * math.gamma(x) * math.gamma(self.rho + 1)
			pdfDenominator = math.gamma(x + self.rho + 1)
			"""
					      ρ Γ(x) Γ(ρ+1)
			f(x;ρ) = ρB(x,ρ+1) = ---------------, x ≥ 1; ρ > 0
						Γ(x+ρ+1)
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
		Method to output the characteristics of the yule simon instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "ρ:{}, Mean:{}, Standard Deviation:{}".format(self.rho,self.mean,self.stdev)