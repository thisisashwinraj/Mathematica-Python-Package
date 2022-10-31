"""
Poisson Distribution
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math
from .generalDistribution import Distribution 	#Import generalDistribution.py module

class Poisson(Distribution):
	"""
	Poisson distribution class for calculating poisson distribution
	Poisson class inherits from distribution class of generalDistribution.py module

	Notation:
		X ~ Pois(μ)

	Attributes:
		1. mu (rate parameter)

	Parameters:
		μ ∈ (0,∞) (rate)

	Support:
		k ∈ ℕ0 (Natural numbers starting from 0)
	"""
	def __init__(self,rateParameter=0.5):
		#Default value of mu = 0.5
		self.mu = rateParameter

		Distribution.__init__(self,self.calculate_mean(),self.calculate_stdev())

	def calculate_mean(self):
		"""
		Method to calculate the mean
        
		Args: 
			none
        
		Returns: 
			self.mean(float): Mean of the data set
		"""
		self.mean = self.mu
		#Mean = μ
		return self.mean

	def calculate_stdev(self):
		"""
		Method to calculate the standard deviation
        
		Args: 
			none
        
		Returns: 
			self.stdev(float): Standard deviation of the data set
		"""
		variance = self.mu

		#Standard deviation = sqrt(variance)
		self.stdev = math.sqrt(variance)
		return self.stdev

	def calculate_mu(self,lamda,t):
		"""
		Method to calculate rate parameter from event rate and time interval
        
		Args:
			lamda(float): Event Rate
			t(float): Time Interval

		Returns:
			self.mu(float): Rate Parameter
		"""
		self.mu = lamda * t
		return self.mu


	def pdf(self,x):
		"""
		Method to calculate probability density function for poisson distribution
        
		Args:
			x(float): Random variable

		Returns:
			pdf(float): Probability density function for poisson distribution
		"""
		pdf = (self.mu ** x) / ((self.mu ** x) * (math.exp(self.mu)))
		"""
			 (e^(-μ) μ(x))
		f(x;μ) = ---------------
			       x!
		"""
		return pdf

	def __add__(self,other):
		"""
		Method to add together two poisson distributions with equal p
        
		Args:
			other(poisson distribution): Poisson instance
            
		Returns:
			result(poisson distribution): Sum of poisson distribution
		"""
		result = Poisson()

		#Calculate the sum of the rate parameter of the two poisson instances
		result.mu = self.mu + other.mu

		#Calculate the mean and standard deviation of the result
		result.calculate_mean()
		result.calculate_stdev()

		return result

	def __repr__(self):
		"""
		Method to output the characteristics of the poisson instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "mu: {}, mean: {}, standard deviation: {}".format(self.mu,self.mean,self.stdev)