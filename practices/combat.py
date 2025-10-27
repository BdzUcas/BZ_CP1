#BZ 1st Combat Program
#I used some code from a previous personal project for the naming and hit/miss messages
import random as r
import time as t

#Define opponent
second_word = ['Joe','Cthulu','Goblin','Man','Cat','Destroyer','Fred','Pencil','Beholder','Dog','Cultist','Worm','Muppet','Robot','Cupboard','Beast','Hog','Assasin','Queen','Idol','Bob','Clang']
first_word = ['Crazy ','Rainbow ','Ultimate ','Incredi','Wimpy ','Awesome ','Interdimensional ','Intimidating ','Forest ','Desert ','Average ','','Zombie ','Robot ','Surprise ','Mystery ','Jeff the ','Winter ','Sneaky ','Evil ','Demon ','Angel ','Death ','Super']
miss_message_1 = ['and misses!','but was blinded by their own beauty.','and thinks they hit.','and misses (in a very cool way).','but chickens out.','and misses (in a very cool way).','but accidently teleports away.','but it was just a trick to intimidate you.','but is too slow.','but gets sand in its eyes.','but misses.','but misses.','but their head falls off.','but makes a calculation error.','and almost hits.','but nothing happened...','but misses.','but is too slow.','but it was a trick!','but is too busy cackling maniacally.','but misses.','but their morals caught up to them.','and almost dies trying.',f'but had to stop Evil {r.choice(second_word)} instead.']
attack_message_1 = ['flails wildly at you','tries to blind you','does some bad karate','does some kung fu','halfheartedly punches at you','does some jujitsu','tries to suck you into a portal','flexs their muscles','grows vines around you','kicks sand at you','punches at you.','attacks you.','bites at you.','charges up a laser','sneak attacks you','does... something','pulls out a weapon','breaths icy air at you','sneak attacks you','tries to use an evil plan','breaths fire at you','starts to smite you','tries to kill you','Tries to stop your evil plans']
miss_message_2 = ['but misses.',"but it doesn't have an effect.",'but was too clumsy.','but misses.','and elegantly misses.','but it hit the ground instead.','but misses','but was just writing a rude word','but gets distracted by its own beauty.','but misses.',"but it doesn't seem to do anything",'but it was innefective',"but it doesn't hit quite right",'but made a calculation error.',"but it doesn't do anything",'but misses','but snorts','but it misses.','but nothing happens.',"but it isn't very impressive",'but sneezed',"But it isn't very effective"]
attack_message_2 = ['punches at you','chants in an eldritch language','stabs at you','punches at you','pounces at you','tries to obliterate you','punches at you','stabs at you','charges up a beam','bites at you','chants eerily','squirms around','tells a joke','charges up a laser','slams its door','charges at you','charges at you','sneak attacks you','orders her soldiers toward you','calls on thier followers','laughs creepily','Clangs you']
first_word_choice = r.randint(0,len(first_word)-1)
second_word_choice = r.randint(0,len(second_word)-1)
opponent = first_word[first_word_choice] + second_word[second_word_choice]
#Define dodge/miss/hit/crit/heal messages
dodges = ['You dodge elegantly.','You dodge, sort of','You bravely defend yourself against the attack!','You try to dodge.','You leap backward in fright','You steel yourself for an attack','You hide - bravely of course','You dodge out of the way of the attack','You run away at full speed','You scream in terror', 'You defend yourself against the incoming attack.']
misses = ['You *almost* hit','You miss!','Your attack misses.','You impressively flourish your blade- oh, oh wow that looks very painful','Your attack misses horribly',"You plunge your blade directly into- that's a tree. Seriously, that's a tree.",'You miss','You miss!','You yell a battle cry! It does nothing.','Nothing happened',f'The {opponent} blocks your attack.','Your attack hits the ground.',f'Whoops, you accidently attacked something else instead. You deal {r.randint(1,10)} damage to the {r.choice(first_word)}{r.choice(second_word)}!']
hits = ['Your attack hits!','Wow! Awesome hit!','Oof- that looks painful.','Your hit lands, sort of.',f'You strike the {opponent} down.']
enemy_hits = ['It hits!','And lands an impressive hit!','Oof- that looks painful.','And it works, sort of.','And it hits perfectly.','And hit!',"Oof- that's a lot of damage.",'and hit!','and lands an impressive attack.',"and it hits, but it wasn't very impressive."]
crits = ['Critical Hit!','CRIT!','SMASH!','BAM!','KAPOW!']
heals = ['You drink a healing potion.','You grit your teeth and try again.','You feel rejuvenated.']
#Define possible inputs
input_fighter = ['1','fighter','barbarian','smash']
input_tank = ['2','tank','protector','cleric']
input_rouge = ['3','rougue','rouge','roug','roge','rogue','theif','assassin']
input_yes = ['yes','y','yep','yes please','yess','ye']
input_1 = ['attack','kill','offense','1']
input_2 = ['sheild','defense','dodge','shield','2']
input_3 = ['heal','3','potion','hael']
input_4 = ['4','Flurry Attack','Hyper Defense','Sneak Attack']
choice = 0
#Define turn functions
def player_turn():
    if class_input in input_fighter:
        print('What would you like to do?\n1. Attack\n2. Shield\n3. Heal\n4. Flurry Attack')
    elif class_input in input_tank:
        print('What would you like to do?\n1. Attack\n2. Shield\n3. Heal\n4. Hyper Defense')
    elif class_input in input_rouge:
        print('What would you like to do?\n1. Attack\n2. Dodge\n3. Heal\n4. Sneak Attack')
    while not False:
        action = input()
        if action in input_1:
            roll = r.randint(1,20)
            t.sleep(1)
            if roll == 20:
                print(r.choice(crits))
                damage = r.randint(1,8) + attack
                damage *= 2
                print(f'You deal {damage} damage to the {opponent}!')
                return 1, damage
            elif roll + attack > monster_defense:
                damage = r.randint(1,8) + attack
                print(r.choice(hits))
                t.sleep(1)
                print(f'You deal {damage} damage to the {opponent}!')
                return 1, damage
            else:
                print(r.choice(misses))
                return 1, 0
        elif action in input_2:
            print(r.choice(dodges))
            return 2, 0
        elif action in input_3:
            print(r.choice(heals))
            t.sleep(1)
            heal = r.randint(3,8)
            print(f'You heal {heal} hp!')
            return 3, heal
        elif action in input_4:
            if stamina < 1:
                print('You are out of special actions!')
            else:
                if class_input in input_fighter:
                    flurry_damage = 0
                    for i in range(1,7):
                        roll = r.randint(1,20)
                        if roll == 20 or roll == 19:
                            print(r.choice(crits))
                            flurry_damage += attack * 2
                        elif roll + attack > monster_defense:
                            flurry_damage += attack
                        t.sleep(0.1)
                    print(f'You deal {flurry_damage} damage from 6 attacks!')
                    return 4, flurry_damage
                elif class_input in input_tank:
                    print('You will take no damage this round!')
                    return 4, 0
                elif class_input in input_rouge:
                    roll = r.randint(1,20)
                    if roll == 20:
                        print(r.choice(crits))
                        damage = r.randint(1,8) + attack * 3
                        damage *= 2
                        print(f'You deal {damage} damage to the {opponent}!')
                    else:
                        damage = r.randint(1,8) + attack * 3
                        print(f'You deal {damage} damage to the {opponent}!')
                    return 4, damage

        else:
            print('Please use a valid input!')
