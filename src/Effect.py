class Effect:
    def __init__(self, effectName, effectAttribute, effectPower):
        self.effectName = effectName

        #Attribute and Power depend on properties of the effect (refer to main.py for more info)
        self.effectAttribute = effectAttribute
        self.effectPower = effectPower
    
    def getEffectName(self):
        return self.effectName
    
    def getEffectAttribute(self):
        return self.effectAttribute
    
    def getEffectPower(self):
        return self.effectPower