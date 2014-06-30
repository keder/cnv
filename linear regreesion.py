#! /usr/bin/env python
"""
Created on Fri Sep  7 10:19:43 2012

@author: keder
"""
from pylab import *
import scipy
from mpl_toolkits.mplot3d import *


def plotGraf(x, y, z, string):
	plot(x, y, z)
	title(string)

x = [0.94,1.01,1.08,1.16,1.26,1.38,1.52,1.69,1.88,2.13,2.40,2.71,3.05,3.45]
y = [-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5]

z = [0.94,4.01,9.08,16.16,24.86,36.18,49.02]
#z = [0.94,2.01,3.08,4.16,4.86,6.18,7.02]
x = [1,2,3,4,5,6,7]

#==============================================================================
# def f(x,theta2,theta1,theta0):
# 	res = []
# 	for i in range(0,len(x)):
#
# 		res.append(theta0 + theta2*((x[i]+theta1)**0.5))
# 	return res
#==============================================================================

def f2(x,theta1,theta0):
	res = []
	for i in range(0,len(x)):
		res.append(theta0 + theta1*x[i])
	return res

def cost(x,z,theta1,theta0):
	m = len(x)
	return 2*sum(elemPow(elemDiff(f(x,theta1,theta0),z),2)) / m

def f(x,theta1,theta0):
	res = []
	for i in range(0,len(x)):
		res.append(theta0 + theta1*x[i]**2)
	return res

#==============================================================================
# def costFunction(x,y,theta1,theta0):
# 	summ = 0
# 	for i in range(0, len(x)):
# 		summ = summ + (f(x[i],theta1,theta0) - y[i]) ** 2
# 	return summ/len(x)
#==============================================================================

def mltSum(x,y):
	summ = 0
	for i in range(0,len(x)):
		summ = summ + x[i]*y[i]
	return summ

m = len(x)

def elemSum(x,y):
	res = []
	for i in range(0,len(x)):
		res.append(x[i]+y[i])
	return res

def elemSum2(x,n):
	res = []
	for i in range(0,len(x)):
		res.append(abs(x[i]+n))
	return res

def elemDiff(x,y):
	res = []
	for i in range(0,len(x)):
		res.append(x[i]-y[i])
	return res

def elemMult(x,y):
	res = []
	for i in range(0,len(x)):
		res.append(x[i]*y[i])
	return res

def elemPow(x,power):
	res = []
	for i in range(0,len(x)):
		res.append(x[i]**power)
	return res

def grad(x,z):
	m = len(x)
	alpha0 = 0.01
	alpha1 = 0.0001
	theta0 = 4
	theta1 = 3
	epsilon = 3
	costi = 0
	oldcost = 1000
	while epsilon > 0.0000001:

		delta0 = alpha0 * sum(elemDiff(f(x,theta1,theta0),z)) / m
#		print "del:" + str(delta0)
		#delta1 = alpha * sum(elemMult(elemDiff(f(x,theta1,theta0),z), x)) / m
		delta1 = alpha1 * sum(elemMult(elemDiff(f(x,theta1,theta0),z), elemPow(x,2))) / m
		theta0 = theta0 - delta0
		print "del:" + str(elemPow(elemMult(elemDiff(f(x,theta1,theta0),z), x),2))
		theta1 = theta1 - delta1
		costi = cost(x,z,theta1,theta0)
		epsilon = abs(oldcost-costi)
		oldcost = costi
		#print sum(elemDiff(f(x,theta2,theta1,theta0),y))
	return [theta0,theta1]

[theta0,theta1] = grad(x,z)
print [theta0,theta1]
#[theta0,theta1,theta2] = [-8,-0.94,8.2]
#[theta0,theta1,theta2] = [16,-45,0.94]
z1 = f(x,theta1,theta0)
print z1
#print [theta0,theta1,theta2]
#[x,y] = scipy.meshgrid(x,y)
#fig = figure()
#ax = Axes3D(fig)
#ax.plot_surface(x,y,z1)
##plotGraf(x,y,z,"")
#show()

