#BZ 1st User Sign In
users = ['bracken','dirk','warren']
user_passwords = ['Fred 123','cool_guy7','1443']
print('Sign In')
yes_replys = ['y','yes','yep','ye','ya','yeah','yea','yop','sure','absolutly','affirmative','positive','cool with me','yees','yyes','yess','yyeess','yyees','yeess','YEAH','yeah, duh','duh','yup','of course','why not?','+','thumbs up!','i suppose','i suppose...','why not','why are there so many valid responses?','yum','waffles','absolutley','yay','yummy','infinite power','good','good with me','good.','nice','ok','okay','yoop','that\'s fine','yo','yeeah','yeaah','yyeah','yeahh','yyeeah','yyeaah','yyeahh','yeeaah','yeeahh','yeaahh','yyeeaah','yyeeahh','yyeaahh','yeeaahh']
while True:
    print('\033[34mInput Username:')
    username = input('\033[0m> ').lower().strip()
    if username in users:
        while True:
            print('\033[34mInput Password:')
            password = input('\033[0m> ')
            if not password in user_passwords:
                print('\033[31mIncorrect password. Try again:')
            else:
                if users.index(username) == user_passwords.index(password):
                    print(f'\033[32mCorrect Password! Welcome to the program, {username}')
                    break
                else:
                    print('\033[31mIncorrect Password. Try again:')
    else:
        print('\033[31mThat account does not exist. Would you like to create it? Y/N:')
        if input('\033[0m> ').lower().strip().replace('!','') in yes_replys:
            print('\033[34mEnter account password:\033[0m')
            password = input('\033[0m> ')
            users.append(username)
            user_passwords.append(password)
            print(f'\033[32mAccount created! Welcome to the program, {username}')

