class Mart:
    def __init__(self, martName, martLocation, martItemsDict):
        self.martName = martName
        self.martLocation = martLocation
        self.martItemsDict = martItemsDict
    
    def __repr__(self):
        return "This is the " + self.martName + " at " + self.martLocation.getLocationName() + "."
    
    def getMartName(self):
        return self.martName

    def getMartLocation(self):
        return self.martLocation
    
    def getMartItemsDict(self):
        return self.martItemsDict()
    
    def addMartItem(self, newItem):
        pass

    def removeMartItem(self, oldItem):
        pass