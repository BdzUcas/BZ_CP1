#BZ 1st Text Adventure Game
import time as t
import random as r
def choiceInput(valid_choices):
    while True:
        choice = input().strip().lower()
        if choice in valid_choices:
            return choice
        elif choice.isdigit():
            choice = int(choice)
            if choice <= len(valid_choices) and choice > 0:
                return valid_choices[choice-1]
        print('Please select a valid choice!')
def display(text = 'Message not defined!', wait = 1):
    print(text)
    t.sleep(wait)
def charismaCheck(cha,goal):
    if r.randint(1,10) + cha < goal:
        return False
    else:
        return True
def useItem(player_info, item):
    if item == 'dinner':
        player_info['hp'] = player_info['hp'] + 2
        if player_info['hp'] > player_info['max hp']:
            player_info['hp'] = player_info['max hp']
    elif item == 'beer':
        player_info['max hp'] = player_info['max hp'] + 1
        player_info['drunk turns'] = player_info['drunk turns'] + 2
        player_info['charisma'] = player_info['charisma'] - 1
    elif item in ['mustache','hat','badge','bandanna']:
        if item in player_info['equipped']:
            print('You already have that equipped!')
        else:
            if (item == 'bandanna') and 'hat' in player_info['equipped']:
                display('You remove the Cowboy Hat.')
                player_info['equipped'].remove('hat')
            if (item == 'hat') and 'bandanna' in player_info['equipped']:
                display('You remove the Bandit Bandanna')
                player_info['equipped'].remove('bandanna')
            player_info['equipped'].append(item)
            player_info['charisma'] += 1
    display(items[item]['use'])
    return player_info
def combat(enemy, player_info):
    display(f'{enemy['name']} begins combat!')
    turn = 0
    while True:
        turn += 1
        print("Attack, Persuade, or Use?")
        action = choiceInput(['attack','persuade','use'])
        if turn == 1:
            enemy_choice = r.choice(['persuade','attack'])
        elif enemy['hp'] < 2:
            enemy_choice = r.choice(['attack','persuade','persuade'])
        else:
            enemy_choice = r.choice(['attack','attack','persuade'])
        if action == 'use':
            if enemy_choice == 'attack':
                player_info['hp'] -=  2
                display(f'{enemy['name']} shoots you!')
                if player_info['hp'] < 1:
                    display('You died!')
                    return False
                else:
                    display(f'You have {player_info['hp']} health remaining!')
            elif enemy_choice == 'persuade':
                display(f'{enemy['name']} tries to persuade you to not use an item... and fails.')
            if player_info['inventory']:
                display('What item are you using?')
                used = choiceInput(player_info['inventory'])
                player_info = useItem(player_info,used)
            else:
                display("You don't have an item to use!")
        elif action == 'attack':
            if enemy_choice == 'attack':
                display('You both shoot!')
                if r.randint(0,1) == 0:
                    player_info['hp'] -= 2
                    display(f'Your bullet goes wide! {enemy['name']} shoots you!')
                    if player_info['hp'] < 1:
                        display('You died!')
                        return False
                    else:
                        display(f'You have {player_info['hp']} health remaining!')
                else:
                    enemy['hp'] -= 1
                    display(f'You shot {enemy['name']}!')
                    if enemy['hp'] < 1:
                        if enemy['name'] != 'your Grandma':
                            display(f'{enemy['name']} dies!')
                        return player_info
            elif enemy_choice == 'persuade':
                if player_info['drunk turns'] > 0:
                    persuaded = charismaCheck(enemy['charisma'], 4 + player_info['charisma'])
                else:
                    persuaded = charismaCheck(enemy['charisma'], 5 + player_info['charisma'])
                if persuaded:
                    display(f'{enemy['name']} persuades you not to shoot them!')
                else:
                    enemy['hp'] -= 1
                    display(f'You shot {enemy['name']}!')
                    if enemy['hp'] < 1:
                        if enemy['name'] != 'your Grandma':
                            display(f'{enemy['name']} dies!')
                        return player_info
        elif action == 'persuade':
            if enemy_choice == 'attack':
                if player_info['drunk turns'] > 0:
                    persuaded = charismaCheck(player_info['charisma'] - 1, 5 + enemy['charisma'])
                else:
                    persuaded = charismaCheck(player_info['charisma'] - 1, 5 + enemy['charisma'])
                if persuaded:
                    display(f'You persuade {enemy['name']} not to shoot you!')
                else:
                    player_info['hp'] -= 2
                    display(f'You try to persuade them, but {enemy['name']} still shoots you!')
                    if player_info['hp'] < 1:
                        display('You died!')
                        return False
                    else:
                        display(f'You have {player_info['hp']} health remaining!')
            elif enemy_choice == 'persuade':
                display(f'You persuade {enemy['name']} not to persuade you to not persuade them to not persuade you to not persuade them to not persuade you')
