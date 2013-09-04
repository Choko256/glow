#-*- coding:utf8 -*-

# Button for SFML

from . import base as b
import sfml as sf

class Button(b.BaseComponent):
	def __init__(self, name, label="Button", onclick=None):
		b.BaseComponent.__init__(self, name)
		self._label = label
		self.events.update({
			'OnClick': onclick
		})
		self.hovered = False
		self.downed = False
		self._b_rect = sf.RectangleShape(sf.Vector2(60, 25))

	def get_size(self):
		return (60, 25)

	def set_position(self, position):
		self._b_rect.position = position

	def get_position(self):
		return self._b_rect.position

	def del_position(self):
		del self._b_rect.position
	position = property(get_position, set_position, del_position, "Position of the Button")

	def _draw(self, target):
		self._b_rect.fill_color = sf.Color(175, 175, 175, 210)
		self._b_rect.outline_color = sf.Color(96, 96, 96, 180)
		self._b_rect.outline_thickness = 2.0

		if self.hovered:
			self._b_rect.fill_color = sf.Color(210, 210, 210, 210)
			self._b_rect.outline_color = sf.Color(125, 125, 125, 180)
		if self.downed:
			self._b_rect.fill_color = sf.Color(80, 80, 80, 210)
			self._b_rect.outline_color = sf.Color(10, 10, 10, 180)

		lbl = sf.Text(self._label)
		lbl.font = self.get_default_font()
		lbl.character_size = self.get_default_font_size()
		lbl.color = self.get_default_font_color()
		if self.hovered:
			lbl.color = self.get_default_font_color()
		if self.downed:
			lbl.color = self.get_default_font_color()
		lbl.position = sf.Vector2(
			self._b_rect.global_bounds.left + ((self._b_rect.global_bounds.width - lbl.global_bounds.width) / 2),
			self._b_rect.global_bounds.top + ((self._b_rect.global_bounds.height - lbl.global_bounds.height) / 2)
		)
		target.draw(self._b_rect)
		target.draw(lbl)

	def handle_event(self, event):
		if type(event) is sf.MouseMoveEvent:
			self.hovered = self._b_rect.global_bounds.contains(event.position)
		elif type(event) is sf.MouseButtonEvent:
			if event.released and event.button == sf.Mouse.LEFT:
				self.downed = False
				if self.hovered:
					self._run_event('OnClick')
			elif self.hovered and event.pressed and event.button == sf.Mouse.LEFT:
				self.downed = True
