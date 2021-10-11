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
	elif "iamaquitter" in x:
		print("You have decided to quit the game. Goodbye.\n\nGAME OVER.")
		exit()
	elif "help" in x:
		return "help"
	elif "location" in x:
		return "location"
	elif "turns" in x:
		return "turns"
	elif "cheatingcheatusingcheats" in x:
		print("You are a cheating cheat using cheats. You are now on round 4.")
		round4()
	else:
		print("Please enter in a valid command.")
		return "bad"

def start():
	print("Welcome to Lover's Delight!")
	print("This is a story about running errands for your significant other.")
	print("\nYou may only enter a command when '>' is present.")
	print("\nThe valid commands are:\n\tnorth\n\tsouth\n\teast\n\twest\n\tlocation - displays useful information about your current location\n\tturns - displays how many turns you have left\n\thelp - HELP! YOU NEED SOMEBODY, HELP!")
	print("\tiamaquitter - ???\n")
	time.sleep(5)
	print("\nP.S: You are expected to lose.\n")
	time.sleep(2)
	rounds()

def help():
	print("\nThe valid commands are:\n\tnorth\n\tsouth\n\teast\n\twest\n\tlocation - displays useful information about your current location\n\tturns - displays how many turns you have left\n\thelp - HELP! YOU NEED SOMEBODY, HELP!")
	print("\tiamaquitter - ???\n")

def round1():
	print("Your Partner: Hey can you pick up some milk from Trader Joe's? I need some more for my strawberry jam. And I need the milk within 3 turns!")
	time.sleep(4)
	print("You: Only because I love you! Be back in a jiffy...\n")
	time.sleep(2)
	turncount = 3
	level = 1
	locations = ["grocery"]
	roundcount = 1
	spawn(turncount, level, roundcount, locations)

def round2():
	print("\nYour Partner: Sweet thanks! This strawberry jam is looking milkier than ever!")
	time.sleep(1)
	print(".")
	time.sleep(1)
	print(".")
	time.sleep(1)
	print(".")
	time.sleep(1)
	print("Your Partner: Oh hey babe? Do you think you could run some more errands for me? I need some money from the Bank, and can you pick up some paperwork from the School? This is really urgent, so I need this stuff within 7 turns.")
	time.sleep(8)
	print("You: Sure! I'm a little tired, but anything for you.")
	time.sleep(4)
	print("Your Partner: Thank you! You're a real life saver, you know?")
	time.sleep(4)
	print("You: That's what you always say...\n")
	time.sleep(2)
	turncount = 7
	level = 2
	locations = ["school", "bank"]
	roundcount = 2
	spawn(turncount, level, roundcount, locations)

def round3():
	print("\nYour Partner: See? this is why you are a real life saver!")
	time.sleep(4)
	print("You: Well yes, but actually no. How many errands can one person have in a single day?")
	time.sleep(5)
	print("Your Partner: I'm a busy person, what can I say?")
	time.sleep(4)
	print("You: No, I am the busy one because I am the one actually going out and doing things and stuffs.")
	time.sleep(5)
	print("Your Partner: Don't worry I don't have any more errands I need you to run. Why don't you go take some time for yourself? Maybe take a fun outing to that Magic Fountain, then stop by the Statue from one of your favorite TV shows, and then maybe grab some money from the Bank, so you can go shopping at the Twin Pines Mall?")
	time.sleep(12)
	print("You: This sounds like errands but with extra steps. But sure. I'll do it. See you in 18 turns. Time for some me time...\n")
	time.sleep(2)
	turncount = 18
	level = 3
	locations = ["magic", "statue", "mall", "bank"]
	roundcount = 3
	spawn(turncount, level, roundcount, locations)

