#BZ 1st Fix the Game
import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        guess = input("Enter your guess: ")
        #i caused an error here by trying to surround the input() in a int() so it crashed if you entered a string
        attempts += 1
        #It wasn't actully increasing the attempts at all (logic error)
        if not guess.isdigit():
            print('Please enter a number')
        else:
            guess = int(guess)
            if attempts >= max_attempts:
                print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
                game_over = True
            elif guess == number_to_guess:
            #this wasn't actulaly an elif before (logic error)
                print("Congratulations! You've guessed the number!")
                game_over = True
            elif guess > number_to_guess:
             #This was causing a runtime error because it was comparing a string and an integer. i fixed it by adding lines 15-18
                print("Too high! Try again.")
            elif guess < number_to_guess:
                print("Too low! Try again.")  
            #continue was redundant (logic error)
    print("Game Over. Thanks for playing!")
start_game()