#BZ 1st Crew Shares
print("The crew earned a whole bunch of money on the last outing, but the captain didn't have time to divvy it all up before release everyone to port. He gave each member of the crew 500 dollars for the evening and then sat down with his first mate to properly divide the shares. ")
while True:
    crew = input("\033[0mHow many crew members are there? \033[32m").strip()
    if crew.isdigit():
        break
    else:
        print("\033[31mThat is not a valid input. Please make it a number.")

while True:
    money = input("\033[0mHow much money has the crew made? \033[32m").strip()
    if not money.replace('.','').isdigit():
        print("\033[31mThat is not a valid input. Please make it a number.")
    else:
        money = float(money)
        crew = int(crew)
        if money >= 500 * (crew + 10):
            #At least 500 for each of the crew plus the captain and first mate
            break
        else:
            print(f"\033[31mThat is not a valid input. Please make it at least {500 * (crew + 10)}.")
# 1 share for each of the crew, plus 7 for the captain and 3 for the first mate
share = money / (crew + 10)
captain_share = share * 7
first_mate_share = share * 3
crew_share = share - 500
print(f"\033[0mCrew number: \033[34m{crew + 2}")
print(f"\033[0mMoney earned: \033[34m{money:.2f}")
print(f"\033[0mCaptains share: \033[34m{captain_share:.2f}")
print(f"\033[0mFirst Mate's share: \033[34m{first_mate_share:.2f}")
print(f"\033[0mRemaining share per crew member: \033[34m{crew_share:.2f}")