def round4():
	print("\nYour Partner: Feeling better?")
	time.sleep(4)
	print("You: Yeah. That helped a lot. Thanks.")
	time.sleep(4)
	print("Your Partner: Great! Well now it's boss battle time.")
	time.sleep(4)
	print("You: OH COME ON!")
	time.sleep(3)
	print("Your Partner: Delorean Dealership, Hover Conversion Shop, Yacht Rock, Developer's House, Mirror Room, Arcade, Caesar's Palace, and THE Bar. This is what you get for marrying me. NOW DO MY BIDDING, PEASANT!...")
	turncount = 30
	level = 4
	locations = ["delorean", "hover", "rock", "dev", "mirror", "arcade", "casino", "bar"]
	roundcount = 4
	spawn(turncount, level, roundcount, locations)

def spawn(turncount, level, roundcount, locations):
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	print("Spawn")
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("How much Spawn could a Spawning Spawn Spawn if a Spawning Spawn could Spawn Spawn?")
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
	print("You ran out of turns at Spawn. Pathetic.\n\nGAME OVER.")
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
			print("You are in an Open Park. It is a Park, and it is called Open.")
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
	print("You ran out of turns at the Open Park. Oh well.\n\nGAME OVER.")
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
			print("You are at the Bank. They have money here.")
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
	print("You ran out of turns at the Bank. Maybe you can ask them for a loan.\n\nGAME OVER.")
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
	print("You ran out of turns on a Road. Such a sad way to go.\n\nGAME OVER.")
	exit()

def grocery(turncount, level, roundcount, locations):
	if "grocery" in locations:
		locations.remove("grocery")
		print("You made it to Trader Joe's!")
	else:
		print("Trader Joe's")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are at Trader Joe's. You remember that the developer LOVES Trader Joe's!")
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
	print("You ran out of turns at Trader Joe's. On the bright side, you see lots of great deals!\n\nGAME OVER.")
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
			print("You are at the School. Not just any School, but the School.")
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
	print("You ran out of turns at the School. Go learn something.\n\nGAME OVER.")
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
			print("You are at the Closed Park. It is a Park, and it is called Closed.")
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
	print("You ran out of turns at the Closed Park. Oh well.\n\nGAME OVER.")
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
				turncount -= 1
				endofroad(turncount, level, roundcount, locations)
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
				turncount -= 1
				delorean(turncount, level, roundcount, locations)
			else:
				print("You: *on phone* So awkward situation. I'm soft locked.")
				time.sleep(2)
				print("Your Partner: You're what?")
				time.sleep(2)
				print("You: Soft locked. I can't go anywhere. I'm on a One Way Road heading East, but there is no East.")
				time.sleep(3)
				print("Your Partner: Babe you aren't making any sense right now. Are you okay?")
				time.sleep(3)
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
				turncount -= 1
				ocean2(turncount, level, roundcount, locations)
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
		print("You made it to Twin Pines Mall!")
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
				turncount -= 1
				road8(turncount, level, roundcount, locations)
			else:
				print("You have not unlocked this part of the map yet!")
		elif "east" in x:
			if level >= 4:
				turncount -= 1
				hover(turncount, level, roundcount, locations)
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
				turncount -= 1
				beach4(turncount, level, roundcount, locations)
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
				turncount -= 1
				beach2(turncount, level, roundcount, locations)
			else:
				print("You have not unlocked this part of the map yet!")
		elif "south" in x:
			turncount -= 1
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
				turncount -= 1
				dev(turncount, level, roundcount, locations)
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
				turncount -= 1
				road5(turncount, level, roundcount, locations)
			else:
				print("You have not unlocked this part of the map yet!")
		elif "east" in x:
			turncount -= 1
			highway1(turncount, level, roundcount, locations)
		elif "west" in x:
			if level >= 4:
				turncount -= 1
				flowers(turncount, level, roundcount, locations)
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
				turncount -=1
				beach3(turncount, level, roundcount, locations)
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

