#! /usr/bin/env python
"""
Created on Tue Aug 28 11:32:37 2012

@author: keder
"""
from copy import copy
from random import random


def check_conditions(conditions, main_obj=None, additional_obj=None):
	if type(conditions) is list:
		if (type(conditions[0]) is list) or (conditions[0] == 'and'):
			result = True
			for item in conditions[1:]:
				result = result and check_conditions(item, main_obj, additional_obj)
			return result
		elif conditions[0] == 'or':
			result = False
			for item in conditions[1:]:
				result = result or check_conditions(item, main_obj, additional_obj)
			return result
		elif conditions[0] == 'not':
			result = True
			for item in conditions[1:]:
				result = result and not check_conditions(item, main_obj, additional_obj)
			return result
		elif (conditions[0] == 'in'):
			return check_conditions(conditions[1], main_obj, additional_obj) in check_conditions(conditions[2], main_obj, additional_obj)
		elif (conditions[0] == 'equals') or (conditions[0] == '==') or (conditions[0] == '='):
			return check_conditions(conditions[1], main_obj, additional_obj) == check_conditions(conditions[2], main_obj, additional_obj)
		elif (conditions[0] == 'more') or (conditions[0] == '>'):
			return check_conditions(conditions[1], main_obj, additional_obj) > check_conditions(conditions[2], main_obj, additional_obj)
		elif (conditions[0] == 'less') or (conditions[0] == '<'):
			return check_conditions(conditions[1], main_obj, additional_obj) < check_conditions(conditions[2], main_obj, additional_obj)
		elif (conditions[0] == '=>') or (conditions[0] == '>='):
			return check_conditions(conditions[1], main_obj, additional_obj) >= check_conditions(conditions[2], main_obj, additional_obj)
		elif (conditions[0] == '<=') or (conditions[0] == '=<'):
			return check_conditions(conditions[1], main_obj, additional_obj) <= check_conditions(conditions[2], main_obj, additional_obj)
		elif type(conditions[0]) is str:
			if conditions[0] == 'main_obj':
				cursor = main_obj
			elif conditions[0] == 'additional_obj':
				cursor = additional_obj
			else:
				cursor = globals()[conditions[0]]
			if len(conditions) > 1:
				for item in conditions[1:]:
					cursor = getattr(cursor, item)
			return cursor
		else:
			return False
	else:
		return conditions



class Law:
	pass


class LegalAge(Law):
	man = 16
	woman = 14

class MasterLaw(Law):
	def __init__(self):
		self.autonomous = False
		self.own_executive = False
		self.own_legislative = False
		self.own_judiciary = False
		self.right_of_censorship = False


