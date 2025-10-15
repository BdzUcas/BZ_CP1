import time as t
import random as r
input_stocks = ['stocks','invest','1']
input_sell_stocks = ['sell stocks','sell','3']
input_pass = ['skip','pass','4']
print('Hello.')
t.sleep(2)
print('Welcome to ....')
t.sleep(2)
print('The bank!')
t.sleep(1)
print('Yes, the bank.')
t.sleep(2)
print('Here, we...')
t.sleep(1)
print('Invest!')
t.sleep(2)
print('There are lots of ways to "invest" your money.')
t.sleep(2)
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
while True:
    print(f'Turn {turn}. You have ${money}, and {stocks} stocks.')
    t.sleep(1)
    if stocks > 0:
        stock_change = r.randint(-2,2)
        if stock_cost + stock_change < 1:
            stock_change = 0
        stock_cost += stock_change
        print(f'The stock value is now {stock_cost}! It changed by {stock_change}.')
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
        while not False:
            stocks_amount = input(f'How many stocks would you like to buy? They are each ${stock_cost}.\n')
            if stocks_amount.isdigit():
                stocks_amount = int(stocks_amount)
                break
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
        while not False:
            print('How many stocks would you like to sell?')
            sell_stocks = input()
            if sell_stocks.isdigit():
                sell_stocks = int(sell_stocks)
                break
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
    t.sleep(2)
