# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 21:03:32 2013

@author: keder
"""

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def get_rad(self, point):
		self.r = sqrt((self.x-point.x)**2 + (self.y-point.y)**2)
		self.phi = arctan((self.y-point.y)/(self.x-point.x))
		return [r, phi]

class Figure:
	def __init__(self, point, parent = 0):
		self.center = point
		self.points = []
		self.neighbours = []
		self.sectors = []
		self.parent = parent

	def make_points(self):
		if len(self.neighbours) == 1:
			pass
		elif len(self.neighbours) == 2:

		elif len(self.neighbours) == 3:
			phi0 = points[0].get_rad(self.center)
			phi2 = points[2].get_rad(self.center)
			if phi2>phi0:
				phi_sum = phi2-phi0
			else:
				phi_sum = phi2+2*pi-phi0
		else:
			phi_left = 2*pi
			initial_rotation = 2*pi*random()
		#max_size = 50
		points_number = (max_points - max(4, len(self.points))) * random()
		#size = max_size/8 + max_size * (7/8) * random()
		#r = size/8 + size * (7/8) * random()
		phi = 0
		phi_sum = 0
		self.sectors[0] = initial_rotation
#		x = int(r * cos(phi + initial_rotation) + central_point[0])
#		y = int(r * sin(phi + initial_rotation) + central_point[1])
#		self.neighbours.append([x,y])
		for i in range(len(self.points), points_number - 1):
			phi = (phi0/2 + 3*phi0/2 * random()) / (points_number-i)
			phi_sum += phi
			r = max_size/20 + max_size/2 * random()
#			print "point:"
#			print phi
#			print r
			phi_left -= phi
			x = int(r * cos(phi_sum + initial_rotation) + central_point[0])
			y = int(r * sin(phi_sum + initial_rotation) + central_point[1])
			self.neighbours.append([x,y])