#! /usr/bin/env python
"""
Created on Thu Aug 30 14:30:34 2012

@author: keder
"""
from copy import copy


class EmptyClass:
	pass

nothing = EmptyClass()

class Federation:
	def setCapital(self, settlement):
		self.capital = settlement
	def setGovernment(self, authority):
		self.authority = authority

class State:
	provinces = []
	def addProvince(self, province):
		self.provinces.append(province)
	def setCapital(self, settlement):
		self.capital = settlement
	def setGovernment(self, authority):
		self.authority = authority

class Province:
	territory = []
	def setState(self, state):
		self.state = state
	def setCapital(self, settlement):
		self.capital = settlement
	def setGovernment(self, authority):
		self.authority = authority

class Activity:
	def __init__(self, activity_type, source):
		self.task_list = []
		self.activity_type = activity_type
		self.source = source
		
	def addTask(self, task_type):
		task = Task(task_type)
		self.task_list.append(task)

class Task:
	def __init__(self, task_type):
		self.task_type = task_type
		self.work_scope_required = work_scope_required
		self.work_scope = 0
		self.materials_required = materials_required
		self.equipment_required = equipment_required
		self.output = output
		self.optional_materials_required = optional_materials_required
		self.optional_equipment_required = optional_equipment_required
		self.materials = []
		self.equipment = []
		self.stage = 0
		#self.optional_materials = []
		#self.optional_equipment = []
	
	def addMaterials(self, materials):
		residue_items = []
		for item in materials:
			if item.name in self.materials_required.keys():
				if item.quality_multiplier:
					if item.quality * item.quantity > self.materials_required[item.name]:
						residue_item = copy(item)
						residue_item.quantity = item.quantity - self.materials_required[item.name] / item.quality
						residue_items.append(residue_item)
						item.quantity = self.materials_required[item.name] / item.quality
				else:
					if item.quantity > self.materials_required[item.name]:
						residue_item = copy(item)
						residue_item.quantity = item.quantity - self.materials_required[item.name]
						residue_items.append(residue_item)
						item.quantity = self.materials_required[item.name]
				self.materials.append(item)
		return residue_items

	def addEquipment(self, equipment):
		residue_items = []
		for item in equipment:
			if item.name in self.equipment_required.keys():
				if item.quality_multiplier:
					if item.quality * item.quantity > self.equipment_required[item.name]:
						residue_item = copy(item)
						residue_item.quantity = item.quantity - self.equipment_required[item.name] / item.quality
						residue_items.append(residue_item)
						item.quantity = self.equipment_required[item.name] / item.quality
				else:
					if item.quantity > self.equipment_required[item.name]:
						residue_item = copy(item)
						residue_item.quantity = item.quantity - self.equipment_required[item.name]
						residue_items.append(residue_item)
						item.quantity = self.equipment_required[item.name]
				self.materials.append(item)
		return residue_items

	def checkMaterials(self):
		materials_required = {}
		aviable_materials = {}
		for item in self.materials:
			if item.quality_multiplier:
				if item.name in aviable_materials.keys():
					aviable_materials[item.name] += item.quality * item.quantity
				else:
					aviable_materials.update({item.name:(item.quality * item.quantity)})
			else:
				if item.name in aviable_materials.keys():
					aviable_materials[item.name] += item.quantity
				else:
					aviable_materials.update({item.name:item.quantity})
		for key in self.materials_required.keys():
			if key in aviable_materials.keys():
				if aviable_materials[key] < self.materials_required[key]:
					materials_required.update({key:(self.materials_required[key] - aviable_materials[key])})
			else:
				materials_required.update({key:self.materials_required[key]})
		return materials_required

	def checkEquipment(self):
		equipment_required = {}
		aviable_equipment = {}
		for item in self.equipment:
			if item.quality_multiplier:
				if item.name in aviable_equipment.keys():
					aviable_equipment[item.name] += item.quality * item.quantity
				else:
					aviable_equipment.update({item.name:(item.quality * item.quantity)})
			else:
				if item.name in aviable_equipment.keys():
					aviable_equipment[item.name] += item.quantity
				else:
					aviable_equipment.update({item.name:item.quantity})
		for key in self.equipment_required.keys():
			if key in aviable_equipment.keys():
				if aviable_equipment[key] < self.equipment_required[key]:
					equipment_required.update({key:(self.equipment_required[key] - aviable_equipment[key])})
			else:
				equipment_required.update({key:self.equipment_required[key]})
		return equipment_required
		
	def begin(self):
		if self.checkMaterials or self.checkEquipment:
			return 0
		else:
			self.stage = 1
			return 1
	
	def residualWorkScope(self):
		return self.work_scope_required - self.work_scope
			
	def do(self, workers, time):
		if self.stage == 1:
			self.work_scope += len(workers) * time
			if self.work_scope >= self.work_scope_required:
				self.stage = 2
		return self.stage
		
	def getOutput(self):
		output = []
		if self.stage == 2:
			output = self.output + self.equipment
		return output
		
	def isDone(self):
		if self.stage == 2:
			return 1
		else:
			return 0
		
		




class ConstructionYard:
	def __init__(self, building, work_scope):
		pass

class Building:
	#tile
	def __init__(self, settlement, owner, tiles):
		self.settlement = settlement
		settlement.buildings.append(self)
		self.owner = owner
		self.tiles = []
		self.tiles += tiles
		self.construction_yard = ConstructionYard()
		
	def found(self, settlement, tiles):
		self.settlement = settlement
		self.tiles = tiles
		self.completed = 0

