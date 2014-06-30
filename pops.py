#! /usr/bin/env python

"""
Created on Wed Aug 22 09:16:46 2012

@author: keder
"""
from copy import copy
from random import random
from goods import *
import pylab
from math import *


class EmptyClass:
	pass

populationConstants = EmptyClass()
populationConstants.pregnancyPeriod = 9

def finiteBordersFunction(x,a = -1,b = 1):
	if x < a:
		return 1
	elif x > b:
		return 0
	else:
		return (sin(pi / 2 * (-2*x+(b+a))/(b-a))+1)/2

def infiniteBordersFunction(x,a = -1,c = 0):
	if x < a:
		return 1
	elif x < c:
		return (sin(-pi / 2 * (x-c)/(b-c))+1)/2
	else:
		return 0.5*exp(-pi/2*(x-c)/(b-c))
	
	

class Stock:
	products = []
	def addItem(item):
		itemCopy = copy(item)
		self.products = self.products.append(itemCopy)

#class Family

class LifeNeeds:
	foodNorm = 16.0
	meatNorm = 4.0

class BaseNeeds:
	pass

class CommonNeeds:
	pass

class LuxuryNeeds:
	pass

class Stratum:

	def getAgeSexDistribution(self):
		table = []
		for generation in self.ageSexDistribution:
			table.append([int(generation[0]),int(generation[1])])
		return table

	def __init__(self, quantity):
		self.pregnanciesInterval = 1
		self.interbirthInterval = populationConstants.pregnancyPeriod + \
		self.pregnanciesInterval
		self.minPregnancyAge = 16 #years
		self.maxPregnancyAge = 35 #years
		self.minLabourAge = 16
		self.maxLabourAge = 40
		self.birthMortality = 0.3
		self.mortality = 0.00#2 #0.005
		self.childrenMortality = 0.002 #* 1.2
		self.senileMortality = 0.05
		self.matureAge = 16 #years
		self.averageLifeLength = 45 #years, reflects hard external conditions causing death like hard-working
		#bad ecology, crime, natural causes etc.
		self.senileAge = 50 #years
		self.mortality = 0.005 #percentages
		self.crimeDeathRate = 0.0
		self.modernFamily = 0
		#Traditional means traditional family which has great amount of children
		#and wife doing housework
		#Value 1 means traditional family, value 0 - modern family
		self.birthFemaleRatio = 0.50
		self.stock = Stock()
		self.ageSexDistribution = []
		generationQuantity = quantity/float((min(self.averageLifeLength, self.senileAge) ))
#		for i in range(0, self.matureAge):
#			self.ageSexDistribution.append(copy([0,0]))
		for i in range(0, min(self.averageLifeLength, self.senileAge)):
			self.ageSexDistribution.append(copy([generationQuantity, generationQuantity]))
#		print self.getAgeSexDistribution()
		self.getQuantity()
		self.getAbleBodied()



	def addToStock(self, goods):
		pass

	def setSettlement(self, settlement):
		self.settlement = settlement

	def getFertileWomen(self):
		self.fertileWomen = 0
		for i in range(self.minPregnancyAge, self.maxPregnancyAge):
			self.fertileWomen = self.fertileWomen + int(self.ageSexDistribution[i][1])
		#print "fert women:" + str(self.fertileWomen)
		return self.fertileWomen

 	def getBirthRate(self):
 		'''
		Recalculate and return birth rate (float)

 		'''
		self.getFertileWomen()
		self.getChildren()
#		m = 2.1
#		if (self.modernFamily) and (self.childrenQuantity/float(self.fertileWomen) > 0) and (self.childrenQuantity/float(self.fertileWomen) < m):
#			reduceGrowth = -(self.childrenQuantity/float(self.fertileWomen)) / m + 1
#			if  reduceGrowth < 0:
#				print self.childrenQuantity/float(self.fertileWomen)
#		elif (self.modernFamily) and (self.childrenQuantity/float(self.fertileWomen) >= m):
#			reduceGrowth = 0
		#normalizationFactor = - 7.05 15 30
		#normalizationFactor = -7.95 16 35
		fertility = 3
		normalizationFactor = -7.95
		if (self.modernFamily) and (self.childrenQuantity/float(self.fertileWomen) > max(normalizationFactor,0)):
			reduceGrowth = self.fertileWomen/float(self.childrenQuantity \
			- normalizationFactor * self.fertileWomen) * self.matureAge/float(self.maxPregnancyAge - self.minPregnancyAge)
		else:
			reduceGrowth = 1
		#print reduceGrowth
		self.birthRate = (1 / float(self.interbirthInterval)) \
		* (1 - self.birthMortality) * reduceGrowth   #and ratio of satiety
		#print "birth:" + str(self.birthRate)

		return self.birthRate

	def getAbleBodied(self):
		'''
		Recalculate and return able-bodied part of pop

		'''
		self.ableBodied = 0
		for i in range(self.minLabourAge, min(self.maxLabourAge,len(self.ageSexDistribution))):
			self.ableBodied = self.ableBodied + int(self.ageSexDistribution[i][0]) \
			+ int(self.modernFamily * 0 * self.ageSexDistribution[i][1])
		return self.ableBodied

	def getQuantity(self):
		self.quantity = 0
		for generation in self.ageSexDistribution:
			self.quantity = self.quantity + int(generation[0]) \
			+ int(generation[1])
		return self.quantity

	def getChildren(self):
		self.childrenQuantity = 0
		for generation in self.ageSexDistribution[0:self.matureAge]:
			self.childrenQuantity = self.childrenQuantity + int(generation[0]) \
			+ int(generation[1])
		return self.childrenQuantity

	def getGirls(self):
		self.girls = 0
		for generation in self.ageSexDistribution[0:self.matureAge]:
			self.girls = self.girls \
			+ int(generation[1])
		return self.childrenQuantity
	
	def getMortality(self, age):
		mortality = (1 - self.mortality) * (1 - self.crimeDeathRate)
		if age < self.matureAge:
				#deathRate = commonDeathRate * (1 - self.childrenMortality * (1 - i / 16)**2)
				mortality *= (1 - self.childrenMortality * 1.5)
			else:
				deathRate *= (1 - 1 / (1 + exp(-age  + self.senileAge)))**(0.083)
				#((abs(24*x)+1)^0.5-1)/4*x/abs(x)

	def mounthChange(self):
		'''
		Calculate population.

		'''
		commonDeathRate =  #Plus starvation