items = {
    'cookie': {
        'name': "Grandma's Cookie", 
        'inspect': "A chocolate chip cookie from your grandma. It's still warm!",
        'use': "..For what? It looks too good to eat. Maybe someone else will take it?"
    },
    'dinner': {
        'name': "Western Dinner", 
        'inspect': "A nice western dinner of steak and potatoes. A hearty meal that will fill you up even if you're starving.",
        'use': "You eat the Western Dinner. Yum!"
    },
    'beer': {
        'name': "Western Beer", 
        'inspect': "A strong alchoholic drink traditional to Westville. What could go wrong?",
        'use': "You drink the Western Beer. You feel a bit tipsy."
    },
    'mustache': {
        'name': "Glue-On Mustache", 
        'inspect': "A silly mustache that attaches just below your nose. It makes you look very sophisticated.",
        'use': "You equip the Glue-On Mustache. How suave!"
    },
    'hat': {
        'name': "Cowboy Hat", 
        'inspect': "A traditional western hat. Perfect for a sheriff like you!",
        'use': "You don the Cowboy Hat. How dashing!"
    },
    'badge': {
        'name': "Sheriff's Badge", 
        'inspect': "A leather badge adorned with a metal star. Lets everyone know who you are!",
        'use': "You equip the Sheriff's Badge!"
    },
    'dentures': {
        'name': "Old Dentures", 
        'inspect': "An old pair of dentures... gross",
        'use': "For- what? Gross!"
    },
    'ranch': {
        'name': "Rancher Ranch", 
        'inspect': "Ranch made by a Rancher. Goes great with a salad!",
        'use': "You're just going to eat it plain? Ew!"
    },
    'milk': {
        'name': "Milk", 
        'inspect': "A bottle of cold milk. It doesn't smell very good...",
        'use': "You lift the bottle to your lips but gag at the mere taste."
    },
    'key': {
        'name': "Priest's Key", 
        'inspect': "A fancy key presumable used to unlock the church.",
        'use': "There aren't any locks around!"
    },
    'handcuffs': {
        'name': "Handcuffs", 
        'inspect': "Strong handcuffs for strong criminals.",
        'use': "On who? Yourself?"
    },
    'bandanna': {
        'name': "Bandit Bandanna", 
        'inspect': "A bandanna worn by the Westville Bandits. Makes you look just like one!",
        'use': "You equip the Bandit Bandanna. Intimidating!"
    }
}
def sherrifOffice(room,player):
    if room['jay']:
        display('You are in your office building. There is a desk, and a small cell with Jay the Outlaw in it. There are two doors, one in the back and one in the front')
    else:
        display('You are in your office building. There is a desk, and a small empty jail cell. There are two doors, one in the back and one in the front.')
    while True:
        print('Use, Inventory, or Inspect?')
        action = choiceInput(['use','inventory','inspect'])
        if action == 'inspect':
            print('What are you inspecting?')
            if room['jay']:
                inspected = choiceInput(player['inventory'] + ['desk','jay','outlaw','jaw the outlaw','front door','back door','door'])
            else:
                inspected = choiceInput(player['inventory'] + ['desk','front door','back door','door'])
            if inspected == 'desk':
                display("It's a wooden desk with some papers on it. Nothing special.")
            elif inspected in ['jay','outlaw','jaw the outlaw']:
                display('You approach Jay the Outlaw. He speaks out to you in a weathered voice.')
                display("> 'Ey there sheriff. Come to play at my game? Or to set me free? *wink wink*", 2)
                display('leave, play, or free?')
                action = choiceInput(['leave','play','free'])
                if action == 'leave':
                    display(">'kay then, come back later!")
                    continue
                elif action == 'play':
                    display("> 'kay then, how much you wagerin'?")
                    while True:
                        wager = input()
                        if wager.isdigit():
                            wager = int(wager)
                            if wager <= player['money']:
                                display("Wow! Quite confident, aren't ya?")
                                player['money'] -= wager
                                break
                            else:
                                display("> Do ya really have that much? Didn't think so.")
                        else:
                            display("While ya can't play if ya don't wager nothin'! How much?")
                    display("> I'm flippin' a coin. If it's heads, ya get the money. If it's tails, I get the money!")
                    coin = r.randint(1,2)
                    if coin == 1:
                        display('> Tails! I win. He He! Come back later!')
                    else:
                        display('> Heads! Darn.')
                        player['money'] += wager * 2
                        continue
                elif action == 'free':
                    display("> You've come to free me? Yipee! Take me handcuffs.")
                    player['inventory'].append('handcuffs')
                    room['jay'] = False
                    continue
            elif inspected == 'front door':
                display("It's a wooden door. It leads to the town square")
            elif inspected == 'back door':
                display("It's a wooden door. It leads to the forest")
            elif inspected == 'door':
                display("It's a wooden door.")
            else:
                display(items[inspected]['inspect'])
        elif action == 'use':
            print('Use what?')
            used = choiceInput(player['inventory'] + ['front door','back door'])
            if used == 'front door':
                display('You go through the front door, out into the town square.')
                return player, room, 1
            elif used == 'back door':
                display('You go through the back door, out into the forest.')
                return player, room, 8
            else:
                player = useItem(player,used)
        elif action == 'inventory':
            print(f'Inventory: {', '.join(player['inventory'])}')

 
