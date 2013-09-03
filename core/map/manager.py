#-*- coding:utf8 -*-

# Glow Map manager

import glob
from .map import Map

class MapManager:
	@staticmethod
	def get_map_list():
		ml = glob.glob("./map/*.map")
		return [ Map.from_file(mp) for mp in ml ]
