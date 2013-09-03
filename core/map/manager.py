#-*- coding:utf8 -*-

# Glow Map manager

import glob
from .map import Map

class MapManager:
	def get_map_list(self):
		ml = glob.glob("./map/*.map")
		return [ Map.from_file(mp) for mp in ml ]
