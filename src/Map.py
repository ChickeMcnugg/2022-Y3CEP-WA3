class Location():
    def __init__(self, locationName):
        self.locationName = locationName
        self.locationNeighboursList = {}
    
    def __repr__(self):
        return "This is the " + self.locationName + "."
    
    def getLocationName(self):
        return self.locationName
    
    def getLocationNeighboursList(self):
        return self.locationNeighboursList
    
    def setOneWayLocationNeighbours(self, newLocation, direction):
        if direction in self.locationNeighboursList:
            print("There is already a location there.")
        else:
            self.locationNeighboursList[direction] = newLocation
    
    def setTwoWayLocationNeighbour(self, newLocation, direction):
        self.setOneWayLocationNeighbours(newLocation, direction)

        if direction == "North":
            newLocation.setOneWayLocationNeighbours(self, "South")
        if direction == "South":
            newLocation.setOneWayLocationNeighbours(self, "North")
        if direction == "East":
            newLocation.setOneWayLocationNeighbours(self, "West")
        if direction == "West":
            newLocation.setOneWayLocationNeighbours(self, "East")