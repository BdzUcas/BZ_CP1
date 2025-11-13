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
print('Welcome Challengers!')
s()
player_amount = intInput('How many are playing?\n')
s()
for player in range(0, player_amount):
    player_name = input(f'Challenger {player + 1}: Enter your name\n')
    player_class = choiceInput(['fighter','wizard','tank','rogue'],f'Challenger {player + 1}: Choose a class:\n- Fighter\n- Wizard\n- Tank\n- Rogue\n')
    players[player_name] = {
        'class': player_class
    }
