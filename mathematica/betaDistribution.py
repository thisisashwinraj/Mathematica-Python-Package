"""
Beta Distribution
(Also known as Normal Distribution)
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math
from .generalDistribution import Distribution	#Import generalDistribution.py module

class Beta(Distribution):
	"""
	Beta distribution class for calculating beta distribution
	Beta class inherits from distribution class of generalDistribution.py module

	Notation:
		X ~ Beta(α, β)

	Attributes:
		1. alpha (shape parameter)
		2. beta (shape parameter)

	Parameters:
		α > 0 shape (real)
		β > 0 shape (real)

	Support:
		x ∈ [0,1]
		x ∈ (0,1)
	"""	
	def __init__(self,xShapeParam=0,yShapeParam=1):
		#Default value of alpha = 0
		self.alpha = xShapeParam
		#Default value of beta = 1
		self.beta = yShapeParam

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
		"""
		#Check mean for divison by zero error
		try:
			self.mean = self.alpha / (self.alpha + self.beta)
			"""
				  α
			Mean = --------
				α + β
			"""
			return self.mean

		#If division by zero occurs, raise an error
		except ZeroDivisionError as error:	
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
			ValueError(string): Raised when negative number passed for square root
		"""
		#Check stdev for divison by zero error and value error
		try:
			#Dividing the expression to calculate standard deviation for convenience
			numerator = self.alpha * self.beta
			denominator = ((self.alpha + self.beta) ** 2) * (self.alpha + self.beta + 1)
			"""
					   α β
			Variance = -------------------
				    (α+β)^(2) (α+β+1)
			"""
			variance = numerator / denominator

			#Standard deviation = sqrt(variance)
			self.stdev = math.sqrt(variance)
			return self.stdev

		#If division by zero occurs, raise an error
		except ZeroDivisionError as error:	
			raise

		#If negative number passed for calculating square root, raise an error
		except ValueError as error:
			raise

	def pdf(self,x,lowerBound=0,upperBound=1):
		"""
		Method to calculate probability density function for beta distribution
        
		Args:
			lowerBound(float): lower bound
			upperBound(float): upper bound

		Returns:
			pdf(float): Probability density function for beta distribution
		"""
		try:
			#Gamma value of sum of the shape parameters
			gammaSum = self.alpha + self.beta
			#normalizingConstant = B(alpha,beta)
			normalizingConstant = (math.gamma(self.alpha) * math.gamma(self.beta)) / math.gamma(gammaSum)

			#Returns power to be used in calculating the pdf
			powDenom = self.alpha + self.beta - 1
			pw1 = self.alpha - 1
			pw2 = self.beta - 1
			"""
				     x^(α-1) (1-x)^(β-1)
			f(x;α,β) = ----------------------
					   B(α,β)

			where,			   Γ(α) Γ(β)
					B(α,β) = -------------, and Γ is the gamma function
						    Γ(α,β)
			"""
			#Calculate the numerator and denominator of the pdf
			pdfDenominator = normalizingConstant * ((upperBound - lowerBound) ** powDenom)
			pdfNumerator = ((x - lowerBound) ** pw1) * ((upperBound - x) ** pw2)
			return pdfNumerator / pdfDenominator

		#If division by zero occurs, raise an error
		except ZeroDivisionError as error:	
			raise

		#If negative number passed for calculating square root, raise an error
		except ValueError as error:
			raise

	def __add__(self,other):
		"""
		Method to add together two beta distributions with equal p
        
		Args:
			other(beta distribution): Beta instance
            
		Returns:
			result(beta distribution): Sum of beta distribution
		"""
		result = Beta()

		#Calculate the shape parameters for the sum of the beta instance
		result.alpha = self.alpha + other.alpha
		result.beta = self.beta + other.beta

		#Calculate the mean of the two beta instances
		result.calculate_mean()
		#Calculate the standard deviations of the two beta instances
		result.calculate_stdev()
		return result

	def __repr__(self):
		"""
		Method to output the characteristics of the beta instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "alpha: {}, beta: {}, mean: {}, standard deviation: {}".format(self.alpha,self.beta,self.mean,self.stdev)