class ApartmentHouse(Building):
	def __init__(self, settlement, owner, tiles, floors):
		self.settlement = settlement
		settlement.buildings.append(self)
		self.owner = owner
		self.tiles = []
		self.tiles += tiles
		#self.floors = floors
		#self.capacity += len(tiles) * floors * 4
		self.apartments = []


	def setApartments(self, size):
		apartment = Apartment(self, size)
		self.apartments.append(apartment)

	def setWorkshop(self,size):
		workshop = Workshop(self, size)
		self.apartments.append(workshop)



class Square(Building):
	pass

class PrivateHouse(Building):
	def __init__(self, settlement, owner, size, tiles):
		self.settlement = settlement
		settlement.buildings.append(self)
		self.owner = owner
		self.tiles = []
		self.tiles += tiles

class StockBuilding(Building):
	pass

class OfficeBuilding(Building):
	pass

class Apartment:
	def __init__(self, building, size):
		self.building = building
		self.size = size
		self.storage = Storage(self, 1)

	def setHousehold(self, household):
		self.household = household

class Workshop:
	def __init__(self, building, size):
		self.building = building
		self.size = size
		self.tasks = []
		self.workers = []
		self.storage = Storage(self, size / 2)
	def setProduction(self, production):
		self.production = production

class Storage:
	def __init__(self, location, capacity):
		self.capacity = capacity
		self.occupied_capacity = 0
		self.location = location
		self.items = []

	def findInStore(self, item_name, quantity, qualityMultiplier = 0):
		aviableQuantity = 0
		for item in self.items:
			if item.name == item_name:
				if qualityMultiplier:
					aviableQuantity += item.quality*item.quantity
				else:
					aviableQuantity += item.quantity
		return aviableQuantity

	def putInStore(self, items):
		residues = []
		for item in items:
			if self.occupied_capacity < self.capacity:
				if item.quantity + self.occupied_capacity > self.aviable_capacity:
					residue = copy(item)
					residue.quantity = item.quantity - (self.capacity - self.occupied_capacity)
					residues.append(residue)
					item.quantity = self.capacity - self.occupied_capacity
				self.occupied_capacity += item.quantity
				self.items.append(item)
			else:
				residues.append(item)
		return residues

	def recalculateOccupation(self):
		self.occupied_capacity = 0
		for item in self.items:
			self.occupied_capacity += item.quantity

	def takeFromStore(self, item_name, quantity, qualityMultiplier = 0):
		estimatedQuantity = copy(quantity)
		items = []
		for item in self.items:
			if item.name == item_name:
				if qualityMultiplier:
					if estimatedQuantity < item.quantity * item.quality:
						item.quantity -= estimatedQuantity/float(item.quality)
						selected_item = copy(item)
						selected_item.quantity = estimatedQuantity
						items.append(selected_item)
						break
					else:
						estimatedQuantity -= item.quantity * item.quality
						items.append(item)
						self.items.remove(item)
						if estimatedQuantity < 0.1:
							break
				else:
					if estimatedQuantity < item.quantity:
						item.quantity -= estimatedQuantity
						selected_item = copy(item)
						selected_item.quantity = estimatedQuantity
						items.append(selected_item)
						break
					else:
						estimatedQuantity -= item.quantity
						items.append(item)
						self.stock.remove(item)
						if estimatedQuantity < 0.1:
							break
		return items


class TempleBuilding(Building):
	pass

class Monument(Building):
	pass

class Infrastructure(Building):
	pass

class StreetInfrastructure(Infrastructure):
	pass

class PlumbingInfrastructure(Infrastructure):
	pass

class SewageInfrastructure(Infrastructure):
	pass

class Baths(Building):
	pass

class Dungeon(Building):
	pass

class Fortification(Building):
	pass

class Moat(Fortification):
	pass

class Mound(Fortification):
	pass

class Wall(Fortification):
	pass

class ResourceGathering(Building):
	pass

class Mine(ResourceGathering):
	pass

class Quarry(ResourceGathering):
	pass

class Field(ResourceGathering):
	pass

class Settlement:
	
	def __init__(self, name, population, settlement_center):
		self.name = name
		self.population = population
		#self.settlement_center = settlement_center
		self.authority = None
		
	
	def setAuthority(self, authority):
		self.authority = authority
		
	def setState(self, state):
		self.state = state
		
	def build(self,building):
		self.buildings.append(building)
		building.settlement = self


class Town(Settlement):
	pops = []
	villages = []
	def setCity(self, city):
		self.city = city
	def addVillage(self, settlement):
		self.villages.append(settlement)
		settlement.setTown(self)
	def becomeCity(self):
		city = City()
		city.name = self.name
		city.territory = self.territory
		city.buildings = self.buildings
		city.villages = self.villages
		city.state = self.state
		city.authority = self.authority
		city.city = nothing
		city.pops = self.pops
		return city

class District(Settlement):
	def __init__(self, name, city):
		self.name = name
		self.city = city
		self.authority = city.authority
		self.pops = []
		self.territory = []
		self.buildings = []
	def addPop(self, pop):
		self.pops.append(pop)

class City(Town):
	towns = []
	districts = []
	def setCenterOfTrade(self, settlement):
		self.centerOfTrade = settlement
	def addTown(self, settlement):
		self.towns.append(settlement)
		settlement.setCity(self)


class Village(Settlement):
	town = Settlement()
	def __init__(self, pop, name, authority, tile):
		self.pop = pop
		self.name = name
		self.authority = authority
		centerOfVillage = Square(self, self.authority, tile)
		self.buildings.append(centerOfVillage)
		self.territory.append(tile)
	def set_town(self, settlement):
		if hasattr(self, 'town'):
			self.town.villages.remove(self)
		self.town = settlement
		settlement.villages.append(self)
	def becomeTown(self):
		town = Town()
		town.name = self.name
		town.territory = self.territory
		town.buildings = self.buildings
		town.state = self.state
		town.authority = self.authority
		town.pops.append(self.pop)
		return town

print 2+4
