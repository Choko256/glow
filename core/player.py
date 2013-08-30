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