def ocean1(turncount, level, roundcount, locations):
	if "ocean1" in locations:
		locations.remove("ocean1")
		print("You made it to the Ocean!")
	else:
		print("Ocean")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are in the Ocean. You only learned now that you knew how to swim.")
		elif "north" in x:
			print("The game does not exist that way!")
		elif "south" in x:
			turncount -= 1
			beach1(turncount, level, roundcount, locations)
		elif "east" in x:
			turncount -= 1
			rock(turncount, level, roundcount, locations)
		elif "west" in x:
			turncount -= 1
			beach2(turncount, level, roundcount, locations)
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns in the Ocean. You are going to have fun drowning.\n\nGAME OVER.")
	exit()

def ocean2(turncount, level, roundcount, locations):
	if "ocean2" in locations:
		locations.remove("ocean2")
		print("You made it to the Ocean!")
	else:
		print("Ocean")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are in the Ocean. Why are you in the Ocean?.")
		elif "north" in x:
			turncount -= 1
			rock(turncount, level, roundcount, locations)
		elif "south" in x:
			turncount -= 1
			beach3(turncount, level, roundcount, locations)
		elif "east" in x:
			print("The game does not exsit that way!")
		elif "west" in x:
			turncount -= 1
			beach1(turncount, level, roundcount, locations)
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns in the Ocean. You are going to have fun drowning.\n\nGAME OVER.")
	exit()

def beach2(turncount, level, roundcount, locations):
	if "beach2" in locations:
		locations.remove("beach2")
		print("You made it to the correct part of the Beach!")
	else:
		print("Ocean Beach")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are at Ocean Beach. No, it is not an ocean. It is a Beach.")
		elif "north" in x:
			print("The game does not exist that way!")
		elif "south" in x:
			turncount -= 1
			magic(turncount, level, roundcount, locations)
		elif "east" in x:
			turncount -= 1
			ocean1(turncount, level, roundcount, locations)
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
	print("You ran out of turns at the Beach. At least it's sunny out.\n\nGAME OVER.")
	exit()

def beach3(turncount, level, roundcount, locations):
	if "beach3" in locations:
		locations.remove("beach3")
		print("You made it to the correct part of the Beach!")
	else:
		print("Lazy Beach")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are at Lazy Beach. The developer of the game gave it this title.")
		elif "north" in x:
			turncount -= 1
			ocean2(turncount, level, roundcount, locations)
		elif "south" in x:
			turncount -= 1
			beach4(turncount, level, roundcount, locations)
		elif "east" in x:
			print("The game does not exist that way!")
		elif "west" in x:
			turncount -= 1
			road4(turncount, level, roundcount, locations)
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

def beach4(turncount, level, roundcount, locations):
	if "beach4" in locations:
		locations.remove("beach4")
		print("You made it to the correct part of the Beach!")
	else:
		print("Lazier Beach")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are at Lazier Beach. The developer of the game gave it this title.")
		elif "north" in x:
			turncount -= 1
			beach3(turncount, level, roundcount, locations)
		elif "south" in x:
			turncount -= 1
			delorean(turncount, level, roundcount, locations)
		elif "east" in x:
			print("The game does not exist that way!")
		elif "west" in x:
			turncount -= 1
			estates(turncount, level, roundcount, locations)
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

def rock(turncount, level, roundcount, locations):
	if "rock" in locations:
		locations.remove("rock")
		print("You made it to the Yacht Rock!")
	else:
		print("Yacht Rock")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are at the Yacht Rock. This is the smoothest rock you have ever seen.")
		elif "north" in x:
			print("The game does not exist that way!")
		elif "south" in x:
			turncount -= 1
			ocean2(turncount, level, roundcount, locations)
		elif "east" in x:
			print("The game does not exist that way!")
		elif "west" in x:
			turncount -= 1
			ocean1(turncount, level, roundcount, locations)
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns at the Yacht Rock. Honestly, you are pretty content with living out the rest of your life with Yacht Rock.\n\nGAME OVER.")
	exit()

