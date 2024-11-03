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
