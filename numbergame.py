import random

def startGame():
    num = random.randint(1,9)
    guesses = 5
    guess = 0
    while guesses != 0:
        guess = input("Pick a number from 1 to 9: ")

        if str(num) == guess:
            print(" ")
            print("Congratulations! You guessed the number!")
            print(" ")
            guesses = 0
        else:
            guesses = guesses - 1
            if guesses == 1:
                print("Wrong number! You still have 1 guess left.")
            else:
                print("Wrong number! You still have",guesses,"guesses left.")
    if str(num) != guess:
        print(" ")
        print("Oh no! You lose!")
        print("The correct number was ",str(num)," !")


startGame()