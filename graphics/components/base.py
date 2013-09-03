#-*- coding:utf8 -*-

# Base for all SFML Components
# Do not create directly a BaseComponent object

import sfml as sf
from abc import abstractmethod

class BaseComponent(sf.TransformableDrawable):
	def __init__(self, name):
		self.component_name = name
		self.events = {
			'OnCreate': None,
			'OnDraw': None,
		}
		self._default_font = sf.Font.from_file('./graphics/components/arial.ttf')

	def get_default_font(self):
		return self._default_font

	def _run_event(self, name, args=None):
		if name in self.events:
			if args:
				self.events[name](self, args)
			else:
				self.events[name](self)

	def draw(self, target, states):
		sf.TransformableDrawable.draw(self, target, states)
		# states.transform *= get_transform()
		self._draw(target)

	@abstractmethod
	def _draw(self, target):
		pass

	@abstractmethod
	def handle_event(self, event):
		pass
