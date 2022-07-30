class Pokemon:
    def __init__(self, pokemonName, pokemonType, pokemonLevel, pokemonMaxHealth, pokemonAttack, pokemonDefense, pokemonSpeed, pokemonEvasion, pokemonAccuracy):
        self.pokemonName = pokemonName
        self.pokemonType = pokemonType
        self.pokemonLevel = pokemonLevel
        self.pokemonMaxHealth = pokemonMaxHealth
        self.pokemonHealth = pokemonMaxHealth
        self.pokemonEXP = 0
        self.pokemonAttack = pokemonAttack
        self.pokemonDefense = pokemonDefense
        self.pokemonSpeed = pokemonSpeed
        self.pokemonEvasion = pokemonEvasion
        self.pokemonAccuracy = pokemonAccuracy
        self.pokemonMovesList = []
    
    def __repr__(self):
        return "This is a " + self.pokemonType + ", Level " + str(self.pokemonLevel) + " " + self.pokemonName + "."
    
    def getPokemonName(self):
        return self.pokemonName
    
    def getPokemonType(self):
        return self.pokemonType
    
    def getPokemonLevel(self):
        return self.pokemonLevel
    
    def getPokemonHealth(self):
        return self.pokemonHealth
    
    def getPokemonAttack(self):
        return self.pokemonAttack
    
    def getPokemonDefense(self):
        return self.pokemonDefense
    
    def getPokemonSpeed(self):
        return self.pokemonSpeed
    
    def getPokemonEvasion(self):
        return self.pokemonEvasion
    
    def getPokemonAccuracy(self):
        return self.pokemonAccuracy
    
    def getPokemonEXP(self):
        return self.pokemonEXP