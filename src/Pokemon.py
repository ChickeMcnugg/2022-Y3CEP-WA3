#The Pokemon class contains the pokemon's name, type, level, health, attack, defense, evasion, accuracy, owner and moves.
#A pokemon's type is referenced during battle for type advantages.
#A pokemon's level boosts the base statistics of the pokemon.
#A pokemon's health, attack, defense, evasion and accuracy are considered when attacking or when being attacked by the opponent.
#A pokemon's owner is referenced after battles to check if it is a random encounter.
#A pokemon's moves are the moves the pokemon can make during battles.

from math import floor
from time import sleep

class Pokemon:
    def __init__(self, pokemonName, pokemonType, pokemonMaxHealth, pokemonAttack, pokemonDefense, pokemonEvasion, pokemonAccuracy):
        self.pokemonName = pokemonName
        self.pokemonType = pokemonType
        self.pokemonLevel = 0
        self.pokemonMaxHealth = pokemonMaxHealth
        self.pokemonHealth = self.pokemonMaxHealth
        self.pokemonEXP = 0
        self.pokemonAttack = pokemonAttack
        self.pokemonDefense = pokemonDefense
        self.pokemonEvasion = pokemonEvasion
        self.pokemonAccuracy = pokemonAccuracy
        self.pokemonMovesDict = {}
        self.pokemonOwner = None
        self.pokemonEffects = []
    
    def __repr__(self):
        return "This is a " + self.pokemonType.getTypeName() + ", Level " + str(self.pokemonLevel) + " " + self.pokemonName + "."
    
    def getPokemonName(self):
        return self.pokemonName
    
    def getPokemonType(self):
        return self.pokemonType
    
    def addPokemonEXP(self, newEXP):
        self.pokemonEXP += newEXP

        #UI
        tempLevel = self.pokemonLevel
        self.pokemonLevel = floor(self.pokemonEXP ** (1/3))
        if self.pokemonLevel > tempLevel:
            print(self.pokemonName + " levelled up, and is now at Level " + str(self.pokemonLevel))
    
    def getPokemonLevel(self):
        return self.pokemonLevel
    
    def addPokemonLevel(self, newLevel):
        self.pokemonLevel += newLevel
        self.pokemonEXP = self.pokemonLevel ** 3
        print(self.pokemonName + " gained " + str(newLevel) + " levels.")
    
    def getPokemonMaxHealth(self):
        return self.pokemonMaxHealth
    
    def getPokemonHealth(self):
        return self.pokemonHealth
    
    def setPokemonHealth(self, newHealth):
        self.pokemonHealth = newHealth

    def addPokemonHealth(self, newHealth):
        self.pokemonHealth += newHealth

        #Bound pokemon's health from 0 to maxHealth
        self.pokemonHealth = max(min(self.pokemonHealth, self.pokemonMaxHealth), 0)

        #UI
        if newHealth <= 0:
            print(self.pokemonName + " took " + str(-newHealth) + " damage, and has " + str(self.pokemonHealth) + " health.")
            sleep(1)
        else:
            print(self.pokemonName + " gained " + str(newHealth) + " health, and has " + self.pokemonHealth + " health.")
            sleep(1)

    def getPokemonAttack(self):
        return self.pokemonAttack
    
    def addPokemonAttack(self, newAttack):
        self.pokemonAttack += newAttack
        print(self.pokemonName + "'s attack rose to " + str(self.pokemonAttack) + ".")
    
    def getPokemonDefense(self):
        return self.pokemonDefense
    
    def addPokemonDefense(self, newDefense):
        self.pokemonDefense += newDefense
        print(self.pokemonName + "'s defense rose to " + str(self.pokemonAttack) + ".")

    def getPokemonEvasion(self):
        return self.pokemonEvasion
    
    def getPokemonAccuracy(self):
        return self.pokemonAccuracy
    
    def addPokemonAccuracy(self, newAccuracy):
        self.pokemonAccuracy = max(self.pokemonAccuracy + newAccuracy, 100)

    def getPokemonMovesDict(self):
        return self.pokemonMovesDict
        
    def addPokemonMoves(self, newMove):
        self.pokemonMovesDict[newMove.getMoveName()] = newMove
    
    def getPokemonOwner(self):
        return self.pokemonOwner
    
    def setPokemonOwner(self, newOwner):
        self.pokemonOwner = newOwner
    
    def getPokemonEffects(self):
        return self.pokemonEffects
    
    def removePokemonEffects(self, effects):
        for effect in effects:
            if effect in self.pokemonEffects:
                self.pokemonEffects.remove(effect)
                print(self.pokemonName + "is no longer " + effect.lower() + ".")
    
    def addPokemonEffects(self, effects):
        for effect in effects:
            if effect not in self.pokemonEffects:
                self.pokemonEffects.append(effect)
                print(self.pokemonName + " has been " + effect.lower() + ".")
    
    def chooseMove(self):
        availableMoves = list(self.pokemonMovesDict.keys())

        #UI
        moveMessage = "Choose your move ("
        for move in availableMoves:
            moveMessage += move + ", "
        moveMessage = moveMessage[:-2] + ") : "

        moveInput = ""
        
        #Wait until user's input is valid
        while moveInput not in self.pokemonMovesDict:
            moveInput = input(moveMessage)
        
        sleep(1)
        return self.pokemonMovesDict[moveInput]