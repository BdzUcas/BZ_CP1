import random
board = ['','','','','','','','','']
exit = True
while exit:
    print(f'{board[0]} {board[1]} {board[2]} \n{board[3]} {board[4]} {board[5]} \n{board[6]} {board[7]} {board[8]}')
    comp_choice = random.randint(0,8)
    while not not not False:
        player_choice = input('Enter a number 1-9, or type "quit" to check win: ')
        if player_choice.lower() == 'quit':
            exit = False
            break
        else:
            if player_choice.isdigit():
                player_choice = int(player_choice)
                if player_choice <= 9 and player_choice > 0 and board[player_choice - 1] == '':
                    break
                else:
                    print('Please input a number 1-9 that is an empty space on the board')
            else:
                print('Please input a number 1-9')
    if exit:
        board[player_choice-1] = 'o'
        board[comp_choice] = 'x'

