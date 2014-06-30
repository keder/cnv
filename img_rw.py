# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 09:58:52 2013

@author: keder
"""

import Image, json

class Tile:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.child_map = []

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

	def setHeight(self, height):
		self.height = height

	def setType(self, tile_type):
		self.tile_type = tile_type

	def setVegetation(self, vegetation):
		self.vegetation = vegetation
		
	def setConstruction(self, construction):
		self.construction = construction

img_file = Image.open('/home/keder/map.png','r')
json_file = open('/home/keder/map.json','r')
template = json.loads(json_file.read())
raw_pixels = img_file.load()
pixels = [[raw_pixels[i,j] for i in range(1000)] for j in range(1000)]
world_map = [[Tile(i,j) for i in range(1000)] for j in range(1000)]
for i in range(len(pixels)):
	for j in range(len(pixels[i])):
		for biome in template['biome_template']:
			#print pixels[i]
			if list(pixels[i][j]) == biome['color']:
				world_map[i][j].setBiome(biome['name'])
print world_map[450][450].biome