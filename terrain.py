#! /usr/bin/env python
"""
Created on Sat Sep  1 23:55:00 2012

@author: keder
"""

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

from copy import copy
from random import *
from math import *
from common import *

scale = (1, 10, 1000, 100000, 22500000)
largeTileTypes = ("sea","coast","land")


class EmptyClass:
	pass

#largeTileTypes = EmptyClass()
#largeTileTypes.sea = "sea"
#largeTileTypes.coast = "coast"
#largeTileTypes.land = "land"
#largeTileTypes.mountains = "mountains"
#largeTileTypes.forest = "forest"
#largeTileTypes.jungle = "jungle"
#largeTileTypes.desert = "desert"
#largeTileTypes.tundra = "tundra"
#largeTileTypes.glacier = "glacier"

def kelvinCelsium(temperature):
	return temperature - 273

def kelvinFarenheit(temperature):
	return (temperature - 273) * 9 / 5 + 32

def normalDistribution(x,standartDeviation,expectedValue):
#	print exp(-float(x-expectedValue)**2/(2*standartDeviation**2))/ \
#	(standartDeviation*(2*pi)**0.5)
	return exp(-float(x-expectedValue)**2/(2*standartDeviation**2))/ \
	(standartDeviation*(2*pi)**0.5)
#	return 1

def hyperbolicDistribution(lowerLimit,upperLimit):
	sum_ = 0.0
	for a in range(lowerLimit,upperLimit):
		sum_ += 1 / float(a-0.5)
	r = sum_ * random()
	sum_ = 0.0
	for a in range(lowerLimit,upperLimit):
		sum_ += 1 / float(a-0.5)
		if r < sum_:
			return a

class Time:
	def __init__(self):
		self.day = 0
		self.daysPassed = 0
		self.month = 0
		self.year = 0
		self.seasonsInYear = 4
		self.daysInMonth = (30,31,30,30,31,30,30,31,30,30,31,30)
		self.monthsInYear = 12
		self.daysInYear = 364
	def dayPassed(self):
		self.daysPassed = self.daysPassed + 1
		#dayChanges()
		if (self.day + 1) > self.daysInMonth[self.month]:
			if (self.month + 1) > self.monthsInYear:
				self.year = self.year + 1
				self.month = 0
				#yearChanges()
			else:
				self.month = self.month + 1
				self.day = 0
				#monthChanges()
		else:
			self.day = self.day + 1

class Calendar:
	pass



class World:
	def __init__(self):
		self.vertical_size = 1000
		self.horizontal_size = 1000
		self.scales = 3
		self.maps = [[] for i in range(self.scales)]
		self.maps[0] = [[BaseTile(x,y) for y in range(self.vertical_size)] for x in range(self.horizontal_size)]
		for scale in range(1, self.scales):
			vertical_size = self.vertical_size/(10 ** scale)
			horizontal_size = self.horizontal_size/(10 ** scale)
			self.maps[scale] = [[Tile(x,y) for y in range(vertical_size)] for x in range(horizontal_size)]
			for x in range(horizontal_size):
				for y in range(vertical_size):
					self.maps[scale][x][y].setMap(select(self.maps[scale-1], [x*10, y*10], [(x+1)*10, (y+1)*10]))

class Tile:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.irregular = 0

	def setMap(self, child_map):
		self.map = child_map
		for line in child_map:
			for child in line:
				child.setParent(self)

	def setParent(self, parent):
		self.parent = parent
		
	def setClimate(self, climate):
		self.climate = climate
		
	def setBiome(self, biome):
		self.biome = biome
	
	def set_distance_from_sea(self, distance):
		self.distance_from_sea = distance

class BaseTile(Tile):
	def setHeight(self, height):
		self.height = height

	def setType(self, tile_type):
		self.tile_type = tile_type

	def setVegetation(self, vegetation):
		self.vegetation = vegetation
		
	def setConstruction(self, construction):
		self.construction = construction

weatherConstants = EmptyClass()
#weatherConstants.precipitationType = EmptyClass()
#weatherConstants.precipitationType.lightRain = "light_rain"
#weatherConstants.precipitationType.rain = "rain"
#weatherConstants.precipitationType.heavyRain = "heavy_rain"
#weatherConstants.precipitationType.lightSnow = "light_snow"
#weatherConstants.precipitationType.snow = "snow"
#weatherConstants.precipitationType.heavySnow = "heavy_snow"
#weatherConstants.precipitationType.hail = "hail"
#weatherConstants.cloudiness.overcast = "overcast"
#weatherConstants.cloudiness.partly = "partly"
#weatherConstants.cloudiness.clear = "clear"

weatherConstants.cloudiness = ("clear", "partly", "overcast")

