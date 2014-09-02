import word_chopper

def enter():
		print "Still dressed to the nines in your floral-patterned sun dress, you"
		print "gambol across the street to Peter Pan Bakery where you can be"
		print "damned sure you'll find some cream-filled delights for your"
		print "stockpile. You walk in with manly, Kate Moss confidence only to find"
		print "a vile Hatchet Sloth behind the counter. Its hatchet hands cast"
		print "a terrible shadow across the neck of a fair Polish maiden."
		print "Do you:\nRUN AWAY\nor\nSEX UP THE SLOTH\n???"
		
		action = word_chopper.chop()

		for word in action:

			if word == 'run' or word == 'away':
				print "Oh, great job. You outran a sloth."
				return 'hs'
			
			elif word == 'sex' or word == 'up':
				print "You smooth out your slightly ruffled but still sextastic"
				print "sun dress and saunter over to the where the sloth is slowly"
				print "but surely terrorizing the fair Polish maiden. You whisper"
				print "sweet sloth-nothings into its hateful ear. Such poetry issues"
				print "from your lips and you know that you will certainly escape"
				print "with your life, not to mention this Hatchet Sloth's heart"
				print "but lo-- OUT OF NOWHERE THE FAIR POLISH MAIDEN BRAINS YOU"
				print "WITH A FIRE EXTINGUISHER. BRAIN ANEURYSM. 0/10 STARS--"
				print "NOT CHILL BRO--"
				return 'death'

			else:
				print "OK, let's try this again. Luckily you are battling a"
				print "sloth and there is plenty of time."
				return 'food'