def arcade(turncount, level, roundcount, locations):
	if "arcade" in locations:
		locations.remove("arcade")
		print("You made it to the Arcade!")
	else:
		print("Arcade")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are at the Arcade. You are having the time of your life.")
		elif "north" in x:
			print("There is no ramp onto the Highway here.")
		elif "south" in x:
			print("The game does not exist that way!")
		elif "east" in x:
			turncount -= 1
			road7(turncount, level, roundcount, locations)
		elif "west" in x:
			turncount -= 1
			road6(turncount, level, roundcount, locations)
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns at the Arcade. You hear a Pacman death noise before you perish.\n\nGAME OVER.")
	exit()

def endofroad(turncount, level, roundcount, locations):
	if "endofroad" in locations:
		locations.remove("endofroad")
		print("You made it to the End of the Road?")
	else:
		print("End of the Road")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are at the End of the Road. This is where the Road ends. Or something.")
		elif "north" in x:
			print("The game does not exist that way!")
		elif "south" in x:
			turncount -= 1
			road2(turncount, level, roundcount, locations)
		elif "east" in x:
			print("You are trying to go into Clayton Ravine. You would need a train to be able to fall into here...")
		elif "west" in x:
			turncount -= 1
			bar(turncount, level, roundcount, locations)
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns at the End of the Road. That sucks.\n\nGAME OVER.")
	exit()

def bar(turncount, level, roundcount, locations):
	if "bar" in locations:
		locations.remove("bar")
		print("You made it to THE Bar")
	else:
		print("THE Bar")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are on at THE Bar. Not just any Bar, but THE Bar.")
		elif "north" in x:
			print("The game does not exist that way!")
		elif "south" in x:
			turncount -= 1
			devundev(turncount, level, roundcount, locations)
		elif "east" in x:
			print("You are trying to enter a construction site, but you have been told to turn around.")
		elif "west" in x:
			print("The game does not exist that way!")
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns at THE Bar. You decide to drink your sorrows away, and let's just say you drank too much.\n\nGAME OVER.")
	exit()

def casino(turncount, level, roundcount, locations):
	if "casino" in locations:
		locations.remove("casino")
		print("You made it to Caesar's Palace!")
	else:
		print("Caesar's Palace!")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are at Caesar's Palace. You are at a casino. You are about to lose a lot of money.")
		elif "north" in x:
			turncount -= 1
			flowers(turncount, level, roundcount, locations)
		elif "south" in x:
			print("The game does not exist that way!")
		elif "east" in x:
			turncount -= 1
			road5(turncount, level, roundcount, locations)
		elif "west" in x:
			print("The game does not exist that way!")
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns at Caesar's Palace. You discoverd gambler's fallacy.\n\nGAME OVER.")
	exit()

def delorean(turncount, level, roundcount, locations):
	if "delorean" in locations:
		locations.remove("delorean")
		print("You made it to the Delorean Dealership!")
	else:
		print("Delorean Dealership")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are at the Delorean Dealership. You would love to own one someday. In fact, you someday will own one.")
		elif "north" in x:
			turncount -= 1
			beach4(turncount, level, roundcount, locations)
		elif "south" in x:
			turncount -= 1
			hover(turncount, level, roundcount, locations)
		elif "east" in x:
			print("The game does not exist that way!")
		elif "west" in x:
			turncount -= 1
			owr_e(turncount, level, roundcount, locations)
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns at the Delorean Dealership. At least you didn't attempt to sell cocaine.\n\nGAME OVER.")
	exit()

