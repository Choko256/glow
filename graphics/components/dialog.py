#-*- coding:utf8 -*-

import sfml as sf
from . import base as b

class Dialog(b.BaseComponent):
	def __init__(self, name, size, title="Dialog", onclose=None):
		b.BaseComponent.__init__(self, name)
		self.size = size
		self._title = sf.Text(title)
		self._title.font = self.get_default_font()
		self._title.character_size = 12
		self._title.style = sf.Text.BOLD
		self._title.color = sf.Color.WHITE

		self._window = sf.RectangleShape(self.size)
		self._window.fill_color = sf.Color(240, 240, 225, 180)

		self._close_button = sf.Texture.from_file('./graphics/components/close.png')
		self.sp_close = sf.Sprite(self._close_button)

		self.components = []
		self.visible = False

		self.events.update({
			'OnClose': onclose
		})

	def set_title(self, title):
		self._title.string = title

	def add_component(self, component, position):
		self.components.append([component, position])

	def _draw(self, target):
		if self.visible:
			self._window.position = sf.Vector2(
				(target.width - self._window.global_bounds.width) / 2,
				(target.height - self._window.global_bounds.height) / 2
			)
			target.draw(self._window)

			titlebar = sf.RectangleShape(sf.Vector2(self._window.global_bounds.width, 40))
			titlebar.position = sf.Vector2(self._window.global_bounds.left, self._window.global_bounds.top)
			titlebar.fill_color = sf.Color(51, 204, 255)
			target.draw(titlebar)

			self._title.position = sf.Vector2(titlebar.global_bounds.left + 15, titlebar.global_bounds.top + 5)
			target.draw(self._title)

			self.sp_close.position = sf.Vector2(titlebar.global_bounds.left + titlebar.global_bounds.width - 36, titlebar.global_bounds.top + 4)
			target.draw(self.sp_close)

			for c in self.components:
				c[0].position = sf.Vector2(self._window.global_bounds.left + c[1].x, self._window.global_bounds.top + c[1].y)
				target.draw(c[0])

	def handle_event(self, event):
		if self.visible:
			if type(event) is sf.MouseButtonEvent:
				if event.released and event.button == sf.Mouse.LEFT:
					if self.sp_close.global_bounds.contains(event.position):
						self.visible = False
						self._run_event('OnClose')
