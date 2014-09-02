import word_chopper

def enter():
		print "You pop next door into Cheap Charlie's to pick up supplies. Clearly"
		print "the long prophesied Hatchet Sloth Apocalypse is at hand and you"
		print "need to be prepared. You study the crap-filled shelf in front of"
		print "you and try to think what would be an effective weapon against"
		print "an army of Hatchet Sloths.\nA vacuum cleaner?\n No." 
		print "A melon baller?\n No.\nA floral-patterned sun dress? \n No."
		print "A Hatchet Sloth? \n N- ARHSLKDA;XKLKJFS HOLY FUCK A HATCHET SLOTH!!!" 
		print "!!!!!!111!!!!11!!!!1!!!"
		print "What will you use to fend it off????"
		print "\n\nVACUUM CLEANER\nor\nMELON BALLER\nor" 
		print "FLORAL-PATTERNED SUN DRESS\n???"
		
		action = word_chopper.chop()

		for word in action:

			if word == 'vacuum' or word == 'cleaner':
				print "You aim the vacuum cleaner at the hatchet sloth's eyes which"
				print "jiggle in their sockets for a moment before POPPING out of"
				print "the sloth's face like corks out of New Years' champagne."
				print "You drop the vacuum to make your escape, but the empty eye"
				print "sockets of the Hatchet Sloth have a hypnotic power over you."
				print "Try as you might, you can't look away, you cannot even move."
				print "Slowly, the hatchet hands come inch closer, closer, closer"
				return 'death'
			
			elif word == 'melon' or word == 'baller':
				print "You carve the Hatchet Sloth's eyes out with the melon baller."
				print "It is hard work and slow going but finally you finish: PLOP,"
				print "PLOP. His eyes drop, one by one, like two scoops of ice cream with" 
				print "cherries on top. You chuck the melon baller, aiming to make your" 
				print "escape, but you happen to glance into the empty eye sockets of the"
				print "Sloth. Try as you might, you can't look away. They have a hypnotic"
				print "power. Even as the blinded Hatchet Sloth raises his terrible hatchet"
				print "hands, you are rooted to the spot, utterly helpless to dodge the"
				print "blades as they inch closer."
				return 'death'
		
			elif (word == 'dress' or word == 'floral-patterned' or
				  word == 'sun'):
				print "Quick as a flash you don the floral-patterned sun dress and,"
				print "like Bugs Bunny seducing easy mark, Elmer Fudd, you charm"
				print "the Hatchet Sloth with such niceties the likes of which he has"
				print "never been paid. His genitals quiver in anticipation. But before"
				print "the Hatchet Sloth has time to blink or lick his lips, you"
				print "stride out the door of the shop. A proud, confident woman."
				print "Gone, you do not see the single tear which rolls, fat and"
				print "slow down the lonely Hatchet Sloth's hateful face."
				return 'rock'
				
			else:
				print "OK, let's try this again. We have time. Luckily you"
				print "are battling a sloth..."
				return 'supplies'
