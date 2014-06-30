#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 19:01:14 2012

@author: keder
"""

from pylab import *
from scipy import *
from mpl_toolkits.mplot3d import *

from random import *
from copy import *
from math import *
from PyQt4.QtGui import *
import sys
import json

#Files io
def load_map(path):
	def_file = open(path,'r')
	defenitions = json.loads(def_file.read())
	biomes_map_file = Image.open(path+defenitions['biomes_map_path'],'r')
	json_file = open('/home/keder/map.json','r')
	template = json.loads(json_file.read())
	raw_biomes_map = biomes_map_file.load()
	biomes_map = [[raw_biomes_map[i,j] for i in range(1000)] for j in range(1000)]
	world_map = [[Tile(i,j) for i in range(1000)] for j in range(1000)]
	for i in range(len(biomes_map)):
		for j in range(len(biomes_map[i])):
			for biome in template['biome_template']:
			#print pixels[i]
				if list(biomes_map[i][j]) == biome['color']:
					world_map[i][j].setBiome(biome['name'])


def select(original_list, first_coordinate, second_coordinate):
	result = []
	if len(first_coordinate) != len(second_coordinate):
		return result
	for i in range(len(first_coordinate)):
		[first_coordinate[i],second_coordinate[i]] = [min(first_coordinate[i],second_coordinate[i]),
			max(first_coordinate[i],second_coordinate[i])]
	for i in range(first_coordinate[0], second_coordinate[0]):
		result.append([])
		for j in range(first_coordinate[1], second_coordinate[1]):
			result[i-first_coordinate[0]].append(original_list[i][j])
	return result


def drawSquare(x,y,pixmap,brushPen):
	brush = brushPen[0]
	pen = brushPen[1]
	m = brushPen[2]
	painter = QPainter()
	painter.begin(pixmap)
	painter.setBrush(brush)
	painter.setPen(pen)
	painter.drawRect(x,y,m-1,m-1)
	painter.end()

def setUI(widget):
	size = 1000
	widget.resize(size, size)
	widget.setWindowTitle("Drawing")
	widget.label = QLabel(widget)
	widget.label.resize(size,size)
	pixmap = QPixmap(size,size)
	pixmap.fill(QColor(0,0,0))
	widget.show()
	return pixmap

def limitedLinearFunction(x, leftLimit, rightLimit):
	if x <= leftLimit:
		return 0
	elif (x > leftLimit) and (x < rightLimit):
		return float(x) / (rightLimit - leftLimit)
	else:
		return 1

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
		if self.points:
			phi_left = 2*pi - (points[-1].get_rad(self.center)-points[-1].get_rad(self.center))
		else:
			phi_left = 2*pi
			initial_rotation = 2*pi*random()
		max_size = 50
		points_number = (max_points - max(min_points, len(self.points))) * random()
		size = max_size/8 + max_size * (7/8) * random()
		r = size/8 + size * (7/8) * random()
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


#class Node:
#	def __init__(self, x, y, parent = self):
#		self.parent = parent
#		self.x = x
#		self.y = y
#
#	def set_sibling(self, sibling):
#		if hasattr(self, "right_sibling"):
#			self.left_sibling = sibling
#		else:
#			self.right_sibling = sibling
#
#	def to_polar(self, point):
#		r = sqrt((self.x-point.x)**2 + (self.y-point.y)**2)
#		phi = arctan((self.y-point.y)/(self.x-point.x))
#		return [r, phi]


def make_ramify_points(sizex, sizey):
	initial_center = Point(int(sizex*random()), int(sizey*random()))
	figures = []
	first_figure = Node(initial_center)
	figures.append(first_figure)




def weightedRandom(array):
	s = sum(array)
	r = s * random()
	s = 0
	l = len(array)
	for i in range(l):
		s += array[i]
		if r < s:
			return i

def gaussProbability(x,mu,sigma):
	if sigma == 0:
		return 0
	else:
		return exp(-float(x-mu)**2/2/sigma**2)/float(sigma*(2*pi)**0.5)

def tPotentialFunction(x):
	if x < 0:
		return 0
	elif x < 1.0/3.0:
		return (1-(x*3-1)**2)**0.5
	elif x < 2.0/3.0:
		return 1
	elif x < 3:
		return 2-(1-(x*3-2)**2)**0.5
	else:
		return 0

def distanceFromLine(x,y,x1,y1,x2,y2):
	if x2 != x1:
		k = float(y2-y1) / float(x2-x1)
		b = float(y1*x2 - y2*x1) / float(x2-x1)
		return round((k*x-y+b)/sqrt(k**2+1)*10000) / 10000.0
	elif y2 == y1:
		return round(abs(y - y1)*10000) / 10000.0
	else:
		return round(abs(x - x1)*10000) / 10000.0

def lineCoefficients(x1,y1,x2,y2):
	if x2 != x1:
		k = float(y2-y1) / float(x2-x1)
		b = float(y1*x2 - y2*x1) / float(x2-x1)
		return [k,b]
	else:
		return "vertical line"


def lineLength(x1,y1,x2,y2):
	return sqrt((x2-x1)**2 + (y2-y1)**2)

#def linearAmplitudeChange(x, a1, a2,size):
##	b = float(a1 + a2) / a1 / 2.0
##	k = float(a1 - a2) / a1 / size
#	b = float(a2) / a1 * 3.0 / 4.0
#	k = (2.0 - 3.0*float(a2)/a1/2) / size
##	print b
##	print x
#	if float(x) / size < 0:
#		return 0
#	elif (float(x) / size >= 0) and (float(x) / size < 0.5):
##		print float(x) * k + b
#		return float(x) * k + b
#	else:
#		return 1

#def thresholdFunction(x)

def setAmplitude(square, amplitude):
	size = len(square[0])
	for i in range(size):
		for j in range(size):
			square[i][j] = (square[i][j]*2 - 1) * amplitude * \
			limitedLinearFunction(i, 0, size/3) * \
			(1 - limitedLinearFunction(i, size*2/3, size)) * \
			limitedLinearFunction(j, 0, size/3) * \
			(1 - limitedLinearFunction(j, size*2/3, size))

def makeSquare(size, amplitude):
	square = perlinNoiseMap(size, 1)
	setAmplutude(square, amplitude)
#	#Set absolute values
#	for i in range(size):
#		for j in range(size):
#			square[i][j] = minimum + 1 * amplitude * linearAmplitudeChange(i, amplitude, leftMaximum - minimum,size) \
#			* linearAmplitudeChange((size - i), amplitude, rightMaximum - minimum,size) \
#			* linearAmplitudeChange(j, amplitude, topMaximum - minimum,size) \
#			* linearAmplitudeChange((size - j), amplitude, bottomMaximum - minimum,size)


	#Make square fade to edges
#	for i in range(size):
#		for j in range(size):
#			square[i][j] *=  limitedLinearFunction(i, 0, size / 3) *\
#			limitedLinearFunction(size - i, 0, size / 3) *\
#			limitedLinearFunction(j, 0, size / 3) *\
#			limitedLinearFunction(size - j, 0, size / 3)

#def placeSquare(squares, heightMap):
#	'''
#	[ ][ ][ ]
#	[ ][x][ ]
#	[ ][ ][ ]
#	'''
#
#	size = len(squares[1][1])
#	for i in range(size/3):
#		for j in range(size/3):

def perlinNoiseMap(originalSize, smoothDepth = 0):
	size = originalSize * 3 / 2
	array = [[copy(0) for i in range(size)] for j in range(size)]
#	scale = [0.5,0.25,0.125,0.0625,0.03125,0.015625,0.015625]
	scale = [1.0/7.0,1.0/7.0,1.0/7.0,1.0/7.0,1.0/7.0,1.0/7.0,1.0/7.0]
#	scale = [1.0/3.0,1.0/6.0,1.0/12.0,1.0/24.0,1.0/48.0,1.0/96.0,1.0/96.0]
	scale = [1.0/4.0,1.0/4.0,1.0/4.0,1.0/8.0,1.0/16.0,1.0/32.0,1.0/32.0]

	#Generate Perlin octaves
	octave1 = perlinOctave(2, size)
	octave2 = perlinOctave(4, size)
	octave3 = perlinOctave(8, size)
	octave4 = perlinOctave(16, size)
	octave5 = perlinOctave(32, size)
	octave6 = perlinOctave(64, size)
	octave7 = [[random() for i in range(size)] for j in range(size)]

	#Sum octaves
	for i in range(size):
		for j in range(size):
			array[i][j] = octave1[i][j] * scale[0] + octave2[i][j] * scale[1] +\
			octave3[i][j] * scale[2] + octave4[i][j] * scale[3] + \
			octave5[i][j] * scale[4] + octave6[i][j] * scale[5] + \
			octave7[i][j] * scale[6]

	#Make values smoother
	for i in range(smoothDepth):
		smoothArray(array,size,5)

	return array

def perlinOctave(generationSteps, originalSize):
	m = originalSize / 128
	generationSteps += 1
	if originalSize % 128 != 0:
		generationSize = (m + 1) * 128 + 1
	else:
		generationSize = m * 128 + 1
	generationStepLength = (generationSize - 1) / (generationSteps - 1) + 1
	maxIndex = generationSize - 1
	maxStepIndex = generationStepLength - 1

	array = [[copy(0) for i in range(generationSize)] for j in range(generationSize)]

	'''Place nodes of random values in corners
	of squares of (generationStepLength)x(generationStepLength) size'''
	for i in range(generationSteps):
		for j in range(generationSteps):
			array[i*maxStepIndex][j*maxStepIndex] = random()

	#Make Perlin noise with interpolation of nodes from previous step
	for i in range(generationSize-1):
		for j in range(generationSize-1):
			'''	This is (generationStepLength)x(generationStepLength)
			interpolation square. Wich is square with nodes of random
			values in corners. a, b, c, d - random values of this nodes

				  x----->
				y a-----b
				| |     |
				| |     |
				V c-----d   '''
			x1 = i / maxStepIndex #Coordinates of square
			y1 = j / maxStepIndex
			a = array[(x1)*maxStepIndex][(y1)*maxStepIndex]
			b = array[(x1+1)*maxStepIndex][(y1)*maxStepIndex]
			c = array[(x1)*maxStepIndex][(y1+1)*maxStepIndex]
			d = array[(x1+1)*maxStepIndex][(y1+1)*maxStepIndex]
			x = i - x1*maxStepIndex #Current point coordinates
			y = j - y1*maxStepIndex #inside the square

			array[i][j] = cosInterpolate(a, b, c, d, x,
				y, maxStepIndex)

	#Cut array to required size
	buf = [[copy(0) for i in range(originalSize)] for j in range(originalSize)]
	for i in range(originalSize):
		for j in range(originalSize):
			buf[i][j] = array[i][j]
	array = buf

	return array

def smoothArray(array, size, parts):

	for i in range(size):
		for j in range(size):
			if i == 0 and j == 0:
				smooth = (1.0 - 1.0 / float(3)) / 2.0
				array[i][j] = array[i][j]/parts + array[i+1][j] * smooth + array[i][j+1] * smooth
			elif i == 0 and j == (size - 1):
				smooth = (1.0 - 1.0 / float(3)) / 2.0
				array[i][j] = array[i][j]/parts + array[i+1][j] * smooth + array[i][j-1] * smooth
			elif i == (size - 1) and j == 0:
				smooth = (1.0 - 1.0 / float(3)) / 2.0
				array[i][j] = array[i][j]/parts + array[i-1][j] * smooth + array[i][j+1] * smooth
			elif i == (size - 1) and j == (size - 1):
				smooth = (1.0 - 1.0 / float(3)) / 2.0
				array[i][j] = array[i][j]/parts + array[i-1][j] * smooth + array[i][j-1] * smooth
			elif i == (size - 1):
				smooth = (1.0 - 1.0 / float(4)) / 3.0
				array[i][j] = array[i][j]/parts + array[i-1][j] * smooth + array[i][j-1] * smooth + array[i][j+1] * smooth
			elif i == 0:
				smooth = (1.0 - 1.0 / float(4)) / 3.0
				array[i][j] = array[i][j]/parts + array[i+1][j] * smooth + array[i][j-1] * smooth + array[i][j+1] * smooth
			elif j == (size - 1):
				smooth = (1.0 - 1.0 / float(4)) / 3.0
				array[i][j] = array[i][j]/parts + array[i-1][j] * smooth + array[i][j-1] * smooth + array[i+1][j] * smooth
			elif j == 0:
				smooth = (1.0 - 1.0 / float(4)) / 3.0
				array[i][j] = array[i][j]/parts + array[i+1][j] * smooth + array[i-1][j] * smooth + array[i][j+1] * smooth
			else:
				smooth = (1.0 - 1.0 / float(parts)) / 4.0
				array[i][j] = array[i][j]/parts + array[i+1][j] * smooth + array[i-1][j] * smooth + array[i][j+1] * smooth + array[i][j-1] * smooth

def cosInterpolate(a, b, c, d, x, y, size):

	'''	  x----->
		y a-----b
		| |     |
		| |     |
		V c-----d   '''

	x1 = x * pi / size / 2
	y1 = y * pi / size / 2
	t1 = sin(x1)**2
	t2 = sin(y1)**2
	return  a * ((1 - t1) * (1 - t2)) + b * (t1 * (1 - t2)) \
	+ c * (t2 * (1 - t1)) + d * (t1 * t2)

def randomWalk(size):
	array = [[copy(0) for i in range(size)] for j in range(size)]
	x = size/2
	y = size/2
	array[x][y] = 1
	for i in range(size):
		h = choice([-1,0,1])
		v = choice([-1,0,1])
		if ((x+h) < 0) or ((x+h) >= size) or \
		((y+v) < 0) or ((y+v) >= size):
			break
		else:
			x += h
			y += v
			array[x][y] = 1
	return array

def pointInflation(size):
	array = [[copy(0) for i in range(size*2+4)] for j in range(size*2+4)]
	candidate = set([])
	emitting = {(size+2, size+2)}
	checked = set([])
	for i in range(size):
		if len(emitting) <> 0:
			while len(emitting) <> 0:
				a = emitting.pop()
				b = [(a[0]-1,a[1]-1),(a[0]-1,a[1]),(a[0],a[1]-1),(a[0]+1,a[1]-1), \
				(a[0]-1,a[1]+1),(a[0]+1,a[1]),(a[0],a[1]+1),(a[0]+1,a[1]+1)]
				for j in b:
					if not((j in emitting) or (j in checked)):
						candidate.add(j)
				checked.add(a)
			while len(candidate) <> 0:
				buf = candidate.pop()
				r = size * random()
				if r < size - i:
					emitting.add(buf)
	while len(checked) <> 0:
		d = checked.pop()
		array[d[0]][d[1]] = 1
	return array

def randomFigure(max_size, central_point, points_number):
	points = []
	phi0 = 2*pi
	initial_rotation = 2*pi*random()
	r = max_size/20 + max_size/2 * random()
	phi = 0
	sum_ = 0
	x = int(r * cos(phi + initial_rotation) + central_point[0])
	y = int(r * sin(phi + initial_rotation) + central_point[1])
	points.append([x,y])
	for i in range(points_number - 1):
		phi = (phi0/2 + 3*phi0/2 * random()) / (points_number-i)
		sum_ += phi
		r = max_size/20 + max_size/2 * random()
		print "point:"
		print phi
		print r
		phi0 -= phi
		x = int(r * cos(sum_ + initial_rotation) + central_point[0])
		y = int(r * sin(sum_ + initial_rotation) + central_point[1])
		points.append([x,y])
	return points

def intersection(point1, point2, point3, point4):
	if (point1[0] == point2[0]) and (point1[1] == point2[1]) or (point3[0] == point4[0]) and (point3[1] == point4[1]):
		return 0
	[k1,b1] = lineCoefficients(point1[0],point1[1],point2[0],point2[1])
	[k2,b2] = lineCoefficients(point3[0],point4[1],point3[0],point4[1])
	x = (b2-b1) / (k1-k2)
	if (x > min(point1[0],point2[0])) and (x < max(point1[0],point2[0])) \
	and (x > min(point3[0],point4[0])) and (x < max(point3[0],point4[0])):
		return 1
	else:
		return 0

def intersectionControl(lines, point1, point2):
	for line in lines:
		for point in range(1, len(line)):
			point3 = line[point-1]
			point4 = line[point]
			if intersection(point1, point2, point3, point4):
				return 1
	return 0


def randomBrokenLine(max_x, max_y):
	max_steps = 20
	max_radius = 50
	min_radius = 4
	branch_prob = 0.1
	lines = []
	line = []
	point_pool = {}
	point = [randrange(0, max_x), randrange(0, max_y)]
	point = [1,1]
	line.append(copy(point))
	lines.append(copy(line))
	line_num = 0
	point_num = 0
	prev_phi = 2*pi*random()
	prev_phi = pi / 4
	while 1:
		line = lines[line_num]
		cur_phi = gauss(prev_phi, pi/4)
		r = min_radius + max_radius * random()
		print cur_phi
		print r
		x = line[point_num][0] + int(r*cos(cur_phi))
		y = line[point_num][1] + int(r*sin(cur_phi))
		point_num += 1
		prev_phi = cur_phi


		if (x<0) or (x>max_x) or (y<0) or (y>max_y):
			#lines.append(copy(line))
			line_num += 1
			point_num = 0
			print line_num
			prev_phi = 2*pi*random()
		else:
			point = [x,y]
			if not intersectionControl(lines, point1, point2):
				point_pool.add((x,y))
				line.append(copy(point))
				rand = random()
				if rand < branch_prob:
					print "branch!"
					print lines
					branch_line = []
					branch_line.append(copy(point))
					lines.append(copy(branch_line))
		if line_num > len(lines)-1:
			break


	return lines



def crawlingPoint(array,x1,y1,x2,y2):
	standartWeight = 1
	weights = [copy(standartWeight)for i in range(8)]
	#array = [[copy(0) for i in range(size)] for j in range(size)]
	points_list = []

	'''
	        X ----->
	      | -1 | 0 | +1
	   -----------------
	Y  -1 | NW | N | NE
	|  -----------------
	|   0 |  W | @ | E
	V  -----------------
	   +1 | SW | S | SE

	@ means you here

	directions = [NW,N,NE,E,SE,S,SW,W]
	'''
	directions = [[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]]
	x = x1
	y = y1
	i = 1
	acceleration = 500
	momentum = 1
	length = lineLength(x1,y1,x2,y2)
	xsign = cmp(x1, x2)
	ysign = cmp(y1, y2)
#	print "l:" + str(length)
	while not((x==x2) and (y==y2)):
		weights = [1, 1, 1, 1, 1, 1, 1, 1]
		d = distanceFromLine(x,y,x1,y1,x2,y2)
		xcursign = cmp(x1, x)
		ycursign = cmp(y1, y)
#		print "x1:"+str(x1)+" y1:"+str(y1)+" x2:"+str(x2)+" y2:"+str(y2)+" x:"+str(x)+" y:"+str(y)
#		print ((x-x1)**2+(y-y1)**2-d**2)
		t = sqrt(((x-x1)**2+(y-y1)**2-d**2)/float(length**2))
#		print "x:"+str(x)+" y:"+str(y)+" t:"+str(t)

		if momentum <= 1:
			momentum = random() * (1 + sin(pi*t)) * int(length) / 40
			momentumDirection = randrange(0,7)

		for j in range(8):
			ds = distanceFromLine(x+directions[j][0],y+directions[j][1],x1,y1,x2,y2)
			xcursign = cmp(x1,x+directions[j][0])
			ycursign = cmp(y1,y+directions[j][1])

			ts = sqrt(((x+directions[j][0]-x1)**2+(y+directions[j][1]-y1)**2-ds**2)/length**2)
			dmax = sin(pi*ts)*length/pi
			weights[j] *= gaussProbability(ds,0,dmax/3)

			if not((xsign==xcursign or xsign==0)and(ysign==ycursign or ysign==0)):
				weights[j] *= 0
			if (ts > 1):
				weights[j] *= 0


			if ts < t:
				weights[j] *= 0.60
			elif round(ts*10) == round(t*10):
				weights[j] *= 1.0
			else:
				weights[j] *= 1.40

		weights[momentumDirection] *= 3
		if momentumDirection+1 <= 7:
			weights[momentumDirection+1] *= 2
		else:
			weights[0] *= 2
		weights[momentumDirection-1] *= 2

		#print weights

		momentum -= 1
		d = directions[weightedRandom(weights)]
		x += d[0]
		y += d[1]
		#array[x][y] = 1
		if [x,y] in points_list:
			while points_list.pop() != [x,y]:
				pass
			points_list.append([x,y])
#			print "loop"
		else:
			points_list.append([x,y])
		i += 1
#		print i
		if i > 4000:
			break
	for point in points_list:
		array[point[0]][point[1]] = 1
	return array

def showHeightMap(world,pixmap,minHeight,maxHeight):
	m = 2
	a = 255
	length = maxHeight - minHeight
#	print length
	Brush = [QBrush(QColor(0,0,0)),QPen(QColor(0,0,0)),m]
#	world = [[random() for i in range(128)] for j in range(128)]
	for i in range(len(world)):
		for j in range(len(world)):
			h = float(world[i][j])/length
#			h = world[i][j]
#			print h

#			if h >= 0.5:
#				h = 1
#			else:
#				h = 0

#			if h > 1:
#				h=1
#			elif h < 0:
#				h=0
			Brush = [QBrush(QColor(a*h,a*h,a*h)),QPen(QColor(a*h,a*h,a*h)),m]
			drawSquare(m*i,m*j,pixmap,Brush)
		Brush = [QBrush(QColor(235,0,0)),QPen(QColor(235,0,0)),m]
		drawSquare(m*i,m*len(world),pixmap,Brush)
		drawSquare(50*m,50*m,pixmap,Brush)
		drawSquare(250*m,250*m,pixmap,Brush)

def plotGraf(y, string):
	xlist = [x for x in range(len(y))]
	ylist = y
	plot(xlist, ylist)
	title(string)

application = QApplication(sys.argv)
widget = QWidget()
pixmap = setUI(widget)
zero = [copy(0) for i in range(129)]
maxHeight = 100
size = 300
bigWorld = [[copy(0) for i in range(128*3)] for j in range(128*3)]
#world = perlinNoiseMap(128, 2)
#makeSquare(world, 0, 50)
#grid = [[[] for i in range(3)] for j in range(3)]
#for i in range(3):
#	for j in range(3):
#		if i == 1 and j ==0:
#			height = 100
#		elif i == 0 and j ==0 or i == 2 and j ==0 or i == 1 and j ==1:
#			height = 50
#		elif i == 0 and j ==1 or i == 1 and j ==2 or i == 2 and j ==1:
#			height = 25
#		else:
#			height = 5
#		world = perlinNoiseMap(size, 2)
#		makeSquare(world, 0, height)
#		grid[i][j] = world

'''
self top left bottom right
'''
#a = []
#for i in range(0,100):
#	a.append(24*linearAmplitudeChange(i, 24, 12,100))
#print a

#world = perlinNoiseMap(size, 2)
#makeSquare(world, 0, 30, 30, 30, 20, 40)
#grid[0][0] = world
#world = perlinNoiseMap(size, 2)
#makeSquare(world, 0, 40, 40, 30, 30, 30)
#grid[1][0] = world
#world = perlinNoiseMap(size, 2)
#makeSquare(world, 0, 30, 30, 40, 20, 30)
#grid[2][0] = world
#world = perlinNoiseMap(size, 2)
#makeSquare(world, 0, 20, 30, 20, 10, 30)
#grid[0][1] = world
#world = perlinNoiseMap(size, 2)
#makeSquare(world, 0, 30, 40, 20, 20, 20)
#grid[1][1] = world
#world = perlinNoiseMap(size, 2)
#makeSquare(world, 0, 20, 30, 30, 10, 20)
#grid[2][1] = world
#world = perlinNoiseMap(size, 2)
#makeSquare(world, 0, 10, 20, 10, 10, 20)
#grid[0][2] = world
#world = perlinNoiseMap(size, 2)
#makeSquare(world, 0, 20, 30, 10, 10, 10)
#grid[1][2] = world
#world = perlinNoiseMap(size, 2)
#makeSquare(world, 0, 10, 20, 20, 10, 10)
#grid[2][2] = world
r = randrange(3,15)
#figure = randomFigure(200, [150,150], 10)
#print figure
heightMap = [[copy(0) for i in range(size)] for i in range(size)]
#prev_point = figure[-1]
#heightMap[150][150] = 10
lines = randomBrokenLine(size, size)
print lines
prev_point = lines[0][0]
for line in lines:
	prev_point = line[0]
	for point in line:
	#	print point[0]
		heightMap = crawlingPoint(heightMap, prev_point[0],prev_point[1],point[0],point[1])
		prev_point = copy(point)
		heightMap[point[0]][point[1]] = 10
#for point in figure:
#
#	heightMap = crawlingPoint(heightMap, prev_point[0],prev_point[1],point[0],point[1])
#	prev_point = copy(point)
#	heightMap[point[0]][point[1]] = 10
#heightMap = crawlingPoint(heightMap, 50,50,150,50)
#for row in range(3):
#	for column in range(3):
#		x0 = row * size - size / 4
#		y0 = column * size - size / 4
#		for i in range(size * 3 / 2):
#			for j in range(size * 3 / 2):
#				x = x0 + i
#				y = y0 + j
##				print grid[row][column]
#
#				if (x >= 0) and (y >= 0) and (x <= (size*3 - 1)) and (y <= (size*3 - 1)):
#
#					heightMap[x][y] += grid[row][column][i][j]
#					if i == 75 and j == 75:
#						print str(row) + " "+str(column)+" "+str(heightMap[x][y])
#					print str(row) + " "+str(column)+" "+str(grid[row][column][i][j])
#summ = 0
#for i in world:
#	summ += sum(i)
#print summ/128**2
#mini = world[0][0]
#for i in world:
#	buf = min(i)
#	mini = min(buf, mini)
#print mini
#dist = [copy(0) for i in range(100)]
#for i in range(len(world)):
#	for j in range(len(world)):
#		n = int(world[i][j] * 100)
#		dist[n] += 1
#print dist
#plotGraf(dist,"")
#show()

path = "/home/keder/test/table.csv"
f = open(path,'w')
#for i in range(len(heightMap)):
#
#	for j in range(len(heightMap)):
#		if j == len(heightMap)-1:
#			f.write(str(heightMap[i][j]))
#		else:
#
#			f.write(str(heightMap[i][j])+";")
#	if i != len(heightMap)-1:
#		f.write("\n")

#showHeightMap(grid[2][0],pixmap,0,100)
showHeightMap(heightMap,pixmap,0,10)
#showHeightMap(heightMap,pixmap,0,50)
widget.label.setPixmap(pixmap)
widget.update()
sys.exit(application.exec_())
