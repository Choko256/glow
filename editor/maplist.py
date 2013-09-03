#-*- coding:utf8 -*-

# Map list dialog

from graphics.components import dialog
import sfml as sf
from settings import *

class MapListDialog(dialog.Dialog):
	def __init__(self, title="Map List", onclose=None):
		dialog.Dialog.__init__(self, 'maplist', (400, 800), title, onclose)
		self.init_ui()

	def init_ui(self):
		d_1 = sf.Text("Select a map to edit :")
		d_1.character_size = 12
		d_1.style = sf.Text.BOLD
		d_1.font = self.get_default_font()
		self.add_component(d_1, sf.Vector2(5, 50))