class Weather:
	temperature = 273
	humidity = 10
	windSpeed = 0
	windDirection = 90
	cloudiness = weatherConstants.cloudiness[0]

class Climate:
	averageTemperature = 273
	averageHumidity = 10
	def getWeather(self):
		weather = Weather()
		weather.temperature = self.averageTemperature + 20 * (random() - 0.5)
		weather.humidity = self.averageHumidity + 20 * (random() - 0.5)
		weather.windSpeed = 30 * random()
		weather.windDirection = 359 * random()
		weather.cloudiness = weatherConstants.cloudiness[round(2 * random())]
		return weather

def randomWorldGeneration(world):
	for i in range(world.size):
		for j in range(world.size):
			if randrange(0,9) == 0:
				world.map[i][j].type = largeTileTypes[2]
	fillGaps(world)
	setCoast(world)

def continentWorldGeneration(world):
	for i in range(world.size):
		for j in range(world.size):
			if randrange(0,9) == 0:
				world.map[i][j].type = largeTileTypes[2]
	fillGaps(world)
	setCoast(world)

def fillGaps(world):
	for i in range(world.size):
		for j in range(world.size):
			if world.map[i][j].type == largeTileTypes[0]:
				sum = 0
				if i-1 >= 0:
					if (world.map[i-1][j].type == largeTileTypes[2]):
						sum += 1

				if j-1 >= 0:
					if (world.map[i][j-1].type == largeTileTypes[2]):
						sum += 1

				if i+1 <= world.size-1:
					if (world.map[i+1][j].type == largeTileTypes[2]):
						sum += 1

				if j+1 <= world.size-1:
					if (world.map[i][j+1].type == largeTileTypes[2]):
						sum += 1

				if sum >= 2:
					world.map[i][j].type = largeTileTypes[2]

def setCoast(world):
	for i in range(world.size):
		for j in range(world.size):
			if world.map[i][j].type == largeTileTypes[0]:
				sum = 0
				if i-1 >= 0:
					if (world.map[i-1][j].type == largeTileTypes[2]):
						sum += 1
				if i-1 >= 0 and j-1 >= 0:
					if (world.map[i-1][j-1].type == largeTileTypes[2]):
						sum += 1
				if j-1 >= 0:
					if (world.map[i][j-1].type == largeTileTypes[2]):
						sum += 1
				if i-1 >= 0 and j+1 <= world.size-1:
					if (world.map[i-1][j+1].type == largeTileTypes[2]):
						sum += 1
				if i+1 <= world.size-1:
					if (world.map[i+1][j].type == largeTileTypes[2]):
						sum += 1
				if i+1 <= world.size-1 and j-1 >= 0:
					if (world.map[i+1][j-1].type == largeTileTypes[2]):
						sum += 1
				if j+1 <= world.size-1:
					if (world.map[i][j+1].type == largeTileTypes[2]):
						sum += 1
				if i+1 <= world.size-1 and j+1 <= world.size-1:
					if (world.map[i+1][j+1].type == largeTileTypes[2]):
						sum += 1
				if sum >= 1:
					world.map[i][j].type = largeTileTypes[1]

def generateHeightMap(world, maxHeight, minHeight, step = 1):
	expectedValue = (maxHeight + minHeight) / 2
#	print expectedValue
	standartDeviation = (maxHeight - minHeight) / 6
#	print standartDeviation
	map_ = world.map
	baseHeight = int(gauss(expectedValue,standartDeviation))
#	for j in range(1,world.size):
#		lower = normalDistribution(map_[0][j-1].height - step,standartDeviation,expectedValue)
#		equal = normalDistribution(map_[0][j-1].height,standartDeviation,expectedValue)
#		higher = normalDistribution(map_[0][j-1].height + step,standartDeviation,expectedValue)
#		r = (lower+equal+higher) * random()
#		print str(lower)+","+str(equal)+","+str(higher)+","+ str(lower+equal+higher)
#		print r
#		if r < lower:
#			map_[0][j].height = map_[0][j-1].height - step
#			print "down!"
#		elif r < lower+higher:
#			map_[0][j].height = map_[0][j-1].height + step
#			print "up!"
#		else:
#			map_[0][j].height = map_[0][j-1].height
#			print "no change"
	randomHeightCurve(map_[0], baseHeight, (maxHeight - minHeight) / 2)
	randomHeightCurve(map_[:][0], baseHeight, (maxHeight - minHeight) / 2)
	for i in range(1,world.size):
		for j in range(1,world.size):
			up = map_[i-1][j].height
			left = map_[i][j-1].height
			if up == left:
#				print "equal"
				lower = normalDistribution(up - step,standartDeviation,expectedValue)
				equal = normalDistribution(up,standartDeviation,expectedValue)
				higher = normalDistribution(up + step,standartDeviation,expectedValue)
				r = (lower+equal+higher) * random()
				if r < lower:
					map_[i][j].height = up - step
