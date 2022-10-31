"""
Geometric Distribution
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math
from .generalDistribution import Distribution	#Import generalDistribution.py module

class Geometric(Distribution):
	"""
	Geometric distribution class for calculating geometric distribution
	Geometric class inherits from distribution class of generalDistribution.py module

	Notation:
		X ∼ Geo(ρ)

	Attributes:
		1. ρ (shape parameter)
		2. trials (kTrials / kFailures)

	Parameters:
		0 < ρ <= 1

	Support:
		k trials where, k ∈ {1,2,3...}
		k failures where, k ∈ {0,1,2,3...}
	"""	
	def __init__(self,rho=1,trials=True):
		#Default value of p = 1
		self.p = rho
		#Default value of trials = True
		self.trial = trials

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
			#Check if k trials where, k ∈ {1,2,3...}
			if self.trial is True:
				#Mean = 1 / ρ
				self.mean = 1 / self.p
				return self.mean

			#Check if k failures where, k ∈ {0,1,2,3...}
			else:
				#Mean = (1 - ρ) / ρ
				self.mean = (1 - self.p) / self.p
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
			#Variance = (1 - ρ) / ρ^2
			variance = (1 - self.p) / (self.p ** 2)
			#Standard deviation = sqrt(variance)
			self.stdev = math.sqrt(variance)

		#If division by zero occurs, raise an error
		except ZeroDivisionError as error:	
			raise

		#If value error occurs, raise an error
		except ValueError as error:
			raise

	def pdf(self,x=1):
		"""
		Method to calculate probability density function for geometric distribution
        
		Args:
			x(float): Random variable

		Returns:
			pdf(float): Probability density function for geometric distribution
		"""
		#If k trials
		if self.trial is True:
			#pdf = (1-ρ)^(k-1) ρ
			return ((1 - self.p) ** (x-1)) * self.p

		#If k failures
		else:
			#pdf = (1-ρ)^k ρ
			return ((1 - self.p) ** x) * self.p

	def __add__(self,other):
		"""
		Method to add together two geometric distributions
        
		Args:
			other(geometric distribution): Geometric instance
            
		Returns:
			result(geometric distribution): Sum of geometric distribution
		"""
		result = Geometric()

		#Calculate the value of ρ of the sum of two instances
		result.p = self.p + other.p

		#Calculate the mean of the two geometric instances
		result.calculate_mean()
		#Calculate the standard deviations of the two geometric instances
		result.calculate_stdev()
		return result

	def __repr__(self):
		"""
		Method to output the characteristics of the geometric instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "ρ: {}, Mean: {}, Standard Deviation: {}".format(self.p,self.mean,self.stdev)