import random
import time
first_word = ['Crazy ','Rainbow ','Ultimate ','Incredi','Wimpy ','Awesome ','Interdimensional ','Intimidating ','Forest ','Desert ','Average ','','Zombie ','Robot ','Surprise ','Mystery ','Jeff the ','Winter ','Sneaky ','Evil ','Demon ','Angel ','Death ']
second_word = ['Joe','Cthulu','Goblin','Man','Cat','Destroyer','Fred','Pencil','Beholder','Dog','Cultist','Worm','Muppet','Robot','Cupboard','Beast','Hog','Assasin','Queen','Idol','Bob']
print('Welcome Challenger!')
time.sleep(1)
print('Meet your opponent: ')
time.sleep(1)
opponent = random.choice(first_word) + random.choice(second_word)
print(opponent)
attack = random.randint(1,10)
defense = (10 - attack) + random.randint(-1,2)
enemy_attack = random.randint(1,10)
enemy_defense = (10 - enemy_attack) + random.randint(-1,2)
time.sleep(1)
print(f'Your Stats: Attack = {attack}, Defense = {defense}.')
round = 1
while True:
    print(f'Round {round}')
    time.sleep(2)        
    print(f'{opponent} attacks!')
    time.sleep(1)
    damage = (enemy_attack + random.randint(1,4)) - (defense / random.randint(1,4))
    if damage < 1:
        print(f'{opponent} missed!')
    else:
        print(f'You took {damage} damage!')
