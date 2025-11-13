import time as t
import random as r
def s(time=1):
    t.sleep(time)
def intInput(prompt='',error='Please input an integer!'):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except:
            print(error)
def choiceInput(choices,prompt='',error='Please input a valid choice!'):
    while True:
        value = input(prompt)
        if value in choices:
            return value
        else:
            print(error)
players = {}
classes = {
    'fighter': {
        'health_die': 10,
        'atk': 4,
        'dex': 1,
        'def': 1
    },
    'wizard': {
        'health_die': 8,
        'atk': 3,
        'dex': 2,
        'def': 0
    },
    'tank': {
        'health_die': 12,
        'atk': 2,
        'dex': -1,
        'def': 5
    },
    'rogue': {
        'health_die': 6,
        'atk': 5,
        'dex': 3,
        'def': 0
    }
}
print('Welcome Challengers!')
s()
player_amount = intInput('How many are playing?\n')
s()
for player in range(0, player_amount):
    player_name = input(f'Challenger {player + 1}: Enter your name\n')
    player_class = choiceInput(['fighter','wizard','tank','rogue'],f'Challenger {player + 1}: Choose a class:\n- Fighter\n- Wizard\n- Tank\n- Rogue\n')
    die = classes[player_class]['health_die']
    player_hp = 0
    for i in range(0,4):
        player_hp += r.randint(1,die)
    player_attack = classes[player_class]['atk']
    player_defense = r.randint(15,17) - player_attack + classes[player_class]['dex'] + classes[player_class]['def']
    players[player_name] = {
        'class': player_class,
        'max_hp': player_hp,
        'hp': player_hp,
        'atk': player_attack,
        'def': player_defense,
        'dex': classes[player_class]['dex']
    }
print(players)
