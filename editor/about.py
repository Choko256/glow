#-*- coding:utf8 -*-

# About dialog for The Glow Game

from graphics.components import dialog
import sfml as sf
from settings import *

class AboutDialog(dialog.Dialog):
	def __init__(self, title="About", onclose=None):
		dialog.Dialog.__init__(self, 'about', (400, 400), title, onclose)
		self.init_ui()

	def init_ui(self):
		logo = sf.Texture.from_file('./res/img/logo.png')
		sp = sf.Sprite(logo)
		# sp.texture_rectangle = sf.Rectangle((10, 60), (380, 156))
		# sp.scale(0.37)
		sp.ratio = sp.ratio * 0.37
		sp.color = sf.Color(255, 255, 255, 200)
		self.add_component(sp, sf.Vector2(10, 60))

		d_1 = sf.Text("Version %s" % (APP_VERSION,))
		d_1.character_size = 14
		d_1.color = sf.Color(30, 30, 210)
		d_1.font = self.get_default_font()
		d_1.style = sf.Text.ITALIC
		self.add_component(d_1, sf.Vector2(50, 170))

		d_2 = sf.Text("This software is protected by international laws on copyright.\nCopyright %s %s.\nAll rights reserved." % (APP_DATE, APP_COPYRIGHT))
		d_2.character_size = 10
		d_2.color = sf.Color.BLACK
		d_2.font = self.get_default_font()
		self.add_component(d_2, sf.Vector2(40, 300))
