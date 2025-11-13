#BZ 1st Order Up!
#import libraries
import time as t
from datetime import datetime
import random as r
#define functions
#tip input function
def get_tip():
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
    return tip
#price calculator function
def finalize_price(order, cost):
    #get tip amount
    tip = get_tip()
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
    return cost
#get time of day function
def get_daytime():
    #get hour as a float
    hour = float(datetime.now().strftime('%H'))
    #if hour is between 1 and 10 am
    if hour <= 9 and hour > 0:
        #set time of day to breakfast
        tod = 'breakfast'
    #if hour is between 10 am and 2 pm
    elif hour > 9 and hour <= 13:
        #set time of day to lunch
        tod = 'lunch'
    #if hour is between 2 pm and 12 am
    elif hour > 13 and hour <= 23:
        #set time of day to dinner
        tod = 'dinner'
    #otherwise (hour will be between 12 and 1 am)
    else:
        #set time of day to illegal
        tod = 'illegal'
    #return time of day
    return tod

#option choosing function
def choose_option(item,tod):
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
            #end loop and return choice
            return choice
        #otherwise
        else:
            #tell user to pick a valid option
            print('Please pick a valid choice!')

#meal choice function
def mealChoice():
    #loop forever
    while True:
        #prompt user to select meal, large meal, or family meal
        meal = input('Would you like a meal, large meal, or family meal?\n').lower().strip()
        #if they selected a valid option
        if meal in ['meal','large meal','family meal']:
            #return meal they chose
            return meal
        #otherwise
        else:
            #tell them to pick a valid option
            print('Please select a valid input!')

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
            'hot dog (not actually a dog)': 5.00
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
            '"candy" eyeballs': 5.00,
            "... ... steak!": 4.00,
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
            'cow... milk': 1.50,
            'mayonnaise': 2.00,
            'coughee': 2.00
        }
        
    }
}

#greetings list
greetings = {
    'breakfast': ['Good morning! What would you like to order?','Nice morning, isn\'t it? What would you like?', 'Good morning, or whatever. What do you want?'],
    'lunch': ['Good afternoon! What would you like to order?','Bit hot, isn\'t it? What would you like to eat?','Afternoon, er, do you want something?'],
    'dinner': ['Good evening! What would you like to order?','Bit chilly, no? What would you like for dinner?','Erm, just take the food.'],
    'illegal': ['You\'re here late! While, lucky for you we offer 24 hour service!','Bit late for food, don\'t you think? Well, if you insist...','Hello, umm... welcome to... wendy\'s or something. We\'re, er, closed. Maybe. That sounds right.']
    
}

tod = get_daytime()
#welcome the user to the program with a different message randomly selected from the messages for the time of day 
print(r.choice(greetings[tod]))
#get user meal size choice
meal = mealChoice()
#reset order and cost variables
order = []
cost = 0
#loop through items in meal choice
for item in menu[meal]:
    #have user pick an option
    choice = choose_option(item,tod)
    #add chosen item to order
    order.append([choice,items[item][tod][choice]])
    #add item's cost to total cost
    cost += items[item][tod][choice]
#display order and finalize price
cost = finalize_price(order, cost)
#thank user for ordering
print('Thanks for ordering!')