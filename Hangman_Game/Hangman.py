#This is an application to simulate the popular word game hangman
import random
import json

print("Welcome to hangman")

def hangman(word):

    turns = 0
    valid_letters = "abcdefghijklmnopqrstuvwxyz"
    guess_made = ''

    print("Hidden word - " + word)
    while (len(word) > 0):
        main = ''   #The visible word after every guess
        for letter in word:
            if letter in guess_made:
                main = main + letter
            else:
                main = main + '-' + ""

        if main == word:
            print(main + "is the word. You win !!!")
            break

        print("Guess the word " + main)
        guess = input()

        if(guess in valid_letters):
            guess_made = guess_made + guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            turns = turns - 1
            if(turns == 9):
                print("9 turns left")
            if(turns == 8):
                print("8 turns left")
            if(turns == 7):
                print("7 turns left")
            if(turns == 6):
                print("6 turns left")
            if(turns == 5):
                print("5 turns left")
            if(turns == 4):
                print("4 turns left")
            if(turns == 3):
                print("3 turns left")
            if(turns == 2):
                print("2 turns left")
            if(turns == 1):
                print("1 turns left")
            if(turns == 0):
                print("You lose !!!!")

name = input("Enter your name")
print("Welcome " + name)
print("Try to guess the word in less than 10 attempts")
data = json.load(open("data.json"))
key_pair = random.choice(list(data.items()))    #key_pair is a list now
word = key_pair[0]
print(word)
hangman(word)
