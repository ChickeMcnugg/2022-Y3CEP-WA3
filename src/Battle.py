#The Encounter classes contain the battle's protagonist and opponent.
#Both are referenced during the battle, and swap when the turn changes.

from math import floor
from random import randint
from time import sleep
from Pokemon import Pokemon

class Encounter:
    def __init__(self, encounterProtagonist, encounterOpponent):
        self.encounterProtagonist = encounterProtagonist
        self.encounterOpponent = encounterOpponent
        self.isPokemonEncounter = isinstance(self.encounterOpponent, Pokemon)

        self.isProtagonistTurn = True
        self.isEnded = False
        
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
    
    def getIsPokemonEncounter(self):
        return self.isPokemonEncounter

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
    
    def startBattle(self):
        if self.isPokemonEncounter:
            opponentActivePokemon = self.encounterOpponent

            #UI
            print("A wild " + opponentActivePokemon.getPokemonName() + " appeared.")
            sleep(1)
            print(opponentActivePokemon)
            sleep(1)
        else:
            opponent = self.encounterOpponent
            opponentActivePokemon = opponent.getTrainerLivePokemonsDict()[opponent.getTrainerActivePokemon()]
            
            #UI
            print(self)
            sleep(1)
            print(opponent.getTrainerName() + " chooses " + opponentActivePokemon.getPokemonName() + ".")
            sleep(1)

        protagonist = self.encounterProtagonist
        protagonistActivePokemon = protagonist.getTrainerLivePokemonsDict()[protagonist.getTrainerActivePokemon()]
        
        #UI
        print(protagonist.getTrainerName() + " chooses " + protagonistActivePokemon.getPokemonName() + ".")
        sleep(1)
        
        #Check if the fight can continue
        while not self.getIsEnded():
            #Update protagonistActivePokemon and opponentActivePokemon
            protagonistActivePokemon = protagonist.getTrainerLivePokemonsDict()[protagonist.getTrainerActivePokemon()]
            if not self.isPokemonEncounter:
                opponentActivePokemon = opponent.getTrainerLivePokemonsDict()[opponent.getTrainerActivePokemon()]

            #Check if it is protagonist's turn
            if self.getIsProtagonistTurn():
                #UI
                print("It is " + protagonist.getTrainerName() + "'s turn.")
                sleep(1)

                #Effects take effect
                protagonistActivePokemon.updateEffects()

                availableActions = []

                #Check if protagonistActivePokemon can fight
                if protagonistActivePokemon.getCannotMoveTurns() > 0:
                    print(protagonistActivePokemon.getPokemonName() + " cannot move.")
                    protagonistActivePokemon.addCannotMoveTurns(-1)
                else:
                    availableActions.append("Fight")
                    availableActions.append("Run")
                
                #Check if protagonist can switch to other pokemon
                if len(protagonist.getTrainerLivePokemonsDict()) > 1:
                    availableActions.append("Switch")
                
                #Check if protagonist can use items
                if len(protagonist.getTrainerItemsDict()) != 0:
                    availableActions.append("Bag")

                if len(availableActions) != 0:
                    #UI
                    actionMessage = "What will " + protagonistActivePokemon.getPokemonName() + " do? ("
                    for action in availableActions:
                        actionMessage += action + ", "
                    actionMessage = actionMessage[:-2] + ") : "

                    action = ""
                    
                    #Wait until user's input is valid
                    while action not in availableActions:
                        action = input(actionMessage)
                    
                    if action == "Fight":
                        move = protagonistActivePokemon.chooseMove()

                        self.useMove(move, protagonistActivePokemon, opponentActivePokemon)

                        self.checkOutcome(protagonistActivePokemon, opponentActivePokemon)
                        self.checkOutcome(opponentActivePokemon, protagonistActivePokemon)
                    elif action == "Switch":
                        protagonist.choosePokemon()
                    elif action == "Run":
                        #UI
                        print(protagonist.getTrainerName() + " has decided to run away.")
                        sleep(1)
                        
                        self.setIsEnded(True)
                    else:
                        item = protagonist.chooseItem()

                        self.useItem(item, protagonistActivePokemon, opponentActivePokemon)

                self.setIsProtagonistTurn(False)
            else:
                #UI
                if self.isPokemonEncounter:
                    print("It is " + opponentActivePokemon.getPokemonName() + "'s turn.")
                else:
                    print("It is " + opponent.getTrainerName() + "'s turn.")
                sleep(1)

                #Effects take effect
                opponentActivePokemon.updateEffects()

                #Check if opponentActivePokemon can fight
                if opponentActivePokemon.getCannotMoveTurns() > 0:
                    print(opponentActivePokemon.getPokemonName() + " cannot move.")
                    opponentActivePokemon.addCannotMoveTurns(-1)
                else:
                    #Randomyl pick a move from opponentActivePOkemon's move dictionary
                    availableMoves = list(opponentActivePokemon.getPokemonMovesDict().keys())

                    if len(availableMoves) == 1:
                        move = opponentActivePokemon.getPokemonMovesDict()[availableMoves[0]]
                    else:
                        move = opponentActivePokemon.getPokemonMovesDict()[availableMoves[randint(0, len(availableMoves) - 1)]]

                    self.useMove(move, opponentActivePokemon, protagonistActivePokemon)

                    self.checkOutcome(opponentActivePokemon, protagonistActivePokemon)
                    self.checkOutcome(protagonistActivePokemon, opponentActivePokemon)
                
                self.setIsProtagonistTurn(True)

    def useMove(self, move, pokemonProtagonist, pokemonOpponent):
        #UI
        print(pokemonProtagonist.getPokemonName() + " uses " + move.getMoveName() + ".")
        sleep(1)

        if move.getMoveAttribute() == "Lower Defense":
            pokemonOpponent.addPokemonDefense(-move.getMovePower())
        elif move.getMoveAttribute() == "Lower Accuracy":
            pokemonOpponent.addPokemonAccuracy(-move.getMovePower())
        if move.getMoveAttribute() == "Gain Defense":
            pokemonProtagonist.addPokemonDefense(move.getMovePower())
        elif move.getMoveAttribute() == "Gain Attack":
            pokemonProtagonist.addPokemonAttack(move.getMovePower())
        elif move.getMoveAttribute() == "Gain Evasiveness":
            pokemonProtagonist.addPokemonEvasion(-move.getMovePower())
        else:
            move.damage(pokemonProtagonist, pokemonOpponent)

    def useItem(self, item, pokemonProtagonist, pokemonOpponent):
        if item.getItemAttribute() == "Ball" and self.isPokemonEncounter:
            isCaught = False

            #Check if ball used is "Master Ball"
            if item.getItemPower() == 0:
                isCaught = True
            else:
                #Calculate chance of being caught with effects
                randomChance = randint(0, item.getItemPower())
                
                for effect in pokemonOpponent.getPokemonEffects():
                    if not isCaught:
                        if effect.getEffectAttribute() == "Move":
                            if randomChance < 25 or randomChance - 25 <= pokemonOpponent.getPokemonCatchRate():
                                isCaught = True
                        elif effect.getEffectAttribute() == "Attack":
                            if randomChance < 12 or randomChance - 12 <= pokemonOpponent.getPokemonCatchRate():
                                isCaught = True

                #Calculate chance of being caught with catch rate
                if not isCaught:    
                    randomChance = randint(0, 255)
                    catchRate = pokemonOpponent.getPokemonMaxHealth() / pokemonOpponent.getPokemonHealth() * 255 * 4

                    #Check if ball used is "Great Ball"
                    if item.getItemPower() == 200:
                        catchRate /= 8
                    else:
                        catchRate /= 12

                    #Bound catchRate from 1 to 255
                    catchRate = max(min(floor(catchRate), 255), 1)
                    
                    if randomChance <= catchRate:
                        isCaught = True

            #Check if pokemonOpponent has been caught
            if isCaught:
                #UI
                print(pokemonOpponent.getPokemonName() + " has been caught.")
                sleep(1)

                nameInput = ""

                #Ask user to change pokemon name to a valid name
                while (nameInput == "") or (nameInput in pokemonProtagonist.getPokemonOwner().getTrainerLivePokemonsDict()):
                    nameInput = input("What is your " + pokemonOpponent.getPokemonName() + "'s name? : ").strip()
                sleep(1)
                
                pokemonOpponent.changePokemonName(nameInput)
                pokemonProtagonist.getPokemonOwner().addTrainerLivePokemonsDict(pokemonOpponent)
            else:
                #UI
                print("It missed. " + pokemonOpponent.getPokemonName() + " ran away.")
                sleep(1)

            #End the battle
            self.isEnded = True
        elif item.getItemAttribute() == "Medicine":
            pokemonProtagonist.removePokemonEffects(item.getItemPower())
        elif item.getItemAttribute() == "Revive":
            trainerProtagonist = pokemonProtagonist.getPokemonOwner()
            availablePokemon = list(trainerProtagonist.getTrainerFaintedPokemonsDict().keys())
            
            #UI
            reviveMessage = "Choose a pokemon to revive ("
            for pokemon in availablePokemon:
                reviveMessage += pokemon + ", "
            reviveMessage = reviveMessage[:-2] + ") : "
            
            reviveInput = ""
            
            #Wait until user's input is valid
            while reviveInput not in availablePokemon:
                reviveInput = input(reviveMessage)
            
            sleep(1)
            revivedPokemon = trainerProtagonist.getTrainerFaintedPokemonsDict()[reviveInput]
            trainerProtagonist.revivePokemon(revivedPokemon)
            revivedPokemon.setPokemonHealth(revivedPokemon.getPokemonMaxHealth() * item.getItemPower())

            #UI
            print(trainerProtagonist.getTrainerName() + "'s " + revivedPokemon.getPokemonName() + " has been revived.")
            sleep(1)
            print(revivedPokemon.getPokemonName() + " has " + revivedPokemon.getPokemonHealth() + " health.")
            sleep(1)
        elif item.getItemAttribute() == "Health":
            pokemonProtagonist.addPokemonHealth(item.getItemPower())
        elif item.getItemAttribute() == "EXP":
            self.setHasEXPAll(True)
        elif item.getItemAttribute() == "Level":
            pokemonProtagonist.addPokemonLevel(item.getItemPower())
        elif item.getItemAttribute() == "Accuracy":
            pokemonProtagonist.addPokemonAccuracy(item.getItemPower())
        elif item.getItemAttribute() == "Attack":
            pokemonProtagonist.addPokemonAttack(item.getItemPower())
        elif item.getItemAttribute() == "Defense":
            pokemonProtagonist.addPokemonDefense(item.getItemPower())

    def checkOutcome(self, pokemonProtagonist, pokemonOpponent):
        #Check if opponent's active pokemon has fainted
        if pokemonOpponent.getPokemonHealth() == 0:
            #UI
            print(pokemonOpponent.getPokemonName() + " has fainted.")
            sleep(1)
            pokemonOpponent.resetStats()
            
            if pokemonOpponent.getPokemonOwner() == None:
                self.setIsEnded(True)
            else:
                pokemonOpponent.getPokemonOwner().setFaintedPokemon(pokemonOpponent)

                #Check if opponent has other available pokemon
                if pokemonOpponent.getPokemonOwner().checkFainted():
                    self.setIsEnded(True)
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
            
            if self.getIsEnded():
                pokemonProtagonist.resetStats()

                #UI
                if pokemonProtagonist.getPokemonOwner() == None:
                    print(pokemonProtagonist.getPokemonName() + " has run away.")
                else:
                    print(pokemonProtagonist.getPokemonOwner().getTrainerName() + " has won.")
                    sleep(1)

                    #Check if winner is encounterProtagonist
                    if self.getEncounterProtagonist() == pokemonProtagonist.getPokemonOwner():
                        pokemonProtagonist.getPokemonOwner().addTrainerMoney(50 * pokemonOpponent.getPokemonLevel())

                        gainedEXP = pokemonOpponent.getPokemonDefeatEXP() * pokemonOpponent.getPokemonLevel()
                        if pokemonOpponent.getPokemonOwner() != None:
                            gainedEXP *= 1.5
                        gainedEXP = int(gainedEXP // 7)

                        #Check if "EXP All" has been used during the battle
                        if not self.getHasEXPAll():
                            pokemonProtagonist.addPokemonEXP(gainedEXP)
                        else:
                            for pokemon in list(pokemonProtagonist.getPokemonOwner().getTrainerLivePokemonsDict().keys()):
                                pokemonProtagonist.getPokemonOwner().getTrainerLivePokemonsDict()[pokemon].addPokemonEXP(gainedEXP)