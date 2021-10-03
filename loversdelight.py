import time

def whereto():
	x = input("> ").lower()
	if "north" in x:
		return "north"
	elif "south" in x:
		return "south"
	elif "east" in x:
		return "east"
	elif "west" in x:
		return "west"
	elif "securepswd" in x:
		print("You have decided to quit the game. Goodbye.\n\nGAME OVER.")
		exit()
	elif "help" in x:
		return "help"
	elif "location" in x:
		return "location"
	elif "turns" in x:
		return "turns"
	else:
		print("Please enter in a valid command.")
		return "bad"

def start():
	print("Welcome to Lover's Delight!")
	print("This is a story about running errands for your significant other.")
	rounds()

def help():
	print("The valid commands are:\n\tnorth\n\tsouth\n\teast\n\twest\n\tlocation\n\tturns\n\thelp")

def round1():
	print("Your Partner: Hey can you pick up some milk from the Grocery Store? I need some more for my strawberry jam. And I need the milk within 3 turns!")
	print("You: Only because I love you! Be back in a jiffy...")
	turncount = 3
	level = 1
	locations = ["grocery"]
	roundcount = 1
	spawn(turncount, level, roundcount, locations)

def round2():
	turncount = 7
	level = 2
	locations = ["school", "bank"]
	roundcount = 2
	spawn(turncount, level, roundcount, locations)

def spawn(turncount, level, roundcount, locations):
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	print("Spawn")
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are at Spawn.")
		elif "north" in x:
			turncount -= 1
			open_park(turncount, level, roundcount, locations)
		elif "south" in x:
			if level >= 3:
				print("no")
				#turncount -= 1
				#insert location here
			else:
				print("You have not unlocked this part of the map!")
		elif "east" in x:
			if level >= 2:
				print("You are attempting to go on a One Way Road, but it is heading West.")
			else:
				print("You have not unlocked this part of the map!")
		elif "west" in x:
			if level >= 2:
				turncount -= 1
				school(turncount, level, roundcount, locations)
			else:
				print("You have not unlocked this part of the map!")
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns at Spawn.\n\nGAME OVER.")
	exit()

def open_park(turncount, level, roundcount, locations):
	if "open_park" in locations:
		locations.remove("open_park")
		print("You have made it to the Open Park!")
	else:
		print("Open Park")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are in an Open Park.")
		elif "north" in x:
			turncount -= 1
			bank(turncount, level, roundcount, locations)
		elif "south" in x:
			turncount -= 1
			spawn(turncount, level, roundcount, locations)
		elif "east" in x:
			if level >= 2:
				turncount -= 1
				closed_park(turncount, level, roundcount, locations)
			else:
				print("You have not unlocked this part of the map!")
		elif "west" in x:
			print("You are trying to enter a construction site, but you have been told to turn around.")
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue	
	if turncount < 0:
		return
	print("You ran out of turns at the Open Park.\n\nGAME OVER.")
	exit()

def bank(turncount, level, roundcount, locations):
	if "bank" in locations:
		locations.remove("bank")
		print("You have made it to the Bank!")
	else:
		print("Bank")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are at the Bank.")
		elif "north" in x:
			if level >= 3:	
				print("no")
				#turncount -= 1
				#insert location here
		elif "south" in x:
			turncount -= 1
			open_park(turncount, level, roundcount, locations)
		elif "east" in x:
			turncount -= 1
			grocery(turncount, level, roundcount, locations)
		elif "west" in x:
			turncount -= 1
			road1(turncount, level, roundcount, locations)
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns at the Bank.\n\nGAME OVER.")
	exit()

def road1(turncount, level, roundcount, locations):
	if "road1" in locations:
		locations.remove("road1")
	else:
		print("Road")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are on a Road. How exciting.")
		elif "north" in x:
			if level >= 3:	
				print("no")
				#turncount -= 1
				#insert location here
		elif "south" in x:
			print("You are trying to enter a construction site, but you have been told to turn around.")
		elif "east" in x:
			turncount -= 1
			bank(turncount, level, roundcount, locations)
		elif "west" in x:
			if level >= 3:
				print("no")
				#turncount -= 1
				#insert location here
			else:
				print("You have not unlocked this part of the map yet!")
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns on the Road.\n\nGAME OVER.")
	exit()

