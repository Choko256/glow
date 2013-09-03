#-*- coding:utf8 -*-

# Glow Map class

import os.path

class MapTile:
	def __init__(self, x, y, _type):
		self._x = x
		self._y = y
		self._type = _type

class Map:
	def __init__(self, name):
		self._name = name

	@staticmethod
	def from_file(self, filename):
		return Map(os.path.join('./map', os.path.basename(filename)))