def monster_turn():
    if r.randint(1,2) == 1:
        print(f'{opponent} {attack_message_1[first_word_choice]}...')
    else:
        print(f'{opponent} {attack_message_2[second_word_choice]}...')
    t.sleep(1)
    if choice == 4 and class_input in input_tank:
        print('But your impenetrable defenses block it!')
    else:
        if choice == 2:
            roll = min(r.randint(1,20),r.randint(1,20))
        else:
            roll = r.randint(1,20)
        if roll + monster_attack > defense:
            print(r.choice(enemy_hits))
            damage = r.randint(1,8) + monster_attack
            print(f'You take {damage} damage!')
            return damage
        else:
            if r.randint(1,2) == 1:
                print(miss_message_1[first_word_choice])
            else:
                print(miss_message_2[second_word_choice])
            return 0
        

#Introduce program
print('Welcome challenger!')
t.sleep(1)
#Get user stats
name = input('Enter your name: ').strip()
while not False:
    class_input = input('Enter your Class:\n1. Fighter\n2. Tank\n3. Rougue\n').lower().strip()
    if class_input in input_fighter:
        attack = r.randint(3,6)
        defense = 19 - attack
        hp = 20
        break
    elif class_input in input_tank:
        attack = r.randint(1,3)
        defense = 21 - attack
        hp = 30
        break
    elif class_input in input_rouge:
        attack = r.randint(4,8)
        defense = 16 - attack
        hp = 15
        break
    else:
        print('Please enter a valid class!')
    t.sleep(1)
