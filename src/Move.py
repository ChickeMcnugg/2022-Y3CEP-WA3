#The Move class contains the move's name, type, attribute, power and accuracy.
#A move's type is referenced when assigning to pokemon that have the same type.
#A move's attribute is referenced during battles to differentiate between attacks, recovers, running away and switching out pokemon.
#A move's power and accuarcy is considered during battles to calculate whetehr the attack hits the opponent, adn how much damage is dealt

from random import randint
from time import sleep

class Move:
    def __init__(self, moveName, moveType, moveAttribute, movePower, moveAccuracy, moveEffectors=[]):
        self.moveName = moveName
        self.moveType = moveType

        self.moveAttribute = moveAttribute
        self.movePower = movePower
        
        self.moveAccuracy = moveAccuracy
        self.moveEffectors = moveEffectors
    
    def __repr__(self):
        return "The " + self.moveType.getTypeName() + " move, " + self.moveName + ", has a power of " + str(self.movePower) + "% and an accuracy of " + str(self.moveAccuracy) + "%."
    
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
    
    def getMoveEffectors(self):
        return self.moveEffectors
    
    def damage(self, pokemonProtagonist, pokemonOpponent):
        #Calculate base damage
        damage = ((((2 / 5 * pokemonProtagonist.getPokemonLevel()) + 2) * self.getMovePower() * pokemonProtagonist.getPokemonAttack() / pokemonOpponent.getPokemonDefense() / 50) + 2) * randint(217, 255) / 255

        #Account for type advantages
        if pokemonOpponent.getPokemonType() in pokemonProtagonist.getPokemonType().getTypeAdvantageList():
            damage *= 1.5
            print("It was effective.")
            sleep(1)
        elif pokemonOpponent.getPokemonType() in pokemonProtagonist.getPokemonType().getTypeDisadvantageList():
            damage *= 0.5
            print("It was not effective.")
            sleep(1)
        elif pokemonOpponent.getPokemonType() in pokemonProtagonist.getPokemonType().getTypeImmuneList():
            damage = 0
            print("It has no effect.")
            sleep(1)
        
        #Bound damage to be non-negative
        damage = max(int(damage), 0)
        
        #Calculate accuracy
        accuracy = ((self.moveAccuracy / 100) * (pokemonProtagonist.getPokemonAccuracy() / 100) * (pokemonOpponent.getPokemonEvasion() / 100)) * 100
        accuracy = max(min(accuracy, 100), 1)
        randomChance = randint(0, 100)
        
        #Check if move hits or misses
        if randomChance > accuracy or randomChance == 100:
            #UI
            print(pokemonProtagonist.getPokemonName() + " missed.")
            sleep(1)

            if self.getMoveAttribute() == "MissHit":
                pokemonProtagonist.addPokemonHealth(-(damage // 8))
        else:
            if self.getMoveAttribute() == "KO":
                pokemonOpponent.addPokemonHealth(-pokemonOpponent.getPokemonHealth())
            elif self.getMoveAttribute() == "Constant Attack":
                pokemonOpponent.addPokemonHealth(-self.getMovePower())
            else:
                totalDamage = 0

                if self.getMoveAttribute() == "Multiple Hits":
                    for _ in range(0, randint(2, 5)):
                        pokemonOpponent.addPokemonHealth(-damage)
                        totalDamage += damage
                else:
                    pokemonOpponent.addPokemonHealth(-damage)
                    totalDamage += damage
                
                if self.getMoveAttribute() == "Leech" and totalDamage != 0:
                    pokemonProtagonist.addPokemonHealth(totalDamage // 2)
                
                if self.getMoveAttribute() == "Faint":
                    pokemonProtagonist.addPokemonHealth(-pokemonProtagonist.getPokemonHealth())
            
            #Apply any effects
            if self.getMoveAttribute() == "Effect":
                pokemonOpponent.addPokemonEffects(self.getMoveEffectors())