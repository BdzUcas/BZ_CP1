#BZ 1st Rock Paper Scissors
import random as r
scissors = """
 o  o
  \\/
  /\\"""
rock = """
 /‾‾‾\\
 \\___/"""
paper = """
 |‾‾‾|
 |   |
 |___|"""
black_hole = """


        """
choices = ['There was an error!',rock,paper,scissors,black_hole]
choices_strings = ['There was an error!','rock','paper','scissors','black hole']
actions = ['There was an error!',' smashed ',' smothered ',' snipped ',' consumed ']
rock_choices = ['rock','r','stone',rock,'smash','rock smash','destroy','obliterate']
scissors_choices = ['scissors','s','cut','snippy snip','snip']
paper_choices = ['paper','p','flap','flimsy','cover','papercut']
exit = True
while exit:
    while not False:
        choice = input('Rock, paper, scissors, or exit?\n').replace('!','').strip().lower()
        computer_choice = r.randint(1,3)
        if choice in rock_choices:
            choice = 1
            break
        elif choice in paper_choices:
            choice = 2
            break
        elif choice in scissors_choices:
            choice = 3
            break
        elif choice == 'black hole':
            choice = 4
            break
        elif choice == 'exit':
            print('Exited Program!')
            exit = False
            break
        else:
            print('Please input a valid choice!')
    if choice == 'exit':
        continue
    print(f'{choices[choice]} \n vs. {choices[computer_choice]}')
    if choice == 4:
        print(f'Their {choices_strings[computer_choice]}{actions[computer_choice]}your {choices_strings[choice]}!')
    elif choice - 1 == computer_choice:
        print(f'Your {choices_strings[choice]}{actions[choice]}their {choices_strings[computer_choice]}!')
    elif computer_choice - 1 == choice:
        print(f'Their {choices_strings[computer_choice]}{actions[computer_choice]}your {choices_strings[choice]}!')
    elif computer_choice == 1 and choice == 3:
        print(f'Their {choices_strings[computer_choice]}{actions[computer_choice]}your {choices_strings[choice]}!')
    elif choice == 1 and computer_choice == 3:
        print(f'Your {choices_strings[choice]}{actions[choice]}their {choices_strings[computer_choice]}!')
    elif choice == computer_choice:
        print('It\'s a tie!')
    else:
        print('An error occured.')
