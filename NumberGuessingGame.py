import random

lowestNum = 1
highestNum = 100
answer = random.randint(lowestNum, highestNum)

guesses = 0
isRunning = True

print ("PYHTON NUMBER GUESSING GAME")
print (f"Select the number between {lowestNum} and {highestNum}")

while isRunning:

    guess = input ("Enter your guess: ")

    if (guess.isdigit()):

        guess = int(guess)
        guesses += 1

        if(guess < lowestNum or guess > highestNum):

            print("The number is out of the range")
            print (f"Please Select the number between {lowestNum} and {highestNum}")

        elif (guess < answer): 

            print ("Too low! Try again!")

        elif (guess > answer):

            print ("Too high! Try again!")

        else:

            print (f"CORRECT! the answer was {answer}")
            print (f"Number of guesses: {guesses}")
            isRunning = False
        
    else:

        print("Invalid guess :()")
        print (f"Please Select the number between {lowestNum} and {highestNum}")
