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
        print(self)
        sleep(1)

        protagonist = self.getTrainerProtagonist()
        protagonistActivePokemon = protagonist.getTrainerLivePokemonsDict()[protagonist.getTrainerActivePokemon()]
        opponent = self.getTrainerOpponent()
        opponentActivePokemon = opponent.getTrainerLivePokemonsDict()[opponent.getTrainerActivePokemon()]

        print(opponent.getTrainerName() + " chooses " + opponentActivePokemon.getPokemonName() + ".")
        sleep(1)
        print(protagonist.getTrainerName() + " chooses " + protagonistActivePokemon.getPokemonName() + ".")
        sleep(1)

        while not self.getIsEnded():
            if self.getIsProtagonistTurn():
                protagonistActivePokemon = protagonist.getTrainerLivePokemonsDict()[protagonist.getTrainerActivePokemon()]
                opponentActivePokemon = opponent.getTrainerLivePokemonsDict()[opponent.getTrainerActivePokemon()]

                move = protagonistActivePokemon.chooseMove()
                
                if move.getMoveAttribute() == "Attack":
                    move.damage(self, protagonistActivePokemon, opponentActivePokemon)
                    self.setIsProtagonistTurn(False)
                elif move.getMoveAttribute() == "Switch":
                    protagonist.choosePokemon()
            else:
                protagonistActivePokemon = protagonist.getTrainerLivePokemonsDict()[protagonist.getTrainerActivePokemon()]
                opponentActivePokemon = opponent.getTrainerLivePokemonsDict()[opponent.getTrainerActivePokemon()]

                availableMoves = opponentActivePokemon.getPokemonMovesDict()

                if len(availableMoves) < 1:
                    move = availableMoves[list(availableMoves.keys())[0]]
                else:
                    move = availableMoves[list(availableMoves.keys())[randint(0, len(availableMoves) - 1)]]

                if move.getMoveAttribute() == "Attack":
                    move.damage(self, opponent.getTrainerLivePokemonsDict()[opponent.getTrainerActivePokemon()], protagonist.getTrainerLivePokemonsDict()[protagonist.getTrainerActivePokemon()])
                    self.setIsProtagonistTurn(True)