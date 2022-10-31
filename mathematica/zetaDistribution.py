"""
Zeta Distribution
(Also known as Zipf Distribution)
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math

class Zeta:
	"""
	Zeta distribution class for calculating zeta distribution

	Notation:
		X ∼ Zipf(α,n)

	Attributes:
		1. n (positive integer)
		2. a (positive integer)

	Parameters:
		α ∈ (1,∞)

	Support:
		n ∈ {1,2,...}
	"""	
	def __init__(self,nLimit=1,aValue=1):
		#Default value of n = 1
		self.n = nLimit
		#Default value of a = 1
		self.a = aValue

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
			riemannZetaFunction1 = 0
			"""
			       ∞     1
			ζ(α) = Σ  -------,  α ∈ (1,∞)
			      n=1  (n)^α
			"""
			for i in range (1,int(self.n)):
				riemannZetaFunction1 = (1 / (self.n ** self.a)) + riemannZetaFunction1

			riemannZetaFunction2 = 0
			b = float(self.a - 1)
			for i in range (1,int(self.n)):
				riemannZetaFunction2 = (1 / (self.n ** b)) + riemannZetaFunction2

			#Calculate the numerator and denominator of the mean
			avgNumerator = riemannZetaFunction2
			avgDenominator = riemannZetaFunction1
			"""
				ζ(α-1)
			Mean = --------, α>2
				 ζ(α)
			"""
			avg = avgNumerator / avgDenominator

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
		#Check stdev for divison by zero error and value error
		try:
			riemannZetaFunction1 = 0
			"""
			       ∞     1
			ζ(α) = Σ  -------,  α ∈ (1,∞)
			      n=1  (n)^α
			"""
			for i in range (1,int(self.n)):
				riemannZetaFunction1 = (1 / (self.n ** self.a)) + riemannZetaFunction1

			riemannZetaFunction2 = 0
			b = float(self.a - 2)
			for i in range (1,int(self.n)):
				riemannZetaFunction2 = (1 / (self.n ** b)) + riemannZetaFunction2

			riemannZetaFunction3 = 0
			c = float(self.a - 1)
			for i in range (1,int(self.n)):
				riemannZetaFunction3 = (1 / (self.n ** c)) + riemannZetaFunction3

			#Calculate the numerator and denominator of the standard deviation
			varNumerator = ((riemannZetaFunction1 * riemannZetaFunction2) - (riemannZetaFunction3) ** 2)
			varDenominator= riemannZetaFunction1 ** 2
			"""
				      ζ(α)ζ(α-2) - ζ(α-1)^2
			Variance =   -----------------------, α>3
					      ζ(α)^2
			"""
			variance = varNumerator / varDenominator

			#standard dviation = sqrt(variance)
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
		Method to calculate probability density function for zeta distribution
        
		Args:
			x(float): Random variable

		Returns:
			pdf(float): Probability density function for zeta distribution

		Raises:
			ZeroDivisionError(string): Raised when division by zero
			ValueError(string): Raised when value error occurs
		"""
		riemannZetaFunction = 0
		"""
		       ∞     1
		ζ(α) = Σ  -------,  α ∈ (1,∞)
		      n=1  (n)^α
		"""
		for i in range (1,int(self.n)):
			riemannZetaFunction = (1 / (self.n ** self.a)) + riemannZetaFunction

		try:
			"""
				     1
			f(x;α) = ---------, x ∈ ℕ+
				  ζ(α)x^α
			"""
			return 1 / (riemannZetaFunction * (x ** self.a))

		#If division by zero occurs, raise an error
		except ZeroDivisionError as error:	
			raise

		#If value error occurs, raise an error
		except ValueError as error:
			raise

	def __add__(self,other):
		"""
		Method to add together two zeta distributions with equal p
        
		Args:
			other(zeta distribution): Zeta instance
            
		Returns:
			result(zeta distribution): Sum of zeta distribution
		"""
		result = Zeta()

		#Calculate the shape parameter of the sum of two instances
		result.n = self.n + other.n
		result.a = self.a + other.a

		#Calculate the mean of the two zeta instances
		result.calculate_mean()
		#Calculate the standard deviations of the two zeta instances
		result.calculate_stdev()
		return result

	def __repr__(self):
		"""
		Method to output the characteristics of the zeta instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "Limit:{}, Value of a:{}".format(self.n,self.a)