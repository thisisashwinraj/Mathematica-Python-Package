"""
Trapezoidal Distribution
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math
from .generalDistribution import Distribution	#Import generalDistribution.py module

class Trapezoidal(Distribution):
	"""
	Trapezoidal distribution class for calculating trapezoidal distribution
	Trapezoidal class inherits from distribution class of generalDistribution.py module

	Notation:
		X ∼ Trapezoidal(a,b,c,d)

	Attributes:
		1. a (lower bound)
		2. b (level start)
		3. c (level end)
		4. d (upper bound)

	Parameters:
		a (a<d) - lower bound
		b (a≤b<c) - level start
		c (b<c≤d) - level end
		d (c≤d) - upper bound

	Support:
		x ∈ [a,d]
	"""
	def __init__(self,lowerBound=1,levelStart=2,levelEnd=3,upperBound=4):
		#Default value of a = 1
		self.a = lowerBound
		#Default value of b = 2
		self.b = levelStart
		#default value of c = 3
		self.c = levelEnd
		#Default value of d = 4
		self.d = upperBound

		Distribution.__init__(self,self.calculate_mean(),self.calculate_stdev())

	def calculate_mean(self):
		"""
		Method to calculate the mean
		
		Args:
			none

		Returns:
			self.mean(float): Mean of the input dataset

		Raises:
        	ZeroDivisionError(string): Raised when division by zero
		"""
		try:
			#Split the expression to calculate mean into two parts for convenience
			operandOne = 1 / (3 * (self.d + self.c - self.b - self.a))
			operandTwo = (((self.d ** 3 - self.c ** 3) / (self.d - self.c)) - ((self.b ** 3 - self.a ** 3) / (self.b - self.a)))
			"""
				    1	       d^(3) - c^(3)	   d^(3) - c^(3)
			Mean = ------------ ((---------------) - (---------------))
				3(d+c-b-a)	   (d-c)		(b-a)
			"""
			self.mean = operandOne * operandTwo
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
			self.stdev(float): Standard deviation of the input dataset

		Raises:
			ZeroDivisionError(string): Raised when division by zero
			ValueError(string): Raised when value error occurs
		"""
		try:
			#Split the expression to calculate standard deviation into three parts for convenience
			varianceOperandOne = 1 / (6 * (self.d + self.c - self.b - self.a))
			varianceOperandTwo = (((self.d ** 4 - self.c ** 4) / (self.d - self.c)) - ((self.b ** 4 - self.a ** 4) / (self.b - self.a)))
			"""
				2
			μ = ---------, a ≤ b ≤ c ≤ d
			     d+c-a-b
			""" 
			mu = 2 / (self.d + self.c - self.a - self.b)

			varianceOperandThree = mu ** 2
			"""
					1	  d^(4) - c^(4)	      d^(4) - c^(4)
			Variance = ------------ (---------------  -  ---------------) - μ^(2)
				    6(d+c-b-a)	      (d-c)		  (b-a)
			"""
			variance = (varianceOperandOne * varianceOperandTwo) - varianceOperandThree
			
			#Standard deviation = sqrt(variance)
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
		Method to calculate probability density function for trapezoidal distribution
        
		Args:
			x(float): Random variable

		Returns:
			pdf(float): Probability density function for trapezoidal distribution

		Raises:
			ZeroDivisionError(string): Raised when division by zero
			ValueError(string): Raised when value error occurs
		"""
		mu = 2 / (self.d + self.c - self.a - self.b)
		"""
				2
		μ = ---------, a ≤ b ≤ c ≤ d
			 d+c-a-b
		""" 
		try:
			if(self.a <= x and self.b > x):
				"""
						  x-a
				f(x;a,b,c,d) = μ -----, a ≤ x < b
						  b-a
				"""
				pdf = mu * ((x - self.a) / (self.b - self.a))

			elif(self.b <= x and self.c > x):
				"""
				f(x;a,b,c,d) = μ, b ≤ x < c
				"""
				pdf = mu

			elif(self.c <= x and self.d >= x):
				"""
						  d-a
				f(x;a,b,c,d) = μ -----, c ≤ x < d
						  d-c
				"""
				pdf = mu * ((self.d - x) / (self.d - self.c))

			else:
				#Value of pdf is undefined for x > d
				pdf = "Undefined"

			return pdf

		#If division by zero occurs, raise an error
		except ZeroDivisionError as error:	
			raise

		#If value error occurs, raise an error
		except ValueError as error:
			raise

	def __repr__(self):
		"""
		Method to output the characteristics of the trapezoidal instance
        
		Args:
			none
        
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "a:{}, b:{}, c:{}, d:{}, Mean:{}, Standard Deviation:{}".format(self.a,self.b,self.c,self.d,self.mean,self.stdev)