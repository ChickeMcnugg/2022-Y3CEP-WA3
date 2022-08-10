#The Type class contains the type advantages, disadvantages and immunity of every type in the game.
#This is used during battles and affects the damage dealt when attacking.

class Type:
    def __init__(self, typeName):
        self.typeName = typeName
        self.typeAdvantageList = []
        self.typeDisadvantageList = []
        self.typeImmuneList = []
    
    def __repr__(self):
        return "This is the " + self.typeName + " type."

    def getTypeName(self):
        return self.typeName
    
    def getTypeAdvantageList(self):
        return self.typeAdvantageList
    
    def setTypeAdvantageList(self, newTypes):
        self.typeAdvantageList = newTypes

    def getTypeDisadvantageList(self):
        return self.typeDisadvantageList

    def setTypeDisadvantageList(self, newTypes):
        self.typeDisadvantageList = newTypes

    def getTypeImmuneList(self):
        return self.typeImmuneList
    
    def setTypeImmuneList(self, newTypes):
        self.typeImmuneList = newTypes