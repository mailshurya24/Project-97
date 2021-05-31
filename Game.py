#Ma'am I am sorry but I am having some trouble with my VS Code app. Could you please evaluate my code?
import random
correct = random.randint(1,9)
gameOver = False

while gameOver == False:
    guess = int(input("Enter your guess"))
    if guess == correct:
        print("You Win! Your Guess is Correct!")
        gameOver = True
    elif guess > correct:
        print("Your number is greater than the correct number. Guess Again!")
    elif guess < correct:
        print("Your number is lesser than the correct number. Guess Again!")