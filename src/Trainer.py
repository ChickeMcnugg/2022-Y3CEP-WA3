class Trainer:
    def __init__(self, trainerName, trainerPokemonsList, trainerItemsList):
        self.trainerName = trainerName
        self.trainerPokemonsList = trainerPokemonsList
        for pokemonKey in self.trainerPokemonsList:
            self.trainerPokemonsList[pokemonKey].setPokemonOwner(self)
        self.trainerItemsList = trainerItemsList
        self.trainerLocation = None
        self.trainerActivePokemon = list(trainerPokemonsList.keys())[0]
        self.trainerFaintedPokemon = {}
    
    def __repr__(self):
        output = self.trainerName + " the trainer has "

        if len(self.trainerPokemonsList) == 0:
            output += "no pokemons "
        else:
            for pokemon in self.trainerPokemonsList:
                output += "a " + pokemon.getPokemonName() + ", "
        
        output += "and "

        if len(self.trainerItemsList) == 0:
            output += "no items"
        else:
            for item in range(0, len(self.trainerItemsList) - 1):
                output += "a " + self.trainerItemsList[item].getItemName() + ", "
            
            output += "and a " + self.trainerItemsList[-1].getItemName()
        
        output += "."

        return output
    
    def getTrainerName(self):
        return self.trainerName
    
    def getTrainerPokemonsList(self):
        return self.trainerPokemonsList
    
    def getTrainerItemsList(self):
        return self.trainerItemsList
    
    def getTrainerActivePokemon(self):
        return self.trainerActivePokemon
    
    def setTrainerActivePokemon(self, newPokemon):
        self.trainerActivePokemon = newPokemon.getPokemonName().capitalize()
    
    def setFaintedPokemon(self, newPokemon):
        self.trainerFaintedPokemon[newPokemon.getPokemonName().capitalize()] = newPokemon
        del(self.trainerPokemonsList[newPokemon.getPokemonName().capitalize()])
        self.trainerActivePokemon = None

    def getTrainerLocation(self):
        return self.trainerLocation

    def placeInLocation(self, location):
        self.trainerLocation = location
        location.addLocationTrainer(self)

    def moveToLocation(self, direction):
        if direction in self.trainerLocation.getLocationNeighboursList():
            self.trainerLocation = self.trainerLocation.getLocationNeighboursList()[direction]
            self.trainerLocation.addLocationTrainer(self)
            print(self.trainerName + " is now in " + self.trainerLocation.getLocationName() + ".")
        else:
            print("It is a dead end. Please try again.")