#					print "down!"
				elif r < lower+higher:
					map_[i][j].height = up + step
#					print "up!"
				else:
					map_[i][j].height = up
#					print "no change"
			elif abs(up-left) == 1:
#				print "one"
				upProbability = normalDistribution(up,standartDeviation,expectedValue)
				leftProbability = normalDistribution(up,standartDeviation,expectedValue)
				r = (upProbability+leftProbability) * random()
				if r < upProbability:
					map_[i][j].height = up
				else:
					map_[i][j].height = left
			elif abs(up-left) == 2:
				map_[i][j].height = (left + up)/2
#				print "two"
			else:
				print "Heights error!"

def randomHorizontalCurve(map_, x, y, length, maxDeviation, value = 1):
	j = y
	r = -1
	for i in range(length):
		if r < 0:
			if j>= y+maxDeviation:
				direction = choice([-1,0])
			elif j<= y-maxDeviation:
				direction = choice([1,0])
			else:
				direction = choice([-1,0,1])
#			print direction
			r = hyperbolicDistribution(1,8)
			if direction == 1:
				r = min(r, length - i, y + maxDeviation - j)
			elif direction == -1:
				r = min(r, length - i, j - y + maxDeviation)
			else:
				r = min(r, length - i)
			print "r:"+str(r)

		print j
		j += direction
		map_[x+i][j].height = value
		r -= 1

def randomHeightCurve(map_, baseHeight, maxDeviation):
	h = baseHeight
	map_[0].height = copy(h)
	r = -1
	for i in range(1,len(map_)):
		if r < 0:
			if h>= baseHeight+maxDeviation:
				direction = choice([-1,0])
			elif h<= baseHeight-maxDeviation:
				direction = choice([1,0])
			else:
				direction = choice([-1,0,1])
#			print direction
			r = hyperbolicDistribution(1,8)
			if direction == 1:
				r = min(r, len(map_) - i, baseHeight + maxDeviation - h)
			elif direction == -1:
				r = min(r, len(map_) - i, h - baseHeight + maxDeviation)
			else:
				r = min(r, len(map_) - i)

		print h
		h += direction
		map_[i].height = copy(h)
		r -= 1



def setUI(widget):
	size = 1000
	widget.resize(size, size)
	widget.setWindowTitle("Drawing")
	widget.label = QLabel(widget)
	widget.label.resize(size,size)
	pixmap = QPixmap(size,size)
	pixmap.fill(Qt.white)
	widget.show()
	return pixmap

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

def showMap(world,pixmap):
	m = 3
	seaBrush = [QBrush(QColor(50,50,210)),QPen(QColor(50,50,210)),m]
	coastBrush = [QBrush(QColor(250,206,141)),QPen(QColor(250,206,141)),m]
	landBrush = [QBrush(QColor(50,210,50)),QPen(QColor(50,210,50)),m]
	for i in range(world.size):
		for j in range(world.size):
			if world.map[i][j].type == largeTileTypes[0]:
				drawSquare(m*i,m*j,pixmap,seaBrush)
			elif world.map[i][j].type == largeTileTypes[1]:
				drawSquare(m*i,m*j,pixmap,coastBrush)
			elif world.map[i][j].type == largeTileTypes[2]:
				drawSquare(m*i,m*j,pixmap,landBrush)

def showHeightMap(world,pixmap,maxHeight,minHeight):
	m = 2
	a = 1
	length = maxHeight - minHeight
	Brush = [QBrush(QColor(0,0,0)),QPen(QColor(0,0,0)),m]
	for i in range(world.size):
		for j in range(world.size):
			h = world.map[i][j].height
#			print world.map[i][j].height
#			if h > 1:
#				h=1
#			elif h < 0:
#				h=0
			Brush = [QBrush(QColor(a*h,a*h,a*h)),QPen(QColor(a*h,a*h,a*h)),m]
			drawSquare(m*i,m*j,pixmap,Brush)

application = QApplication(sys.argv)
widget = QWidget()
pixmap = setUI(widget)
#world = World()
#randomWorldGeneration(world)
#showMap(world,pixmap)
world = EmptyClass()
cl  = EmptyClass()
world.map = []
emptymap = []
world.size = 500
for i in range(world.size):
	world.map.append(copy(emptymap))
	for j in range(world.size):
		world.map[i].append(copy(cl))
		world.map[i][j].height = 0
maxHeight = 50
minHeight = 0
generateHeightMap(world, maxHeight, minHeight)
showHeightMap(world,pixmap,maxHeight,minHeight)
widget.label.setPixmap(pixmap)
widget.update()
sys.exit(application.exec_())













