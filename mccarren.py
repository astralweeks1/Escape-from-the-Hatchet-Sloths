import word_chopper

def enter():
		print "You hustle across the street to McCarren Park. There"
		print "is the familiar scent of bread being baked by hairy-knuckled"
		print "Polish men and it recalls the calm of home. Maybe everything will"
		print "be okay. You jog down past the play area and chance to see"
		print "a peculiar looking child on a swing. This child has large black"
		print "eyes and a longish snout and-- could it be?-- hatchets for hands."
		print "HATCHETS FOR HANDS????????????????"
		print "Do you approach the swinging sloth and\nBUST NUTS\nor"
		print "SURRENDER\n???"
		
		action = word_chopper.chop()

		for word in action:
		
			if word == 'bust' or word == 'nuts':
				print "You jet over to the swinging Hatchet Sloth and launch a"
				print "flying double kick to its hateful chest. IT'S SUPER"
				print "EFFECTIVE!!!!111!!! Its chest collapses and it is left"
				print "sucking wind like a pathetic sucker. HA HA HA HA HA HA HA."
				print "That's when you look up: MY GOD. There are Hatchet Sloths" 
				print "everywhere. On the see-saw, on the slide, in the sandbox." 
				print "They are not quite so terrible after all. But now you've" 
				print "gone and murdered one. What is your problem, dude?"
				print "Seriously. You grab the dying Hatchet Sloth's hatchet and" 
				print "use it to \n\nSEPPUKUUUUUUUUUU"
				return 'death'
				
			elif word == 'surrender':
				print "You give in to the mighty will of the Hatchet Sloth and"
				print "saunter over to accept your fate. That's when you realize"
				print "there are Hatchet Sloths all over the playground. On the"
				print "swings, on the slides, in the sandbox. They are laughing."
				print "Slowly, sure, but they are laughing. And they are not so"
				print "terrible as you might have thought at first. Yes, the hateful"
				print "Hatchet Sloth isn't as hateful or as fearsome as you'd presumed."
				print "You resign to live together, intermarry. In time, your"
				print "differences will be forgotten. THE END."
				exit(1)

			else:
				print "OK, let's try this again. Luckily you are battling sloths"
				print "and there is plenty of time..."
				return 'safe_house'
