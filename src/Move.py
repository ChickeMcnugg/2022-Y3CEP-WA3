from random import randint

class Move:
    def __init__(self, moveName, moveType, moveAttribute, movePower, moveAccuracy):
        self.moveName = moveName
        self.moveType = moveType
        self.moveAttribute = moveAttribute
        self.movePower = movePower
        self.moveAccuracy = moveAccuracy
    
    def __repr__(self):
        return "The " + self.moveType.getTypeName() + " move, " + self.moveName + ", has a power of " + str(self.movePower) + "% and an accuarcy of " + str(self.moveAccuracy) + "%."
    
    def getMoveName(self):
        return self.moveName
    
    def getMoveType(self):
        return self.moveType
    
    def getMoveAttribute(self):
        return self.moveAttribute
    
    def getMovePower(self):
        return self.movePower
    
    def getMoveAccuracy(self):
        return self.moveAccuracy
    
    def damage(self, battle, pokemonProtagonist, pokemonOpponent):
        if randint(1, 100) > 100 - (((self.moveAccuracy / 100) * (pokemonProtagonist.getPokemonAccuracy() / 100) * (pokemonOpponent.getPokemonEvasion() / 100)) * 100):
            damage = pokemonProtagonist.getPokemonAttack() * (self.getMovePower() / 50)
            defense = pokemonOpponent.getPokemonDefense()
            netDamage = int(max(damage - defense, 0))
            
            pokemonOpponent.addPokemonHealth(-netDamage)

            if pokemonOpponent.getPokemonHealth() == 0:
                pokemonOpponent.getPokemonOwner().setFaintedPokemon(pokemonOpponent)
                pokemonProtagonist.addPokemonEXP(30)
                battle.setIsEnded(True)
                
                print(pokemonOpponent.getPokemonName() + " has fainted.")
                print(pokemonProtagonist.getPokemonOwner().getTrainerName() + " has won.")
                print(pokemonProtagonist.getPokemonName() + " gained 30 EXP.")
        else:
            print(pokemonProtagonist.getPokemonName() + " missed.")