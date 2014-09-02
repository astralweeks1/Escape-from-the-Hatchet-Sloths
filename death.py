from sys import exit
import word_chopper

def enter():
		print "You are dead. Years from now, long after your body has"
		print "returned to earth, Hatchet Sloths will inhabit all the places"
		print "you once loved. They will be do all the things you loved to do"
		print "Worst of all: they will have no knowledge that you ever even"
		print "existed.\n\nFIN\n\n(exeunt)\n"
		print "WANNA PLAY AGAIN???"

		action = word_chopper.chop()

		for word in action:
			if word == 'yes':
				return 'home'
			else:
				exit(1)
