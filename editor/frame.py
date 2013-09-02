#-*- coding:utf8 -*-

# Glow Editor main frame

import sfml as sf
from graphics.components import menu, statusbar

class MainFrame:
	def __init__(self):
		self.window = sf.RenderWindow(sf.VideoMode(1024, 600), 'Glow Map Editor')
		self.window.framerate_limit = 60
		self.window.vertical_synchronization = True
		self.menubar = menu.MenuBar('mbar')
		self.statusbar = statusbar.StatusBar('status_bar')
		self.components = [ self.menubar, self.statusbar ]

	def __getattr__(self, name):
		if not hasattr(self, name):
			for c in self.components:
				if c.name == name:
					return c

	def init(self):
		system = self.menubar.add_item('System')
		system.add_children('New Map', onclick=None)
		# system.add_separator()
		system.add_children('Quit', onclick=self.close)		
		self.menubar.add_item('Map')
		self.menubar.add_item('Help')

		ver = sf.Text("Version 0.1A")
		ver.font = self.statusbar.get_default_font()
		ver.character_size = 10
		ver.color = sf.Color.WHITE
		self.statusbar.add_item(ver)

	def close(self):
		self.window.close()

	def open(self):
		self.init()
		while self.window.is_open:
			for ev in self.window.events:
				if type(ev) is sf.CloseEvent:
					self.window.close()
				else:
					for c in self.components:
						try:
							c.handle_event(ev)
						except AttributeError:
							pass
			self.window.clear()
			for c in self.components:
				self.window.draw(c)
			self.window.display()
