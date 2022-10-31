"""
Bates Distribution
(Also known as Rectangular Mean Distribution)
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math
from .generalDistribution import Distribution	#Import generalDistribution.py module

class Bates(Distribution):
	"""
	Bates distribution class for calculating bates distribution
	Bates class inherits from distribution class of generalDistribution.py module

	Notation:
		X ~ Bates(n,a,b)

	Attributes:
		1. n (sample size, k>0)
		2. a (lower bound, a>0)
		3. b (upper bound, b>0)

	Parameters:
		-∞ < a < b < +∞

	Support:
		x ∈ [a,b]
	"""	
	def __init__(self,sampleSize=12,lowerBound=0,upperBound=1):
		#Default value of n = 12
		self.n = sampleSize
		#Default value of a = 0
		self.a = lowerBound
		#Default value of b = 1
		self.b = upperBound

		Distribution.__init__(self,self.calculate_mean(),self.calculate_stdev())

	def calculate_mean(self):
		"""
		Method to calculate the mean of the input dataset
		
		Args:
			none

		Returns:
			self.mean(float): Mean of the input dataset
		"""
		self.mean = (self.a + self.b) / 2
		return self.mean

	def calculate_stdev(self):
		"""
		Method to calculate the standard deviation
        
		Args: 
			none
        
		Returns: 
			self.stdev(float): Standard deviation of the data set

		Raises:
			ZeroDivisionError(string): Raised when division by zero
		"""
		try:
			"""
				    (b - a)^(2)
			Variance = -------------
					12n
			"""
			variance = (self.b - self.a) ** 2 / (12 * self.n)

			#standard deviation = sqrt(variance)
			self.stdev = math.sqrt(variance)
			return self.stdev

		#If division by zero occurs, raise an error
		except ZeroDivisionError as error:	
			raise

	def pdf(self,x):
		"""
		Method to calculate probability density function for bates distribution
        
		Args:
			x(float): Random variable

		Returns:
			pdf(float): Probability density function for bates distribution

		Raises:
			ZeroDivisionError(string): Raised when division by zero
			ValueError(string): Raised when value error occurs
		"""
		try:
			#r = n[(x-a)/(b-a)]
			r = self.n * ((x - self.a) / (self.b - self.a))
			#i = greatest integer ≤ r
			i = math.ceil(r)
			#nCk = binomial coefficient
			nCk = math.factorial(int(self.n)) / (math.factorial(int(r)) * math.factorial(int(self.n - r)))

			partA = self.n / ((self.b - self.a) * math.factorial(int(self.n - 1)))
			partB = 0	#Lower bound value of partB

			#Value of Σ[(-1)^k·nCk·(r-k)^(n-1)]
			for k in range(0,i):
				partB += ((-1)**k) * nCk * ((r-k)**(self.n-1))

			"""
					    n       i
			f(x;a,b,n) =  ------------  Σ[(-1)^k·nCk·(r-k)^(n-1)]
				       (b-a)(n-1)! k=0
			"""
			return partA * partB

		#If division by zero occurs, raise an error
		except ZeroDivisionError as error:	
			raise

		#If value error occurs, raise an error
		except ValueError as error:
			raise

	def __add__(self,other):
		"""
		Method to add together two bates distributions with equal p
        
		Args:
			other(bates distribution): Bates instance
            
		Returns:
			result(bates distribution): Sum of bates distribution
		"""
		result = Bates()

		#Calculate the sample size for the sum of the bates instances
		result.n = self.n + other.n

		#Calculate the lower bound and upper bound of the resultant bates instance
		result.a = self.a + other.a
		result.b = self.b + other.b

		#Calculate the mean of the two bates instances
		result.calculate_mean()
		#Calculate the standard deviation of the two bates instances
		result.calculate_stdev()
		return result

	def __repr__(self):
		"""
		Method to output the characteristics of the bates instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "Number of random variables: {}, Lower Bound: {}, Upper Bound: {}, Mean: {}, Standard Deviation: {}".format(self.n,self.a,self.b,self.mean,self.stdev)