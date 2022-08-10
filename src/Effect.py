class Effect:
    def __init__(self, effectName, effectType, effectAttribute, effectPower):
        self.effectName = effectName
        self.effectType = effectType
        self.effectAttribute = effectAttribute
        self.effectPower = effectPower
    
    def getEffectName(self):
        return self.effectName
    
    def getEffectType(self):
        return self.effectType
    
    def getEffectAttribute(self):
        return self.effectAttribute
    
    def getEffectPower(self):
        return self.effectPower