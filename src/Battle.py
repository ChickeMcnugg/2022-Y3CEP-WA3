#The Encounter classes contain the battle's protagonist and opponent.
#Both are referenced during the battle, and swap when the turn changes.

from random import randint
from time import sleep
from Pokemon import Pokemon

class Encounter:
    def __init__(self, encounterProtagonist, encounterOpponent):
        self.encounterProtagonist = encounterProtagonist
        self.encounterOpponent = encounterOpponent
        self.isProtagonistTurn = True
        self.isEnded = False
        self.isPokemonEncounter = isinstance(self.encounterOpponent, Pokemon)
        self.hasEXPAll = False
    
    def __repr__(self):
        if self.isPokemonEncounter:
            return "This is a battle between " + self.encounterProtagonist.getTrainerName() + " and " + self.encounterOpponent.getPokemonName() + "."
        else:
            return "This is a battle between " + self.encounterProtagonist.getTrainerName() + " and " + self.encounterOpponent.getTrainerName() + "."

    def getEncounterProtagonist(self):
        return self.encounterProtagonist
    
    def getEncounterOpponent(self):
        return self.encounterOpponent
    
    def getIsProtagonistTurn(self):
        return self.isProtagonistTurn
    
    def setIsProtagonistTurn(self, isTurn):
        self.isProtagonistTurn = isTurn
    
    def getIsEnded(self):
        return self.isEnded
    
    def setIsEnded(self, isEnded):
        self.isEnded = isEnded
    
    def getHasEXPAll(self):
        return self.hasEXPAll
    
    def setHasEXPAll(self, hasEXPAll):
        self.hasEXPAll = hasEXPAll
    
    def getIsPokemonEncounter(self):
        return self.isPokemonEncounter

    def startBattle(self):
        if self.isPokemonEncounter:
            opponentActivePokemon = self.encounterOpponent
            print("A wild " + opponentActivePokemon.getPokemonName() + " appeared.")
            sleep(1)
        else:
            opponent = self.encounterOpponent
            opponentActivePokemon = opponent.getTrainerLivePokemonsDict()[opponent.getTrainerActivePokemon()]
            print(self)
            sleep(1)
            print(opponent.getTrainerName() + " chooses " + opponentActivePokemon.getPokemonName() + ".")
            sleep(1)

        protagonist = self.encounterProtagonist
        protagonistActivePokemon = protagonist.getTrainerLivePokemonsDict()[protagonist.getTrainerActivePokemon()]
        print(protagonist.getTrainerName() + " chooses " + protagonistActivePokemon.getPokemonName() + ".")
        sleep(1)
        
        while not self.getIsEnded():
            protagonistActivePokemon = protagonist.getTrainerLivePokemonsDict()[protagonist.getTrainerActivePokemon()]
            if not self.isPokemonEncounter:
                opponentActivePokemon = opponent.getTrainerLivePokemonsDict()[opponent.getTrainerActivePokemon()]
        
            if self.getIsProtagonistTurn():
                print("It is " + protagonist.getTrainerName() + "'s turn.")
                sleep(1)

                availableActions = []
                protagonistActivePokemon.updateEffects()

                if protagonistActivePokemon.getCannotMoveTurns() > 0:
                    print(protagonistActivePokemon.getPokemonName() + " cannot move.")
                    protagonistActivePokemon.addCannotMoveTurns(-1)
                else:
                    availableActions.append("Fight")
                    availableActions.append("Run")

                if len(protagonist.getTrainerLivePokemonsDict()) > 1:
                    availableActions.append("Switch")
                
                if len(protagonist.getTrainerItemsDict()) != 0:
                    availableActions.append("Bag")

                if len(availableActions) != 0:
                    actionMessage = "What will " + protagonistActivePokemon.getPokemonName() + " do? ("
                    for action in availableActions:
                        actionMessage += action + ", "
                    actionMessage = actionMessage[:-2] + ") : "

                    action = ""
                    while action not in availableActions:
                        action = input(actionMessage)
                    
                    if action == "Fight":
                        move = protagonistActivePokemon.chooseMove()
                        move.damage(self, protagonistActivePokemon, opponentActivePokemon)
                        
                        if not self.checkDamageOutcome(protagonistActivePokemon, opponentActivePokemon):
                            if move.getMoveAttribute() == "Lower Defense":
                                continue
                            elif move.getMoveAttribute() == "Lower Accuracy":
                                continue
                            elif move.getMoveAttribute() == "Freeze":
                                continue
                            elif move.getMoveAttribute() == "Paralysis":
                                continue
                            elif move.getMoveAttribute() == "Burn":
                                continue
                            elif move.getMoveAttribute() == "Sleep":
                                continue
                            elif move.getMoveAttribute() == "Poison":
                                continue
                        
                        if move.getMoveAttribute() == "Leech":
                            continue
                        elif move.getMoveAttribute() == "MissHit":
                            continue
                        elif move.getMoveAttribute() == "Gain Defense":
                            continue
                        elif move.getMoveAttribute() == "Gain Attack":
                            continue
                        elif move.getMoveAttribute() == "Gain Evasiveness":
                            continue
                        elif move.getMoveAttribute() == "Multiple Hits":
                            continue   
                        elif move.getMoveAttribute() == "Constant Attack":
                            continue
                        elif move.getMoveAttribute() == "Faint":
                            continue
                        elif move.getMoveAttribute() == "KO":
                            continue
                    elif action == "Switch":
                        protagonist.choosePokemon()
                    elif action == "Run":
                        print(protagonist.getTrainerName() + " has decided to run away.")
                        sleep(1)
                        self.setIsEnded(True)
                    else:
                        item = protagonist.chooseItem()

                        if item.getItemAttribute() == "Ball" and self.isPokemonEncounter:
                            continue
                        elif item.getItemAttribute() == "Medicine":
                            protagonistActivePokemon.removePokemonEffects(item.getItemPower())
                        elif item.getItemAttribute() == "Revive":
                            availablePokemon = list(protagonist.getTrainerFaintedPokemonsDict().keys())
                            reviveMessage = "Choose a pokemon to revive ("
                            for pokemon in availablePokemon:
                                reviveMessage += pokemon + ", "
                            reviveMessage = reviveMessage[:-2] + ") : "
                            
                            reviveInput = ""
                            while reviveInput not in availablePokemon:
                                reviveInput = input(reviveMessage)
                            
                            revivedPokemon = protagonist.getTrainerFaintedPokemonsDict()[reviveInput]

                            protagonist.revivePokemon(revivedPokemon)
                            print(protagonist.trainerName + "'s " + revivedPokemon.getPokemonName() + " has been revived.")
                            sleep(1)
                            revivedPokemon.setPokemonHealth(revivedPokemon.getPokemonMaxHealth() * item.getItemPower())
                            print(revivedPokemon.getPokemonName() + " has " + revivedPokemon.getPokemonHealth() + " health.")
                        elif item.getItemAttribute() == "Health":
                            protagonistActivePokemon.addPokemonHealth(item.getItemPower())
                        elif item.getItemAttribute() == "EXP":
                            self.setHasEXPAll(True)
                        elif item.getItemAttribute() == "Level":
                            protagonistActivePokemon.addPokemonLevel(item.getItemPower())
                        elif item.getItemAttribute() == "Accuracy":
                            protagonistActivePokemon.addPokemonAccuracy(item.getItemPower())
                        elif item.getItemAttribute() == "Attack":
                            protagonistActivePokemon.addPokemonAttack(item.getItemPower())
                        elif item.getItemAttribute() == "Defense":
                            protagonistActivePokemon.addPokemonDefense(item.getItemPower())
                        else:
                            continue

                self.setIsProtagonistTurn(False)
            else:
                if self.isPokemonEncounter:
                    print("It is " + opponentActivePokemon.getPokemonName() + "'s turn.")
                else:
                    print("It is " + opponent.getTrainerName() + "'s turn.")
                sleep(1)

                opponentActivePokemon.updateEffects()

                if opponentActivePokemon.getCannotMoveTurns() > 0:
                    print(opponentActivePokemon.getPokemonName() + " cannot move.")
                    opponentActivePokemon.addCannotMoveTurns(-1)
                else:
                    availableMoves = list(opponentActivePokemon.getPokemonMovesDict().keys())

                    if len(availableMoves) == 1:
                        move = opponentActivePokemon.getPokemonMovesDict()[availableMoves[0]]
                    else:
                        move = opponentActivePokemon.getPokemonMovesDict()[availableMoves[randint(0, len(availableMoves) - 1)]]

                    if move.getMoveAttribute() == "Attack":
                        move.damage(self, opponentActivePokemon, protagonistActivePokemon)
                
                self.setIsProtagonistTurn(True)

    def checkOutcome(self, pokemonProtagonist, pokemonOpponent):
        #Check if opponent's active pokemon has fainted
        if pokemonOpponent.getPokemonHealth() != 0:
            return False
        else:
            #UI
            print(pokemonOpponent.getPokemonName() + " has fainted.")
            sleep(1)
            
            if pokemonOpponent.getPokemonOwner() == None:
                self.setIsEnded(True)
                print(pokemonProtagonist.getPokemonOwner().getTrainerName() + " has won.")
                sleep(1)
            else:
                pokemonOpponent.getPokemonOwner().setFaintedPokemon(pokemonOpponent)

                #Check if opponent has other available pokemon
                if pokemonOpponent.getPokemonOwner().checkFainted():
                    self.setIsEnded(True)
                    print(pokemonProtagonist.getPokemonOwner().getTrainerName() + " has won.")
                    sleep(1)
                    if not self.getHasEXPAll():
                        print(pokemonProtagonist.getPokemonName() + " gained 30 EXP.")
                        pokemonProtagonist.addPokemonEXP(30)
                        sleep(1)
                    else:
                        for pokemon in list(pokemonProtagonist.getPokemonOwner().getTrainerLivePokemonsDict().keys()):
                            pokemonProtagonist.getPokemonOwner().getTrainerLivePokemonsDict()[pokemon].addPokemonEXP(30)
                            print(pokemon + " gained 30 EXP.")
                else:
                    #Check if opponent is the opponent, because the player can only input for the protagonist
                    if self.getEncounterProtagonist() == pokemonOpponent.getPokemonOwner():
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
            
            return True