class TitleTransitionLaw(Law):
	def __init__(self, item_groups_num=0, min_heirs=0):
		"""
		item_groups_num - from all candidates only this amount of people will receive positions
		0 means all candidates receives heritage items since there is enough of them
		min_heirs - if this minimum is not met special actions will be taken

		"""
		self.item_groups_num = item_groups_num
		self.min_heirs = min_heirs
		self.office
		self.candidates = []
		"""
		primary_only - means
		"""
		self.primary_only = False
		'''
		Defines one or ones who appoint (even if automatic - someone should choose
		successor if ruler is dead and there is no appropriate heirs)
		'''
		self.disposer = None
		'''
		succession - automatic
		appointment - select or elect the most suitable
		'''
		self.appointment_type = "succession"
		"""
		seniority - by age decreasing
		juniority - by age increasing
		primogeniture - sorting along the descending line
		power - sort by influence
		support - sort by popularity
		"""
		self.sorting = "seniority"
		"""
		-2 - only female
		-1 - male only if there is no female successor
		0 - gender equality
		1 - female only if there is no male successor
		2 - only male
		"""
		self.gender_sorting = 0
		"""
		cycle - heritage items added to groups following their list order until item_groups_num reached,
		then next item will be added to the first group and so on
		first_gets_best - all groups except the first gets last items in the list, one item per group, first get the rest items
		first_gets_rest - every group gets one item following the list order, rest items get first group
		"""
		self.items_grouping_type = "cycle"
		"""
		candidate_conditions - exact name of function in conditions.py
		"""
		self.filter = None

	def gender_sort(self):
		if self.gender_sorting == 0:
			return True
		males = []
		females = []
		for person in self.heirs:
				if person.gender:
					females.append(person)
				else:
					males.append(person)
		if self.gender_sorting == -2:
			self.heirs = females
			return True
		elif self.gender_sorting == -1:
			self.heirs = females + males
			return True
		elif self.gender_sorting == 1:
			self.heirs = males + females
			return True
		elif self.gender_sorting == 2:
			self.heirs = males
			return True
		else:
			return False

	def candidates_sort(self):
		if self.sorting == 'seniority':


	def group_heritage_items(self,items):
		if len(items) < self.min_heirs:
			return False
		self.item_groups = [list() for j in range(self.item_groups_num)]
		if self.item_groups_num > len(items):
			for i in range(self.item_groups_num):
				self.item_groups[i] = [items[i]]
			return True
		if self.item_groups_num == 1:
			self.item_groups = [items]
			return True
		elif self.items_grouping_type == "cycle":
			i = 0
			j = 0
			flag = True
			while flag:
				if i >= self.item_groups_num:
					i = 0
				self.item_groups[i].append(items[j])
				i += 1
				j += 1
				if j >= len(items):
					flag = False
			return True
		elif self.items_grouping_type == "first_gets_best":
			items = items.reverse()
			for i in range(self.item_groups_num-1):
				self.item_groups[i] = [items[i]]
			self.item_groups[-1] = items[self.item_groups_num:]
			self.item_groups.reverse()
			return True
		elif self.items_grouping_type == "first_gets_rest":
			for i in len(self.item_groups):
				self.item_groups[i].append(items[i])
			self.item_groups[0] += items[len(self.item_groups):]
			return True
		else:
			return False


	def filter_candidates(self):
		"""

		"""



class Office:
	def __init__(self):
		self.holder = None
		self.subjects = []
		self.social_groups = []
		self.master = None
		self.residence = None
		self.title = ""
		self.transition_law = None
		self.bound_titles = []

	def set_master(self, master):
		self.master = master

	def add_subject(self, subject):
		self.subjects.append(subject)
		subject.set_master(self)

	def add_function(self, function):
		self.functions.append(function)

	def set_advisory(self, office):
		self.advisory = office

	def add_censor(self, office):
		self.censor = office

	def set_master_law(self, law):
		self.master_law = law

class Organization:
	def __init__(self, name=None):
		self.name = name
		self.social_groups = []
		self.head = None
		self.owner = None
		self.master = None
		self.real_estate = []
		self.property = []
		self.offices = []

#Set of offices is authority
class Authority:

	def set_master(self, master):
		self.master = master

	def add_subject(self, subject):
		if not hasattr(self, "subjects"):
			self.subjects = []
		self.subjects.append(subject)
		subject.set_master(self)

	def set_ruler(self, office):
		self.ruler = office

	def __init__(self):
		self.offices = []

	def add_office(self, office, power = 0):
		self.offices.append({"office":office,"power":power})

	def set_executive(self, office):
		self.executive = office

	def set_legislative(self, office):
		self.legislative = office

	def set_judiciary(self, office):
		self.judiciary = office

	def add_auxillary(self, office):
		self.auxillary.append(office)




class Community(Authority):
	#No leader, all issues are solved collectively
	name = "community"

class Assembly(Office):
	def set_group(self, group):
		self.group = group

	def update_members(self):
		if hasattr(self.group, "members"):
			self.members = copy(self.group.members)
		if hasattr(self.group, "population"):
			self.members = copy(self.group.population)
	def gather(self):
		self.update_members()
		self.gathered = 1

	def dismiss(self):
		self.gathered = 0

