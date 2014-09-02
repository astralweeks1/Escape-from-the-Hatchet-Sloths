import word_chopper

def enter():
		print "You wake in your bedroom. Daylight streams in through your" 
		print "window and there is a KNOCK KNOCK KNOCK sound at your door." 
		print "Open the door to find a Hatchet Sloth staring you down. Like"
		print "all Hatchet Sloths, this Hatchet Sloth has hatchets for hands." 
		print "Also he hates everything that is true and beautiful." 
		print "His hatchet hands are poised and ready to TAKE YOU DOWN. Do you:"
		print "SPARTA KICK\nor\nRUN\nor\nDO NOTHING\n???"
		
		action = word_chopper.chop()

		for word in action:

			if word == 'sparta' or word == 'kick':
				print "\n\nYou sparta kick the slow-moving hatchet sloth right in" 
				print "his hateful chest.\nIT'S SUPER EFFECTIVE!!!!111!!!!"
				print "you mutter something crass about its mother being a tool"
				print "shed before slipping out the door and down the stairs."
				print "As the door clicks shut you mutter, 'Goodbye 700 Manhattan" 
				print "Ave, Apt. 2!'"
				return 'supplies'
		
			elif word == 'run':
				print "Yes, ok, fine. You can outrun a fucking sloth with fucking"
				print "hatchet for hands. Good for you."
				print "You slip out the door and down the stairs."
				print "As the door clicks shut you mutter, 'Goodbye 700 Manhattan" 
				print "Ave, Apt. 2!'"
				return 'supplies'
			
			elif word == 'do' or word == 'nothing':
				print "You have seen something on the Discovery Channel about"
				print "sloths' vision being based on motion. You decide to use"
				print "this information, praying to God that Hatchet Sloths'" 
				print "vision works similarly to hatchetless sloths. You wait" 
				print "hours, not daring to move a muscle. Eventually the" 
				print "Hatchet Sloth's hatchet comes to rest upon your cranium." 
				print "A mere eight hours hence, the sloth's hatchet has sawed"
				print "through your skull and severed enough brain tissue that,"
				print "mercifully, you lose consciousness. You are not actually" 
				print "dead, however. That doesn't happen for another five hours"
				print "at which point you unceremoniously release your bowels and"
				print "expire. Coincidentally, this is also when your roommate"
				print "arrives home from work."
				return 'death'
			
			else:
				print "OK, let's try this again. We have time. Luckily you"
				print "are battling a sloth..."
				return 'home'
