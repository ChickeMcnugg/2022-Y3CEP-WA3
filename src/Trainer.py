class Trainer:
    def __init__(self, trainerName, trainerPokemonsList, trainerItemsList):
        self.trainerName = trainerName
        self.trainerPokemonsList = trainerPokemonsList
        self.trainerItemsList = trainerItemsList
        self.trainerLocation = "0"
        self.trainerActivePokemon = trainerPokemonsList[0]
        self.trainerFaintedPokemon = []
    
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

    def placeInLocation(self, location):
        self.trainerLocation = location

    def moveToLocation(self, direction):
        if direction in self.trainerLocation.getLocationNeighboursList():
            self.trainerLocation = self.trainerLocation.getLocationNeighboursList()[direction]
            print(self.trainerName + " is now in " + self.trainerLocation.getLocationName() + ".")
        else:
            print("It is a dead end. Please try again.")