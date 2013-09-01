#-*- coding:utf8 -*-

# Glow Map class

class MapTile:
	def __init__(self, x, y, _type):
		self._x = x
		self._y = y
		self._type = _type

class Map:
	def __init__(self, name):
		self._name = name
