import random

guessed_number = -1
play_again = bool(True)
ask_user = ""
lives = 10
print("Welcome to Random Number Guesser!")
print("You have 10 lives at the beginning.")

while (play_again):
    random_number = random.randrange(1, 100)
    lives = 10
    print("A new random number has been generated.")

    while (lives > 0):
        guessed_number = int(input("Guess a number between 1 - 100: "))

        if (guessed_number < random_number):
            lives -= 1
            print("Go higher! You have", lives, "lives left.")
            continue
        elif (guessed_number > random_number):
            lives -= 1
            print("Go lower! You have", lives, "lives left.")
        else:
            print("Correct!", guessed_number, "was the correct guess.")
            break

    if lives == 0:
        print("You lose. :(")

    ask_user = input("Do you want to play again? Type Yes or No: ").lower()

    if (ask_user == "yes"):
        play_again = True
    else:
        play_again = False
        print("See you next time!")
