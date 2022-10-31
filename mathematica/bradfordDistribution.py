"""
Bradford Distribution
(Also known as the Bradford Law of Scattering)
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math
from .generalDistribution import Distribution	#Import generalDistribution.py module

class Bradford(Distribution):
	"""
	Bradford distribution class for calculating bradford distribution
	Bradford class inherits from distribution class of generalDistribution.py module

	Notation:
		X ~ Bradford(θ,min,max)

	Attributes:
		1. θ (theta)
		2. min (minimum value)
		3. max (maximum value)

	Parameters:
		0 < θ, min < max

	Support:
		min <= x <= max 
	"""	
	def __init__(self,theta=0,minVal=1,maxVal=1):
		#Default value of theta = 0
		self.theta = theta
		#Default value of min = 1
		self.min = minVal
		#Default value of max = 1
		self.max = maxVal

		Distribution.__init__(self,self.calculate_mean(),self.calculate_stdev())

	def calculate_mean(self):
		"""
		Method to calculate the mean of the input dataset
		
		Args:
			none

		Returns:
			self.mean(float): Mean of the input dataset

		Raises:
			ZeroDivisionError(string): Raised when division by zero
			ValueError(string): Raised when value error occurs
		"""
		try:
			#k = log(θ + 1)
			k = math.log(self.theta + 1)

			#Divided the formulae for mean into 2 parts: avgNumerator and avgDenominator
			avgNumerator = (self.theta * (self.max - self.min)) + (k * ((self.min * (self.theta + 1)) - self.max))
			avgDenominator = self.theta * k
			"""
				θ(max - min) + k[min(θ + 1) - max]
			Mean = ------------------------------------
					     θk
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
		Method to calculate the standard deviation of the input dataset
		
		Args:
			none

		Returns:
			self.stdev(float): Standard deviation of the input dataset

		Raises:
			ZeroDivisionError(string): Raised when division by zero
			ValueError(string): Raised when value error occurs
		"""
		try:
			#k = log(θ + 1)
			k = math.log(self.theta + 1)

			#Divided the formulae for mean into 2 parts: varNumerator and varDenominator
			varNumerator = ((self.max - self.min)**2) *((self.theta * (k - 2)) + (2 * k))
			varDenominator = 2 * self.theta * (k)**2
			"""
						     (max - min)^2 + [θ(k - 2) + 2k]
			Standard deviation =  sqrt  [-------------------------------]
							         2θk^2
			"""
			variance = varNumerator / varDenominator

			#Standard deviation = sqrt(variance)
			self.stdev = math.sqrt(variance)

		#If division by zero occurs, raise an error
		except ZeroDivisionError as error:	
			raise

		#If value error occurs, raise an error
		except ValueError as error:
			raise

	def pdf(self,x):
		"""
		Method to calculate probability density function for bradford distribution
	        
		Args:
			x(float): Random variable

		Returns:
			pdf(float): Probability density function for bradford distribution

		Raises:
			ZeroDivisionError(string): Raised when division by zero
			ValueError(string): Raised when value error occurs
		"""
		try:
			#Divided the formulae for mean into 2 parts: pdfNumerator and pdfDenominator
			pdfNumerator = self.theta
			pdfDenominator = ((self.theta * (x - self.min)) + self.max -self.min) * math.log(self.theta + 1)
			"""
							       θ
			Standard deviation =  ----------------------------------
					      (θ(x - min) + max - min)log(θ + 1) 
			"""
			return pdfNumerator / pdfDenominator

		#If division by zero occurs, raise an error
		except ZeroDivisionError as error:	
			raise

		#If value error occurs, raise an error
		except ValueError as error:
			raise


	def __add__(self,other):
		"""
		Method to add together two bradford distributions with equal p
        
		Args:
			other(bradford distribution): Bradford instance
            
		Returns:
			result(bradford distribution): Sum of bradford distribution
		"""
		result = Bradford()

		#Calculate the value of theta, min and max of the two bradford instances
		result.theta = self.theta + other.theta
		result.min = self.min + other.min
		result.max = self.max + other.max

		#Calculate the mean and standard deviation of the resultant bradford instances
		result.calculate_mean()
		result.calculate_stdev()
		return result

	def __repr__(self):
		"""
		Method to output the characteristics of the bradford instance

		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "θ: {}, Min: {}, Max: {}, Mean: {}, Standard Deviation: {}".format(self.theta,self.min,self.max,self.mean,self.stdev)