"""
Gaussian Distribution
(Also known as Normal Distribution)
"""
# Author: Ashwin Raj <rajashwin733@gmail.com>
# License: GNU General Public License v3.0

import math
from .generalDistribution import Distribution	#Import generalDistribution.py module

class Gaussian(Distribution):
	"""
	Gaussian distribution class for calculating gaussian distribution
	Gaussian class inherits from distribution class of generalDistribution.py module

	Notation:
		X ~ N(μ,σ)

	Attributes:
		1. mean (mean value of the distribution)
		2. stdev (standard deviation of the distribution)

	Parameters:
		μ ∈ ℝ = mean (location)
		σ > 0 = variance (squared scale)

	Support:
		x ∈ ℝ
	"""	
	def __init__(self,mu=0,sigma=1):
		#Default value of mu = 0 and sigma = 1
		Distribution.__init__(self,mu,sigma)

	def calculate_mean(self):
		"""
		Method to calculate the mean of the input dataset
		
		Args:
			none

		Returns:
			self.mean(float): Mean of the input dataset
		"""
		avg = 1.0 * sum(self.data)/len(self.data)
		
		#Mean = μ
		self.mean = avg
		return self.mean

	def calculate_stdev(self,sample=True):
		"""
		Method to calculate the standard deviation of the input dataset
		
		Args:
			sample(Bool): Check whether the data represents a sample or a population

		Returns:
			self.stdev(float): Standard Deviation of the input dataset
		"""

		if sample:
			#Value of n, if data represents sample
			n = len(self.data) - 1
		else:
			#Value of n, if data represents population
			n = len(self.data)

		mean = self.mean
		#Initializing value of sigma
		sigma = 0
		for d in self.data:
			#For each number, subtract the mean and square the result
			sigma += (d-mean)**2

		sigma = math.sqrt(sigma/n)
		#Standard deviation = σ
		self.stdev = sigma
		return self.stdev

	def pdf(self,x):
		"""
		Method to calculate probability density function for gaussian distribution
		
		Args:
			x(float): Point for calculating pdf
					
		Returns:
			pdf(float): Probability density function for gaussian distribution
		"""
		pdf = (1.0 / (self.stdev * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - self.mean) / self.stdev) ** 2)
		"""
			      1	    -(1/2)((x-μ)/σ)^(2)
		f(x;μ,σ) = ------- e
			    σ √2π
		"""
		return pdf

	def __add__(self, other):
		
		"""
		Method to add two Gaussian distributions
		
		Args:
			other(gaussian distribution): Gaussian instance
			
		Returns:
			result(gaussian distribution): Sum of gaussian distributions	
		"""
		result = Gaussian()

		#Calculate the mean of the two gaussian instances
		result.mean = self.mean + other.mean
		#Calculate the standard deviations of the two gaussian instances
		result.stdev = math.sqrt(self.stdev ** 2 + other.stdev ** 2)
		
		return result
		
	def __repr__(self):
	
		"""
		Method to output the characteristics of the gaussian instance
		
		Args:
			none
		
		Returns:
			output(string): Characteristics of the distribution
		"""
		return "Mean: {}, Standard Deviation: {}".format(self.mean, self.stdev)