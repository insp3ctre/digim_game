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
	print("\nThe valid commands are:\n\tnorth\n\tsouth\n\teast\n\twest\n\tlocation\n\tturns\n\thelp\n")
	rounds()

def help():
	print("The valid commands are:\n\tnorth\n\tsouth\n\teast\n\twest\n\tlocation\n\tturns\n\thelp")

def round1():
	print("Your Partner: Hey can you pick up some milk from the Grocery Store? I need some more for my strawberry jam. And I need the milk within 3 turns!")
	time.sleep(2)
	print("You: Only because I love you! Be back in a jiffy...\n")
	time.sleep(1)
	turncount = 3
	level = 1
	locations = ["grocery"]
	roundcount = 1
	spawn(turncount, level, roundcount, locations)

def round2():
	print("Your Partner: Sweet thanks! This strawberry jam is looking milkier than ever!")
	time.sleep(1)
	print(".")
	time.sleep(1)
	print(".")
	time.sleep(1)
	print(".")
	time.sleep(1)
	print("Your Partner: Oh hey babe? Do you think you could run some more errands for me? I need some money from the Bank, and can you pick up some paperwork from the School? This is really urgent, so I need this stuff within 8 turns.")
	time.sleep(6)
	print("You: Sure! I'm a little tired, but anything for you.")
	time.sleep(2)
	print("Your Partner: Thank you! You're a real life saver, you know?")
	time.sleep(2)
	print("You: That's what you always say...\n")
	time.sleep(2)
	turncount = 7
	level = 2
	locations = ["school", "bank"]
	roundcount = 2
	spawn(turncount, level, roundcount, locations)

def round3():
	print("Round 3. 17 turns.")
	turncount = 100
	level = 3
	locations = ["magic", "statue", "mall", "bank"]
	roundcount = 3
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
				print("There is no ramp onto the Highway here.")
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
			if level >= 2:
				print("You are trying to enter a construction site, but you have been told to turn around.")
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
				print("You are trying to go into Clayton Ravine. You would need a train to be able to fall into here...")
			else:
				print("You have not unlocked this part of the map yet!")
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
				turncount -= 1
				road2(turncount, level, roundcount, locations)
			else:
				print("You have not unlocked this part of the map yet!")
		elif "south" in x:
			if level >= 2:
				print("You are trying to enter a construction site, but you have been told to turn around.")
			else:
				print("You have not unlocked this part of the map yet!")
		elif "east" in x:
			turncount -= 1
			bank(turncount, level, roundcount, locations)
		elif "west" in x:
			if level >= 3:
				print("You are trying to enter a construction site, but you have been told to turn around.")
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
				turncount -= 1
				magic(turncount, level, roundcount, locations)
			else:
				print("You have not unlocked this part of the map yet!")
		elif "south" in x:
			if level >= 2:
				turncount -= 1
				closed_park(turncount, level, roundcount, locations)
			else:
				print("You have not unlocked this part of the map yet!")
		elif "east" in x:
			if level >= 3:
				turncount -= 1
				road4(turncount, level, roundcount, locations)
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
				print("There is no ramp onto the Highway here.")
			else:
				print("You have not unlocked this part of the map!")
		elif "east" in x:
			turncount -= 1
			spawn(turncount, level, roundcount, locations)
		elif "west" in x:
			if level >= 3:
				turncount -= 1
				statue(turncount, level, roundcount, locations)
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
			turncount -=1
			owr_w(turncount, level, roundcount, locations)
		elif "east" in x:
			if level >= 3:
				turncount -= 1
				estates(turncount, level, roundcount, locations)
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
			print("You cannot go South on a One Way Road heading West.")
		elif "east" in x:
			print("You cannot go East on a One Way Road heading West.")
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

def road2(turncount, level, roundcount, locations):
	print("Road")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are on a Road. Thrilling.")
		elif "north" in x:
			if level >= 4:
				print("no")
				# turncount -= 1
				# #insert location here
			else:
				print("You have not unlocked this part of the map yet!")
		elif "south" in x:
			turncount -=1
			road1(turncount, level, roundcount, locations)
		elif "east" in x:
			print("You are trying to go into Clayton Ravine. You would need a train to be able to fall into here...")
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
	print("You ran out of turns on a Road. Such a sad way to go.\n\nGAME OVER.")
	exit()

