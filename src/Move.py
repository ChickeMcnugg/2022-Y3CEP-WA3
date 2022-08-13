#The Move class contains the move's name, type, attribute, power and accuracy.
#A move's type is referenced when assigning to pokemon that have the same type.
#A move's attribute is referenced during battles to differentiate between attacks, recovers, running away and switching out pokemon.
#A move's power and accuarcy is considered during battles to calculate whetehr the attack hits the opponent, adn how much damage is dealt

from random import randint
from time import sleep

class Move:
    def __init__(self, moveName, moveType, moveAttribute, movePower, moveAccuracy):
        self.moveName = moveName
        self.moveType = moveType
        self.moveAttribute = moveAttribute
        self.movePower = movePower
        self.moveAccuracy = moveAccuracy
        self.moveEffectors = []
    
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

    def addMoveEffectors(self, newEffector):
        self.moveEffectors.append(newEffector)
    
    def damage(self, battle, pokemonProtagonist, pokemonOpponent):
        #UI
        print(pokemonProtagonist.getPokemonName() + " uses " + self.moveName + ".")
        sleep(1)
        
        #Calculate if move hits pokemonOpponent based on accuracy
        if randint(1, 100) < 100 - (((self.moveAccuracy / 100) * (pokemonProtagonist.getPokemonAccuracy() / 100) * (pokemonOpponent.getPokemonEvasion() / 100)) * 100):
            print(pokemonProtagonist.getPokemonName() + " missed.")
            sleep(1)
        else:
            damage = pokemonProtagonist.getPokemonAttack() * (self.getMovePower() / 30)
            hasEffect = True

            #Account for type advantages
            if pokemonOpponent.getPokemonType() in pokemonProtagonist.getPokemonType().getTypeAdvantageList():
                damage *= 2
                print("It was effective.")
                sleep(1)
            elif pokemonOpponent.getPokemonType() in pokemonProtagonist.getPokemonType().getTypeDisadvantageList():
                damage *= 0.5
                print("It was not effective.")
                sleep(1)
                hasEffect = False
            elif pokemonOpponent.getPokemonType() in pokemonProtagonist.getPokemonType().getTypeImmuneList():
                damage = 0
                print("It has no effect.")
                sleep(1)
                hasEffect = False
            
            defense = pokemonOpponent.getPokemonDefense()
            netDamage = int(max(damage - defense, 0))
            
            pokemonOpponent.addPokemonHealth(-netDamage)

            #Check if opponent's active pokemon has fainted
            if pokemonOpponent.getPokemonHealth() == 0:
                #UI
                print(pokemonOpponent.getPokemonName() + " has fainted.")
                sleep(1)
                
                if pokemonOpponent.getPokemonOwner() == None:
                    battle.setIsEnded(True)
                    print(pokemonProtagonist.getPokemonOwner().getTrainerName() + " has won.")
                    sleep(1)
                else:
                    pokemonOpponent.getPokemonOwner().setFaintedPokemon(pokemonOpponent)

                    #Check if opponent has other available pokemon
                    if pokemonOpponent.getPokemonOwner().checkFainted():
                        battle.setIsEnded(True)
                        print(pokemonProtagonist.getPokemonOwner().getTrainerName() + " has won.")
                        sleep(1)
                        if not battle.getHasEXPAll():
                            print(pokemonProtagonist.getPokemonName() + " gained 30 EXP.")
                            pokemonProtagonist.addPokemonEXP(30)
                            sleep(1)
                        else:
                            for pokemon in list(pokemonProtagonist.getPokemonOwner().getTrainerLivePokemonsDict().keys()):
                                pokemonProtagonist.getPokemonOwner().getTrainerLivePokemonsDict()[pokemon].addPokemonEXP(30)
                                print(pokemon + " gained 30 EXP.")
                    else:
                        #Check if opponent is the opponent, because the player can only input for the protagonist
                        if battle.getEncounterProtagonist() == pokemonOpponent.getPokemonOwner():
                            pokemonOpponent.getPokemonOwner().choosePokemon()
                        else:
                            #Randomly choose new active pokemon from live pokemons
                            availablePokemon = pokemonOpponent.getPokemonOwner().getTrainerLivePokemonsDict()
                            if len(availablePokemon) > 1:
                                pokemonOpponent.getPokemonOwner().setTrainerActivePokemon(list(availablePokemon.values())[randint(0, len(availablePokemon.values()) - 1)])
                            else:
                                pokemonOpponent.getPokemonOwner().setTrainerActivePokemon(list(availablePokemon.values())[0])

                            print(pokemonOpponent.getPokemonOwner().getTrainerName() + " chooses " + pokemonOpponent.getPokemonOwner().getTrainerActivePokemon() + ".")
                            sleep(1)
            else:
                if hasEffect:
                    for effector in self.getMoveEffectors():
                        if effector.getEffectType() != pokemonOpponent.getPokemonType():
                            pokemonOpponent.addPokemonEffects([effector])