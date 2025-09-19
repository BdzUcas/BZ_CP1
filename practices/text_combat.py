import random
import time
first_word = ['Crazy ','Rainbow ','Ultimate ','Incredi','Wimpy ','Awesome ','Interdimensional ','Intimidating ','Forest ','Desert ','Average ','','Zombie ','Robot ','Surprise ','Mystery ','Jeff the ','Winter ','Sneaky ','Evil ','Demon ','Angel ','Death ']
miss_message_1 = ['and misses!','but was blinded by their own beauty.','and thinks they hit.','and misses (in a very cool way).','but chickens out.','and misses (in a very cool way).','but accidently teleports away.','but it was just a trick to intimidate you.','but is too slow.','but gets sand in its eyes.','but misses.','but misses.','but their head falls off.','but makes a calculation error.','and almost hits.','but nothing happened...','but misses.','but is too slow.','but it was a trick!','but is too busy cackling maniacally.','but misses.','but their morals caught up to them.','and almost dies trying.']
attack_message_1 = ['flails wildly at you','tries to blind you','does some bad karate','does some kung fu','halfheartedly punches at you','does some jujitsu','tries to suck you into a portal','flexs their muscles','grows vines around you','kicks sand at you','punches at you.','attacks you.','bites at you.','charges up a laser','sneak attacks you','does... something','pulls out a weapon','breaths icy air at you','sneak attacks you','tries to use an evil plan','breaths fire at you','starts to smite you','tries to kill you']
second_word = ['Joe','Cthulu','Goblin','Man','Cat','Destroyer','Fred','Pencil','Beholder','Dog','Cultist','Worm','Muppet','Robot','Cupboard','Beast','Hog','Assasin','Queen','Idol','Bob','Clang']
miss_message_2 = ['but misses.',"but it doesn't have an effect.",'but was too clumsy.','but misses.','and elegantly misses.','but it hit the ground instead.','but misses','but was just writing a rude word','but gets distracted by its own beauty.','but misses.',"but it doesn't seem to do anything",'but it was innefective',"but it doesn't hit quite right",'but made a calculation error.',"but it doesn't do anything",'but misses','but snorts','but it misses.','but nothing happens.',"but it isn't very impressive",'but sneezed',"But it isn't very effective"]
attack_message_2 = ['punches at you','chants in an eldritch language','stabs at you','punches at you','pounces at you','tries to obliterate you','punches at you','stabs at you','charges up a beam','bites at you','chants eerily','squirms around','tells a joke','charges up a laser','slams its door','charges at you','charges at you','sneak attacks you','orders her soldiers toward you','calls on thier followers','laughs creepily','Clangs you']
print('Welcome Challenger!')
time.sleep(1)
print('Meet your opponent: ')
time.sleep(1)
first_word_choice = random.randint(0,len(first_word)-1)
second_word_choice = random.randint(0,len(second_word)-1)
opponent = first_word[first_word_choice] + second_word[second_word_choice]
print(opponent)
attack = random.randint(1,10)
defense = (10 - attack) + random.randint(-1,2)
enemy_attack = random.randint(1,10)
enemy_defense = (10 - enemy_attack) + random.randint(-1,2)
time.sleep(1)
print(f'Your Stats: Attack = {attack}, Defense = {defense}.')
round = 1
defend_actions = ['d','defend','dodge','defense']
attack_actions = ['a','attack','kill','offense']
temp_defense = defense
dodges = ['You dodge elegantly.','You dodge, sort of','You bravely defend yourself against the attack!','You try to dodge.','You leap backward in fright','You steel yourself for an attack','You hide - bravely of course','You dodge out of the way of the attack','You run away at full speed','You scream in terror']
misses = ['You *almost* hit','You miss!','Your attack misses.','You impressively flourish your blade- oh, oh wow that looks very painful','Your attack misses horribly',"You plunge your blade directly into- that's a tree. Seriously, that's a tree.",'You miss','You miss!','You yell a battle cry! It does nothing.']
hits = ['Your attack hits!','Wow! Awesome hit!','Oof- that looks painful.','Your hit lands, sort of.',f'You strike the {opponent} down.']

while True:
    time.sleep(2)
    print(f'Round {round}')
    time.sleep(1)
    if random.randint(0,1) == 0:
        print(f'{opponent} {attack_message_1[first_word_choice]}...')
    else:
        print(f'{opponent} {attack_message_2[second_word_choice]}...')

    time.sleep(1)
    
    damage = ((enemy_attack / 2) + random.randint(1,10)) - ((defense / 2) + random.randint(2,5))
    if damage < 1:
        if random.randint(0,1) == 0:
            print(miss_message_1[first_word_choice])
        else:
            print(miss_message_2[second_word_choice])
    else:
        print(f'and hits! You take {damage} damage!')
    defense = temp_defense
    time.sleep(2)
    while True:

        print("What action would you like to take? Attack or Defend: ")
        action = input('> ').lower().replace('!','').replace('.','').replace(' ','')
        if action in defend_actions or action in attack_actions:
            break
    time.sleep(1)
    if action in attack_actions:
        damage = ((attack / 2) + random.randint(1,10)) - ((enemy_defense / 2) + random.randint(2,5))
        if damage < 1:
            print(random.choice(misses))
        else:
            print(f'{random.choice(hits)} You deal {damage} damage to {opponent}!')
    elif action in defend_actions:
        temp_defense = defense
        defense = temp_defense * 2
        print(random.choice(dodges))

    round += 1
    
