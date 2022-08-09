class Location():
    def __init__(self, locationName):
        self.locationName = locationName
        self.locationNeighboursDict = {}
        self.locationTrainersDict = {}
        self.locationPokemonDict = {}
    
    def __repr__(self):
        return "This is the " + self.locationName + "."
    
    def getLocationName(self):
        return self.locationName
    
    def getLocationNeighboursDict(self):
        return self.locationNeighboursDict
    
    def getLocationTrainersDict(self):
        return self.locationTrainersDict
    
    def addLocationTrainer(self, newTrainer):
        self.locationTrainersDict[newTrainer.getTrainerName().capitalize()] = newTrainer
    
    def removeLocationTrainer(self, oldTrainer):
        del(self.locationTrainersDict[oldTrainer.getTrainerName().capitalize()])

    def getLocationPokemonDict(self):
        return self.locationPokemonDict

    def addLocationPokemon(self, newPokemon):
        self.locationPokemonDict[newPokemon.getPokemonName().capitalize()] = newPokemon
    
    def removeLocationPokemon(self, oldPokemon):
        del(self.locationPokemonDict[oldPokemon.getPokemonName().capitalize()])

    def setOneWayLocationNeighbours(self, newLocation, direction):
        #Check if input direction is valid and available
        if direction in self.locationNeighboursDict:
            print("There is already a location there.")
        else:
            self.locationNeighboursDict[direction] = newLocation
    
    def setTwoWayLocationNeighbour(self, newLocation, direction):
        self.setOneWayLocationNeighbours(newLocation, direction)

        #Sets opposite direction from the other location
        if direction == "North":
            newLocation.setOneWayLocationNeighbours(self, "South")
        elif direction == "South":
            newLocation.setOneWayLocationNeighbours(self, "North")
        elif direction == "East":
            newLocation.setOneWayLocationNeighbours(self, "West")
        else:
            newLocation.setOneWayLocationNeighbours(self, "East")