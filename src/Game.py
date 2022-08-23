from time import sleep

class Game:
    def __init__(self):
        pass

    def __repr__(self):
        return "Pokemon - the game."

    def intro(self):
        print("------------------- POKEMON\u2122 Red Version -------------------")
        print("--------------- By Tan Teng Fong, Christopher --------------")

        sleep(5)

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

        playerName = input("First, what is your name? : ")
        sleep(1)
        print("Right, so your name is " + playerName + ".")
        sleep(1)
        print(playerName + "! Your very own Pokemon legend is about to unfold!")
        sleep(1)
        print("A world of dreams and adventures awaits! Let's go!")

        return playerName