def owr_e(turncount, level, roundcount, locations):
	print("One Way Road heading East")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are on a One Way Road heading East.")
		elif "north" in x:
			print("You cannot go North on a One Way Road heading East.")
		elif "south" in x:
			print("You cannot go South on a One Way Road heading East.")
		elif "east" in x:
			if level >= 4:
				print("no")
				# turncount -= 1
				# #insert location here
			else:
				print("You: *on phone* So awkward situation. I'm soft locked.")
				time.sleep(2)
				print("Your Partner: You're what?")
				time.sleep(2)
				print("You: Soft locked. I can't go anywhere. I'm on a One Way Road heading East, but there is no East.")
				time.sleep(3)
				print("Your Partner: Explain this like I'm five.")
				time.sleep(2)
				print("You: I cannot progress further without restarting. Hasta la vista, baby.\n\nGAME OVER.")
				exit()
		elif "west" in x:
			print("You cannot go West on a One Way Road heading East.")
		elif "help" in x:
			print(help())
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns on a One Way Road heading East.\n\nGAME OVER.")
	exit()

def highway1(turncount, level, roundcount, locations):
	print("Highway")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("Life is a Highway. You're gonna ride it all game long.")
		elif "north" in x:
			print("There is no exit here.")
		elif "south" in x:
			print("There is no exit here.")
		elif "east" in x:
			turncount -= 1
			highway2(turncount, level, roundcount, locations)
		elif "west" in x:
			turncount -= 1
			road3(turncount, level, roundcount, locations)
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns on a Highway. You are now a Highway Dweller.\n\nGAME OVER.")
	exit()

def highway2(turncount, level, roundcount, locations):
	print("Highway")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("Life is a Highway. You're gonna ride it all game long.")
		elif "north" in x:
			print("There is no exit here.")
		elif "south" in x:
			print("There is no exit here.")
		elif "east" in x:
			turncount -= 1
			highway3(turncount, level, roundcount, locations)
		elif "west" in x:
			turncount -= 1
			highway1(turncount, level, roundcount, locations)
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns on a Highway. You are now a Highway Dweller.\n\nGAME OVER.")
	exit()

def highway3(turncount, level, roundcount, locations):
	print("Highway")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("Life is a Highway. You're gonna ride it all game long.")
		elif "north" in x:
			print("There is no exit here.")
		elif "south" in x:
			print("There is no exit here.")
		elif "east" in x:
			turncount -= 1
			mall(turncount, level, roundcount, locations)
		elif "west" in x:
			turncount -= 1
			highway2(turncount, level, roundcount, locations)
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns on a Highway. You are now a Highway Dweller.\n\nGAME OVER.")
	exit()

def beach1(turncount, level, roundcount, locations):
	if "beach1" in locations:
		locations.remove("beach1")
		print("You made it to the correct part of the Beach!")
	else:
		print("Amity Beach")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are at Amity Be- OH MY GOSH YOU SEE A SHARK!?!?")
		elif "north" in x:
			if level >= 4:
				turncount -= 1
				ocean1(turncount, level, roundcount, locations)
			else:
				print("You have not unlocked this part of the map yet!")
		elif "south" in x:
			turncount -= 1
			road4(turncount, level, roundcount, locations)
		elif "east" in x:
			if level >= 4:
				print("no")
				# turncount -= 1
				# highway2(turncount, level, roundcount, locations)
			else:
				print("You have not unlocked this part of the may yet!")
		elif "west" in x:
			turncount -= 1
			magic(turncount, level, roundcount, locations)
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns at the Beach. At least it's sunny out.\n\nGAME OVER.")
	exit()

def mall(turncount, level, roundcount, locations):
	if "mall" in locations:
		locations.remove("mall")
		print("You made it to the Mall!")
	else:
		print("Twin Pines Mall")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("Malls? Where you're going, you don't need Malls.")
		elif "north" in x:
			turncount -= 1
			owr_e(turncount, level, roundcount, locations)
		elif "south" in x:
			if level >= 4:
				print("no")
				# turncount -= 1
				# #insert location here
			else:
				print("You have not unlocked this part of the map yet!")
		elif "east" in x:
			if level >= 4:
				print("no")
				# turncount -= 1
				# #insert location here
			else:
				print("You have not unlocked this part of the may yet!")
		elif "west" in x:
			turncount -= 1
			highway3(turncount, level, roundcount, locations)
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns at Twin Pines Mall. If only you had a way to go back in time...\n\nGAME OVER.")
	exit()

