#-*- coding:utf8 -*-

# Textbox for SFML

import sfml as sf
from . import base as b

class TextBox(b.BaseComponent):
	def __init__(self, name, width, onvalidate=None):
		b.BaseComponent.__init__(self, name)
		self.events.update({
			'OnValidate': onvalidate
		})
		self._width = width
		self._height = 30

		self._t_rect = sf.RectangleShape(sf.Vector2(self._width, self._height))

	def _draw(self, target):
		pass

	def handle_event(self, event):
		pass
