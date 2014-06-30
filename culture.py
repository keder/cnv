#! /usr/bin/env python
"""
Spyder Editor

This temporary script file is located here:
/home/keder/.spyder2/.temp.py
"""
class EmptyClass:
	pass



#class LocalCulture:
#	def __init__(self, name):
#		self.name = name
#
#	def set_language(self, language):
#		self.language = language
#
#	def set_religion(self, religion):
#		self.religion = religion
#
#	def set_culture(self, culture):
#		self.culture = culture


class Culture:
	def set_clothes(self, clothes):
		self.clothes = clothes

	def set_customs(self, customs):
		self.customs = customs

	def set_architecture(self, architecture):
		self.architecture = architecture

class Customs:
	def __init__(self):
		self.patriarchal = 1
		self.maturity_age = 16


class Language:
	def __init__(self, name, parent=False, writing_system=False):
		self.name = name
		self.parent = parent
		self.writing_system = writing_system
		self.influences = []

	def degree_of_similarity(self, language):
		if (self.parent == language) or (self == language.parent) or (self == language):
			return 1
		influence = 0
		for item in self.influences:
			if item["language"] == language:
				influence = item["influence"]
		cursor = self
		first_line = []
		second_line = []
		while cursor.parent:
			first_line.append(cursor.parent)
			cursor = cursor.parent
		cursor = language
		while cursor.parent:
			second_line.append(cursor.parent)
			cursor = cursor.parent
		for i in range(len(first_line)):
			for j in range(len(second_line)):
				if first_line[i] == second_line[j]:
					return max(round((i+1)*(1-influence)),round((j+1)*(1-influence)))


class Religion:
	def __init__(self, name, founder=False):
		self.name = name
		self.founder = founder
		self.sacred_figures = [founder]
		self.heresies = []
		self.sacred_scripts = []
		self.gods = []
		self.priesthood = False
		self.sacred_places = []
		self.orders = []

	def split_away(self, name, founder):
		heresy = Religion(name, founder)
		heresy.sacred_figures.append(self.sacred_figures)
		self.heresies.append(heresy)
		heresy.parent = self
		heresy.heresies.append(self)

class SocialGroup:
	def __init__(self, name, primary=False):
		self.name = name
		"""
		Groups with the same extrusion_group replace each other, except empty string extrusion_group - those can stack
		"""
		self.extrusion_group = ''

		"""
		inheritance:
		0 - not inherited
		1 - not strict inheritance - if any of parents in group child inherit one
		2 - strict inheritance - only if both parents in group child inherit one
		"""
		self.inheritance = 1
		"""
		0 - spouse does not get social groups of other spouse
		1 - spouse gets social groups of other spouse only with advance
		"""
		self.spouse_get_into_social_group = 0
		self.related_office = False
		self.lost_with_office = False



#LANGUAGE
writingSystems = EmptyClass()
writingSystems.none = "none"
writingSystems.logograph = "logograph"
writingSystems.hieroglyph = "hieroglyph"
writingSystems.syllabary = "syllabary"
writingSystems.abjad = "abjad"
writingSystems.abugida = "abugida"
writingSystems.alphabet = "alphabet"

fenotype = EmptyClass()
fenotype.northAfrican = "north_african"
fenotype.african = "african"
fenotype.iranian = "iranian"
fenotype.indian = "indian"
fenotype.southAsian = "south_asian"
fenotype.northAsian = "north_asian"
fenotype.altaic = "altaic"
fenotype.american = "american"
fenotype.australian = "australian"
fenotype.northEuropean = "north_european"
fenotype.southEuropean = "south_european"

class WritingSystem:
	group = writingSystems.none
	name = "none"

class Language:
	writingSystem = WritingSystem()

class IndoEuropean(Language):
	family = "indo-european"

class IndoIranian(IndoEuropean):
	subfamily = "indo-iranian"

class GreekArmenian(IndoEuropean):
	subfamily = "greek-armenian"

class BaltoSlavic(IndoEuropean):
	subfamily = "balto-slavic"

class Slavic(BaltoSlavic):
	group = "slavic"

class SouthSlavic(Slavic):
	subgroup = "south_slavic"

class WestSlavic(Slavic):
	subgroup = "west_slavic"

class EastSlavic(Slavic):
	subgroup = "east_slavic"

class Russian(EastSlavic):
	name = "russian"

class Ukrainian(EastSlavic):
	name = "ukrainian"

class Baltic(BaltoSlavic):
	group = "baltic"

class Germanic(IndoEuropean):
	subfamily = 3

class Celtic(IndoEuropean):
	subfamily = 4

class Italic(IndoEuropean):
	subfamily = 5

class Anatolian(IndoEuropean):
	subfamily = 6

class SinoTibetian(Language):
	family = 1

class AfroAsiatic(Language):
	family = 2

class Altaic(Language):
	family = 3

class NiloSaharan(Language):
	family = 4

class NigerCongo(Language):
	family = 5



#RELIGION
class Religion:
	def __init__(self, name, category,)

class NoReligion(Religion):
	pass

noReligion = NoReligion()

class Pantheon:
	name = ""
	mainDiety = ""
	afterworldDiety = ""
	familyDiety = ""
	warDiety = ""
	seaDiety = ""
	tradeDiety = ""


#RELIGION
'''Religion always was comlicated topic to discus. So no insult is imlied.
Everything below is only a subjective opinion'''

class ReligiousStructure:
	hierarchies = []
	def addHierarchy(self, hierarchy):
		self.hierarchies.append(hierarchy)

class Hierarchy():
	name = ""
	#head = Title()

class Pagan(Religion):
	def __init__(self, name, subcategory)
	category = "pagan"
	priest = "shaman"
	temple = 0

class Polytheism(Pagan):
	pantheon = Pantheon()
	priest = "priest"
	temple = 1

class NonPagan(Religion):
	name = ""
	holyScripts = ""
	founder = "" #should be link to person here
	religionGlobalBranch = ""
	def setParentReligion(self, religion):
		self.holyScripts = religion.holyScripts
		self.founder = religion.founder
		self.parentRelgion = religion
	religiousStructure = ReligiousStructure()

class Monotheism(NonPagan):
	pass

class Judaism(Monotheism):
	name = "judaism"
	holyScripts = "torah"
	#founder = Moses
	#holyCity = Jerusalem
	godName = "God"
	#religiousBuildings = [synagogue, theTemple]

judaism = Judaism()

class Christianity(Monotheism):
	name = "christianity"
	holyScripts = "bible"
	#founder = JesusChrist
	#holyCities = [Jerusalem]
	godName = "God"
	#religiousBuildings = [church, cathedral, grandCathedral]
	parentReligion = judaism

christianity = Christianity()

class Catholicism(Christianity):
	name = "catholicism"
	parentReligion = christianity








class Culture:
	language = Language()


culture = Culture()
russian = Russian()
culture.language = russian
#print True*0