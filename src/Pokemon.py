class Pokemon:
    def __init__(self, pokemonName, pokemonType, pokemonLevel, pokemonMaxHealth):
        self.pokemonName = pokemonName
        self.pokemonType = pokemonType
        self.pokemonLevel = pokemonLevel
        self.pokemonMaxHealth = pokemonMaxHealth
        self.pokemonHealth = pokemonMaxHealth
    
    def __repr__(self):
        return "This is a " + self.pokemonType + ", Level " + str(self.pokemonLevel) + " " + self.pokemonName + "."
    
    def getPokemonName(self):
        return self.pokemonName
    
    def getPokemonType(self):
        return self.pokemonType
    
    def getPokemonLevel(self):
        return self.pokemonLevel
    
    def getPokemonHealth(self):
        return self.getPokemonHealth
