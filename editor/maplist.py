#-*- coding:utf8 -*-

# Map list dialog

from graphics.components import dialog, listbox
import sfml as sf
from settings import *
from core.map import manager

class MapListDialog(dialog.Dialog):
	def __init__(self, title="Map List", onclose=None):
		dialog.Dialog.__init__(self, 'maplist', (400, 500), title, onclose)
		self.init_ui()

	def init_ui(self):
		d_1 = sf.Text("Select a map to edit :")
		d_1.character_size = 12
		# d_1.style = sf.Text.BOLD
		d_1.color = sf.Color.BLACK
		d_1.font = self.get_default_font()
		self.add_component(d_1, sf.Vector2(5, 50))

		d_2 = listbox.ListBox('maplist-list', (350, 400))
		mlist = manager.MapManager.get_map_list()
		for mp in mlist:
			d_2.add_object(mp)
		self.add_component(d_2, sf.Vector2(25, 75))

		if len(mlist) == 0:
			d_3 = sf.Text("No map available.")
			d_3.character_size = 10
			d_3.font = self.get_default_font()
			d_3.color = sf.Color(210, 30, 25)
			d_3.style = sf.Text.ITALIC or sf.Text.BOLD
			self.add_component(d_3, sf.Vector2(30, 80))
