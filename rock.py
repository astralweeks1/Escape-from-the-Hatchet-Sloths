import random

moves = ['rock', 'paper', 'scissors']

def players_throw():
		throw = 0
		while throw == 0:		
			print "\nROCK, PAPER, SCISSORS"
			a = raw_input("SHOOT!!\n>> ")
			action = str(a.lower())
			if action in moves:
				throw = moves.index(action) 
				return throw
			else:
				print "TRY AGAIN!"

def compare_throws(throw): 
		x = random.randint(0,2)
		sloth_throw = moves[x]
		print "\nThe Hatchet Sloth throws %s with great manual dexterity!!" % sloth_throw
		diff = throw - x
		if diff == 0:
			print "You both threw %s!" % sloth_throw
			print "Go again!"
			return 0
		if diff == -1 or diff == 2:
			return -1
		if diff == 1 or diff == -2:
			return 1	

def enter():
		print "Out on the street there is no one around for miles. It is"
		print "possible that you are among the last humans alive on earth."
		print "The awesome labor or repopulating the human race weighs"
		print "heavy on your mind. You think of the hundreds, thousands,"
		print "even millions who will spring forth from your loins, carrying"
		print "your genes. You are suddenly very self conscious about your"
		print "backne. A tumbleweed rolls down Manhattan Ave, interrupting"
		print "your thoughts. You look up to spy a Hatchet Sloth looming" 
		print "large, blocking your path. His right-hand hatchet is raised"
		print "as if to say 'DO YA FEEL LUCKY, PUNK?' And you know" 
		print "instinctively what you must do. You must beat the Hatchet"
		print "Sloth in Rock, Paper, Scissors."
		while True:
			a = raw_input("\n\n\nDo you accept???\n>> ")
			action = a.lower()
			if action == 'yes':
				break
		print "\nFANTASTIC!!!!\n"
		print "The Hatchet Sloth nods its head along as you shout"
		check = 0
		while check == 0:
			throw = players_throw()
			check = compare_throws(throw)
		if check > 0:
			print "You have beaten the hateful Hatchet Sloth. You let him know"
			print "in no uncertain terms exactly how you feel about him and"
			print "the horse he rode into town on. He hangs his head in shame." 
			print "Then a powerful hunger sets in."
			return 'food'
		else:
			print "YOU LOSE!!!!1111!11"
			print "Abiding by the unwritten contract for apocalyptic Rock,"
			print "Paper, Scissors games, you bow your head in surrender and"
			print "allow the Hatchet Sloth to bite your throat and slake its" 
			print "terrible thirst on your hot, spurting blood."
			return 'death'

enter()
