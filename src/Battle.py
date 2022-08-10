from random import randint
from time import sleep

class Battle:
    def __init__(self, trainerProtagonist, trainerOpponent):
        self.trainerProtagonist = trainerProtagonist
        self.trainerOpponent = trainerOpponent
        self.isProtagonistTurn = True
        self.isEnded = False
    
    def __repr__(self):
        return "This is a battle between " + self.trainerProtagonist.getTrainerName() + " and " + self.trainerOpponent.getTrainerName() + "."
    
    def getTrainerProtagonist(self):
        return self.trainerProtagonist
    
    def getTrainerOpponent(self):
        return self.trainerOpponent
    
    def getIsProtagonistTurn(self):
        return self.isProtagonistTurn
    
    def setIsProtagonistTurn(self, isTurn):
        self.isProtagonistTurn = isTurn
    
    def getIsEnded(self):
        return self.isEnded
    
    def setIsEnded(self, isEnded):
        self.isEnded = isEnded

    def startBattle(self):
        #UI
        print(self)
        sleep(1)

        #defining variables for later use
        protagonist = self.getTrainerProtagonist()
        protagonistActivePokemon = protagonist.getTrainerLivePokemonsDict()[protagonist.getTrainerActivePokemon()]
        opponent = self.getTrainerOpponent()
        opponentActivePokemon = opponent.getTrainerLivePokemonsDict()[opponent.getTrainerActivePokemon()]

        #UI
        print(opponent.getTrainerName() + " chooses " + opponentActivePokemon.getPokemonName() + ".")
        sleep(1)
        print(protagonist.getTrainerName() + " chooses " + protagonistActivePokemon.getPokemonName() + ".")
        sleep(1)

        #Check if one player has no available pokemon left to fight
        while not self.getIsEnded():
            #Switches from manual if it is the player's turn, to AI if it is the opponent's turn
            if self.getIsProtagonistTurn():
                #UI
                print("It is " + protagonist.getTrainerName() + "'s turn.")
                sleep(1)

                protagonistActivePokemon = protagonist.getTrainerLivePokemonsDict()[protagonist.getTrainerActivePokemon()]
                opponentActivePokemon = opponent.getTrainerLivePokemonsDict()[opponent.getTrainerActivePokemon()]

                move = protagonistActivePokemon.chooseMove()
                
                #Subsequent actions are found inside the functions
                if move.getMoveAttribute() == "Attack":
                    move.damage(self, protagonistActivePokemon, opponentActivePokemon)
                elif move.getMoveAttribute() == "Switch":
                    protagonist.choosePokemon()
                elif move.getMoveAttribute() == "Run":
                    print(protagonist.getTrainerName() + " has decided to run away.")
                    sleep(1)
                    self.setIsEnded(True)
                
                self.setIsProtagonistTurn(False)
            else:
                #UI
                print("It is " + opponent.getTrainerName() + "'s turn.")
                sleep(1)

                protagonistActivePokemon = protagonist.getTrainerLivePokemonsDict()[protagonist.getTrainerActivePokemon()]
                opponentActivePokemon = opponent.getTrainerLivePokemonsDict()[opponent.getTrainerActivePokemon()]

                availableMoves = list(opponentActivePokemon.getPokemonMovesDict().keys())

                #Check if there are available pokemon to switch to
                if len(opponent.getTrainerLivePokemonsDict()) < 2:
                    availableMoves.remove("Switch")

                #Opponent cannot run away from the battle
                availableMoves.remove("Run")

                #Checks for number of available moves, because randint() cannot work with only one element in a list
                if len(availableMoves) < 1:
                    move = opponentActivePokemon.getPokemonMovesDict()[availableMoves[0]]
                else:
                    move = opponentActivePokemon.getPokemonMovesDict()[availableMoves[randint(0, len(availableMoves) - 1)]]

                if move.getMoveAttribute() == "Attack":
                    move.damage(self, opponent.getTrainerLivePokemonsDict()[opponent.getTrainerActivePokemon()], protagonist.getTrainerLivePokemonsDict()[protagonist.getTrainerActivePokemon()])
                elif move.getMoveAttribute() == "Switch":
                    availablePokemon = list(opponent.getTrainerLivePokemonsDict().keys())

                    #Checks for number of available mvoes, because randint() cannot work with only one element in a list
                    if len(availablePokemon) < 1:
                        newPokemon = opponent.getTrainerLivePokemonsDict()[availablePokemon[0]]
                    else:
                        newPokemon = opponent.getTrainerLivePokemonsDict()[availablePokemon[randint(0, len(availablePokemon) - 1)]]
                    
                    opponent.setTrainerActivePokemon(newPokemon)

                self.setIsProtagonistTurn(True)