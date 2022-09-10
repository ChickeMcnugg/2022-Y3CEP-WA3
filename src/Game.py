from time import sleep
from copy import deepcopy

class Game:
    def __init__(self):
        pass

    def __repr__(self):
        return "Pokemon - the game."

    def intro(self):
        #Start the game
        print("------------------- POKEMON\u2122 Red Version -------------------")
        print("--------------- By Tan Teng Fong, Christopher --------------")

        sleep(3)

        print("Hello there! Welcome to the world of Pokemon!")
        sleep(1)
        print("My name is OAK! People call me the Pokemon Prof!")
        sleep(1)
        print("This world is inhabited by creatures called Pokemon.")
        sleep(1)
        print("For some people, Pokemon are pets. Others use them to fight.")
        sleep(1)
        print("Myself...")
        sleep(1)
        print("I study Pokemon as a profession.")
        sleep(1)

        #Player only has one try at inputting their name with no confirmation screen
        playerName = input("First, what is your name? : ")
        sleep(1)
        
        print("Right, so your name is " + playerName + ".")
        sleep(1)
        print(playerName + "! Your very own Pokemon legend is about to unfold!")
        sleep(1)
        print("A world of dreams and adventures awaits! Let's go!")
        sleep(1)

        return playerName
    
    def starter(self):
        #Provide options and wait for valid user input
        starterInput = ""
        while starterInput not in ["Bulbasaur", "Charmander", "Squirtle"]:
            starterInput = input("Choose you starter Pokemon (Bulbasaur, Charmander, Squirtle) : ")

        sleep(1)

        #Wait for valid user input
        nameInput = ""
        while nameInput == "":
            nameInput = input("What is your Pokemon's name? : ").strip()
        
        sleep(1)

        return starterInput, nameInput