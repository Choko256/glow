#-*- coding:utf8 -*-

# Glow Editor main frame

import sfml as sf
from graphics.components import menu, statusbar
from . import about, maplist
from settings import *

class MainFrame:
	def __init__(self):
		self.window = sf.RenderWindow(sf.VideoMode(1024, 600), 'Glow Map Editor')
		self.window.framerate_limit = 60
		self.window.vertical_synchronization = True

		self.loaded_map = None

		self.menubar = menu.MenuBar('mbar')
		self.statusbar = statusbar.StatusBar('status_bar')
		self.components = [ self.menubar, self.statusbar ]

	def __getattr__(self, name):
		if not hasattr(self, name):
			for c in self.components:
				if c.name == name:
					return c

	def init_ui(self):
		_system = self.menubar.add_item('System')
		self.mi_new_map = _system.add_children('New Map', onclick=None)
		self.mi_quit = _system.add_children('Quit', onclick=self.close)		
		_map = self.menubar.add_item('Map')
		self.mi_open_map = _map.add_children('Open map...', onclick=self.openmap)
		self.mi_save_map = _map.add_children('Save map', onclick=self.savemap)
		self.mi_close_map = _map.add_children('Close map', onclick=self.closemap)
		self.mi_close_map.visible = False
		_display = self.menubar.add_item('Tools')
		self.mi_show_tools = _display.add_children('Show/Hide tools', onclick=self.show_tools)
		_help = self.menubar.add_item('Help')
		self.mi_about = _help.add_children('About...', onclick=self.show_about)

		ver = sf.Text("Version %s" % (APP_VERSION,))
		ver.font = self.statusbar.get_default_font()
		ver.character_size = 10
		ver.color = sf.Color.WHITE
		self.statusbar.add_item(ver)

		self.lmap = sf.Text("No map loaded.")
		self.lmap.font = self.statusbar.get_default_font()
		self.lmap.character_size = self.statusbar.get_default_font_size()
		self.lmap.color = sf.Color.WHITE
		self.statusbar.add_item(self.lmap)

	def openmap(self):
		mapdlg = maplist.MapListDialog(onclose=self.on_destroy_component)
		mapdlg.visible = True
		mapdlg.bind_event('OnSelectMap', self.load_map)
		self.components.append(mapdlg)

	def savemap(self):
		pass

	def closemap(self):
		self.loaded_map = None
		self.lmap.string = "No map loaded."
		self.mi_close_map.visible = False

	def show_tools(self):
		pass

	def on_destroy_component(self, component):
		if component in self.components:
			self.components.remove(component)

	def show_about(self):
		abdlg = about.AboutDialog(title="About %s" % (APP_NAME,), onclose=self.on_destroy_component)
		abdlg.visible = True
		self.components.append(abdlg)

	def load_map(self, origin, args):
		self.loaded_map = args[0].data
		self.lmap.string = "Map: %s" % (str(self.loaded_map),)
		self.mi_close_map.visible = True

	def close(self):
		self.window.close()

	def open(self):
		self.init_ui()
		while self.window.is_open:
			z_faced = [ c for c in self.components if c.z_faced ]
			for ev in self.window.events:
				if type(ev) is sf.CloseEvent:
					self.window.close()
				else:
					for c in self.components:
						try:
							if len(z_faced) == 0 or c.z_faced:
								c.handle_event(ev)
						except AttributeError:
							pass
			self.window.clear()
			for c in self.components:
				if len(z_faced) == 0 or c.z_faced:
					self.window.draw(c)
			self.window.display()