#		print	commonDeathRate
		self.ageSexDistribution[0][0] = self.ageSexDistribution[0][0] + \
		float(self.getBirthRate() * self.fertileWomen * (1 - self.birthFemaleRatio))
#		if self.ageSexDistribution[0][0] < 0:
#			print self.ageSexDistribution[0][0]
		#print "ratio:" + str(1 - self.birthFemaleRatio)
		self.ageSexDistribution[0][1] = self.ageSexDistribution[0][1] + \
		float(self.getBirthRate() * self.fertileWomen * self.birthFemaleRatio)
		for i in range (1,len(self.ageSexDistribution)):
			

			self.ageSexDistribution[i] = [self.ageSexDistribution[i][0] * deathRate,\
			self.ageSexDistribution[i][1] * deathRate]
			if self.ageSexDistribution[i][0] < 1:
				self.ageSexDistribution[i][0] = 0
			if self.ageSexDistribution[i][1] < 1:
				self.ageSexDistribution[i][1] = 0
		self.getQuantity()
		self.getAbleBodied()
		self.getChildren()
		self.getGirls()

	def yearChange(self):
		#print "birth:" + str(self.ageSexDistribution[0])
		maxIndex = len(self.ageSexDistribution)-1
		#print "last:" + str(self.ageSexDistribution[maxIndex])
		if (self.ageSexDistribution[maxIndex][0] > 1) or \
		self.ageSexDistribution[maxIndex][1] > 1:
			self.ageSexDistribution.append( \
			copy(self.ageSexDistribution[maxIndex]))
			#print "appended!"
		for i in range(0, maxIndex):
			self.ageSexDistribution[maxIndex - i] = \
			copy(self.ageSexDistribution[maxIndex - i - 1])
		self.ageSexDistribution[0] = copy([0, 0])


	def split(self, quant):
		'''
		Split pop on two parts and return new pop with specified quantity
		quantity (float) - population of new pop

		'''
		newPop = copy(self)
		self.quantity = self.quantity - quant
		newPop.quantity = quant
		print newPop.quantity
		return newPop

def plotGraf(y, string):
	xlist = [x for x in range(len(y))]
	ylist = y
	pylab.plot(xlist, ylist)
	pylab.title(string)

#pop = Stratum(5000 + 10000 * random())
pop = Stratum(50000)

#pop1 = copy(pop)
#pop1.modernFamily = 0

y1 = []
y2 = []
y3 = []
y5 = []
years = 12 * 1000

for i in range(years):
	if (i % 12) == 0:
		print "population at year " + str(int(i/12)) + " month " + str(i-int(i/12)*12) + ":" + str(pop.quantity)
		print "0s/16s at year " + str(int(i/12)) + " month " + str(i-int(i/12)*12) + ":" + str(pop.ageSexDistribution[0][1]/pop.ageSexDistribution[16][1])
		pop.yearChange()

#		pop1.yearChange()
#		if i/12 > 450:
#			tab = []
#			for gen in pop.ageSexDistribution:
#				tab.append(gen[1] + gen[0])
#
#			plotGraf(tab,'Year-'+str(i/12)+'.png')

#	#	pylab.show()
		#pylab.clf()

	pop.mounthChange()
#	if i == years / 2:
#		pop.modernFamily = 1
#	pop1.mounthChange()
#	print pop.getAgeSexDistribution()

	#print "child per others:" + str(float(pop.childrenQuantity)/pop.fertileWomen)
	#y1.append(copy(float(pop.childrenQuantity)/pop.ableBodied))
	y1.append(copy(float(pop.quantity)))
	y5.append(copy(float(pop.ageSexDistribution[14][1]/float(pop.ageSexDistribution[15][1]))*(pop.maxPregnancyAge - pop.minPregnancyAge)/pop.matureAge))
	y3.append(copy(float(pop.ageSexDistribution[14][1]/float(pop.ageSexDistribution[15][1]))*(pop.maxPregnancyAge - pop.minPregnancyAge)/pop.matureAge))

#print len(pop.getAgeSexDistribution())
pylab.savefig('/home/keder/test/Year-'+str(i/12)+'.png')
y2 = []
print exp(float(0.005*5+1))
#print "last:" + str(pop.ageSexDistribution[-1][1])
for gen in pop.ageSexDistribution:
	y2.append(gen[1])
#		pylab.savefig('/home/keder/test/Year-'+str(i/12)+'.png')
pylab.show()
pylab.clf()

summ = 0
for n in range(pop.maxPregnancyAge-pop.minPregnancyAge):
	prod = 1
	for a in range(pop.minPregnancyAge,pop.minPregnancyAge+n):
		prod = prod * (1-)


plotGraf(y1,"")

pylab.show()
plotGraf(y2, "Population")

pylab.show()

plotGraf(y3, "Girls/Women")
plotGraf(y5, "Girls/Women")
pylab.show()
#print "modern:" + str(pop.modernFamily)
#print "modern:" + str(pop1.modernFamily)
