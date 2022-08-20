class Shop:
    def __init__(self, shopName, shopItemsDict):
        self.shopName = shopName
        self.shopItemsDict = shopItemsDict
    
    def __repr__(self):
        return "This is the " + self.shopName + "."
    
    def getShopName(self):
        return self.shopName
    
    def getShopItemsDict(self):
        return self.shopItemsDict()
    
    def addShopItem(self, newItem):
        pass

    def removeShopItem(self, oldItem):
        pass