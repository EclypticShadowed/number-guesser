# imports random
from random import randint
def easy():
        lives = 8
        num = randint(1,100)
        score = 0
        print("I have my number")
        guess = input("What number am I thinking of: ")
        while int(guess) != num:
                lives = lives -1
                guess = int(guess)
                if num < guess:
                        print("The number is lower")
                else:
                        print("The number is higher")
                guess = input ("What number am i thinking of: ")
                if lives == 0:
                        print("Game Over, my number was " + str(num))
                        main_menu()
        if int(guess) == num:
                if lives > 1:
                        score = int(score) + 400*int(lives)
                else:
                        score = int(score) + 400
                print("Congrats you won, you scored: " + str(score) + " points")
                
                
def medium():
        lives = 5
        num = randint(1,100)
        score = 0
        print("I have my number")
        guess = input("What number am I thinking of: ")
        while int(guess) != num:
                lives = lives -1
                guess = int(guess)
                if num < guess:
                        print("The number is lower")
                else:
                        print("The number is higher")
                guess = input ("What number am i thinking of: ")
                if lives == 0:
                        print("Game Over, my number was " + str(num))
                        main_menu()
        if int(guess) == num:
                if lives > 1:
                        score = score + 400*int(lives)*3
                else:
                        score = score + 400
                print("Congrats you won, you scored: " + str(score) + " points")
                
def hard():
        lives = 3
        num = randint(1,100)
        score = 0
        print("I have my number")
        guess = input("What number am I thinking of: ")
        while int(guess) != num:
                lives = lives -1
                guess = int(guess)
                if num < guess:
                        print("The number is lower")
                else:
                        print("The number is higher")
                guess = input ("What number am i thinking of: ")
                if lives == 0:
                        print("Game Over, my number was " + str(num))
                        main_menu()
        if int(guess) == num:
                if lives > 1:
                        score = score + 400*int(lives)*6
                else:
                        score = score + 400
                print("Congrats you won, you scored: " + str(score) + " points")
                
def main_menu():
        print("Welcome to the number guessing game.\n I will be thinking of a number between 1 and 100.\n you will have a set amount of chances to guess my number")
        print("The number of guesses will be determined by what difficulty you choose.\n You can choose from easy medium or hard.")
        print("In easy you get 8 guesses, in medium you get 5 and in hard you get 3.")
        diff = input("Please pick a difficulty: ")
        while diff == "":
                print("Invalid option")
                diff = input("Please pick a difficulty: ")
        if diff.lower() == "easy":
            easy()
        elif diff.lower() == "medium":
                medium()
        else:
                hard()
main_menu()
