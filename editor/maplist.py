#-*- coding:utf8 -*-

# Map list dialog

from graphics.components import dialog, listbox, button
import sfml as sf
from settings import *
from core.map import manager

class MapListDialog(dialog.Dialog):
	def __init__(self, title="Map List", onclose=None, onselectmap=None):
		dialog.Dialog.__init__(self, 'maplist', (400, 500), title, onclose)
		self.events.update({
			'OnSelectMap': onselectmap
		})
		self.init_ui()

	def init_ui(self):
		self.lb_maps = listbox.ListBox('maplist-list', (350, 300))

		d_1 = sf.Text("Select a map to edit :")
		d_1.character_size = 12
		# d_1.style = sf.Text.BOLD
		d_1.color = sf.Color.BLACK
		d_1.font = self.get_default_font()
		self.add_component(d_1, sf.Vector2(5, 50))

		mlist = manager.MapManager.get_map_list()
		for mp in mlist:
			self.lb_maps.add_object(mp)
		self.add_component(self.lb_maps, sf.Vector2(25, 75))

		if len(mlist) == 0:
			d_3 = sf.Text("No map available.")
			d_3.character_size = 10
			d_3.font = self.get_default_font()
			d_3.color = sf.Color(210, 30, 25)
			d_3.style = sf.Text.ITALIC or sf.Text.BOLD
			self.add_component(d_3, sf.Vector2(30, 80))

		b_ok = button.Button('b_ok', 'OK', onclick=self.select_map)
		b_cancel = button.Button('b_cancel', 'Cancel', onclick=self.close)
		self.add_component(
			b_ok,
			sf.Vector2(
				(self._window.global_bounds.width - (2 * b_ok.get_size()[0]) - 15) / 2,
				(self._window.global_bounds.height - 20 - b_ok.get_size()[1])
			)
		)
		self.add_component(
			b_cancel,
			sf.Vector2(
				((self._window.global_bounds.width - (2 * b_cancel.get_size()[0]) - 15) / 2) + b_ok.get_size()[0] + 15,
				(self._window.global_bounds.height - 20 - b_cancel.get_size()[1])
			)
		)

	def select_map(self, origin):
		self._run_event('OnSelectMap', [ self.lb_maps.get_selected() ])
		self.close()
