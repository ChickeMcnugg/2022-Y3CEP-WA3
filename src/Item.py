class Item:
    def __init__(self, itemName, itemAttribute, itemPower):
        self.itemName = itemName
        self.itemAttribute = itemAttribute
        self.itemPower = itemPower
    
    def __repr__(self):
        return "This is a " + self.itemName + "."
    
    def getItemName(self):
        return self.itemName
    
    def getItemAttribute(self):
        return self.itemAttribute
    
    def getItemPower(self):
        return self.itemPower