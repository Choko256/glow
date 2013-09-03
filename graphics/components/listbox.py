#-*- coding:utf8 -*-

# List box for SFML Python

from . import base as b
import sfml as sf

class ListBoxItem(b.BaseComponent):
	def __init__(self, name, index, width, relative_to, _object=None, onselect=None):
		b.BaseComponent.__init__(self, name)
		self._object = _object
		self._width = width
		self._index = index
		self.hovered = False
		self.selected = False
		self._relative_parent_pos = relative_to
		self.events.update({
			'OnSelect': onselect
		})

		self._i_rect = sf.RectangleShape(sf.Vector2(width, 30 * (index + 1)))

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
		self._i_rect.position = sf.Vector2(self._relative_parent_pos.x, self._relative_parent_pos.y * (self._index + 1))
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
	def __init__(self, name, size, objects=[]):
		b.BaseComponent.__init__(self, name)
		self._objects = objects
		self.hovered = False
		self.selected = -1

		self.l_rect = sf.RectangleShape(size)
		self.l_rect.fill_color = sf.Color(220, 220, 220, 200)

	def set_position(self, position):
		self.l_rect.position = position
		for itm in self._objects:
			itm._relative_parent_pos = sf.Vector2(self.l_rect.global_bounds.left, self.l_rect.global_bounds.top)

	def get_position(self):
		return self.l_rect.position

	def del_position(self):
		del self.l_rect.position
	position = property(get_position, set_position, del_position, "Position of the ListBox")

	def add_object(self, _object):
		self._objects.append(ListBoxItem('item-%d' % (len(self._objects),), len(self._objects), self.l_rect.global_bounds.width, sf.Vector2(self.l_rect.global_bounds.left, self.l_rect.global_bounds.top)
			, _object, onselect=self.on_select_item)
		)

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
