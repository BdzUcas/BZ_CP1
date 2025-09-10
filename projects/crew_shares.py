#BZ 1st Crew Shares
print("The crew earned a whole bunch of money on the last outing, but the captain didn't have time to divvy it all up before release everyone to port. He gave each member of the crew 500 dollars for the evening and then sat down with his first mate to properly divide the shares. ")
while True:
    crew = ("How many crew members are there? ").strip()
    if crew.isdigit():
        break
    else:
        print("That is not a valid input. Please make it a number.")
