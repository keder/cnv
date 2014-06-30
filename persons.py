#! /usr/bin/env python
"""
Created on Mon Aug 27 12:17:21 2012

@author: keder
"""
from culture import *
from random import *

#==============================================================================
# def includes(list_, obj):
# 	for i in range(0, len(list_)):
# 		if list_[i] == obj:
# 			return i
# 	else:
# 		return -1
#==============================================================================

girlProbability = 0.49
satietyThresholdList = {'crops':0.4}
healthThresholdConsumablesList = {'proteinic':0.2, 'vegetables':0.2, 'fruits':0.1}
happynessThresholdConsumablesList = {}
healthThresholdUsageList = {'clothes':0.5, 'footwear':0.5}
houseHoldMinimumStaffTheshold = {'dishes':3.0, 'furniture':30.0}

class EmptyClass:
	pass

empty = EmptyClass()

class Family:
	def __init__(self, name, progenitor):
		self.name = name
		self.living_members = []
		self.dead_members = []
		self.addMember(progenitor)

	def addMember(self, person):
		self.living_members.append(person)
		person.family = self

	def deadMember(self, person):
		self.living_members.remove(person)
		self.dead_members.append(person)

	def removeMember(self, person):




class EmptyPerson:
	pass

unknown = EmptyPerson()
nobody = False
dead = EmptyPerson()

class Organization:
	def __init__(self, activity, budget):
		self.activity = activity
		self.activity.organization = self
		self.stock = []
		self.budget = budget

	def addWorker(self, person, position):
		if not hasattr(self, 'workers'):
			self.workers = {}
		if not position in self.workers.keys():
			self.workers.update({position:[]})
		self.workers[position].append(person)
		person.setJob(self)

class Company(Organization):
	def setOwner(self, owner):
		self.owner = owner
		owner.addProperty(self)

class Activity:
	pass

class Agriculture(Activity):
	def addField(self, field):
		if not hasattr(self, 'workers'):
			self.fields = []
		self.fields.append(field)
	def addToHerd(self, animals):
		if type(animals) == type([]):
			self.herd += animals
		else:
			self.herd.append(animals)

	def setYearTasks(self):
		self.year_tasks = {'seed fields':0, 'stock hay':0, 'harvest':0}


class Item:
	def produce(self, name, quantity, quality, production_cost, owner):
		self.name = name
		self.quantity = quantity
		self.quality = quality
		self.real_cost = production_cost

class Trait:
	def __init__(self, name):
		self.name = name

	def setEffects(self):
		pass

class Needs:
	def __init__(self, household):
		self.happiness = 1.0
		self.satiety = 1.0
		self.health = 1.0
		self.household = household

	def fulfillSatiety(self, content):
		items_number = 0
		satiety = 0.0
		for key in satietyThresholdList.keys():
			items_number += 1
			if key in content.keys():
				satiety += content[key]/satietyThresholdList[key]
		self.satiety = satiety/items_number


class Household:
	def __init__(self, money):
		self.money = money
		self.realty = []
		self.stock = []
		self.inUsage = []
		self.people = []
		self.dwelling = empty

	def addToStock(self, item):
		self.stock.append(item)

	def buyGoods(self, item):
		pass

	def addPerson(self, person):
		person.household = self
		self.people.append(person)

	def removePerson(self, person):
		person.household = empty
		self.people.remove(person)

	def gainMoney(self, payer, amount):
		payer.money -= amount
		self.money += amount

	def payMoney(self, recipient, amount):
		recipient.money += amount
		self.money -= amount

	def setDwelling(self, dwelling):
		self.dwelling = dwelling
		dwelling.setHousehold(self)


