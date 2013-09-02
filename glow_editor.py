#-*- coding:utf8 -*-

# Glow map editor

import sfml as sf
from editor.frame import MainFrame

class GlowEditor:
	def __init__(self):
		f = MainFrame()
		f.open()

if __name__ == "__main__":
	editor = GlowEditor()