def grocery(turncount, level, roundcount, locations):
	if "grocery" in locations:
		locations.remove("grocery")
		print("You made it to the Grocery Store!")
	else:
		print("Grocery Store")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are at the Grocery Store.")
		elif "north" in x:
			if level >= 3:	
				print("no")
				#turncount -= 1
				#insert location here
		elif "south" in x:
			if level >= 2:
				turncount -= 1
				closed_park(turncount, level, roundcount, locations)
			else:
				print("You have not unlocked this part of the map yet!")
		elif "east" in x:
			if level >= 3:
				print("no")
				#turncount -= 1
				#insert location here
			else:
				print("You have not unlocked this part of the map yet!")
		elif "west" in x:
			turncount -= 1
			bank(turncount, level, roundcount, locations)
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns at the Grocery Store.\n\nGAME OVER.")
	exit()

def school(turncount, level, roundcount, locations):
	if "school" in locations:
		locations.remove("school")
		print("You made it to the School!")
	else:
		print("School")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are at the School.")
		elif "north" in x:
			print("You are trying to enter a construction site, but you have been told to turn around.")
		elif "south" in x:
			if level >= 3:
				print("no")
				# turncount -= 1
				#insert location here
			else:
				print("You have not unlocked this part of the map!")
		elif "east" in x:
			turncount -= 1
			spawn(turncount, level, roundcount, locations)
		elif "west" in x:
			if level >= 3:
				print("no")
				#turncount -= 1
				#insert location here
			else:
				print("You have not unlocked this part of the map!")
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns at the School.\n\nGAME OVER.")
	exit()

def closed_park(turncount, level, roundcount, locations):
	if "closed_park" in locations:
		locations.remove("closed_park")
		print("You made it to the Closed Park!")
	else:
		print("Closed Park")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are at the Closed Park.")
		elif "north" in x:
			turncount -= 1
			grocery(turncount, level, roundcount, locations)
		elif "south" in x:
			print("You are turning onto a One Way Road going West.")
			turncount -=1
			owr_w(turncount, level, roundcount, locations)
		elif "east" in x:
			if level >= 3:
				print("no")
				#turncount -= 1
				#insert location here
			else:
				print("You have not unlocked this part of the map yet!")
		elif "west" in x:
			turncount -= 1
			open_park(turncount, level, roundcount, locations)
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns at the Closed Park.\n\nGAME OVER.")
	exit()

def owr_w(turncount, level, roundcount, locations):
	print("One Way Road heading West")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are on a One Way Road heading West.")
		elif "north" in x:
			print("You cannot go North on a One Way Road heading West.")
		elif "south" in x:
			print("You cannot go North on a One Way Road heading West.")
		elif "east" in x:
			print("You cannot go North on a One Way Road heading West.")
		elif "west" in x:
			turncount -= 1
			spawn(turncount, level, roundcount, locations)
		elif "help" in x:
			print(help())
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns on a One Way Road heading West.\n\nGAME OVER.")
	exit()

def rounds(roundcount=1):
	if roundcount == 1:
		round1()
	elif roundcount == 2:
		print("Your Partner: Sweet thanks! This strawberry jam is looking milkier than ever!")
		time.sleep(1)
		print(".")
		time.sleep(1)
		print(".")
		time.sleep(1)
		print(".")
		time.sleep(1)
		print("Your Partner: Oh hey babe? Do you think you could run some more errands for me? I need some money from the Bank, and can you pick up some paperwork from the School? This is really urgent, so I need this stuff within 8 turns.")
		print("You: Sure! I'm a little tired, but anything for you.")
		print("Your Partner: Thank you! You're a real life saver, you know?")
		print("You: That's what you always say...")
		round2()
	elif roundcount == 3:
	 	print("You have beaten everything that has currently been implemented!\n\nGAME OVER.")
	 	exit()
	# 	#round3()
	# else:
	# 	#winnerwinnerchickendinner()

def roundOver(locations):
	return len(locations) == 0

start()