#Define function townSquare(room_info, player_info):
#	display(You are in the town square. There is an old beggar sitting on a bench. You can head off to 
#the Westaurant, the church, the ranch, the clothes shop, or the sheriff's office)
#	Loop forever:
#display(Use, Move, Inventory, or Inspect?)
#action = choiceInput(inspect, use, inventory, move)
#If action = inspect:
#	Inspected = choiceInput(Inventory items, beggar)
#	If inspected = beggar:
#		display(>Food for the poor?)
#		If western dinner is in inventory:
#			display(Offer food?)
#			choice = player input
#			If choice is yes or y:
#				Remove western dinner from the inventory
#				display(>Really? Here, take these as a sign of my gratitude)
#				Add dentures to inventory
#				display(You gain the Old Dentures!)
#			Otherwise:
#				display(You hide the Western Dinner.)
#	Otherwise:
#		Display normal inspect message for object
#Otherwise if action = use:
#	used_item = choiceInput(current inventory)
#	player_data = useItem(player_data,used_item)	
#Otherwise if action = inventory:
#	Display inventory
#Otherwise if action = move:
#	display(move where?)
#	moved = choiceInput(westaurant, church, ranch, clothes shop, sherrif's office)
#	if moved = church:
#		if player has priest key:
#			display(You unlock the door with the key)
#		otherwise:
#			display(It's locked!)
#			return to top of loop
#	return room_info, player_info, and the id of the room moved to
#define function grandmaHouse(room_info, player_info)
#	display(You enter your grandma's house. She is sitting in a rocking chair. The door is behind you.)
#	If player has not visited this room yet:
#		display(>Oh hello dearie! How is the job going? Are you getting hungry?)
#		player input
#		no matter what the player answered:
#		display(>Oh of course you are! Take a cookie.)
#		add cookie to inventory
#		display(>Grandma's Cookie added to inventory)
#	otherwise if they haven't given the dentures:
#		display(>Oh hello dearie! I have another cookie in the oven for you. I only made one since I 
#can't eat them without my dentures.)
#if player has dentures in inventory:
#	display(>Oh! Those must be them! Hand ‘em over!)
#	display(>Thanks for returning them! Here, have a cookie.)
#		add cookie to inventory
#			display(Grandma's Cookie added to inventory)
#	otherwise:
#display(Oh i wish i could find them…)
#	otherwise if the player has max charisma:
#		display(>Oh hello dearie! Want to hear a story?)
#		player input
#		display(>Of course you do! Back when i was young i was part of this fantasmic group of 
#flapjacks. We had so much fun! We used to wear these scarves on our head. Like this one!)
#add bandit bandanna to inventory
#display(bandit bandanna added to inventory!)
#display(>We always used to hang out at the church, you know?)
#display(>Have fun!)
#otherwise:
#	display(She appears to be asleep.)
#display(You leave through the door.)
#return room_info, player_info, and 8
#define function forest(room_info, player_info):
#	if player has not caught the weasel:
#if Bandit Bart is defeated:
#display(You enter the forest. There is a weasel hiding under a fern. Your grandma's 
#house is just a short walk away. The Ranch and Sheriff's office are nearby.)
#		otherwise:
#			display(You enter the forest. There is a bandit sitting on a tree stump and a weasel 
#hiding under a fern. Your grandma's house is just a short walk away. The Ranch and Sheriff's office are nearby.)
#	otherwise:
#		if Bandit Bart is defeated:
#			display(You enter the forest. Your grandma's house is just a short walk away. The 
#Ranch and Sheriff's office are nearby.)
#		otherwise:
#			display(You enter the forest. There is a bandit sitting on a tree stump. Your 
#Grandma's house is just a short walk away. The Ranch and Sheriff's office are 
#nearby.)
#if player is wearing the sheriff's badge and bandit bart is not defeated:
#	display(>Hang on a minute… You're the sheriff! Take this!)
#	player_info = combat(bandit bart's info, player_info)
#		if player_info = false:
#			return false
#		set bandit bart defeated to true
#		give the player 5 money
#	Loop forever:
#display(Use, Move, Inventory, or Inspect?)
#action = choiceInput(inspect, use, inventory, move)
#create list called options containing all inventory items
#if bandit bart is not defeated:
#	add bandit to options
#if weasel has not been caught
#	add weasel to options
#
#If action = inspect:
#	Inspected = choiceInput(options)
#	if inspected = bandit:
#		display(>Hey dude.)
#	otherwise if inspected = weasel:
#		display(It's just a weasel. It is a bit fat, looks like it has been eating well.)
#	otherwise:
#		display normal inspect message for the object
#otherwise if action = use:
#	used_item = choiceInput(current inventory)
#	if used item = weasel trap:
#		display(You catch the weasel in the trap!)
#		add captured weasel to inventory
#		set weasel caught to true
#	otherwise:
#player_data = useItem(player_data,used_item)
#Otherwise if action = inventory:
#	Display inventory
#Otherwise if action = move:
#	display(move where?)
#	moved = choiceInput(grandma's house, ranch, sheriff's office)
#	return room_info, player_info, and the id of the room moved to
#function clothesShop(room_info, player_info):
#	display(Taylor the Taylor is sitting at a desk.)
#	display(>Hello! What can I do for you today?)
#	if player has cookie and not the sheriff's badge:
#		display(>Wait a minute… is that a cookie i smell? Could i have it?)
#		choice = choiceinput(y,yes,n,no)
#		if choice = y or yes:
#			display(>Thanks! Here, take this. I think you lost it.)
#			add sheriff's badge to inventory
#			display(You got the sheriff's badge!)
#		otherwise:
#			display(Aw… okay.)
#		display(Anyways, would you like to buy some clothes?)
#	display(>We have the glue-on mustache and the cowboy hat!)
#	display(Mustache, Hat, or Leave?)
#	choice = choiceInput(mustache, hat, leave)
#	if choice = mustache:
#		display(>That will be $(4 - charisma).)
#		if money is greater than or equal to 4 - charisma:
#			display(You got the Glue-On Mustache!)
#			add mustache to inventory
#		otherwise:
#			display(>Aw, darn… you don't have enough. Come back later when you have some 
#more!)
#	otherwise if choice = hat:
#		display(>That will be $(4 - charisma).)
#		if money is greater than or equal to 4 - charisma:
#			display(You got the Cowboy Hat!)
#			add cowboy hat to inventory
#		otherwise:
#			display(>Aw, darn… you don't have enough. Come back later when you have some 
#more!)
#	display(You leave through the door.)
#	if taylor does not have the sheriff's badge:
#		display(>Man… i could sure use a treat about now)
#	return room_info, player_info, and 1
#function church(room_info, player_info):
#	if Garret is defeated:
#display(You enter the church. You can walk down into the bandit hideout or 
#out into the town square.)
#moved = choiceInput(hideout, town square, bandit hideout)
#if moved = hideout or bandit hideout:
#	display(You move down into the bandit hideout.)
#	return room_info, player_info, and 9
#		otherwise:
#			display(You leave the church.)
#			return room_info, player_info, and 1
#	otherwise:
#		display(You enter the church. Garret the Guard is standing guard over the entrance to the 
#hideout.)
#if you are wearing the sheriff's badge:
#	display(>Hey! You!)
#	player_info = combat(garret's info, player_info)
#		if player_info = false:
#			return false
#		set bandit bart defeated to true
#		give the player 5 money
#		display(You can walk down into the bandit hideout or out into the town square.)
#moved = choiceInput(hideout, town square, bandit hideout)
#if moved = hideout or bandit hideout:
#	display(You move down into the bandit hideout.)
#	return room_info, player_info, and 9
#		otherwise:
#			display(You leave the church.)
#			return room_info, player_info, and 1
#	otherwise if you are wearing the Bandit Bandanna:
#		display(>Oh, hey! Come to hang out in the hideout? Go ahead!)
#			display(You can walk down into the bandit hideout or out into the town square.)
#moved = choiceInput(hideout, town square, bandit hideout)
#if moved = hideout or bandit hideout:
#	display(You move down into the bandit hideout.)
#	return room_info, player_info, and 9
#		otherwise:
#			display(You leave the church.)
#			return room_info, player_info, and 1
#		otherwise:
#			display(Hey, uhh… I can't let you down there. Sorry.)
#			display(You leave the church.)
#		return room_info, player_info, and 1
#function westaurant(room_info, player_info)
#	if jed is defeated:
#		display(You enter the westaurant. Jed is dead, but Leviticus is still here.)
#		display(>Ranch?)
#		if player has ranch:
#			display(>Ranch!)
#			display(Leviticus seizes the ranch. He drops a key from his pocket without noticing.)
#			display(You got the Priest's Key!)
#		display(You can move into the back room or into the town square.)
#moved = choiceInput(town square, back room)
#if moved = back room:
#	display(You move down into the back room.)
#	return room_info, player_info, and 10
#		otherwise:
#			display(You leave the westaurant.)
#			return room_info, player_info, and 1
#	otherwise:
#		display(You enter the westaurant. Jed is tending the counter.)
#		display(A strange voice rings out from the corner)
#		display(>Ranch?)
#		display(Leviticus is sitting in the corner, wearing priest's robes covered in ranch stains.)
#		if player is wearing the sheriff's badge:
#			display(Jed is staring at your badge)
#			display(>Hang on… you're the new sheriff! Take this!)
#			display(Jed takes off his hat, revealing a bandit bandanna.)
#			player_info = combat(jed's info, player_info)
#		if player_info = false:
#			return false
#		set jed defeated to true
#		give the player 5 money
#		display(You can move into the back room or into the town square.)
#moved = choiceInput(town square, back room)
#if moved = back room:
#	display(You move down into the back room.)
#	return room_info, player_info, and 10
#		otherwise:
#			display(You leave the westaurant.)
#			return room_info, player_info, and 1
#
#		otherwise:
#			display(Jed is looking at you.)
#			display(>Hey! Would you like to buy some food?)
#			display(Western Dinner, Western Beer, or Leave?)
#	choice = choiceInput(dinner, beer, leave)
#	if choice = dinner:
#		display(>That will be $(3 - charisma).)
#		if money is greater than or equal to 3 - charisma:
#			display(You got the Western Dinner!)
#			add western dinner to inventory
#		otherwise:
#			display(>Aw, darn… you don't have enough. Come back later when 
#you have some more!)
#	otherwise if choice = beer:
#		display(>That will be $(2 - charisma).)
#		if money is greater than or equal to 2 - charisma:
#			display(You got the Western Beer!)
#			add beer to inventory
#		otherwise:
#			display(>Aw, darn… you don't have enough. Come back later when 
#you have some more!)
#	display(You leave through the door.)
#	display(>Ranch?)
#	return room_info, player_info, and 1
#define function ranch(room_info, player_info):
#	if player has gotten the weasel trap from Billy:
#display(You enter the ranch. Rancher Bob is tending to the animals and Billy the Kid is running around with a strange metal trap. You can move to the forest or town square.)
#	otherwise:
#display(You enter the ranch. Rancher Bob is tending to the animals and Billy the Kid is eating a cookie. You can move to the forest or town square.)
#	Loop forever:
#		Loop forever:
#display(Use, Move, Inventory, or Inspect?)
#action = choiceInput(inspect, use, inventory, move)
#If action = inspect:
#	Inspected = choiceInput(Inventory items, bob, billy)
#	if inspected = bob:
#				if player has given the captured weasel to Bob:
#					display(>Hey there! Thanks for earlier!)
#				otherwise:
#					display(>Oh, hello.)
#					display(Rancher Bob looks sad)
#					display(>Sorry about me, i'm just down because this weasel keeps 
#eating my crops. I can never catch it!)
#if player has not gotten the weasel trap from billy:
#display(>Billy is trying to catch it with that weasel trap he 
#has.)
#					otherwise if player has a captured weasel:
#						display(Wait! That's the weasel! Thank you so much! Take 
#this.)
#add ranch to inventory
#display(You got the Rancher's Ranch!)
#display(>Anyways, see you later.)
#			otherwise if inspected = billy:
#				if player has given him the cookie:
#					display(>Hi mister! Thanks for the cookie!)
#				otherwise:
#					display(>Hi mister! I'm trying to catch a weasel!)
#					display(>All this running around is making me hungry. I could sure go 
#for a cookie and some milk about now!)
#if player has a cookie and the milk:
#	display(>Oh hey! Look at that!)
#	display(Billy grabs the cookie and milk from you.)
#	remove cookie from inventory
#	remove milk from inventory
#	display(He drops his weasel trap as he runs away.)
#	display(You got the weasel trap!)
#	add weasel trap to inventory.
#			otherwise:
#				Display normal inspect message for that item
#		Otherwise if action = use:
#			used_item = choiceInput(current inventory)
#	player_data = useItem(player_data,used_item)
#		Otherwise if action = inventory:
#	Display inventory
#Otherwise if action = move:
#	display(move where?)
#	moved = choiceInput(town square, forest)
#	return room_info, player_info, and the id of the room moved to
#define function hideout(room_info, player_info):
#	display(You enter the hideout. Standing in the center of the room is a familiar face.)
#	display(Wearing a bandit bandanna, and munching on one of her signature cookies.)
#	display(>That's right… I am Bad Guy Bill! Didn't expect that, now did you?)
#	display(>The clues were there all along- but of course a young whippersnapper like you wouldn't 
#be able to figure them out!)
#if player has the bandit bandanna:
#	display(>I gave you the bandanna you used to sneak in here!)
#display(>I gave you the cookies to give to Taylor and Billy!)
#display(>I helped you along every step of your journey!)
#if the player has the bandit bandanna:
#display(>I even hinted that I was Bad Guy Bill!)
#display(>I told you I was a bandit!)
#display(>All to get you here.)
#display(>Why?)
#display(>This town doesn't need a sheriff.)
#display(>Crime is the way of the world!)
#display(>I couldn't kill you myself, of course.)
#display(>“Sheriff murdered by deranged outlaw” is a much better headline than “Sheriff murdered by senile grandma)
#display(>So that brings us to here.)
#display(>Now prepare to die!)
#player_info = combat(bad guy bill's stats,  player_stats)
#	if player_info = false:
#		return false
#	otherwise:
#		display(>You don't want to kill me!)
#		display(>I'm your sweet old grandma!)
#		display(>Here, take a cookie! Take a whole batch!)
#		display(Your grandma throws a tray of cookies in your face!)
#display(She runs to the door to escape!)		
#if player has handcuffs in inventory:
#			remove handcuffs from inventory
#			display(She trips as she realizes- her ankles are handcuffed together)
#			display(>You… handcuffed me? With your only pair of handcuffs?)
#			display(>Nooooo!!!! My crime empire!!!!!)
#			display(With the town saved, you are revered as the greatest sheriff Westville has 
#ever seen.)
#display(And seriously…)
#display(Those cookies were pretty good.)
#display(THE END)
#return true
#otherwise:
#	display(you run out the door after her!)
#	display(as she is running away, you fire a shot from your pistol.)
#	display(Congratulations. You killed your grandma.)
#			display(With the town saved, you are revered as the greatest sheriff Westville has 
#ever seen.)
#			display(But you will forever have to live with your regret.)
#			display(THE END)
#			return true
#define function backRoom(room_info, player_info):
#	display(You enter the back room of the westaurant.)
#	display(There is some food stored in crates, a small kitchen, and a bottle of milk sitting out.)
#	display(You got the Milk!)
#	display(You leave back into the main room.)
#	return room_info, player_info, and 2
#
#Set up a dictionary with dictionaries inside it for each room. Each of those dictionaries stores info about the room specific to it and any NPCs in there.

