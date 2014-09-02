import random

def make_list():
		presidents = []
		p = open('presidents.txt')
		for name in p:
			clean_names = name.strip('\n')
			presidents.append(clean_names)
		return presidents

def scramble_president():	
		presidents = make_list()
		pick = presidents[random.randint(0,len(presidents)-1)]
		listed_pick = list(pick)
		random.shuffle(listed_pick)
		pickled = ' '.join(listed_pick)
		upper_pickled = pickled.upper()
		print "WHO IS %s" % upper_pickled
		guess = raw_input("\n>> ")
		if pick.lower() == guess.lower():
			return True
		else:
			print "\nIt was %s!!" % pick
			return False

def enter():
		print "A terrifying thought flares in your mind. God, what about the"
		print "innocencents? What about the precious children? You sprint over"
		print "to the Automotive High School across from McCarren, your floral-"
		print "patterned sun dress billowing. You throw open the door of the"
		print "first classroom. Inside are rows of empty desks. At the front"
		print "of the class, someone scratches lines into the blackboard. The"
		print "figure turns. It is a Hatchet Sloth, inexplicably dressed"
		print "in the waistcoat, bifocals, and wig of Benjamin Franklin. The" 
		print "sound of its hatchet scraping across the blackboard is"
		print "excruciating. You look at what is printed there-- a word. It is"
		print "an anagram, the name of a U.S. president. But whose?\n\n"

		if scramble_president():
			print "You shout your answer proudly and Hatchet Franklin drops to"
			print "his knees, awed and humbled by your historico-linguistic prowess."
			print "You recall that today is Sunday which explains the empty desks.\n"
			print "You take your leave of the Automotive High School."
			return 'safe_house'
		else:
			print "Hatchet Franklin lurches toward you. You are hypnotized by"
			print "the sight of his eyes, magnified 2x by the bifocals. This is"
			print "the last thing you see before Hatchet Franklin slices you,"
			print "Chien Andalou style!!"
			return 'death'
