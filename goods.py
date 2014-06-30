#! /usr/bin/env python
"""
Created on Thu Aug 23 13:07:05 2012

@author: keder
"""
from copy import copy

import core



class Item:
	def __init__(self, name, quality, quantity, weight_multiplier, base_cost):
		self.name = name
		self.quality = quality
		self.quantity = quantity
		self.weight = self.quantity * core.commonLists.items[self.name]["weight_multiplier"]
		self.base_cost = base_cost
	
	def select(self, quantity):
		new_item = copy(self)
		new_item.quantity = quantity
		self.quantity -= quantity
		self.recalculateWeight()
		return new_item
		
	def recalculateWeight(self):
		self.weight = self.quantity * self.weight_multiplier
		
		

#FOOD
class Food(Product):
	productType = "food"
	
#Cereals
class Cereal(Food):
	category = "cereal"
	
class Wheat(Cereal):
	name = "wheat"
	
class Rice(Cereal):
	name = "rice"
	
class Oat(Cereal):
	name = "oat"
	quality = 1.1
	
class Buckwheat(Cereal):
	name = "buckwheat"
	
class Corn(Cereal):
	name = "corn"
	
class Millet(Cereal):
	name = "millet"
	
class Soybean(Cereal):
	name = "soybean"
	quality = 1.5
	
class Beans(Cereal):
	name = "beans"
	quality = 0.2
	
class Barley(Cereal):
	name = "barley"
	
class Rye(Cereal):
	name = "rye"
	
class Sorghum(Cereal):
	name = "sorghum"
	
class Lens(Cereal):
	name = "lens"
	quality = 0.3

class Bread(Food):
	category = "bread"
	
class WheatBread(Bread):
	name = "wheat_bread"
	
class RyeBread(Bread):
	name = "rye_bread"	
	
#Meat	
class Meat(Food):
	category = "meat"

class Beef(Meat):
	name = "beef"
	
class Pork(Meat):
	name = "pork"
	
class Mutton(Meat):
	name = "mutton"

class Horseflesh(Meat):
	name = "horseflesh"
	
class Chicken(Meat):
	name = "chicken"

class Goose(Meat):
	name = "goose"

class Duck(Meat):
	name = "duck"

class Rabbit(Meat):
	name = "rabbit"	
	
class Wildfowl(Meat):
	name = "wildfowl"	

#Fruit	
class Fruit(Food):
	category = "fruit"
	
class Vegetables(Food):
	category = "vegetables"
	
class Dairy(Food):
	category = "dairy"

class Cheese(Dairy):
	name = "cheese"
	
class Milk(Dairy):
	name = "milk"
	
class Butter(Dairy):
	name = "butter"
	
class Eggs(Food):
	category = "eggs"
	
class Spice(Food):
	category = "spice"
	
class Salt(Spice):
	name = "salt"
	
class Fish(Food):
	category = "fish"
	
class Sugar(Food):
	category = "sugar"
	
class Confection(Food):
	category = "confection"
	
class Cake(Food): #is a lie
	name = "cake"
	
class Honey(Food):
	name = "honey"
	
class Chocolate(Food):
	name = "chocolate"
	
	
#Domestic
class Domestic(Product):
	productType = "domestic"
	
class Furniture(Domestic):
	category = "furniture"
	
class Dishes(Domestic):
	category = "dishes"

class HomeTools(Domestic):
	category = "home_tools"
	

#Clothes
class Outfit(Product):
	productType = "outfit"
	
class Clothing(Outfit):
	category = "clothing"
	
class CheapClothing(Clothing):
	name = "cheap_clothing"
	
class CommonClothing(Clothing):
	name = "common_clothing"
	
class LuxuriousClothing(Clothing):
	name = "luxurious_clothing"
	
class Footwear(Outfit):
	category = "footwear"
	
class CheapFootwear(Footwear):
	name = "cheap_clothing"
	
class CommonFootwear(Footwear):
	name = "common_clothing"
	
class LuxuriousFootwear(Footwear):
	name = "luxurious_clothing"
	
class Jewellery(Outfit):
	category = "jewellery"
	
class PreciousJewellery(Jewellery):
	name = "precious_jewellery"
	