class CommonPerson(EmptyPerson):
	def __init__(self, age = 0, gender = 1):
		#WIP!!!!
		self.age = age
		self.gender = gender
		self.social_groups = []

	def becomeIndependent(self, money = 0):
		self.household.removePerson(self)
		self.household = Household()
		self.household.addPerson(self)
		self.household.money = money

	def setJob(self, job):
		self.job = job

	def setCulture(self, culture):
		self.culture = culture

	def setReligion(self, religion):
		self.religion = religion

	def setEducation(self, education):
		self.education = education #basic, professional, high

	def setHousehold(self, household):
		household.addPerson(self)

	def learnLanguage(self, language):
		if not hasattr(self, "otherLanguages"):
			self.otherLanguages = []
		self.otherLanguages.append(language)

	def earnMoney(self, money):
		self.household.money += money

	def spend_money(self, money):
		self.household.money -= money

	def is_female(self):
		return self.gender

	def is_child_of(self, person):
		return self in person.children

	def is_parent_of(self, person):
		return person in self.children

	def meets_conditions(self, conditions):
		flag = 1
		for condition in conditions:
			if condition["type"] == "male" and self.gender:
				flag = 0
			if condition["type"] == "female" and not self.gender:
				flag = 0
			if condition["type"] == "child" and not self.is_child_of(condition["scope"]):
				flag = 0

	def inheritAttributes(self, mother, father):
		if (father == dead) or (father == unknown) or mother.matrilinealMarriage == 1 or father.culture.customs.patriarchal == 0:
			primary_parent = mother
			inferior_parent = father
		else:
			primary_parent = father
			inferior_parent = mother

		self.culture = primary_parent.culture
		self.language = primary_parent.language
		self.religion = primary_parent.religion
		"""
		legal_status:
		1 - privileged
		0 - free person
		-1 - limited in rights, serves, prisoners
		-2 - slave
		"""
		self.legal_status = inferior_parent.legal_status
		for social_group in  inferior_parent.social_groups:
			if social_group.inheritance == 1:
				self.social_groups.append(social_group)
			elif (social_group.inheritance == 2) and (social_group in primary_parent.social_groups):
				self.social_groups.append(social_group)
		for social_group in  primary_parent.social_groups:
			if social_group.inheritance == 1:
				self.social_groups.append(social_group)
			elif (social_group.inheritance == 2) and (social_group in inferior_parent.social_groups):
				self.social_groups.append(social_group)

class MaleCommonPerson(CommonPerson):

	def getMarried(self, spouse, matrilineality = 0):
		if (not hasattr(self, "spouse")) or (spouse == nobody):
			self.spouse = spouse
		else:
			if not hasattr(self, "otherSpouses"):
				self.otherSpouses = []
			self.otherSpouses.append(spouse)

		spouse.spouse = self
		self.matrilinealMarriage = matrilineality
		if matrilineality:
			self.household = spouse.household
		else:
			spouse.household = self.household



class FemaleCommonPerson(CommonPerson):

	def concieveChild(self):
		self.pregnant = 1

	def giveBirth(self, father = unknown):
		mother = self

		age = 0

		r = random()
		if r < girlProbability:
			gender = 1
			child = FemaleCommonPerson(age, gender)
		else:
			gender = 0
			child = MaleCommonPerson(age, gender)

		child.needs = Needs()

		child.mother = mother
		child.father = father
		if not hasattr(mother, "children"):
			mother.children = []
		mother.children.append(child)
		mother.pregnant = 0
		if (father!=unknown) and (father!=dead):
			if not hasattr(father, "children"):
				father.children = []
			father.children.append(child)

		child.mixFenotype(mother, father)


		child.residence = mother.residence
		mother.houdehold.addPerson(child)


class Person(EmptyPerson):

	def __init__(self, name, age, gender):
		#WIP!!!!
		self.name = name
		#Gender: 0 - male, 1 - female
		self.gender = gender
		self.dead = 0
		self.age = age
		self.titles = []
		self.traits = []
		self.friends = []
		self.rivals = []
		self.children = []
		self.bastards = []
		self.spouse = nobody
		self.mother = unknown
		self.father = unknown
#		self.health = 10
#		#Primary characteristics
#		self.rational_emotional = 0
#		self.introvert_extrovert = 0
#		self.selfish_altruistic = 0
#		self.persistent_compliant = 0
#		#self.emotion_threshold = 0
#		#self.emotion_intesivity = 0
#		#self.emotion_duration = 0
#		self.steady_abrupt = 0
#		self.passive_active = 0
#		self.incredulous_trustful = 0
#		self.serious_lightminded = 0
#		self.just_arbitrary = 0
#
#		#secondary characteristics
#		self.cruel_mercyful = 0
#		self.loyal_treacherous = 0
#		self.coward_brave = 0
#		self.lazy_diligent = 0
#		self.rough_polite = 0
#		self.agressive_defensive = 0
#		self.humble_conceited = 0
#		self.sly_straight = 0
#		self.grim_merry = 0
#		self.slow_quick = 0
#		self.creativity = 10
#		self.power = 0



	def die(self, cause):
		self.dead = 1
		self.death_cause = cause
		#self.death_time =
		self.family.deadMember(self)
		for title in self.titles:
			title.deadHolder()

	def doDailyRoutine(self):
		self.consume()
		if hasattr(self, job) and self.jod != none:
			self.doJob()
		if self.household.head == self:
			self.buyProducts()
		self.getMood()

	def fellInLove(self, person):
		self.lover = person

	def becomeFriends(self, person):
		self.friends.append(person)
		person.friends.append(self)

	def becomeRivals(self, person):
		self.rivals.append(person)
		person.rivals.append(self)

	def gainTitle(self, title):
		self.titles.append(title)
		if title.holder == nobody:
			title.setHolder(self)
		else:
			title.transfer(self)

	def getPower(self):
		power = 0
		for title in self.titles:
			power += titles.power

	def transferTitle(self, person, title):
		self.titles.remove(title)
		person.gainTitle(title)

	def getAttitude(self,person):
		result = person.power	# + many other stuff
		return result

