"""
Bernoulli Distribution
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math
from .generalDistribution import Distribution	#Import generalDistribution.py module

class Bernoulli(Distribution):
	"""
	Bernoulli distribution class for calculating bernoulli distribution
	Bernoulli class inherits from distribution class of generalDistribution.py module

	Notation:
		X ~ Ber(p)

	Attributes:
		1. p(probability of success on a single trial)

	Parameters:
		0 ≤ p ≤ 1
		q = 1 - p

	Support:
		k ∈ {0,1}
	"""
	def __init__(self,prob=0.5):
		#Default value of p = 0.5
		self.p = prob

		Distribution.__init__(self,self.calculate_mean(),self.calculate_stdev())

	def calculate_mean(self):
		"""
		Method to calculate the mean
        
		Args:
			none
        
		Returns: 
			self.mean(float): Mean of the data set
		"""
		self.mean = self.p
		return self.mean

	def calculate_stdev(self):
		"""
		Method to calculate the standard deviation
        
		Args: 
			none
        
		Returns: 
			self.stdev(float): Standard deviation of the data set
		"""
        	#q = 1-p
		variance = self.p * (1 - self.p)
		
		#Standard deviation = sqrt(variance)
		self.stdev = math.sqrt(variance)
		return self.stdev

	def replace_stats_with_data(self):
		"""
		Method to calculate p from the data set
        
		Args: 
			none
        
		Returns: 
			self.p(float): Value of p
		"""
		self.n = len(self.data) 
		self.p = 1.0 * sum(self.data) / self.n

		#Calculate mean and standard deviation
		self.mean = self.calculate_mean()
		self.stdev = self.calculate_stdev()
		return self.p

	def pdf(self,x):
		"""
		Method to calculate probability density function for bernoulli distribution
        
		Args:
			k(float): Number of times for a specific outcome within n trials

		Returns:
			pdf(float): Probability density function for bernoulli distribution
		"""
		pdf = ((self.p ** x) * ((1 - self.p) ** x))
		"""
		f(x;p) = p^(k) (1-p)^(1-k)
		"""
		return pdf

	def __add__(self,other):
		"""
		Method to add together two bernoulli distributions with equal p
        
		Args:
			other(bernoulli distribution): Bernoulli instance
            
		Returns:
			result(bernoulli distribution): Sum of bernoulli distribution
		"""
		result = Bernoulli()

		#Calculate sum of the success probability of the two bernoulli instances
		result.p = self.p + other.p
		#Calculate the mean of the two bernoulli instances	
		result.calculate_mean()
		#Calculate the standard deviations of the two bernoulli instances
		result.calculate_stdev()
		return result

	def __repr__(self):
		"""
		Method to output the characteristics of the bernoulli instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return " p: {}, mean: {}, standard deviation: {}".format(self.p,self.mean,self.stdev)