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
#Define dodge/miss/hit messages
dodges = ['You dodge elegantly.','You dodge, sort of','You bravely defend yourself against the attack!','You try to dodge.','You leap backward in fright','You steel yourself for an attack','You hide - bravely of course','You dodge out of the way of the attack','You run away at full speed','You scream in terror', 'You defend yourself against the incoming attack.']
misses = ['You *almost* hit','You miss!','Your attack misses.','You impressively flourish your blade- oh, oh wow that looks very painful','Your attack misses horribly',"You plunge your blade directly into- that's a tree. Seriously, that's a tree.",'You miss','You miss!','You yell a battle cry! It does nothing.','Nothing happened',f'The {opponent} blocks your attack.','Your attack hits the ground.',f'Whoops, you accidently attacked something else instead. You deal {r.randint(1,10)} damage to the {r.choice(first_word)}{r.choice(second_word)}!']
hits = ['Your attack hits!','Wow! Awesome hit!','Oof- that looks painful.','Your hit lands, sort of.',f'You strike the {opponent} down.']
enemy_hits = ['It hits!','And lands an impressive hit!','Oof- that looks painful.','And it works, sort of.','And it hits perfectly.','And hit!',"Oof- that's a lot of damage.",'and hit!','and lands an impressive attack.',"and it hits, but it wasn't very impressive."]
#Define possible inputs
input_fighter = ['1','fighter','barbarian','smash']
input_tank = ['2','tank','protector','cleric']
input_rouge = ['3','rougue','rouge','roug','roge','rogue','theif','assassin']
input_yes = ['yes','y','yep','yes please','yess','ye']
#Define turn functions
def player_turn():
    print()
#Introduce program
print('Welcome challenger!')
t.sleep(1)
#Get user stats
name = input('Enter your name: ').strip()
class_input = input('Enter your Class:\n1. Fighter\n2. Tank\n3. Rougue\n').lower().strip()
t.sleep(1)
if class_input in input_fighter:
    attack = r.randint(3,6)
    defense = 19 - attack
    hp = 20
elif class_input in input_tank:
    attack = r.randint(1,3)
    defense = 21 - attack
    hp = 30
elif class_input in input_rouge:
    attack = r.randint(4,8)
    defense = 16 - attack
    hp = 15
#i need an else here!
print(f'Stats:\n\033[31m### {name} ###\033[0m\nAttack: +{attack}\nDefense: {defense}\nHealth: {hp}')
t.sleep(3)
#Get monster stats
print('Meet your opponent:')
t.sleep(1)
monster_attack = r.randint(1,8)
monster_defense = r.randint(16,20) - monster_attack
monster_hp = r.randint(15,30)
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
    p_initiative += 1
if p_initiative > m_initiative:
    print(f'{name} goes first!')
    while not False:
        break
else:
    print(f'{opponent} goes first!')
    while not False:
        break