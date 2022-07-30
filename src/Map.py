class Map():
    def __init__(self, mapName, mapLocationsList={}):
        self.mapName = mapName
        self.mapLocationsList = mapLocationsList
    
    def __repr__(self):
        return "This is the map of " + self.mapName + "."
    
    def getMapName(self):
        return self.mapName
    
    def getMapLocationsList(self):
        return self.mapLocationsList

class Location():
    def __init__(self, locationName, locationNeighbourNorth, locationNeighbourSouth, locationNeighbourEast, locationNeighbourWest):
        self.locationName = locationName
        self.locationNeighboursList = { "north" : locationNeighbourNorth
                                        "south" : locationNeighbourSouth
                                        "east" : locationNeighbourEast
                                        "west" : locationNeighbourWest
                                        }
    
    def __repr__(self):
        return "This is the " + self.locationName + "."
    
    def getLocationName(self):
        return self.locationName
    
    def getLocationNeighboursList(self):
        return self.locationNeighboursList
    
    def setLocationNeighboursList(self, newLocationNorth, newLocationSouth, newLocationEast, newLocationWest):
        self.locationNeighboursList[north] = newLocationsNorth
        self.locationNeighboursList[south] = newLocationsSouth
        self.locationNeighboursList[east] = newLocationsEast
        self.locationNeighboursList[west] = newLocationsWest