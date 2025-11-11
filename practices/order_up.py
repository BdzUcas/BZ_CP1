#BZ 1st Order Up!
#import libraries
import time
from datetime import datetime
#Add meal size options (meal, large meal, family meal)
menu = {
    'meal': ['entree','side','side','drink'],
    'large meal': ['entree','entree','side','side','drink'],
    'family meal': ['entree','entree','entree','entree','entree','side','side','side','side','side','drink','drink','drink','drink','drink']
}
#Add options for each type item (entree, side, drink) associated with their prices and per time of day
items = {
    'entree': {
        'breakfast': {
            'egg sandwich': 5.00,
            'breakfast burrito': 4.00,
            'scrambled eggs': 3.00,
            'pancakes': 3.00,
            'waffles': 3.50,
            'oatmeal': 2.00,
            'cinnamon roll': 4.00
        },
        'lunch': {
            'deli sandwich': 5.00,
            'nachos': 3.00,
            'tba': 5.00,
            'tomato soup': 2.50,
            'tacos': 4.00,
            'grilled cheese': 3.00,
            'hamburger': 3.50
        },
        'dinner': {
            'steak': 8.00,
            'tacos': 4.00,
            'chicken soup': 3.00,
            'grilled cheese': 3.00,
            'hamburger': 3.50
        },
        'illegal': {
            'the souls of your enemies': 10.00,
            'unlimited power': 15.00,
            'fred': 10.00,
            'hot (totally not real) dog': 5.00
        }
    },

    'side': {
        'breakfast': {
            'boiled egg': 1.00,
            'cereal': 1.50,
            'fries': 1.00,
            'bacon': 1.00,
            'sausage': 1.00,
            'biscuits': 2.00,
            'biscuits and gravy': 2.50,
            'toast': 1.50
        },
        'lunch': {
            'fries': 1.00,
            'fruit': 1.00,
            'muffin': 1.50,
            'cheese curds': 1.50,
            'onion rings': 2.00
        },
        'dinner': {
            'fries': 1.50,
            'dinner roll': 1.00,
            'onion rings': 2.50,
            'mashed potatoes': 3.00,
            'meatballs': 1.00
        },
        'illegal': {
            '"totally not real" eyeballs': 5.00,
            "how'd you get here anyway?": 4.00,
            'lava chicken': 3.00
        }
    },
    'drink': {
        'breakfast': {
            'water': 0.50,
            'juice': 1.00,
            'milk': 1.00,
            'soda': 1.50,
            'coffee': 1.50
        },
        'lunch': {
            'water': 0.50,
            'chocolate milk': 1.50,
            'milk': 1.00,
            'soda': 1.50,
            'coffee': 1.50
        },
        'dinner': {
            'water': 1.00,
            'hot chocolate': 2.00,
            'milk': 1.50,
            'soda': 2.00,
            'coffee': 2.00
        },
        'illegal': {
            '"water"': 1.00,
            'assorted juices': 2.00,
            '"cow" milk': 1.50,
            'mayonnaise': 2.00,
            'coughee': 2.00
        }
        
    }
}
#loop forever
while True:
    #prompt user to select meal, large meal, or family meal
    meal = input('Would you like a meal, large meal, or family meal?\n').lower().strip()
    #if they selected a valid option
    if meal in ['meal','large meal','family meal']:
        #end loop
        break
    #otherwise
    else:
        #tell them to pick a valid option
        print('Please select a valid input!')
#determine time of day
hour = float(datetime.now().strftime('%H'))
if hour <= 9 and hour > 0:
    tod = 'breakfast'
elif hour > 9 and hour <= 13:
    tod = 'lunch'
elif hour > 13 and hour <= 23:
    tod = 'dinner'
else:
    tod = 'illegal'
order = []
cost = 0
#loop through items in choice
for item in menu[meal]:
    #tell user to pick an option
    print(f'\nSelect a {item}:')
    #loop through potential options for item type based on time of day
    options = items[item][tod].keys()
    for option in options:
        #display option and price
        print(f'{option.capitalize()}: ${items[item][tod][option]}')
    #loop forever
    while True:
        #take user input
        choice = input().lower().strip()
        #if it is a valid choice
        if choice in options:
            #end loop
            break
        #otherwise
        else:
            #tell user to pick a valid option
            print('Please pick a valid choice!')
    #add chosen item to order
    order.append([choice,items[item][tod][option]])
    #add item's cost to total cost
    cost += items[item][tod][option]
#loop forever
while True:
    #prompt user to add a tip
    print('How much would you like to tip?')
    #take user input
    tip = input()
    #if input is "no"
    if tip in ['no','no thanks','no thank you']:
        #set tip to 0
        tip = 0
        #exit loop
        break
    #otherwise, if tip is a number
    elif tip.replace('.','').isdigit():
        #exit loop
        break
    #otherwise
    else:
        #tell user to input a number
        print('Please input a number!')
#add tip amount to price
cost += int(tip)
print('Your order:')
#loop through items in order
for order_item in order:
    #Display item and its cost
    print(f'{order_item[0].capitalize()}: {order_item[1]}')
print(f'Tip: {tip}')
#display total price
print(f'Total: {cost}')
#thank user for ordering
print('Thanks for ordering!')