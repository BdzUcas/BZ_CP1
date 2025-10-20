import time as t
import random as r
import useful_functions as u
input_stocks = ['stocks','invest','1']
input_sell_stocks = ['sell stocks','sell','3']
input_pass = ['skip','pass','4']
input_loan = ['free money','free','2','loan','money','moneys']

print('Hello.')
t.sleep(1.5)
print('Welcome to ....')
t.sleep(2)
print('The bank!')
t.sleep(1)
print('Yes, the bank.')
t.sleep(1.5)
print('Here, we...')
t.sleep(1)
print('Invest!')
t.sleep(1.5)
print('There are lots of ways to "invest" your money.')
t.sleep(1.5)
print('"Investing" works in turns.')
t.sleep(1.5)
print("Let's start!")
t.sleep(2)
turn = 1
money = 100
stock_cost = 5
stocks = 0
stocks_amount = 0
stock_change = 0
loan = 0
loan_turns = 0
owed = 0
while True:
    print(f'Turn {turn}. You have ${money}, and {stocks} stocks.')
    t.sleep(1)
    if stocks > 0:
        stock_change = r.randint(-2,2)
        if stock_cost + stock_change < 1:
            stock_change = r.randint(1,2)
        stock_cost += stock_change
        print(f'The stock value is now {stock_cost}! It changed by {stock_change}.')
        t.sleep(1)
    if loan_turns > 0:
        loan_turns -= 1
        if loan_turns > 0:
            print(f'You have {loan_turns} turns left to return the money!')
        elif loan_turns == 0:
            print('It\'s time! Pay up!')
            t.sleep(1)
            if owed > money:
                print('Looks like you owe a bit too much!')
                t.sleep(1)
                print('Too bad, so sad, you lose.')
                break
            else:
                money -= owed
                owed = 0
                print(f'You now have ${money}.')
        t.sleep(1)
    activity = input('1. "Stocks!" \n2. "Free money!"\n3. Sell Stocks \n4. Pass\n5. End\n').lower().strip()
    if activity in input_stocks:
        print('Welcome to the stock market!')
        t.sleep(2)
        print('Here you can buy stocks in my company.')
        t.sleep(0.5)
        print('I mean-')
        t.sleep(1)
        print('The bank!')
        t.sleep(1)
        stocks_amount = u.int_input(f'How many stocks would you like to buy? They are each ${stock_cost}.\n','That\'s not a number, now is it?')
        #while not False:
        #    stocks_amount = input(f'How many stocks would you like to buy? They are each ${stock_cost}.\n')
        #    if stocks_amount.isdigit():
        #        stocks_amount = int(stocks_amount)
        #        break
        if stocks_amount == 0:
            print('No stocks? Okay then.')
        elif stocks_amount * stock_cost > money:
            print('You can\'t afford that many stocks.')
        else:
            print('Thank you for buying my stocks!')
            money -= stocks_amount * stock_cost
            stocks += stocks_amount
    elif activity in input_sell_stocks:
        print('Here you can sell your stocks!')
        t.sleep(2)
        sell_stocks = u.int_input('How many stocks would you like to sell?\n','That\'s not a number, now is it?')
        if sell_stocks > stocks:
            print('You don\'t have that many stocks!')
        elif sell_stocks == 0:
            print('None? Very well.')
        else:
            print(f'You sold {sell_stocks} for ${sell_stocks * stock_cost}!')
            money += sell_stocks * stock_cost
            stocks -= sell_stocks
    elif activity in input_pass:
        print('You passed this turn.')
        pass
    elif activity in input_loan:
        print('You need some money, ay?')
        t.sleep(2)
        print('While don\'t worry about it! I got you covered.')
        t.sleep(2)
        print('I\'ll give you some right now if you\'ll pay it back later.')
        t.sleep(2)
        print('With interest, of course.')
        t.sleep(1.5)
        loan = u.int_input('So, what\'ll it be?\n','That\'s not a number, now is it?')
        if loan == 0:
            print('No money? Okay then.')
        else:
            print(f'Here\'s your ${loan}. Spend it wisely! I\'ll come collect the return in 5 turns.')
            money += loan
            loan_turns = 6
            owed = loan * 1.5
            t.sleep(3)
            print(f'That\'ll be ${owed} by the way.')
    t.sleep(2)
