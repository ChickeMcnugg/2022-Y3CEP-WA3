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

                availableActions = ["Fight", "Run"]
                if len(protagonist.getTrainerLivePokemonsDict()) > 1:
                    availableActions.append("Switch")
                if len(protagonist.getTrainerItemsDict()) != 0:
                    availableActions.append("Bag")

                actionMessage = "What will " + protagonistActivePokemon.getPokemonName() + " do? ("
                for action in availableActions:
                    actionMessage += action + ", "
                actionMessage = actionMessage[:-2] + ") : "

                action = ""
                while action not in availableActions:
                    action = input(actionMessage)
                
                if action == "Fight":
                    move = protagonistActivePokemon.chooseMove()
                    
                    #Subsequent actions are found inside the functions
                    if move.getMoveAttribute() == "Attack":
                        move.damage(self, protagonistActivePokemon, opponentActivePokemon)

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
                        continue
                    elif item.getItemAttribute() == "Revive":
                        continue
                    elif item.getItemAttribute() == "Health":
                        protagonistActivePokemon.addPokemonHealth(item.getItemPower())
                    elif item.getItemAttribute() == "EXP":
                        continue
                    elif item.getItemAttribute() == "Level":
                        continue
                    elif item.getItemAttribute() == "Accuracy":
                        continue
                    elif item.getItemAttribute() == "Attack":
                        continue
                    elif item.getItemAttribute() == "Defense":
                        continue
                    else:
                        continue
                self.setIsProtagonistTurn(False)
            else:
                if self.isPokemonEncounter:
                    print("It is " + opponentActivePokemon.getPokemonName() + "'s turn.")
                else:
                    print("It is " + opponent.getTrainerName() + "'s turn.")
                sleep(1)

                availableMoves = list(opponentActivePokemon.getPokemonMovesDict().keys())

                if len(availableMoves) == 1:
                    move = opponentActivePokemon.getPokemonMovesDict()[availableMoves[0]]
                else:
                    move = opponentActivePokemon.getPokemonMovesDict()[availableMoves[randint(0, len(availableMoves) - 1)]]

                if move.getMoveAttribute() == "Attack":
                    move.damage(self, opponentActivePokemon, protagonistActivePokemon)
                
                self.setIsProtagonistTurn(True)