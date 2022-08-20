#The Location class contains the location's name, neighbouring locations, and existing trainers and wild pokemon that can be found.
#A location's neighbouring locations is referenced when teh player is moving from location to location on the map.
#A location's existing trainers and wild pokemon are referenced during traienr battles and random encounters.

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
    
    def getLocationTrainersDict(self):
        return self.locationTrainersDict
    
    def addLocationTrainer(self, newTrainer):
        self.locationTrainersDict[newTrainer.getTrainerName().capitalize()] = newTrainer
    
    def removeLocationTrainer(self, oldTrainer):
        del(self.locationTrainersDict[oldTrainer.getTrainerName().capitalize()])

    def getLocationPokemonDict(self):
        return self.locationPokemonDict

    def addLocationPokemon(self, newPokemon):
        for pokemon in newPokemon:
            self.locationPokemonDict[pokemon.getPokemonName().capitalize()] = pokemon
    
    def removeLocationPokemon(self, oldPokemon):
        del(self.locationPokemonDict[oldPokemon.getPokemonName().capitalize()])