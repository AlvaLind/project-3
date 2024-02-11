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

