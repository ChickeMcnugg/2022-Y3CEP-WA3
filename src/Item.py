class Item:
    def __init__(self, itemName):
        self.itemName = itemName
    
    def __repr__(self):
        return "This is a " + self.itemName + "."
    
    def getItemName(self):
        return self.itemName