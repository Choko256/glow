#-*- coding:utf8 -*-

# Status bar for SFML

import sfml as sf
from . import base as b

class StatusBar(b.BaseComponent):
	def __init__(self, name):
		b.BaseComponent.__init__(self, name)
		self._items = []
		self._sb_rect = sf.RectangleShape()
		self._sb_rect.fill_color = sf.Color.BLACK

	def add_item(self, item):
		self._items.append(item)

	def remove_item(self, item):
		self._items.remove(item)

	def _draw(self, target):
		self._sb_rect.size = sf.Vector2(target.width, 20)
		self._sb_rect.position = sf.Vector2(0, target.height - 20)
		self._sb_rect.outline_thickness = 2.0
		self._sb_rect.outline_color = sf.Color(240, 240, 240)
		target.draw(self._sb_rect)
		startpos = 10
		for itm in self._items:
			itm.position = sf.Vector2(startpos, self._sb_rect.global_bounds.top + 5)
			target.draw(itm)
			startpos += itm.global_bounds.width + 10

	def handle_event(self, event):
		pass
