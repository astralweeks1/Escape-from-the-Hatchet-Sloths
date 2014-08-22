from sys import exit

class Scene(object):

	def enter(self):
		"""What I put here doesn't matter because this is just a base class. 
		Subsequent scenes will inherit from this class. Rather pointlessly 
		actually because their enter() methods will just override this one."""
		
class Death(Scene):
	def enter(self):
		print "You are dead. There's nothing else. Go home, kid."
		exit(1)		

class Bedroom(Scene):
	
	def enter(self):
		print "You wake in your bedroom. Daylight streams in through your" 
		print "window and there is a KNOCK KNOCK KNOCK sound at your door." 
		print "Open the door to find a Hatchet Sloth staring you down. Like"
		print "all Hatchet Sloths, this Hatchet Sloth has hatchets for hands." 
		print "Also he hates everything that is true and beautiful." 
		print "His hatchet hands are poised and readyto TAKE YOU DOWN. Do you:"
		print """
			  SPARTA KICK
			  or 
			  RUN
			  or
			  DO NOTHING"""
		
		a = raw_input(">> ")
		action = a.lower().split(' ')

		for word in action:
			if word == 'sparta' or word == 'kick':
				print "You sparta kick the slow-moving hatchet sloth right in" 
				print "his hateful chest. \n IT'S SUPER EFFECTIVE!!!!!!!!!!"
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
				print "Expire. Coincidentally, this is also when your roommate"
				print "arrives home from work."
				return 'death'
			
			else:
				print "OK, let's try this again. We have time. Luckily you"
				print "are battling a sloth..."
				return 'home'
		
	
class Cheap_Charlies(Scene):
	
	def enter(self):
		print "You pop next door into Cheap Charlie's to pick up supplies. Clearly"
		print "the long prophesied Hatchet Sloth Apocalypse is at hand and you"
		print "need to be prepared. You study the crap-filled shelf in front of"
		print "you and try to think what would be an effective weapon against"
		print "an army of Hatchet Sloths.\nA vacuum cleaner?\n No." 
		print "A melon baller?\n No.\nA floral-patterned sun dress? \n No."
		print "A Hatchet Sloth? \n N- ARHSLKDA;XKLKJFS HOLY FUCK A HATCHET SLOTH!!!" 
		print "!!!!!!111!!!!11!!!!1!!!"
		print "What will you use to fend it off????"
		print "\n VACUUM CLEANER \n or \n MELON BALLER \n or" 
		print " FLORAL-PATTERNED SUN DRESS"
		
		a = raw_input(">> ")
		action = a.lower().split(' ')

		for word in action:

			if word == 'vacuum' or word == 'cleaner':
				print "You aim the vacuum cleaner at the hatchet sloth's eyes which"
				print "seem to jiggle in their sockets for a moment before POPPING out"
				print "of the sloths face."
				print "You drop the vacuum, aiming to make your escape, but the empty"
				print "eye sockets of the Hatchet Sloth have a hypnotic power over you."
				print "Try as you might, you can't look away. You are rooted to the spot."
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
				print "Quick as a flash you don the floral-patterned sun dress and"
				print "like Bugs Bunny seducing easy mark, Elmer Fudd, you charm"
				print "the Hatchet Sloth with such niceties the likes of which he has"
				print "never been paid. His genitals quiver in anticipation. Then, before"
				print "the Hatchet Sloth has time to blink his eyes or lick his lips"
				print "you stride out the door of the shop. A proud, confident woman."
				print "Because you are gone, you do not see the single tear which rolls"
				print "fat and slow down the Hatchet Sloth's hateful face."
				return 'food'
				
			else:
				print "OK, let's try this again. We have time. Luckily you"
				print "are battling a sloth..."
				return 'supplies'
		
class Peter_Pan(Scene):
	
	def enter(self):
		print "Dressed to the nines in your floral-patterned sun dress, you"
		print "gambol across the street to Peter Pan Bakery where you can be"
		print "damned sure you'll find some cream-filled delights for your"
		print "stockpile. You walk in with manly, Kate Moss confidence only to spy"
		print "a vile Hatchet Sloth behind the counter. Its hatchet hands cast"
		print "a terrible shadow across the neck of a fair Polish maiden."
		print "Do you:\nRUN AWAY\n or\nSEX UP THE SLOTH\n???"
		
		a = raw_input(">>> ")
		action = a.lower().split(' ')

		for word in action:

			if word == 'run' or word == 'away':
				print "Great job. You outran a sloth."
				return 'safe_house'
			
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
				print "OK, let's try this again. We have time. Luckily you"
				print "are battling a sloth..."
				return 'food'
	
class McCarren_Rec(Scene):
	
	def enter(self):
		print "You make your way down Manhattan Ave to McCarren Park. There"
		print "is the familiar scent of bread being baked by hairy-knuckled"
		print "Polish men and it recalls the calm of home. Everything is going"
		print "to be okay. You cut down past the play area and chance to see"
		print "a peculiar looking child on a swing. This child has large black"
		print "eyes and a longish snout and-- could it be?-- hatchets for hands."
		print "HATCHETS FOR HANDS????????????????"
		print "Do you approach the swinging sloth and\nBUST NUTS\nor"
		print "SURRENDER"
		
		a = raw_input(">> ")
		action = a.lower().split(' ')

		for word in action:
		
			if word == 'bust' or word == 'nuts':
				print "You jet over to the swinging Hatchet Sloth and launch a"
				print "flying double kick to its hateful chest. IT'S SUPER"
				print "EFFECTIVE!!!!111!!! Its chest collapses and it is left"
				print "sucking wind like a pathetic sucker. HA HA HA HA HA HA HA."
				print "That's when you look up: MY GOD."
				print "There are Hatchet Sloths everywhere. On the"
				print "see-saw, on the slide, in the sandbox. They are not quite so"
				print "terrible after all. But now you've gone and murdered one. What"
				print "is your fucking problem, dude? Seriously. You grab the dying"
				print "Hatchet Sloth's hatchet hand and use it to SEPPUKUUUUUUUU"
				return 'death'
				
			elif word == 'surrender':
				print "You give in to the mighty will of the Hatchet Sloth and"
				print "saunter over to accept your fate. That's when you realize"
				print "there are Hatchet Sloths all over the playground. On the"
				print "swings, on the slides, in the sandbox. They are laughing."
				print "Slowly, sure, but they are laughing. And they are not so"
				print "terrible as you might have thought at first. Yes, the hateful"
				print "Hatchet Sloth isn't as hateful or as fearsome as once thought."
				print "You resign to live together, intermarry, and in time, your"
				print "differences will be forgotten. THE END."
				exit(1)

			else:
				print "OK, let's try this again. We have time. Luckily you"
				print "are battling a sloth..."
				return 'safe_house'

class Engine(object):
		
	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		
		while True:
			print "\n------------------------------------------------" 
			new_scene = current_scene.enter()
			current_scene = self.scene_map.next_scene(new_scene)
			
				
class Map(object):
	scenes = {'home': Bedroom(),
	'supplies': Cheap_Charlies(),
	'food': Peter_Pan(),
	'safe_house': McCarren_Rec(),
	'death': Death()
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
	
	def next_scene(self, scene_name):		
		return Map.scenes.get(scene_name)
		
	def opening_scene(self):	
		return self.next_scene(self.start_scene)


a_map = Map('home')
a_game = Engine(a_map)
a_game.play()		