stamina = 3
print(f'Stats:\n\033[31m### {name} ###\033[0m\nAttack: +{attack}\nDefense: {defense}\nHealth: {hp}')
t.sleep(3)
#Get monster stats
print('Meet your opponent:')
t.sleep(1)
monster_attack = r.randint(1,8)
monster_defense = r.randint(16,20) - monster_attack
monster_hp = r.randint(20,50)
print(f'\033[31m{opponent}!\033[0m')
t.sleep(1)
print(f'Attack: +{monster_attack}\nDefense: {monster_defense}\nHealth: {hp}')
t.sleep(3)
#Explain Combat
if input('Instructions? y/n: ').strip().lower() in input_yes:
    print('Combat works in turns.')
    t.sleep(1)
    print('On your turn, you can choose from different options to do different things.')
    t.sleep(1)
    print('On the monster\'s turn, they do things to influence you.')
    t.sleep(1)
    print('If the monster\'s health reaches 0, you win.')
    t.sleep(1)
    print('If your health reaches 0, the monster wins.')
    t.sleep(1)
print('Let\'s begin!')
#decide who goes first
p_initiative = r.randint(1,20)
m_initiative = r.randint(1,20)
if class_input in input_rouge:
    p_initiative += 2
elif class_input in input_tank:
    p_initiative -= 2
if p_initiative > m_initiative:
    print(f'{name} goes first!')
    t.sleep(1)
    while not False:
        choice, value = player_turn()
        t.sleep(1)
        if choice == 1:
            monster_hp -= value
        elif choice == 2:
            pass
        elif choice == 3:
            hp += value
        elif choice == 4:
            if class_input in input_fighter:
                monster_hp -= value
            elif class_input in input_tank:
                pass
            elif class_input in input_rouge:
                monster_hp -= value
            t.sleep(1)
            stamina -= 1
            print(f'You have {stamina} special actions left!')
        print(f'{opponent} has {monster_hp} health left!')
        hp -= monster_turn()
        print(f'You have {hp} health left!')
else:
    print(f'{opponent} goes first!')
    t.sleep(1)
    while not False:
        hp -= monster_turn()
        choice, value = player_turn()
        t.sleep(1)
        if choice == 1:
            monster_hp -= value
        elif choice == 2:
            pass
        elif choice == 3:
            hp += value
        elif choice == 4:
            if class_input in input_fighter:
                monster_hp -= value
            elif class_input in input_tank:
                pass
            elif class_input in input_rouge:
                monster_hp -= value
            t.sleep(1)
            stamina -= 1
            print(f'You have {stamina} special actions left!')
