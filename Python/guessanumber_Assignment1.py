# 1)Write a python function named GuessANumber(), in which you build a number
# guessing game. The game asks the player to start guessing the number. Every time
# player fails to guess the secret number, the game prints a message letting the player
# know if the guess was too low or too high. The ask to play again. It should also let
# player quit the game by typing "quit".
# -If player guesses the secret number before the count limit of 10 is reached, the game
# prints a victory message. Otherwise, prints some a 'sorry' message.
# -It should let player choose to play another game or quit the game altogether.

# The function starts like this:

# def GuessANumber():
# 	import random   # this is to use random numbers. We talk more about it later
# 	secretNumber = random.randint(3, 30) # generates a random int between 3 and 30
# 	guessCountLimit = 5


# Don't forget to call the function in the script, so it get executed when you call the script.
# You put the above function in a python script named "guessANumberGame.py".


from random import randint

def GuessANumber():
    secretNumber = randint(1, 10)
    print('Welcome to the number guessing game!!!\nYou have 10 attempts to guess the secret number correctly.\nGOOD LUCK!\n')

    for chances in range(10):
        player_guess = input("Guess the number (or type 'quit' to exit): ").lower()

        if player_guess == 'quit':
            print('Thank you for playing!')
            return

        if player_guess.isdigit():
            player_guess = int(player_guess)
            if player_guess == secretNumber:
                print("Congratulations, you guessed the right number!!!\n")
                if input("Would you like to play again? (Yes/No): ").lower() == 'yes':
                    GuessANumber()
                return
            else:
                print("Too high!" if player_guess > secretNumber else "Too low!")
        else:
            print("Invalid input. Please enter a number or 'quit'.")

    print(f"You've used all your attempts! The correct answer was {secretNumber}")

GuessANumber()
