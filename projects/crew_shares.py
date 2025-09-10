#BZ 1st Crew Shares
print("The crew earned a whole bunch of money on the last outing, but the captain didn't have time to divvy it all up before release everyone to port. He gave each member of the crew 500 dollars for the evening and then sat down with his first mate to properly divide the shares. ")
while True:
    crew = input("How many crew members are there? ").strip()
    if crew.isdigit():
        break
    else:
        print("That is not a valid input. Please make it a number.")

while True:
    money = input("How much many has the crew made? ").strip()
    if not money.replace('.','').isdigit():
        print("That is not a valid input. Please make it a number.")
    else:
        money = float(money)
        crew = int(crew)
        if money >= (501 * crew) + 2:
            #At least 500 for each of the crew plus shares of at least one dollar for the crew, captain, and first mate
            break
        else:
            print("That is not a valid input. Please add more money.")
# 1 share for each of the crew, plus 7 for the captain and 3 for the first mate
share = (money - (500 * crew)) / (crew + 10)
captain_share = share * 7
first_mate_share = share * 3