player_info = {
    'charisma': 0,
    'max hp': 4,
    'hp': 4,
    'money': 5,
    'drunk turns': 0,
    'inventory': [],
    'equipped': []
}
#make a variable called room set to 4. This stores what room you are in
#loop forever:
#	display(Welcome to Westville! This rough-and-tumble town is troubled by a gang of bandits led by 
#the infamous Bad Guy Bill. The previous sheriff of this town was killed by Bad Guy Bill. Now you 
#are the replacement. Your mission: Find and incarcerate Bad Guy Bill. Only trouble is, nobody 
#knows where or who he is. Maybe you should ask your grandma.)
#	forever:
#		if room = 1:
#		town square info and player_info and room = townSquare(town square info, 
#player_info)
#	otherwise if room = 2:
#		westaurant and player_info and room = townSquare(westaurant info, 
#player_info)
#otherwise if room = 3:
#		grandma's house info and player_info and room = grandmaHouse(grandma's house 
#info, player_info)
#		otherwise if room = 4:
#		sheriff's office info and player_info and room = sheriffsOffice(sheriff's office info, 
#player_info)
#	otherwise if room = 5:
#		clothes shop info and player_info and room = clothesShop(clothes shop info, 
#player_info)
#otherwise if room = 6:
#		church info and player_info and room = church(church info,  player_info)
#	otherwise if room = 7:
#		ranch info and player_info and room = ranch(ranch info,  player_info)
#	otherwise if room = 8:
#		forest info and player_info and room = forest(forest info,  player_info)
#otherwise if room = 9:
#		won = hideout(bandit hideout info,  
#player_info)
#if won is false:
#	display(GAME OVER)
#choice = choiceInput(y, yes, n, no)
#		if choice is n or no:
#			exit loop
#otherwise if room = 10:
#		westaurant back room info and player_info and room = backRoom(westaurant back 
#room info,  player_info)
#if player_info is false:
#	display(GAME OVER)
#	display(Play again?)
#	choice = choiceInput(y, yes, n, no)
#	if choice is n or no:
#		exit loop
#	
#
sherrifOffice({'jay': True},player_info)