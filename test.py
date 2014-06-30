# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 17:49:04 2013

@author: keder
"""

def linearFunction(x,x1,y1,x2,y2):
	k = float(y2-y1) / float(x2-x1)
	b = float(y1*x2 - y2*x1) / float(x2-x1)
	return k*x + b
	
def rasterizeLine(point1, point2):
	real_x1 = point1[0] + 0.5
	real_y1 = point1[1] + 0.5
	real_x2 = point2[0] + 0.5
	real_y2 = point2[1] + 0.5
	result = []
	for x in range(point1[0], point2[0] + 1):
		result.append([x, int(linearFunction(x + 0.5, real_x1, real_y1, real_x2, real_y2))])
	return result
		
colors = ['red', 'green', 'blue', 'yellow']
def first(elem):
	return elem[0]

print sorted(colors, key=first)
		
		