class Counsil(Office):
	name = "counsil"

	def __init__(self, appointmentLaw):
		self.appointmentLaw = appointmentLaw
		self.members = []
		self.dismissed = 1

	def set_head(self, person):
		if person in self.members:
			self.head = person
			return 1
		else:
			return 0

	def dismiss(self):
		self.members = []
		self.dismissed = 1

	def set_seats(self, seats_number):
		if self.dismissed:
			self.seats = seats_number
			return 1
		else:
			return 0

	def add_member(self, person):
		self.dismissed = 0
		if len(self.members) < self.seats:
			self.members.append(person)
			return 1
		else:
			return 0


class Ministry(Office):

	def __init__(self):
		self.staff = []

	def set_head(self, person):
		self.head = person


class Cabinet(Office):
	def set_religious(self, office):
		self.religious = office

	def set_military(self, office):
		self.military = office

	def set_financial(self, office):
		self.economic = office

	def set_cultural(self, office):
		self.cultural = office

	def set_security(self, office):
		self.police = office

	def set_educational(self, office):
		self.educational = office

	def set_foreign(self, office):
		self.foreign = office

	def set_infrastructial(self, office):
		self.infrastructial = office

	def set_espionage(self, office):
		self.espionage = office


class PersonalOffice(Office):
	def __init__(self, name, successionLaw, holder = nobody):
		self.name = name
		self.holder = holder
		self.former_holders = []
		self.successionLaw = successionLaw

	def create(self, person):
		self.holder = person

	def dead_holder(self):
		self.former_holders.append(self.holder)
		self.holder = nobody

	def set_holder(self, person):
		self.holder = person

	def transfer(self,person):
		self.former_holders.append(self.holder)
		self.holder = person

	def set_advisory(self, office):
		self.advisory = office


class Position(PersonalOffice):
	def __init__(self, appointmentLaw, holder = nobody):
		self.appointmentLaw = appointmentLaw
		self.holder = holder



class LandTitle(PersonalOffice):
	category = "land"
	holdings = []
	regent = nobody
	#successionLaw = Law()
	def set_tier(self, tier):
		self.tier = tier

	def check_tier(self):
		self.tier = 0
		cursor = self
		checked = set([])
		while 1:
			pass

	def add_vassal(self, vassal):
		if not hasattr(self, "vassals"):
			self.vassals = []
		self.vassals.append(vassal)
		vassal.set_liege(self)
		self.check_tier()

	def set_liege(self, liege):
		self.liege = liege

	def dead_holder(self, regent):
		self.former_holders.append(self.holder)
		self.holder = nobody
		self.regent = regent
		#self.successionLaw.dead_holder()

	def set_holder(self, person):
		if (person.age >= legalAge) and (disabled in person.traits):
			self.regent = nobody
			self.holder = person
		else:
			self.holder = person


#class ReligiousTitle(PersonalOffice):
#	category = "religious"
#	holdings = []
#	#residency = Temple()
#	vassals = []
#	lieges = []
#	tier = 0
#	regent = nobody
#	#successionLaw = Law()
#	def dead_holder(self, regent):
#		self.former_holders.append(self.holder)
#		self.holder = nobody
#		self.regent = regent
#		#self.successionLaw.dead_holder()
#
#	def set_holder(self, person):
#			self.regent = nobody
#			self.holder = person



class VassalElection(TitleTransitionLaw):
	def __init__(self, title):
		self.title = title
		self.timeLag = 30


	def getNewHolder():
		self.getVoters()
		self.getContenders()

	def getVoters(self):
		if voting_law == "full_vassal":
			self.voters = self.title.vassals
		elif voting_law == "top_vassal":
			for vassal in self.title.vassals:
				if vassal.tier == (self.title.tier - 1):
					self.voters.append(vassal)

	def getContenders(self):
		b = copy(self.title.vassals)
		for j in range(0,len(b)-1):
			maximum = j
			for i in range(j+1, len(b)):
				if b[i].power > b[maximum].power:
					maximum = i
			buf = b[maximum]
			b[maximum]	= b[j]
			b[j] = buf
		self.contenders = b

	def getVotes(self):
		pass


