# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random 

print("Welcome! The theme of this game is countries. Let's play hangman!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

gameWords = ["australia","sweden","finland", "norway", "denmark", "poland", "ireland", "spain", "italy", "portugal", "greece", "albania", "ukrain", "switzerland", "cyprus", "argentina", "mauritius", "canada", "usa", "mexico", "morocco", "brazil", "chile", "philippines", "new Zealand", "qatar", "estonia", "france", "singapore", "germany", "guatemala", "turkey", "jordan", "syria", "japan", "china"]

"""
Shuffle a random word from gameWords
"""
pickWord = random.choice(gameWords)

for x in pickWord:
    print("_", end = " ")

def create_hangman(incorrect):
    if (incorrect == 0):
        print("\n +-----+")
        print("       |")
        print("       |")
        print("       |")
        print("       |")
        print("      /|\")
        print("---------")
    elif(incorrect == 1):
        print("\n +-----+")
        print(" O     |")
        print("       |")
        print("       |")
        print("       |")
        print("      /|\")
        print("---------")
    elif(incorrect == 2):
        print("\n +-----+")
        print(" O     |")
        print(" |     |")
        print("       |")
        print("       |")
        print("      /|\")
        print("---------")
    elif(incorrect == 3):
        print("\n +-----+")
        print(" O     |")
        print(" |\    |")
        print("       |")
        print("       |")
        print("      /|\")
        print("---------")
    elif(incorrect == 4):
        print("\n +-----+")
        print(" O     |")
        print("/|\    |")
        print("       |")
        print("       |")
        print("      /|\")
        print("---------")
    elif(incorrect == 5):
        print("\n +-----+")
        print(" O     |")
        print("/|\    |")
        print("/      |")
        print("       |")
        print("      /|\")
        print("---------")
    elif(incorrect == 6):
        print("\n +-----+")
        print(" O     |")
        print("/|\    |")
        print("/ \    |")
        print("       |")
        print("      /|\")
        print("---------")