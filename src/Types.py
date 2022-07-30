class Type:
    def __init__(self, typeName, typeAdvantageList=[], typeDisadvantageList=[], typeImmuneList=[]):
        self.typeName = typeName
        self.typeAdvantageList = typeAdvantageList
        self.typeDisadvantageList = typeDisadvantageList
        self.typeImmuneList = typeImmuneList
    
    def __repr__(self):
        return "This is the " + self.typeName + " type."

    def getTypeName(self):
        return self.typeName
    
    def getTypeAdvantageList(self):
        return self.typeAdvantageList
    
    def setTypeAdvantage(self, newTypes):
        self.typeAdvantageList = newTypes

    def getTypeDisadvantage(self):
        return self.typeDisadvantageList

    def setTypeDisadvantageList(self, newTypes):
        self.typeDisadvantageList = newTypes

    def getTypeImmuneList(self):
        return self.typeImmuneList
    
    def setTypeImmuneList(self, newTypes):
        self.typeImmuneList = newTypes

    def setup():
        global bugType, dragonType, electricType, fightingType, fireType, flyingType, ghostType, grassType, groundType, iceType, normalType, poisonType, psychicType, rockType, waterType

        bugType = Type("Bug")
        dragonType = Type("Dragon")
        electricType = Type("Electric")
        fightingType = Type("Fighting")
        fireType = Type("Fire")
        flyingType = Type("Flying")
        ghostType = Type("Ghost")
        grassType = Type("Grass")
        groundType = Type("Ground")
        iceType = Type("Ice")
        normalType = Type("Normal")
        poisonType = Type("Poison")
        psychicType = Type("Psychic")
        rockType = Type("Rock")
        waterType = Type("Water")

        bugType.setTypeAdvantageList([poisonType, grassType, psychicType])
        bugType.setTypeDisadvantageList([fightingType, flyingType, ghostType, fireType])
        
        dragonType.setTypeAdvantageList([dragonType])
        
        electricType.setTypeAdvantageList([flyingType, waterType])
        electricType.setTypeDisadvantageList([grassType, electricType, , dragonType])
        electricType.setImmuneList([groundType])
        
        fightingType.setTypeAdvantageList([normalType, rockType, iceType])
        fightingType.setTypeDisadvantageList([flyingType, poisonType, bugType, psychicType])
        fightingType.setImmuneList([ghostType])

        fireType.setTypeAdvantageList([bugType, grassType, iceType])
        fireType.setTypeDisadvantageList([rockType, fireType, waterType, dragonType])

        flyingType.setTypeAdvantageList([fightingType, bugType, grassType])
        flyingType.setTypeDisadvantageList([rockType, electricType])

        ghostType.setTypeAdvantageList([ghostType])
        ghostType.setImmuneList([normalType, psychicType])

        grassType.setTypeAdvantageList([groundType, rockType, waterType])
        grassType.setTypeDisadvantageList([flyingType, poisonType, bugType, fireType, grassType, dragonType])
        
        groundType.setTypeAdvantageList([poisonType, rockType, fireType, electricType])
        groundType.setTypeDisadvantageList([bugType, grassType])
        groundType.setImmuneList([flyingType])

        iceType.setTypeAdvantageList([flyingType, groundType, grassType, dragonType])
        iceType.setTypeDisadvantageList([waterType, iceType])
        
        normalType.setTypeDisadvantageList([rockType])
        normalType.setImmuneList([ghostType])

        poisonType.setTypeAdvantageList([bugType, grassType])
        poisonType.setTypeDisadvantageList([poisonType, groundType, rockType, rockType])

        psychicType.setTypeAdvantageList([fightingType, groundType, grassType, dragonType])
        psychicType.setTypeDisadvantageList([waterType, iceType])
        
        rockType.setTypeAdvantageList([flyingType, bugType, fireType, iceType])
        rockType.setTypeDisadvantageList([fightingType, groundType])
        
        waterType.setTypeAdvantageList([groundType, rockType, fireType])
        waterType.setTypeDisadvantageList([waterType, grassType, dragonType]) 