class CommonJewellery(Jewellery):
	name = "common_jewellery"
	
class Cloth(Outfit):
	category = "cloth"
	
class CottonCloth(Cloth):
	name = "cotton_cloth"
	
class SilkCloth(Cloth):
	name = "silk_cloth"
	
class FlaxCloth(Cloth):
	name = "flax_cloth"
	
class WoolCloth(Cloth):
	name = "wool_cloth"
	
class HempCloth(Cloth):
	name = "hemp_cloth"
	
	


class Mineral(Product):
	productType = "mineral"
	
class Stone(Mineral):
	category = "stone"
	
class Granite(Stone):
	name = "garnite"
	
class Marble(Stone):
	name = "marble"
	
class Sandstone(Stone):
	name = "sandstone"
	
class Lemonstone(Stone):
	name = "lemonstone"
	
class Slate(Stone):
	name = "slate"
	
class NonOre(Mineral):
	category = "nonore"
	
class Clay(NonOre):
	name = "clay"
	
class Sand(NonOre):
	name = "sand"
	
class QuartzSand(NonOre):
	name = "quartz_sand"
	
class Bauxite(NonOre):
	name = "bauxite"
	
class Ore(Mineral):
	category = "ore"
	
class IronOre(Ore):
	name = "iron_ore"
	
class GoldOre(Ore):
	name = "gold_ore"
	
class CopperOre(Ore):
	name = "copper_ore"
	
class TinOre(Ore):
	name = "tin_ore"
	
class SilverOre(Ore):
	name = "silver_ore"
	
class LeadOre(Ore):
	name = "lead_ore"
	
class ZinkOre(Ore):
	name = "zink_ore"
	
class Nugget(Mineral):
	category = "nugget"
	
class IronNugget(Nugget):
	name = "iron_ore"
	
class GoldNugget(Nugget):
	name = "gold_ore"
	
class CopperNugget(Nugget):
	name = "copper_ore"
	
class TinNugget(Nugget):
	name = "tin_ore"
	
class SilverNugget(Nugget):
	name = "silver_ore"
	
class LeadNugget(Nugget):
	name = "lead_ore"
	
class ZinkNugget(Nugget):
	name = "zink_ore"
	
class Gems(Mineral):
	category = "gems"
	
class Liquid(Mineral):
	category = "liquid"
	
	

class Metal(Product):
	productType = "Metal"
	
class PureMetal(Metal):
	category = "pure_metals"
	
class Iron(PureMetal):
	name = "iron"
	
class Gold(PureMetal):
	name = "gold" 	
	
class Copper(PureMetal):
	name = "copper"
	
class Tin(PureMetal):
	name = "tin"
	
class Silver(PureMetal):
	name = "silver"
	
class Lead(PureMetal):
	name = "lead"
	
class Zink(PureMetal):
	name = "zink"
	
class Alloy(Metal):
	category = "alloys"
	
class Steel(Alloy):
	name = "steel"
	
class CastIron(Alloy):
	name = "cast_iron"	
	
class Bronze(Alloy):
	name = "bronze"	
	
class Brass(Alloy):
	name = "brass"
	
	
	
class Tool(Product):
	productType = "tool"
	
class FarmingTool(Tool):
	category = "farming_tool"
	
class Plow(FarmingTool):
	name = "plow"
	
class Hoe(FarmingTool):
	name = "hoe"
	
class Pitchfork(FarmingTool):
	name = "pitchfork"

class Sickle(FarmingTool):
	name = "sickle"
	
class Rake(FarmingTool):
	name = "rake"

class BuildingTool(Tool):
	category = "building_tool"
	
class WoodworkingTool(Tool):
	category = "woodworking_tool"
	
class StoneworkingTool(Tool):
	category = "stoneworking_tool"
	
	
	
class Weapon(Product):
	productType = "weapon"
	
class MeleeWeapon(Weapon):
	category = "melee_weapon"
	
class ProjectileWeapon(Weapon):
	category = "projectile_weapon"
	
class Firearm(Weapon):
	category = "firearm"
	
class Explosive(Weapon):
	category = "explosive"



class Leather():
	name = "leather"
	







	
	