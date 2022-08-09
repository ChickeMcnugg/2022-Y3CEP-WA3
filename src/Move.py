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
            if pokemonOpponent.getPokemonType() in pokemonProtagonist.getPokemonType().getTypeAdvantageList():
                damage *= 2
            elif pokemonOpponent.getPokemonType() in pokemonProtagonist.getPokemonType().getTypeDisadvantageList():
                damage *= 0.5
            elif pokemonOpponent.getPokemonType() in pokemonProtagonist.getPokemonType().getTypeImmuneList():
                damage = 0
            
            defense = pokemonOpponent.getPokemonDefense()
            netDamage = int(max(damage - defense, 0))
            
            pokemonOpponent.addPokemonHealth(-netDamage)

            if pokemonOpponent.getPokemonHealth() == 0:
                print(pokemonOpponent.getPokemonName() + " has fainted.")
                pokemonOpponent.getPokemonOwner().setFaintedPokemon(pokemonOpponent)
                print(pokemonProtagonist.getPokemonName() + " gained 30 EXP.")
                pokemonProtagonist.addPokemonEXP(30)
                
                if pokemonOpponent.getPokemonOwner().checkFainted():
                    battle.setIsEnded(True)
                    print(pokemonProtagonist.getPokemonOwner().getTrainerName() + " has won.")
                else:
                    if battle.getTrainerOpponent() == pokemonOpponent.getPokemonOwner():
                        availablePokemon = pokemonOpponent.getPokemonOwner().getTrainerLivePokemonsDict()
                        if len(availablePokemon) > 1:
                            pokemonOpponent.getPokemonOwner().setTrainerActivePokemon(list(availablePokemon.values())[randint(0, len(availablePokemon.values()) - 1)])
                        else:
                            pokemonOpponent.getPokemonOwner().setTrainerActivePokemon(list(availablePokemon.values())[0])

                        print(pokemonOpponent.getPokemonOwner().getTrainerName() + " chooses " + pokemonOpponent.getPokemonOwner().getTrainerActivePokemon().getPokemonName() + ".")
                    else:
                        pokemonOpponent.getPokemonOwner().choosePokemon()
        else:
            print(pokemonProtagonist.getPokemonName() + " missed.")