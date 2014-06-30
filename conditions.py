#! /usr/bin/env python

"""
Condition object should match the following rules:
	begins with "condition_"
	have one item as input
	return True or False

"""

class Condition:
	def __init__(self, parent=None):
		self.__parent__ = parent

class Condition_default(Condition):
	def check(self, input_object):
		return True

class Condition_adult_family_member(Condition):
	def check(self, input_object):
		if self.
		family = self.__parent__.family

['or',
	 [
		 ['=', ['self', 'former_holder', 'family'], ['obj', 'family']]
	 ],
	 [
		 ['<', ['self', 'former_holder', 'culture', 'customs', 'maturity_age'], ['obj', 'age']]
	 ]
 ]

