#BZ 1st Formatting outputs notes
name = 'Grant'
age = 98989898
dollars = 2.3
#Theres tons of stuff you can do with the format method!
print("Hello {}, you are {:,}. Youth is wasted on the young. WOW! You have ${:.2f}? YOU MUST BE RICH!".format(name, age, dollars))
#                          ^adds commas to numbers every 3 places               ^rounds to 2 decimal places

#YAY F-STRINGS This does the same thing
print(f'Hello {name}, you are {age:,}. Youth is wasted on the young. WOW! You have ${dollars:.2f}? YOU MUST BE RICH!')
#    f^    ^string    brackets^  ^variables                                                   ^format colons