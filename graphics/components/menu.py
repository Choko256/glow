#-*- coding:utf8 -*-

# Menu bar for SFML

import sfml as sf
from . import base as b

MENU_ITEM_WIDTH = 100
MENU_BAR_HEIGHT = 35

"""class MenuItemSeparator(b.BaseComponent):
	def __init__(self, name, width=MENU_ITEM_WIDTH):
		b.BaseComponent.__init__(self, name)
		self._width = width

	def handle_event(self, event):
		pass

	def _draw(self, target):
		sep = sf.RectangleShape(sf.Vector2(self._width, 1))
		sep.outline_thickness = 1.0
		sep.outline_color = sf.Color.BLACK
		target.draw(sep)"""

class MenuItem(b.BaseComponent):
	def __init__(self, name, label, position=(0,0), toplevel=False, parent_index=0):
		b.BaseComponent.__init__(self, name)
		self._label = label
		self._children = []
		self._checked = False
		self._on_click = None
		self._opened = False
		self._hovered = False
		self._itm = sf.Text(self._label)
		self._itm.color = sf.Color.BLACK
		self._itm.character_size = 12
		self._itm.font = self.get_default_font()
		self._top_level = toplevel
		self._i_rect = sf.RectangleShape(sf.Vector2(MENU_ITEM_WIDTH, MENU_BAR_HEIGHT))
		self._i_rect.position = position
		self._i_rect.fill_color = sf.Color(100, 100, 100)
		self._i_rect.outline_thickness = 1.0
		self._i_rect.outline_color = sf.Color.BLACK
		self.__parent_index = parent_index

	def set_position(self, position):
		self._i_rect.position = position

	def width(self):
		return self._i_rect.global_bounds.width

	def height(self):
		return self._i_rect.global_bounds.height

	def add_separator(self):
		self._children.append(MenuItemSeparator('sep-%d' % (len(self._children),)))

	def add_children(self, text, onclick=None):
		item = MenuItem(
			'%s-%d' % (self.component_name, len(self._children)),
			text,
			parent_index=len(self._children)
		)
		if self._top_level:
			item.set_position(sf.Vector2(self.position.x, self.position.y + ((len(self._children)+1) * self.height())))
		else:
			item.set_position(sf.Vector2(self.position.x + self.width(), self.position.y))
		item._on_click = onclick
		self._children.append(item)
		return item

	def __str__(self):
		return self._label

	def _draw(self, target):
		if self._hovered:
			self._itm.color = sf.Color(50, 50, 250)
		else:
			self._itm.color = sf.Color.BLACK

		# Not top level item
		if self._opened or not self._top_level:
			self._i_rect.fill_color = sf.Color(200, 200, 200)
		# Opened top level item
		if self._opened and self._top_level:
			self._i_rect.fill_color = sf.Color(240, 240, 210)
			self._i_rect.outline_color = sf.Color(155, 155, 155)
			self._i_rect.outline_thickness = 3.0
		# Closed top level item
		elif self._top_level and not self._opened:
			self._i_rect.outline_thickness = 0.0
			self._i_rect.fill_color = sf.Color(100, 100, 100)

		target.draw(self._i_rect)
		offset = 0 if self._top_level else 1
		self._itm.position = sf.Vector2(
			(self.__parent_index * MENU_ITEM_WIDTH) + ((self._i_rect.global_bounds.width - self._itm.global_bounds.width) / 2),
			((self.__parent_index + offset) * MENU_BAR_HEIGHT) + ((self._i_rect.global_bounds.height - self._itm.global_bounds.height) / 2)
		)

		target.draw(self._itm)
		if self._opened:
			for c in self._children:
				target.draw(c)

	def handle_event(self, event):
		if type(event) is sf.MouseMoveEvent:
			self._hovered = self._itm.global_bounds.contains(event.position)
		elif type(event) is sf.MouseButtonEvent:
			if event.released and event.button == sf.Mouse.LEFT:
				if self._hovered:
					if len(self._children) > 0:
						self._opened = not self._opened
					else:
						if self._on_click:
							self._on_click()
		for c in self._children:
			c.handle_event(event)

class MenuBarPosition:
	POSITION_TOP = 0xA0
	POSITION_BOTTOM = 0xA1
	POSITION_LEFT = 0xA2
	POSITION_RIGHT = 0xA3

class MenuBar(b.BaseComponent):
	def __init__(self, name, position=MenuBarPosition.POSITION_TOP, size=MENU_BAR_HEIGHT):
		b.BaseComponent.__init__(self, name)
		self.events.update({
			'OnClick': None,
		})
		self._items = []
		self._position = position
		self._size = size
		self._fill_color = sf.Color(153, 153, 153)

	def add_item(self, text, onclick=None):
		item = MenuItem('mitem-%d' % (len(self._items)), text, toplevel=True, parent_index=len(self._items))
		item.set_position(sf.Vector2((len(self._items) * MENU_ITEM_WIDTH), 0))
		item._on_click = onclick
		self._items.append(item)
		return item

	def _draw(self, target):
		if self._position in [ MenuBarPosition.POSITION_TOP, MenuBarPosition.POSITION_LEFT ]:
			pos = (0, 0)
			if self._position == MenuBarPosition.POSITION_TOP:
				bar = sf.RectangleShape(sf.Vector2(target.width, self._size))
			elif self._position == MenuBarPosition.POSITION_LEFT:
				bar = sf.RectangleShape(sf.Vector2(self._size, target.height))
		elif self._position == MenuBarPosition.POSITION_BOTTOM:
			pos = (0, target.height - self._size)
			bar = sf.RectangleShape(sf.Vector2(target.width, self._size))
		elif self._position == MenuBarPosition.POSITION_RIGHT:
			pos = (target.width - self._size, 0)
			bar = sf.RectangleShape(sf.Vector2(self._size, target.height))
		else:
			raise Exception("Bad Menu bar position value: Expected one of MenuBarPosition constant values.")
		bar.position = pos
		bar.fill_color = self._fill_color
		target.draw(bar)

		for itm in self._items:
			target.draw(itm)

	def handle_event(self, event):
		for itm in self._items:
			itm.handle_event(event)
