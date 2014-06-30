# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 17:03:33 2013

@author: keder
"""

import json


class NameSortedList:
	def __init__(self, json_file):
		json_file = open(json_file, 'r')
		raw_json = json_file.read()
		data = json.loads(raw_json)
		self.list = {}
		for item in data:
			self.list.update({item["name"]:item})

class CommonLists:
	def __init__(self, files):
		self.items = NameSortedList(files.items)
		self.buildings = NameSortedList(files.buildings)
		self.tasks = NameSortedList(files.tasks)
		self.activities = NameSortedList(files.activities)