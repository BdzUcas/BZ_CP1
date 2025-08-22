#BZ 1st Who are you?
print('\033[31m###     User Information Program Initiated     ###')
print('### Type "End" in continue prompt to terminate ###')
users = []
exit = True
while exit:
    name = input("\033[33m### Input User Name > ")
    age = input("### Input User Age > ")
    color = input("### Input User Color > ")
    print("\033[31m ### Is this information correct: User " + name + ", of age " + age + ", with favorite color " + color + "?")
    continue_prompt = input("Enter to continue with this information, 1 to delete this information, or End to terminate program > ")


    