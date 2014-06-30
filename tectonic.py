#! /usr/bin/env python
"""
Created on Thu Aug 30 14:30:34 2012

@author: keder
"""
from random import *
from math import *

figures_list = []

min_neighbours = 4
max_neighbours = 8
max_distance = 60
min_distance = 20


class Point:
	x = 0
	y = 0


def to_polar(point, center=[]):
	if center and type(center) == type([]):
		x0 = center[0]
		y0 = center[1]
	elif center and isinstance(center, Point):
		x0 = center.x
		y0 = center.y
	else:
		x0 = 0
		y0 = 0
	if type(center) == type([]):
		x = point[0]
		y = point[1]
	elif isinstance(point, Point):
		x = point.x
		y = point.y
	r = sqrt((x-x0)**2 + (y-y0)**2)
	if ((x-x0) > 0) and ((y-y0) >= 0):
		phi = atan((y-y0)/(x-x0))
	elif ((x-x0) > 0) and ((y-y0) < 0):
		phi = atan((y-y0)/(x-x0)) + 2*pi
	elif (x-x0) < 0:
		phi = atan((y-y0)/(x-x0)) + pi
	elif ((x-x0) == 0) and ((y-y0) > 0):
		phi = pi/2
	elif ((x-x0) == 0) and ((y-y0) < 0):
		phi = 3*pi/2
	else:
		phi = 0
	return r, phi


class Figure:
	border = []
	points = []
	neighbours = []
	center = Point()

	def create_neighbours(self):
		initial_points_num = len(self.points)
		points_num = randrange(max(2 * min_neighbours, initial_points_num), 2 * max_neighbours)
		if self.points:
			phi_remains = pi - abs(self.points[-1]['phi'] - self.points[0]['phi'])
			phi = self.points[-1]['phi'] + phi_remains/(points_num - initial_points_num) * (1/2 + random())
			is_center = not self.points[-1]['is_center']
		else:
			phi_remains = pi
			phi = pi/points_num*(1/2 + random())  # +- half of average angle
			is_center = False
		phi_remains -= phi

		for i in range(initial_points_num, points_num):
			point = {'phi': False, 'r': False, 'x': False, 'y': False, 'obj': False, 'is_center': False}
			point['phi'] = phi
			point['is_center'] = is_center
			is_center = not is_center
			if points_num - (i + 1):
				phi += phi_remains/(points_num - i) * (1/2 + random())
				phi_remains -= phi
			self.points.append(point)
		for point in self.points:
			if point['is_center'] and not point['r']:
				point['r'] = min_distance + (max_distance - min_distance)*random()
		for point in self.points:
			if not point['is_center'] and not point['r']:
				i = self.points.index(point)
				prev_index = i-1
				if i+1 >= points_num:
					next_index = 0
				else:
					next_index = i+1
				min_real_distance = min(self.points[prev_index]['r'], self.points[next_index]['r'])
				point['r'] = min_real_distance/4 + min_real_distance/2 * random()
		for point in self.points:
			flag = False
			if point['x'] is False:
				x = round(point['r'] * cos(point['phi']))
				flag = True
			if point['y'] is False:
				y = round(point['r'] * sin(point['phi']))
				flag = True
			if flag:
				r, phi = to_polar([x, y], self.center)
				point['x'] = x
				point['y'] = y
				point['r'] = r
				point['phi'] = phi










