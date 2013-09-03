#-*- coding:utf8 -*-

# List box for SFML Python

from . import base as b
import sfml as sf

class ListBoxItem(b.BaseComponent):
	def __init__(self, name, index, width, _object=None, onselect=None):
		b.BaseComponent.__init__(self, name)
		self._object = _object
		self._width = width
		self._index = index
		self.hovered = False
		self.selected = False
		self.events.update({
			'OnSelect': onselect
		})

		self._i_rect = sf.RectangleShape(sf.Vector2(width, 30))

	def _draw(self, target):
		label = sf.Text(str(self._object))
		label.character_size = 12
		label.font = self.get_default_font()
		label.color = sf.Color.BLACK
		if self.selected:
			label.style = sf.Text.BOLD
		if self.hovered:
			self._i_rect.fill_color = sf.Color(240, 240, 240, 220)
		else:
			self._i_rect.fill_color = sf.Color(230, 230, 230, 210)
		label.position = sf.Vector2(self._i_rect.global_bounds.left + 20, self._i_rect.global_bounds.top + 10)
		target.draw(self._i_rect)
		target.draw(label)

	def handle_event(self, event):
		if type(event) is sf.MouseMoveEvent:
			self.hovered = self._i_rect.global_bounds.contains(event.position)
		elif type(event) is sf.MouseButtonEvent:
			if self.hovered and event.released and event.button == sf.Mouse.LEFT:
				self.selected = True
				self._run_event('OnSelect')

class ListBox(b.BaseComponent):
	def __init__(self, name, size, objects=[], shown=10):
		b.BaseComponent.__init__(self, name)
		self._objects = objects
		self._max_height = maxheight
		self.hovered = False
		self.selected = -1
		self._shown = 10

		self.l_rect = sf.RectangleShape(size)
		self.l_rect.fill_color = sf.Color(220, 220, 220, 200)

	def add_object(self, _object):
		self._objects.append(ListBoxItem('item-%d' % (len(self._objects),), len(self._objects), _object, onselect=self.on_select_item))

	def on_select_item(self, item):
		self.selected = self._objects.index(item)
		for itm in self._objects:
			if itm != item:
				itm.selected = False

	def remove_object(self, _object):
		if type(_object) is ListBoxItem:
			self._objects.remove(_object)
		else:
			itm = [ item for item in self._objects if item._object == _object ][0]
			self._objects.remove(itm)

	def remove_at(self, index):
		self._objects.remove(self._objects[index])

	def _draw(self, target):
		target.draw(self.l_rect)
		for obj in self._objects:
			target.draw(obj)

	def handle_event(self, event):
		if type(event) is sf.MouseMoveEvent:
			self.hovered = self.l_rect.global_bounds.contains(event.position)
		for itm in self._objects:
			itm.handle_event(event)
