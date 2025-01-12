class Mart:
    def __init__(self, martName, martLocation, martItemsDict):
        self.martName = martName
        self.martLocation = martLocation
        self.martLocation.setLocationMart(self)
        self.martItemsDict = martItemsDict
    
    def __repr__(self):
        return "This is the " + self.martName + " at " + self.martLocation.getLocationName() + "."
    
    def getMartName(self):
        return self.martName

    def getMartLocation(self):
        return self.martLocation
    
    def getMartItemsDict(self):
        return self.martItemsDict()

    def openShop(self, protagonist):
        actionInput = ""
        while actionInput not in ["Buy", "Sell"]:
            actionInput = input("Do you want to buy or sell? (Buy, Sell) : ")

        #Display buyable items or sellable items depending on what player chooses to do
        if actionInput == "Buy":
            #UI
            print("        Item        |     Buy Price      ")
            print("-----------------------------------------")

            #For every item that can be bought, list down item name and price according to UI
            for item in list(self.martItemsDict.keys()):
                row = " " * ((20 - len(item)) // 2)
                row += item
                row += " " * (20 - len(row))
                row += "|"
                row += " " * ((20 - len(str(self.martItemsDict[item].getItemBuyPrice()))) // 2)
                row += str(self.martItemsDict[item].getItemBuyPrice())
                row += " " * (41 - len(row))
                print(row)
            
            #Wait for valid user input
            buyInput = ""
            while buyInput not in list(self.martItemsDict.keys()):
                buyInput = input("What would you like to buy? : ")
            
            #Provide option of choosing number of items to buy
            counterInput = 0
            while counterInput <= 0 or counterInput * self.martItemsDict[buyInput].getItemBuyPrice() > protagonist.getTrainerMoney():
                try:
                    counterInput = int(input("How many would you like to buy? : "))
                except:
                    pass
            
            boughtitem = self.martItemsDict[buyInput]
            protagonist.addTrainerItem(boughtitem, counterInput)
            protagonist.addTrainerMoney(-(counterInput * boughtitem.getItemBuyPrice()))
        else:
            #UI
            print("        Item        |     Sell Price     ")
            print("-----------------------------------------")

            #For every item that can be sold, list down item name and price according to UI
            for item in list(protagonist.getTrainerItemsDict().keys()):
                row = " " * ((20 - len(item)) // 2)
                row += item
                row += " " * (20 - len(row))
                row += "|"
                row += " " * ((20 - len(str(protagonist.getTrainerItemsDict()[item][0].getItemSellPrice()))) // 2)
                row += str(self.martItemsDict[item].getItemSellPrice())
                row += " " * (41 - len(row))
                print(row)
            
            #Wait for valid user input
            sellInput = ""
            while sellInput not in list(protagonist.getTrainerItemsDict().keys()):
                sellInput = input("What would you like to sell? : ")
            
            #Provide option of choosing number of items to sell
            counterInput = 0
            while counterInput <= 0 or counterInput > protagonist.getTrainerItemsDict()[sellInput][1]:
                try:
                    counterInput = int(input(f"How many would you like to sell? ({protagonist.getTrainerItemsDict()[sellInput][1]}) : "))
                except:
                    pass

            solditem = protagonist.getTrainerItemsDict()[sellInput][0]
            protagonist.useTrainerItem(solditem, counterInput)
            protagonist.addTrainerMoney(counterInput * solditem.getItemSellPrice())