def hover(turncount, level, roundcount, locations):
	if "hover" in locations:
		locations.remove("hover")
		print("You made it to the Hover Conversion Shop!")
	else:
		print("Hover Conversion Shop")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are at the Hover Conversion Shop. You can get a hover conversion on your vehicle in the early 21st century.")
		elif "north" in x:
			turncount -= 1
			delorean(turncount, level, roundcount, locations)
		elif "south" in x:
			print("You run into a wall. When you touch it, it feels like a lazy game developer.")
		elif "east" in x:
			print("The game does not exist that way!")
		elif "west" in x:
			turncount -= 1
			mall(turncount, level, roundcount, locations)
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns at the Hover Conversion Shop. Maybe you can ask for a hover conversion for yourself.\n\nGAME OVER.")
	exit()

def warehouse(turncount, level, roundcount, locations):
	if "warehouse" in locations:
		locations.remove("warehouse")
		print("You made it to the Warehouse?")
	else:
		print("Warehouse")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are at a Warehouse. You don't know, but it is a Warehouse.")
		elif "north" in x:
			turncount -= 1
			devundev(turncount, level, roundcount, locations)
		elif "south" in x:
			turncount -= 1
			mirror(turncount, level, roundcount, locations)
		elif "east" in x:
			print("You are trying to enter a construction site, but you have been told to turn around.")
		elif "west" in x:
			print("The game does not exist that way!")
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns at a Warehouse. Houseware, warehouse.\n\nGAME OVER.")
	exit()

def dev(turncount, level, roundcount, locations):
	if "dev" in locations:
		locations.remove("dev")
		print("You made it to the Developer's House!")
	else:
		print("Developer's House")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are at the Developer's House. You ask him if he can make a better game, but he just smiles and waves.")
		elif "north" in x:
			turncount -= 1
			mirror(turncount, level, roundcount, locations)
		elif "south" in x:
			turncount -= 1
			flowers(turncount, level, roundcount, locations)
		elif "east" in x:
			turncount -= 1
			statue(turncount, level, roundcount, locations)
		elif "west" in x:
			print("The game does not exist that way!")
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns at the Developer's House. This is the laziest house you have ever seen.\n\nGAME OVER.")
	exit()

def road5(turncount, level, roundcount, locations):
	if "road5" in locations:
		locations.remove("road5")
		print("You made it to the Road?")
	else:
		print("Road")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are on a Road. Splendid.")
		elif "north" in x:
			turncount -= 1
			road3(turncount, level, roundcount, locations)
		elif "south" in x:
			print("The game does not exist that way!")
		elif "east" in x:
			turncount -= 1
			road6(turncount, level, roundcount, locations)
		elif "west" in x:
			turncount -= 1
			casino(turncount, level, roundcount, locations)
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

def road6(turncount, level, roundcount, locations):
	if "road6" in locations:
		locations.remove("road6")
		print("You made it to the Road?")
	else:
		print("Road")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are on a Road. Radical.")
		elif "north" in x:
			print("There is no ramp onto the Highway here.")
		elif "south" in x:
			print("The game does not exist that way!")
		elif "east" in x:
			turncount -= 1
			arcade(turncount, level, roundcount, locations)
		elif "west" in x:
			turncount -= 1
			road5(turncount, level, roundcount, locations)
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

def road7(turncount, level, roundcount, locations):
	if "road7" in locations:
		locations.remove("road7")
		print("You made it to the Road?")
	else:
		print("Road")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are on a Road. Totally tubular.")
		elif "north" in x:
			print("There is no ramp onto the Highway here.")
		elif "south" in x:
			print("The game does not exist that way!")
		elif "east" in x:
			turncount -= 1
			road8(turncount, level, roundcount, locations)
		elif "west" in x:
			turncount -= 1
			arcade(turncount, level, roundcount, locations)
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

def road8(turncount, level, roundcount, locations):
	if "road8" in locations:
		locations.remove("road8")
		print("You made it to the Road?")
	else:
		print("Road")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are on a Road. Radical.")
		elif "north" in x:
			turncount -= 1
			mall(turncount, level, roundcount, locations)
		elif "south" in x:
			print("The game does not exist that way!")
		elif "east" in x:
			print("You run into a wall. When you touch it, it feels like a lazy game developer.")
		elif "west" in x:
			turncount -= 1
			road7(turncount, level, roundcount, locations)
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

