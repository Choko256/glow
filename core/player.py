#-*- coding:utf8 -*-

# Glow Player Main class

class PlayerClass:
	def __init__(self, name):
		self._name = name

class Player:
	def __init__(self, name):
		self._name = name
		self._level = 0
		self._experience = 0
		self._money = 0
		self._title = None
		self._inventory = []

	def buy_object(self, _object):
		self._money -= _object._value
		self.add_object(_object)

	def add_object(self, _object):
		self._inventory.append(_object)

	def drop_object(self, _object):
		self._inventory.remove(_object)

	def set_title(self, _title):
		self._title = _title
