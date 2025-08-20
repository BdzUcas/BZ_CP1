#BZ 1st Hello World
# Lists the Admin Users
admins = ['bracken', 'Bracken', 'BDZ', 'bdz', 'Ms. LaRose', 'Ms. larose', 'Ms. Larose', 'Ms LaRose', 'Ms larose', 'Ms Larose']
# Declares the Users list
users = []
# Declares the Exit variable
exit = 0
# Code runs while Exit is equal to 0
while exit == 0:
    # Asks the user for their name.
    print("What is your name?")
    name = input()
    # If they input "End" than set exit to 1, ending the while loop
    if name == "End":
        exit = 1
    # If the name they input is an admin user, outputs Hello Admin User (whatever they input as their name)
    elif name in admins:
        print("Hello Admin User " + name)
    # If they are listed as a user, outputs Hello Again (whatever they input as their name)
    elif name in users:
        print("Hello again " + name)
    # If none of those are true, outputs Hello (whatever they input as their name), and then adds them to the list of users.
    else:
        print("Hello " + name)
        users.append(name)
    #an unused input function that prompts "Press Enter to continue" with green text. Just to create a pause before asking their name again.
    input("\033[1;32mPress Enter to continue\033[0m")
#Outside of the while loop, prints "See you next time!" In red
print('\033[31mSee you next time!\033[0m')
