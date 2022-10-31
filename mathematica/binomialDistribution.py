"""
Binomial Distribution
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math
from .generalDistribution import Distribution	#Import generalDistribution.py module

class Binomial(Distribution):
	"""
	Binomial distribution class for calculating binomial distribution
	Binomial class inherits from distribution class of generalDistribution.py module
	
	Notation:
		X ~ Bin(n, p)

	Attributes:
		1. p (probability of success on a single trial)
		2. n (number of trials)

	Parameters:
		n ∈ {0,1,2...} - number of trials
		p ∈ [0,1] - success probability for each trial
		q = 1-p

	Support:
		k ∈ {0,1,...,n} - number of successess
	"""
	def __init__(self,prob=0.5,size=20):
		#Default value of p = 0.5
		self.p = prob
		#Default value of n = 20
		self.n = size

		Distribution.__init__(self,self.calculate_mean(),self.calculate_stdev())

	def calculate_mean(self):
		"""
		Method to calculate the mean
        
		Args: 
			none
        
		Returns: 
			self.mean(float): Mean of the data set
		"""
		#Mean = np
		self.mean = self.n * self.p
		return self.mean

	def calculate_stdev(self):
		"""
		Method to calculate the standard deviation
        
		Args: 
			none
        
		Returns: 
			self.stdev(float): Standard deviation of the data set
		"""
		#Variance = npq
		variance = self.n * self.p * (1 - self.p)

		#Standard deviation = sqrt(variance)
		self.stdev = math.sqrt(variance)
		return self.stdev

	def replace_stats_with_data(self):
		"""
		Method to calculate p and n from the data set
        
		Args: 
			none
        
		Returns: 
			self.p(float): Value of p
			self.n(float): Value of n    
		"""
		self.n = len(self.data)
		self.p = 1.0 * sum(self.data) / self.n

		#Calculate mean and standard deviation
		self.mean = self.calculate_mean()
		self.stdev = self.calculate_stdev()
		return self.p, self.n

	def pdf(self,k):
		"""
		Method to calculate probability density function for binomial distribution
        
		Args:
			k(float): Number of times for a specific outcome within n trials

		Returns:
			pdf(float): Probability density function for binomial distribution
        	"""
        	#Value of a = ((n!)/((n-x)! * x!))
		a = math.factorial(self.n) / (math.factorial(k) * (math.factorial(self.n - k)))

		#Value of b = (p**x) * (1-p)**(n-x)
		b = (self.p ** k) * (1 - self.p) ** (self.n - k)
		"""
		f(x;n,p) = nCk p^(k) q^(n-k), for k = 0,1,2,...,n

		where,			 n!
				nCk = ---------
				      k! (n-k)!
		"""
		return a * b

	def __add__(self,other):
		"""
		Method to add together two binomial distributions with equal p
        
		Args:
			other(binomial distribution): Binomial instance
            
		Returns:
			result(binomial distribution): Sum of binomial distribution

		Raises:
			assertionError(string): Raised when values of p are not equal
        	"""
		#Check if success probabilities of both binomial distributions are the same
		try:
			assert self.p == other.p, 'p values are not equal'

		#If values are not same, raise an error
		except AssertionError as error:
			raise

		result = Binomial()

		#Calculate sum of the number of trials of the two binomial instances
		result.n = self.n + other.n
		#Success probability of the resultant binomial distribution (same as the two distributions)
		result.p = self.p

		#Calculate the mean and standard deviation of the two binomial instances	
		result.calculate_mean()
		result.calculate_stdev()

		return result

	def __repr__(self):
		"""
		Method to output the characteristics of the binomial instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
        	"""
		return "p: {}, n: {}, mean: {}, standard deviation: {}".format(self.p,self.n,self.mean,self.stdev)