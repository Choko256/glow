#-*- coding:utf8 -*-

# Glow Editor main frame

import sfml as sf
from graphics.components import menu, statusbar, dialog

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
		_system = self.menubar.add_item('System')
		_system.add_children('New Map', onclick=None)
		_system.add_children('Quit', onclick=self.close)		
		_map = self.menubar.add_item('Map')
		_map.add_children('Open map...', onclick=self.openmap)
		_map.add_children('Save map', onclick=self.savemap)
		_display = self.menubar.add_item('Tools')
		_display.add_children('Show/Hide tools', onclick=self.show_tools)
		_help = self.menubar.add_item('Help')
		_help.add_children('About...', onclick=self.show_about)

		ver = sf.Text("Version 0.1A")
		ver.font = self.statusbar.get_default_font()
		ver.character_size = 10
		ver.color = sf.Color.WHITE
		self.statusbar.add_item(ver)

	def openmap(self):
		pass

	def savemap(self):
		pass

	def show_tools(self):
		pass

	def on_destroy_component(self, component):
		if component in self.components:
			self.components.remove(component)

	def show_about(self):
		abdlg = dialog.Dialog('about', (400, 400), title="About Glow", onclose=self.on_destroy_component)
		apptitle = sf.Text("The Glow")
		apptitle.character_size = 32
		apptitle.color = sf.Color.BLACK
		apptitle.font = abdlg.get_default_font()
		abdlg.add_component(apptitle, sf.Vector2(40, 60))
		abdlg.visible = True
		self.components.append(abdlg)

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
