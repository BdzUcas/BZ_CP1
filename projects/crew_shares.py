#BZ 1st Crew Shares
#The \033[0m are to change text colors
print("\033[0mThe crew earned a whole bunch of money on the last outing, but the captain didn't have time to divvy it all up before release everyone to port. He gave each member of the crew 500 dollars for the evening and then sat down with his first mate to properly divide the shares. ")
#While loops with break statements when a valid input is given
while True:
    #Takes an input, strips it and removes commas and periods
    crew = input("\033[0mHow many crew members are there (not including the captain and first mate)? \033[32m\n").strip().replace('.','').replace(',','')
    if crew.isdigit():
        crew = int(crew)
        if crew > 99:
            print("\033[31mThat's absurd, please input something reasonable.")
        else:
            break
    else:
        print("\033[31mThat is not a valid input. Please make it a number.")

while True:
    money = input("\033[0mHow much money has the crew made? \033[32m\n").strip().replace(',','')
    if not money.replace('.','').isdigit():
        print("\033[31mThat is not a valid input. Please make it a number.")
    else:
        money = float(money)
        if money >= 500 * (crew + 10):
            #At least 500 for each of the crew plus the captain and first mate
            if money / (crew + 10) >= 100000:
                print("\033[31mThat's absurd, please input something reasonable.")
            else:
                break
        else:
            print(f"\033[31mThat is not a valid input. Please make it at least {500 * (crew + 10)}.")
# 1 share for each of the crew, plus 7 for the captain and 3 for the first mate
#Calulates everything and rounds it to 2 decimal places
money = round(money, 2)
share = money / (crew + 10)
captain_share = round(share * 7, 2)
first_mate_share = round(share * 3, 2)
crew_share = round(share - 500, 2)
#Outputs everything
print(f"\033[0mCrew number: \033[34m{crew + 2}")
print(f"\033[0mMoney earned: \033[34m{money}")
print(f"\033[0mCaptains share: \033[34m{captain_share}")
print(f"\033[0mFirst Mate's share: \033[34m{first_mate_share}")
print(f"\033[0mRemaining share per crew member: \033[34m{crew_share}\033[0m")