#Python application to simulate a dictionary
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if(word.lower() in data):
        return data[word.lower()]
    elif(word.upper() in data):
        return data[word.upper()]
    elif(word.title() in data):
        return data[word.title()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("Enter y for yes and n for no")
        if(decide == 'y' or decide == 'Y'):
            return data[get_close_matches(word, data.keys())[0]]
        elif(decide == 'n' or decide == 'N'):
            return "Enter a valid word"
    else:
        return "Enter a valid word"

word = input("Enter the word you want to search --->")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(word)
