#BZ 1st Order Up!
#import libraries

#Add meal size options (meal, large meal, family meal)
menu = {
    'meal': ['entree','side','side','drink'],
    'large meal': ['entree','entree','side','side','drink'],
    'family meal': ['entree','entree','entree','entree','entree','side','side','side','side','side','drink','drink','drink','drink','drink']
}
#Add options for each type item (entree, side, drink) associated with their prices and per time of day
entree = {
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
        ''
    }
}
breakfast_entree = {
    'egg sandwich': 5.00,
    'breakfast burrito': 4.00,
    'scrambled eggs': 3.00,
    'pancakes': 3.00,
    'waffles': 3.50,
    'oatmeal': 2.00,
    'cinnamon roll': 4.00
}
breakfast_side = {
    'boiled egg': 1.00,
    'cereal': 1.50,
    'fries': 1.00,
    'bacon': 1.00,
    'sausage': 1.00,
    'biscuits': 2.00,
    'biscuits and gravy': 2.50,
    'toast': 1.50
}
breakfast_drink = {
    'water': 0.50,
    'juice': 1.00,
    'milk': 1.00,
    'soda': 1.50,
    'coffee': 1.50
}

#prompt user to select meal, large meal, or family meal
#loop through items in choice
    #display choices for item based on time of day
    #prompt user to choose one
    #add chosen item to order
#set price to 0
#prompt user to add a tip
#add tip amount to price
#loop through items in order
    #Display item and its cost
    #add cost of item to total 
#display total price
#thank user for ordering