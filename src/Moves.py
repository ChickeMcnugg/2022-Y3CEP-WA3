class Moves:
    def __init__(self, moveName, moveType, movePower, moveAccuracy):
        self.moveName = moveName
        self.moveType = moveType
        self.movePower = movePower
        self.moveAccuracy = moveAccuracy
    
    def __repr__(self):
        return "The " + self.moveType.getTypeName() + " move, " + self.moveName + ", has a power of " + str(self.movePower) + "% and an accuarcy of " + str(self.moveAccuracy) + "%."
    
    def getMoveName(self):
        return self.moveName
    
    def getMoveType(self):
        return self.moveType
    
    def getMovePower(self):
        return self.movePower
    
    def getMoveAccuracy(self):
        return self.moveAccuracy