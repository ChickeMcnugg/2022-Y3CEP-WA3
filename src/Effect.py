class Effect:
    def __init__(self, effectName, effectAttribute, effectPower):
        self.effectName = effectName
        self.effectAttribute = effectAttribute
        self.effectPower = effectPower
    
    def getEffectName(self):
        return self.effectName
    
    def getEffectAttribute(self):
        return self.effectAttribute
    
    def getEffectPower(self):
        return self.effectPower