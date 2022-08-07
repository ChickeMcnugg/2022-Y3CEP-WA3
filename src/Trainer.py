class Trainer:
    def __init__(self, trainerName, trainerLivePokemonsDict, trainerItemsDict, trainerLocation):
        self.trainerName = trainerName
        self.trainerLivePokemonsDict = trainerLivePokemonsDict
        for pokemonKey in self.trainerLivePokemonsDict:
            self.trainerLivePokemonsDict[pokemonKey].setPokemonOwner(self)
        self.trainerActivePokemon = list(trainerLivePokemonsDict.keys())[0]
        self.trainerFaintedPokemonDict = {}
        self.trainerItemsList = trainerItemsDict
        self.trainerLocation = trainerLocation
    
    def __repr__(self):
        output = self.trainerName + " the trainer has "

        if len(self.trainerLivePokemonsDict) == 0:
            output += "no pokemons "
        else:
            for pokemonKey in self.trainerPokemonsDict:
                output += "a " + pokemonKey + ", "
        
        output += "and "

        if len(self.trainerItemsDict) == 0:
            output += "no items"
        else:
            for itemKey in range(0, len(self.trainerItemsDict) - 1):
                output += "a " + itemKey + ", "
            
            output += "and a " + self.trainerItemsDict[-1]
        
        output += "."

        return output
    
    def getTrainerName(self):
        return self.trainerName
    
    def getTrainerLivePokemonsDict(self):
        return self.trainerLivePokemonsDict
    
    def getTrainerFaintedPokemonsDict(self):
        return self.trainerFaintedPokemonDict

    def setFaintedPokemon(self, newPokemon):
        self.trainerFaintedPokemonDict[newPokemon.getPokemonName().capitalize()] = newPokemon
        del(self.trainerLivePokemonsDict[newPokemon.getPokemonName().capitalize()])
        self.trainerActivePokemon = list(self.trainerLivePokemonsDict.keys())[0]
    
    def getTrainerActivePokemon(self):
        return self.trainerActivePokemon
    
    def setTrainerActivePokemon(self, newPokemon):
        self.trainerActivePokemon = newPokemon.getPokemonName().capitalize()
    
    def getTrainerItemsList(self):
        return self.trainerItemsList

    def getTrainerLocation(self):
        return self.trainerLocation

    def setTrainerLocation(self, newLocation):
        self.trainerLocation = newLocation
        newLocation.addLocationTrainer(self)

    def moveToLocation(self, newDirection):
        if newDirection in self.trainerLocation.getLocationNeighboursDict():
            self.setTrainerLocation(self.trainerLocation.getLocationNeighboursDict()[newDirection])
            print(self.trainerName + " is now in " + self.trainerLocation.getLocationName() + ".")
        else:
            print("It is a dead end. Please try again.")