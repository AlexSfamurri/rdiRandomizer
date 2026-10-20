from random import *

class Deck:
    def __init__(self):
        self.deck = []

    def getDeck(self):
        return self.deck

    def addCharacter(self, character):
        self.deck.append(character)

    def shuffle(self):
        rando = randrange(len(self.deck))
        
        return self.deck;



def playerInput():
    playerCount = input("How many players?");
    playerCount = int(playerCount);
    playerNames = []
    if playerCount >= 2 and playerCount <= 6:
        for i in range(0,playerCount):
            player = input("What is your name? ")
            playerNames.append(player)
        return playerNames
    else:
        input('Please enter a number between 2 and 6. Press any button to try again.')
        return playerInput()

print(playerInput())

#first function player input
    #needs to get player count and their names.
    #needs to verify a number for player count
    #needs to verify player count is between 2 and 6
    #return a list of players and a number of players

#second function is random assignment
    #takes the list of players
    #needs a list of characters
    #needs to iterate over the players
    #needs to select a random character from the list
    #needs to remove the character from the list of characters
    #return tuple of player character for each player in the list