def flowers(turncount, level, roundcount, locations):
	if "flowers" in locations:
		locations.remove("flowers")
		print("You made it to the Flower Field!")
	else:
		print("Flower Field")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are at a Flower Field. Is it a Field called Flower or a Field of Flowers?")
		elif "north" in x:
			turncount -= 1
			dev(turncount, level, roundcount, locations)
		elif "south" in x:
			turncount -= 1
			casino(turncount, level, roundcount, locations)
		elif "east" in x:
			turncount -= 1
			road3(turncount, level, roundcount, locations)
		elif "west" in x:
			print("The game does not exist that way!")
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns at the Flower Field. You think to yourself how pretty this place is.\n\nGAME OVER.")
	exit()

def devundev(turncount, level, roundcount, locations):
	if "devundev" in locations:
		locations.remove("devundev")
		print("You made it to Developed Undeveloped Location.")
	else:
		print("Developed Undeveloped Location")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are at the Developed Undeveloped Location. This is some meta stuff you do not understand.")
		elif "north" in x:
			turncount -= 1
			bar(turncount, level, roundcount, locations)
		elif "south" in x:
			turncount -= 1
			warehouse(turncount, level, roundcount, locations)
		elif "east" in x:
			print("You are trying to enter a construction site, but you have been told to turn around.")
		elif "west" in x:
			print("The game does not exist that way!")
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns at the Developed Undeveloped Location. The amount of meta overloads your brain.\n\nGAME OVER.")
	exit()

def mirror(turncount, level, roundcount, locations):
	if "mirror" in locations:
		locations.remove("mirror")
		print("You made it to the Mirror Room!")
	else:
		print("Mirror Room")
	if roundOver(locations):
		roundcount += 1
		rounds(roundcount)
	while turncount > 0:
		x = whereto()
		if "location" in x:
			print("You are at the Mirror Room. When you look into the Mirror, someone ugly looks back at you.")
		elif "north" in x:
			turncount -= 1
			warehouse(turncount, level, roundcount, locations)
		elif "south" in x:
			turncount -= 1
			dev(turncount, level, roundcount, locations)
		elif "east" in x:
			print("You are trying to enter a consturction site, but you have been told to turn around.")
		elif "west" in x:
			print("The game does not exist that way!")
		elif "help" in x:
			help()
		elif "turns" in x:
			print("You have " + str(turncount) + " turn(s) left.")
		elif "bad" in x:
			continue
	if turncount < 0:
		return
	print("You ran out of turns at the Mirror Room. The ugliness of the person staring at you from the Mirror causes everything to stop.\n\nGAME OVER.")
	exit()

def rounds(roundcount=1):
	if roundcount == 1:
		round1()
	elif roundcount == 2:
		round2()
	elif roundcount == 3:
		round3()
	elif roundcount == 4:
		round4()
	else:
	 	winnerwinnerchickendinner()

def roundOver(locations):
	return len(locations) == 0

def winnerwinnerchickendinner():
	print("\nYour Partner: Wait, you've actually done it? No... this can't be possible.")
	time.sleep(4)
	print("You: Oh. It is.")
	time.sleep(3)
	print("You: You've been hit by...")
	time.sleep(3)
	print("You: You've been struck by...")
	time.sleep(4)
	print("You: An ex partner.")
	time.sleep(4)
	print("You snap your fingers, and your ex partner begins to turn into dust and fade away.")
	time.sleep(4)
	print(".")
	time.sleep(1)
	print(".")
	time.sleep(1)
	print(".")
	time.sleep(3)
	print("You're still here?")
	time.sleep(4)
	print("It's over.")
	time.sleep(4)
	print("Go home.")
	time.sleep(4)
	print("Go.")
	time.sleep(2)
	exit()

start()