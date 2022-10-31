"""
Burr Distribution
(Also known as Burr Type XII Distribution or the Singh-Maddala Distribution or the Generalised Log-Logistic Distribution)
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math
from .generalDistribution import Distribution	#Import generalDistribution.py module

class Burr(Distribution):
	"""
	Burr distribution class for calculating burr distribution
	Burr class inherits from distribution class of generalDistribution.py module

	Notation:
		X ~ Burr(a,b,k) or, X ~ SM(a,b,x)

	Attributes:
		1. k (shape parameter, k>0)
		2. a (shape parameter, a>0)
		3. b (shape parameter, b>0)

	Parameters:
		c > 0, k > 0

	Support:
		x > 0
	"""	
	def __init__(self,kParameter=1,alpha=1,beta=1):
		#Default value of k = 1
		self.k = kParameter
		#Default value of a = 1
		self.a = alpha
		#Default value of b = 1
		self.b = beta

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
		#Check mean for divison by zero error and value error
		try:
			partOne = self.a - (1 / self.b)
			#Value of Γ(a - (1/b))
			gammaOne = math.gamma(partOne)

			partTwo = 1 + (1 / self.b)
			#Value of Γ(1 + 1/b)
			gammaTwo = math.gamma(partTwo)

			#Value of Γ(a)
			gammaThree = math.gamma(self.a)

			powK = 1 / self.b
			#k raised to the power of powK
			partThree = self.k ** powK

			#Combining all parameters to calculate the mean
			avg = gammaOne * gammaTwo * (partThree / gammaThree)
			"""
			Mean = Γ(α-(1/β)) Γ(1+(1/β)) (k^(1/β)/Γ(α))
			"""
			self.mean = avg
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
        	#Check for divison by zero error and value error
		try:
			partOne = self.a - (2 / self.b)
			#Value of Γ(a - (2/b))
			gammaOne = math.gamma(partOne)

			partTwo = 1 + (2 / self.b)
			#Value of Γ(1 + (2/b))
			gammaTwo = math.gamma(partTwo)

			partThree = self.a - (1 / self.b)
			#Value of Γ(a - (1/b))
			gammaThree = math.gamma(partThree)

			partFour = 1 + (1 / self.b)
			#Value of Γ(1 + 1/b)
			gammaFour = math.gamma(partFour)

			#Value of Γ(a)
			gammaFive = math.gamma(self.a)

			powK = 2 / self.b
			#k raised to the power of powK
			partThree = self.k ** powK

			#operandOne = Γ(a - (2/b)) * Γ(1 + (2/b))
			operandOne = gammaOne * gammaTwo
			multiplierOne = gammaThree * gammaFour

			#operandTwo = ((Γ(a - (1/b)) * Γ(1 + 1/b))^2) / Γ(a)
			operandTwo = (multiplierOne ** 2) / gammaFive

			difference = operandOne - operandTwo

			"""
			Variance = [Γ(α - (2/β)) Γ(1 + (2/β)) - (((Γ(a - 1/b) Γ(1 + 1/b))^(2) / Γ(a))] (k^(2/β) / Γ(α))
			"""
			variance = difference * (partThree / gammaFive)

			#standard deviation = sqrt(variance)
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
		Method to calculate probability density function for burr distribution
        
		Args:
			x(float): Random variable

		Returns:
			pdf(float): Probability density function for burr distribution

		Raises:
			ZeroDivisionError(string): Raised when division by zero
		"""
		try:
			#k raised to power a
			powK = self.k ** self.a
			#x raised to power (b-1)
			powX = x ** (self.b - 1)

			#numerator = a * b * k^(a) * x^(b-1)
			numerator = self.a * self.b * powK * powX

			#denomSum = k + x^(b)
			denomSum = self.k + (x ** self.b)
			"""
				      α β k^(α) x^(β-1)
			f(x;k,a,b) = -------------------
				       (k+(x)^β)^(α+1)
			"""			
			powSum = self.a + 1

			#denominator = (k + x^(b))^(a+1)
			denominator = denomSum ** powSum
			return numerator / denominator

		#If division by zero occurs, raise an error
		except ZeroDivisionError as error:
			raise

	def __add__(self,other):
		"""
		Method to add together two burr distributions with equal p
        
		Args:
			other(burr distribution): Burr instance
            
		Returns:
			result(burr distribution): Sum of burr distribution
		"""
		result = Burr()

		#Calculate the shape parameters for the sum of the burr instances
		result.k = self.k + other.k
		result.a = self.a + other.a
		result.b = self.b + other.b

		#Calculate the mean of the two beta instances
		result.calculate_mean()
		#Calculate the standard deviations of the two burr instances
		result.calculate_stdev()
		return result

	def __repr__(self):
		"""
		Method to output the characteristics of the burr instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "k: {}, a: {}, b: {}, Mean: {}, Standard Deviation: {}".format(self.k,self.a,self.b,self.mean,self.stdev)