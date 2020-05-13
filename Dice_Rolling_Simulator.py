#Program to create a dice rolling simulator
import random
print("This is a program to simulate dice rolling game")

answer = "y"

while (answer == "y" or answer == "Y"):
    x = random.randint(1,6)
    if(x == 1):
        print(" ----------")
        print("|          |")
        print("|     0    |")
        print("|          |")
        print(" ----------")

    elif(x == 2):
        print(" ----------")
        print("|          |")
        print("|   0  0   |")
        print("|          |")
        print(" ----------")

    elif(x == 3):
        print(" ----------")
        print("|          |")
        print("|  0  0  0 |")
        print("|          |")
        print(" ----------")

    elif(x == 4):
        print(" ----------")
        print("|    0    |")
        print("|  0    0 |")
        print("|    0    |")
        print(" ----------")

    elif(x == 5):
        print(" ----------")
        print("|    0     |")
        print("|  0 0 0   |")
        print("|    0     |")
        print(" ----------")

    elif(x == 6):
        print(" ----------")
        print("|   0 0 0   |")
        print("|           |")
        print("|   0 0 0   |")
        print(" ----------")

    answer = (str)(input("enter y to keep rolling else n to exit rolling ----->   "))

print("Thank you for playing the dice game")
