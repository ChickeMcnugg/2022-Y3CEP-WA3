from math import floor


class Pokemon:
    def __init__(self, pokemonName, pokemonType, pokemonMaxHealth, pokemonAttack, pokemonDefense, pokemonSpeed, pokemonEvasion, pokemonAccuracy):
        self.pokemonName = pokemonName
        self.pokemonType = pokemonType
        self.pokemonLevel = 0
        self.pokemonMaxHealth = pokemonMaxHealth
        self.pokemonHealth = self.pokemonMaxHealth
        self.pokemonEXP = 0
        self.pokemonAttack = pokemonAttack
        self.pokemonDefense = pokemonDefense
        self.pokemonSpeed = pokemonSpeed
        self.pokemonEvasion = pokemonEvasion
        self.pokemonAccuracy = pokemonAccuracy
        self.pokemonMovesList = {}
        self.pokemonOwner = None
    
    def __repr__(self):
        return "This is a " + self.pokemonType.getTypeName() + ", Level " + str(self.pokemonLevel) + " " + self.pokemonName + "."
    
    def getPokemonName(self):
        return self.pokemonName
    
    def getPokemonType(self):
        return self.pokemonType
    
    def getPokemonLevel(self):
        return self.pokemonLevel
    
    def getPokemonHealth(self):
        return self.pokemonHealth
    
    def setPokemonHealth(self, newHealth):
        self.pokemonHealth = min(newHealth, self.pokemonMaxHealth)
    
    def getPokemonAttack(self):
        return self.pokemonAttack
    
    def getPokemonDefense(self):
        return self.pokemonDefense
    
    def getPokemonSpeed(self):
        return self.pokemonSpeed
    
    def getPokemonEvasion(self):
        return self.pokemonEvasion
    
    def getPokemonAccuracy(self):
        return self.pokemonAccuracy
    
    def getPokemonEXP(self):
        return self.pokemonEXP
    
    def addPokemonEXP(self, newEXP):
        self.pokemonEXP += newEXP
        tempLevel = self.pokemonLevel
        self.pokemonLevel = floor(self.pokemonEXP ** (1/3))
        if self.pokemonLevel > tempLevel:
            print(self.pokemonName + " levelled up, and is now at Level " + str(self.pokemonLevel))
    
    def getPokemonMovesList(self):
        return self.pokemonMovesList
    
    def getPokemonOwner(self):
        return self.pokemonOwner
    
    def setPokemonOwner(self, newOwner):
        self.pokemonOwner = newOwner
    
    def addMove(self, newMove):
        self.pokemonMovesList[newMove.getMoveName()] = newMove
        print(self.pokemonName + " learnt the move, " + newMove.getMoveName() + ".")