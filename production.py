#! /usr/bin/env python
"""
Created on Wed Sep  5 10:17:01 2012

@author: keder
"""
from goods import *

class Production:
	inputs = []
	optionalInputs = [] # [[product1, multiplier1], [product2, multiplier2]]
	outputs = []
	instruments = []
	baseWorkScope = 1.0
	
class Bakery(Production):
	inputs = ["wheat", "rye"]
	optionalInputs = [[salt, 2], [yeast, 2]]
	outputs = ["wheat_bread", "rye_bread"]