class Primogeniture(TitleTransitionLaw):

	def __init__(self, female_right):
		'''female_right: 0 means only male heir
		1 males has advantage'''

		self.female_right = female_right

	def getHeir(self, title):
		root_parent = title.former_holders[-1]
		checked = set([])
		while root_parent != unknown:
			checked.add(root_parent)
			if root_parent.children:
				male_candidate = 0
				female_candidate = 0
				for child in root_parent.children:
					if not male_candidate and (child.gender == 0) and not (child in checked):
						male_candidate = child
					if not female_candidate and (child.gender == 1) and not (child in checked):
						female_candidate = child
					if male_candidate and female_candidate:
						break
				if male_candidate:
					if not male_candidate.dead:
						return male_candidate
					elif male_candidate.children:
						root_parent = male_candidate
						continue
					else:
						checked.add(male_candidate)
				elif female_candidate and self.female_right == 1:
					if not female_candidate.dead:
						return female_candidate
					else:
						checked.add(female_candidate)
			root_parent = root_parent.father

class OfficeTransitionLaw:
	def __init__(self, office, contenders_selection, winners_selection = "drawing", voters_selection = "contenders"):
		self.office = office
		self.contenders_selection = contenders_selection
		self.winners_selection = winners_selection
		self.voters_selection = voters_selection

	def get_winners(self):
		if self.winners_selection == "seniority":
			for i in range(int(len(self.contenders)/2)):
				__maximum__ = self.contenders[i]
				__minimum__ = self.contenders[-i-1]
				for j in range(i,len(self.contenders)-i):
					if self.contenders[j].age > __maximum__.age:
						__maximum__ = self.contenders[j]
					elif self.contenders[j].age < __minimum__.age:
						__minimum__ = self.contenders[j]
				self.contenders[i] = __maximum__
				self.contenders[-i-1] = __minimum__
			if hasattr(self.office, "seats"):
				if self.office.seats < len(self.contenders):
					return self.contenders[:self.office.seats]
				else:
					return self.contenders
			else:
				return self.contenders[0]
		elif self.winners_selection == "open_ballot":
			result = {}
			for contender in self.contenders:
				result.update({contender:0})
			if hasattr(self.office, "seats"):
				if self.office.seats < len(self.contenders):
					return self.contenders[:self.office.seats]
				else:
					return self.contenders
			else:
				for voter in self.voters:
					vote = self.contenders[0]
					for contender in self.contenders:
						if (voter.get_support(contender) + voter.get_fear(contender)) > \
						(voter.get_support(vote) + voter.get_fear(vote)):
							vote = contender
					result[vote] += 1
				winner = []
				for key in result.keys():
					if winner:
						if result[key] > result[winner]:
							winner = key
					else:
						winner = key
				return winner

		else:
			if hasattr(self.office, "seats"):
				if self.office.seats < len(self.contenders):
					result = []
					for i in range(self.office.seats):
						r = len(self.contenders) * random()
						result.append(self.contenders[int(r)])
						self.contender.remove(self.contender[int(r)])
					return result
				else:
					return self.contenders
			else:
				r = len(self.contenders) * random()
				return self.contenders[int(r)]


class Seniority(TitleTransitionLaw):

	def __init__(self, female_right):
		'''female_right: 0 means only male heir
		1 males has advantage'''

		self.female_right = female_right

	def getHeir(self, title):
		if title.holder != nobody:
			holder = title.holder
		else:
			holder = title.former_holders[-1]
		for person in holder.family.live_members:
			if person.gender == 0:
				return person
		for person in holder.family.live_members:
			if (person.gender == 1) and (self.female_right == 1):
				return person








b=[3,6,4,89,45,31,80,39]
for j in range(0,len(b)-1):
	maximum = j
	for i in range(j+1, len(b)):
		if b[i] > b[maximum]:
			maximum = i
	buf = b[maximum]
	b[maximum]	= b[j]
	b[j] = buf
print str(b)



















