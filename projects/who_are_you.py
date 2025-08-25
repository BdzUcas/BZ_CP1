#BZ 1st Who are you?
print('\033[31m###     User Information Program Initiated     ###')
print('### Type "End" in continue prompt to terminate ###')
users = []
exit = True
while exit:
    prompt = "1"
    name = input("\033[33m### Input User Name  > ")
    for i in users:
        if i.get("name") == name:
            print("\033[31m### You have already input information. Would you like to change it?")
            print("### Current information: Age " + i.get("age") + ", with favorite color " + i.get("color") + ".")
            prompt = input("\033[33m### Enter to continue with current information, 1 to override it. > ")
            break
    if prompt == "1":
        age = input("### Input User Age   > ")
        color = input("### Input User Color > ")
        print("\033[31m### Is this information correct: User " + name + ", of age " + age + ", with favorite color " + color + "?")
        prompt = input("\033[33m### Enter to continue with this information, 1 to delete this information, or End to terminate program > ")
    else:
        prompt = input("\033[33m### Continuing with current information. Type End to terminate, or press enter to continue > ")
    if prompt == "End":
        exit = False
    elif prompt == "1":
        print("\033[31m### Deleted information. Input new information below")
    else:
        user_info = {"name": name, "age": age, "color": color}
        users.append(user_info)
print("\033[32m### Program Terminated")