def estates(turncount, level, roundcount, locations):
	if "estates" in locations:
		locations.remove("estates")
		print("You made it to Lyon Estates!")
	else:
		print("Lyon Estates")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("Lyon Estates? You think this is heavy.")
		elif "north" in x:
			turncount -= 1
			road4(turncount, level, roundcount, locations)
		elif "south" in x:
			turncount -= 1
			owr_e(turncount, level, roundcount, locations)
		elif "east" in x:
			if level >= 4:
				print("no")
				# turncount -= 1
				# #insert location here
			else:
				print("You have not unlocked this part of the map yet!")
		elif "west" in x:
			turncount -= 1
			closed_park(turncount, level, roundcount, locations)
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns at the Lyon Estates. At least you were able to see your future home.\n\nGAME OVER.")
	exit()

def magic(turncount, level, roundcount, locations):
	if "magic" in locations:
		locations.remove("magic")
		print("You made it to the Magic Fountain!")
	else:
		print("Magic Fountain")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are at a Magic Fountain. Or at least you have heard it is magical.")
		elif "north" in x:
			if level >= 4:
				print("no")
				# turncount -= 1
				# #insert location here
			else:
				print("You have not unlocked this part of the map yet!")
		elif "south" in x:
			turncoung -= 1
			grocery(turncount, level, roundcount, locations)
		elif "east" in x:
			turncount -= 1
			beach1(turncount, level, roundcount, locations)
		elif "west" in x:
			print("You are trying to go into Clayton Ravine. You would need a train to be able to fall into here...")
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns at the Magic Fountain. You wish for another life, but you are promptly hit by a falling coconut, struck by lightning, eaten by a shark, and then the shark is crushed by a vending machine.\n\nGAME OVER.")
	exit()

def statue(turncount, level, roundcount, locations):
	if "statue" in locations:
		locations.remove("statue")
		print("You made it to the Greatest American Hero Statue!")
	else:
		print("Greatest American Hero Statue")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("Believe it or not you're walking on air. You never thought you could feel so free at the Greatest American Hero Statue.")
		elif "north" in x:
			print("You are trying to enter a construction site, but you have been told to turn around.")
		elif "south" in x:
			turncount -= 1
			road3(turncount, level, roundcount, locations)
		elif "east" in x:
			turncount -= 1
			school(turncount, level, roundcount, locations)
		elif "west" in x:
			if level >= 4:
				print("no")
				# turncount -= 1
				# #insert location here
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
	print("You ran out of turns at the Greatest American Hero Statue. You did not watch enough of this show, so you do not know how you lost.\n\nGAME OVER.")
	exit()

def road3(turncount, level, roundcount, locations):
	if "road3" in locations:
		locations.remove("road3")
		print("You made it to the Road?")
	else:
		print("Road")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are on a Road. Daring today, aren't you?")
		elif "north" in x:
			turncount -= 1
			statue(turncount, level, roundcount, locations)
		elif "south" in x:
			if level >= 4:
				print("no")
				# turncoung -= 1
				# #insert location here
			else:
				print("You have not unlocked this part of the map yet!")
		elif "east" in x:
			turncount -= 1
			highway1(turncount, level, roundcount, locations)
		elif "west" in x:
			if level >= 4:
				print("no")
				# turncount -= 1
				# #insert location here
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
	print("You ran out of turns on a Road. Such a sad way to go.\n\nGAME OVER.")
	exit()

def road4(turncount, level, roundcount, locations):
	if "road4" in locations:
		locations.remove("road4")
		print("You made it to the Road?")
	else:
		print("Road")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are on a Road. You must really like roads.")
		elif "north" in x:
			turncount -= 1
			beach1(turncount, level, roundcount, locations)
		elif "south" in x:
			turncount -= 1
			estates(turncount, level, roundcount, locations)
		elif "east" in x:
			if level >= 4:
				print("no")
				# turncount -= 1
				# #insert location here
			else:
				print("You have not unlocked this part of the map yet!")
		elif "west" in x:
			turncount -= 1
			grocery(turncount, level, roundcount, locations)
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns on a Road. Such a sad way to go.\n\nGAME OVER.")
	exit()

# def ocean1(turncount, level, roundcount, locations):

# def ocean2(turncount, level, roundcount, locations):

# def rock(turncount, level, roundcount, locations):

# def beach2(turncount, level, roundcount, locations):

# def beach3(turncount, level, roundcount, locations):

def rounds(roundcount=1):
	if roundcount == 1:
		round1()
	elif roundcount == 2:
		round2()
	elif roundcount == 3:
		round3()
	else:
	 	winnerwinnerchickendinner()

def roundOver(locations):
	return len(locations) == 0

def winnerwinnerchickendinner():
	print("Huzah! You win.\n\nGAME OVER.")
	exit()

start()