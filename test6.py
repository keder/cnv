from copy import copy
from random import random

def qsort(L):
	print L
	if L: return qsort([x for x in L[1:] if x<L[0]]) + L[0:1] + qsort([x for x in L[1:] if x>=L[0]])
	return []
		
a = [int(10 * random()) for i in range(10)]
a = [9,8,7,6,5,4,3,2,1,0]
a = qsort(a)
print a		
	