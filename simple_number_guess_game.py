print("Hello and welcome to the number guessing game.\nIn this game you have to guess a number within the specified range(the range will also be defined by you),\nThe program will notify you whether your guess is lower or higher than the number you have to guess.")
import random
start=int(input("Please enter the starting point of the range: "))
end=int(input("Please enter the end point of the range(it will also be included): "))
a=random.randint(start,end)
while True:
    guess=int(input("Please enter your guessed number: "))
    if a==guess:
        print("You guessed the correct number that is:",a)
        break
    elif a>guess:
        print("Your guess is lower than the number.")
    else:
        print("Your guess is higher than the number.")