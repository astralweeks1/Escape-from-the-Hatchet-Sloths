import bedroom
import cheap_charlies
import rock
import peter_pan
import auto_hs
import mccarren
import death


class Map(object):
	
	levels = {'home': bedroom,
	'supplies': cheap_charlies,
	'rock': rock,
	'food': peter_pan,
	'hs' : auto_hs,
	'safe_house': mccarren,
	'death': death,
	}

	def	get_scene(self, level):
		return Map.levels.get(level)


class Engine(object):

	def go(self):
		level = the_map.get_scene('home')
		while True:
			print '\n\n',' ' * 25,'~ ~ ~','\n\n'
			next_level = level.enter()
			level = the_map.get_scene(next_level)	


the_map = Map()
vroom = Engine()
vroom.go()	