class MalePerson(Person):

	def getMarried(self, spouse, matrilineality = 0):
		if (not hasattr(self, "spouse")) or (spouse == nobody):
			self.spouse = spouse
		else:
			if not hasattr(self, "otherSpouses"):
				self.otherSpouses = []
			self.otherSpouses.append(spouse)

		spouse.spouse = self
		self.matrilineal_marriage = matrilineality
		if matrilineality:
			self.household = spouse.household
		else:
			spouse.household = self.household

class FemaleCommonPerson(CommonPerson):

	def concieveChild(self):
		self.pregnant = 1

	def giveBirth(self):
		mother = self
		age = 0

		r = random()
		if r < girlProbability:
			gender = 1
			child = FemalePerson(age, gender)
		else:
			gender = 0
			child = MalePerson(age, gender)

		if self.spouse != nobody:
			child.father = self.spouse
		else:
			child.father = unknown

		child.needs = Needs()

		child.mother = mother
		child.father = father
		if not hasattr(mother, "children"):
			mother.children = []
		mother.children.append(child)
		mother.pregnant = 0
		if (father!=unknown):
			if not hasattr(father, "children"):
				father.children = []
			father.children.append(child)

		child.residence = mother.residence
		mother.houdehold.addPerson(child)

#		if mother.fenotype == father.fenotype:
#			fenotype = mother.fenotype
#		else:
#			fenotype = mother.fenotype.mixFenotype(father.fenotype)
#
#		appearance = getAppearance(mother.appearance, father.appearance)
#
#
#		if mother.spouse <> nobody:
#			#if she conceive baby from someone but her spouse
#			realFather = father
#			if not(father in mother.spouse) and scandal:
#				officialFather = father
#				priority = 0
#			else:
#				officialFather = mother.spouse
#		if mother.spouse == nobody:
#			#if she conceive baby while being unmarried
#			priority = 0
#			realFather = father
#			officialFather = father
#
#		if priority:
#			culture = officialFather.culture
#			religion = officialFather.religion
#			family = officialFather.family
#		else:
#			culture = mother.culture
#			religion = mother.religion
#			family = mother.family
#
#		traits = {}
#		for trait in mother.traits:
#			if (trait.inheritable <> 0) and (trait.inheritable > random()):
#				traits.add(trait)
#		for trait in realFather.traits:
#			if (trait.inheritable <> 0) and (trait.inheritable > random()):
#				traits.add(trait)
#
#		name = generateName(mother,officialFather,culture)
#		baby = Person(name, age, mother, officialFather, realFather, family, culture, religion)
#		mother.children.append(baby)
#		if father <> unknown:
#			if not(scandal) or (father == mother.spouse):
#				officialFather.children.append(baby)
#			elif not(scandal) or (father == mother.spouse):
#				officialFather.children.append(baby)
#			else:
#				realFather.bastards.append(baby)


class Attitude():
	def __init__(self, subjectPerson, objectPerson):
		getFear(self, subjectPerson, objectPerson)
		getLiking(self, subjectPerson, objectPerson)
		getRespect(self, subjectPerson, objectPerson)

	def getFear(self, subjectPerson, objectPerson):
		self.fear = 0.0
		if self.fear < 0:
			self.fear = 0.0
		elif self.fear > 100:			self.fear = 100.0


	def getLiking(self, subjectPerson, objectPerson):
		self.liking = 0.0
		if self.liking < -100:
			self.liking = -100.0
		elif self.liking > 100:
			self.liking = 100.0

	def getRespect(self, subjectPerson, objectPerson):
		self.respect = 0.0
		if self.respect < -100:
			self.respect = -100.0
		elif self.respect > 100:
			self.respect = 100.0















