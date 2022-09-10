#The Pokemon class contains the pokemon's name, type, level, health, attack, defense, evasion, accuracy, owner and moves.
#A pokemon's type is referenced during battle for type advantages.
#A pokemon's level boosts the base statistics of the pokemon.
#A pokemon's health, attack, defense, evasion and accuracy are considered when attacking or when being attacked by the opponent.
#A pokemon's owner is referenced after battles to check if it is a random encounter.
#A pokemon's moves are the moves the pokemon can make during battles.

from math import floor
from random import randint
from time import sleep

class Pokemon:
    def __init__(self, pokemonName, pokemonType, pokemonMaxHealth, pokemonAttack, pokemonDefense, pokemonCatchRate, pokemonDefeatEXP):
        self.pokemonName = pokemonName
        self.pokemonType = pokemonType

        self.pokemonMaxHealth = pokemonMaxHealth
        self.pokemonHealth = self.pokemonMaxHealth

        self.pokemonAttack = pokemonAttack
        self.pokemonBaseAttack = self.pokemonAttack
        self.pokemonDefense = pokemonDefense
        self.pokemonBaseDefense = self.pokemonDefense
        self.pokemonEvasion = 100
        self.pokemonAccuracy = 100

        self.pokemonEXP = 0
        self.pokemonLevel = 5
        
        self.pokemonMovesDict = {}
        self.pokemonEffects = []
        self.cannotMoveTurns = 0
        self.pokemonCatchRate = pokemonCatchRate

        self.pokemonOwner = None

        self.pokemonDefeatEXP = pokemonDefeatEXP
        
    def __repr__(self):
        return self.pokemonName + " is a " + self.pokemonType.getTypeName() + " pokemon at Level " + str(self.pokemonLevel) + "."
    
    def getPokemonName(self):
        return self.pokemonName
    
    def changePokemonName(self, newName):
        self.pokemonName = newName
    
    def getPokemonType(self):
        return self.pokemonType
    
    def getPokemonMaxHealth(self):
        return self.pokemonMaxHealth
    
    def getPokemonHealth(self):
        return self.pokemonHealth

    def addPokemonHealth(self, newHealth):
        #Bound pokemon's health from 0 to pokemonMaxHealth
        self.pokemonHealth = max(min(self.pokemonHealth + newHealth, self.pokemonMaxHealth), 0)

        #UI
        if newHealth <= 0:
            print(self.pokemonName + " took " + str(-newHealth) + " damage, and has " + str(self.pokemonHealth) + " health.")
        else:
            print(self.pokemonName + " gained " + str(newHealth) + " health, and has " + str(self.pokemonHealth) + " health.")
        
        sleep(1)
    
    def getPokemonAttack(self):
        return self.pokemonAttack
    
    def addPokemonAttack(self, newAttack):
        #Bound pokemon's attack to be non-negative
        self.pokemonAttack = max(self.pokemonAttack + newAttack, 0)

        #UI
        if newAttack >= 0:
            print(self.pokemonName + "'s attack rose to " + str(self.pokemonAttack) + ".")
        else:
            print(self.pokemonName + "'s attack dropped to " + str(self.pokemonAttack) + ".")
        
        sleep(1)

    def getPokemonDefense(self):
        return self.pokemonDefense
    
    def addPokemonDefense(self, newDefense):
        #Bound pokemon's defense to be non-negative
        self.pokemonDefense = max(self.pokemonDefense + newDefense, 0)
        
        #UI
        if newDefense >= 0:
            print(self.pokemonName + "'s defense rose to " + str(self.pokemonDefense) + ".")
        else:
            print(self.pokemonName + "'s defense dropped to " + str(self.pokemonDefense) + ".")
        
        sleep(1)

    def updateAttackDefense(self, newLevel):
        #Update based on actual game equation
        self.pokemonAttack = int(self.pokemonBaseAttack + (newLevel / 50 * self.pokemonBaseAttack))
        self.pokemonDefense = int(self.pokemonBaseDefense + (newLevel / 50 * self.pokemonBaseDefense))

    def getPokemonEvasion(self):
        return self.pokemonEvasion
    
    def addPokemonEvasion(self, newEvasion):
        #Bound pokemon's evasion to be non-negative
        self.pokemonEvasion = max(self.pokemonEvasion + newEvasion, 0)

        #UI
        if newEvasion >= 0:
            print(self.pokemonName + "'s evasion rose to " + str(self.pokemonEvasion) + ".")
        else:
            print(self.pokemonName + "'s evasion dropped to " + str(self.pokemonEvasion) + ".")
        
        sleep(1)

    def getPokemonAccuracy(self):
        return self.pokemonAccuracy
    
    def addPokemonAccuracy(self, newAccuracy):
        #Bound pokemon's accuracy to be non-negative
        self.pokemonAccuracy = max(self.pokemonAccuracy + newAccuracy, 0)

        #UI
        if newAccuracy >= 0:
            print(self.pokemonName + "'s accuracy rose to " + str(self.pokemonAccuracy) + ".")
        else:
            print(self.pokemonName + "'s accuracy dropped to " + str(self.pokemonAccuracy) + ".")
        
        sleep(1)

    def resetStats(self):
        self.updateAttackDefense(self.pokemonLevel)
        self.pokemonAccuracy = 100
        self.pokemonEvasion = 100

    def addPokemonEXP(self, newEXP):
        self.pokemonEXP = max(self.pokemonEXP + newEXP, 0)

        #UI
        print(self.pokemonName + " has gained " + str(newEXP) + " EXP.")
        sleep(1)

        #Check if pokemon has levelled up by checking if there is a difference between the previous level and the new level
        tempLevel = self.pokemonLevel
        self.pokemonLevel = floor(self.pokemonEXP ** (1/3))
        if self.pokemonLevel > tempLevel:
            print(self.pokemonName + " levelled up, and is now at Level " + str(self.pokemonLevel))
            self.updateAttackDefense(self.pokemonLevel)
    
    def getPokemonLevel(self):
        return self.pokemonLevel
    
    def addPokemonLevel(self, newLevel):
        #Updating levels affects minimum EXP and stats
        self.pokemonLevel = max(self.pokemonLevel + newLevel, 0)
        self.pokemonEXP = self.pokemonLevel ** 3
        self.updateAttackDefense(self.pokemonLevel)

        #UI
        print(self.pokemonName + " gained " + str(newLevel) + " levels.")
    
    def setPokemonLevel(self, newLevel):
        #Prevent any chance that newLevel is negative, which should not be possible in the first place
        self.pokemonLevel = max(newLevel, 0)
        self.pokemonEXP = self.pokemonLevel ** 3
        self.updateAttackDefense(self.pokemonLevel)
    
    def getPokemonMovesDict(self):
        return self.pokemonMovesDict
        
    def addPokemonMoves(self, newMove):
        self.pokemonMovesDict[newMove.getMoveName()] = newMove

    def getPokemonEffects(self):
        return self.pokemonEffects
    
    def removePokemonEffects(self, effects):
        #effects is a list in case multiple effects are added at once by certain moves
        for effect in effects:
            if effect in self.pokemonEffects:
                self.pokemonEffects.remove(effect)
                
                #UI
                print(self.pokemonName + "is no longer " + effect.getEffectName().lower() + ".")
    
    def addPokemonEffects(self, effects):
        #effects is a list in case multiple effects are added at once by certain moves
        for effect in effects:
            if effect not in self.pokemonEffects:
                self.pokemonEffects.append(effect)
                
                #UI
                print(self.pokemonName + " has been " + effect.getEffectName().lower() + ".")

    def getCannotMoveTurns(self):
        return self.cannotMoveTurns
    
    def addCannotMoveTurns(self, newCannotMoveTurns):
        self.cannotMoveTurns += newCannotMoveTurns

    def chooseMove(self):
        #Provide move options
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

    def updateEffects(self):
        pokemonEffects = self.getPokemonEffects()

        for effect in pokemonEffects:
            #Check if the effect is "Poisoned" or "Burned"
            if effect.getEffectAttribute() == "Attack":
                print(self.getPokemonName() + " was " + effect.getEffectName().lower() + ".")
                self.addPokemonHealth(-int(self.getPokemonMaxHealth() * effect.getEffectPower()))
            #Check if the effect is "Paralysed", "Slept" or "Frozen"
            elif effect.getEffectAttribute() == "Move":
                #Check if the effect is "Paralysed" or "Frozen"
                if effect.getEffectPower() <= 1:
                    #Check if "Paralysed" takes effect
                    if randint(0, 100) > (1 - effect.getEffectPower()) * 100:
                        self.addCannotMoveTurns(1)
                else:
                    self.addCannotMoveTurns(effect.getEffectPower())

    def getPokemonCatchRate(self):
        return self.pokemonCatchRate

    def getPokemonOwner(self):
        return self.pokemonOwner
    
    def setPokemonOwner(self, newOwner):
        self.pokemonOwner = newOwner
    
    def getPokemonDefeatEXP(self):
        return self.pokemonDefeatEXP