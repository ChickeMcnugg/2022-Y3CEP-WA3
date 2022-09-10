class Item:
    def __init__(self, itemName, itemBuyPrice, itemSellPrice, itemAttribute, itemPower):
        self.itemName = itemName
        self.itemBuyPrice = itemBuyPrice
        self.itemSellPrice = itemSellPrice

        #Attribute and Power depends on the properties of the item (refer to main.py for more info)
        self.itemAttribute = itemAttribute
        self.itemPower = itemPower
    
    def __repr__(self):
        return "This is a " + self.itemName + "."
    
    def getItemName(self):
        return self.itemName

    def getItemBuyPrice(self):
        return self.itemBuyPrice
    
    def getItemSellPrice(self):
        return self.itemSellPrice
    
    def getItemAttribute(self):
        return self.itemAttribute
    
    def getItemPower(self):
        return self.itemPower