from random import randint

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

        protagonist = self.getTrainerProtagonist()
        protagonistActivePokemon = protagonist.getTrainerLivePokemonsDict()[protagonist.getTrainerActivePokemon()]
        opponent = self.getTrainerOpponent()
        opponentActivePokemon = opponent.getTrainerLivePokemonsDict()[opponent.getTrainerActivePokemon()]

        print(opponent.getTrainerName() + " chooses " + opponentActivePokemon.getPokemonName() + ".")
        print(protagonist.getTrainerName() + " chooses " + protagonistActivePokemon.getPokemonName() + ".")

        while not self.getIsEnded():
            if self.getIsProtagonistTurn():
                moveMessage = "Choose your move ("
                for move in list(protagonistActivePokemon.getPokemonMovesDict().keys()):
                    moveMessage += move + ", "
                moveMessage = moveMessage[:-2] + ") : "

                moveInput = ""
                
                while moveInput not in list(protagonistActivePokemon.getPokemonMovesDict().keys()):
                    moveInput = input(moveMessage)
                else:
                    move = protagonistActivePokemon.getPokemonMovesDict()[moveInput]
                    
                    if move.getMoveAttribute() == "Attack":
                        move.damage(self, protagonistActivePokemon, opponentActivePokemon)
                        self.setIsProtagonistTurn(False)
                    elif move.getMoveAttribute() == "Switch":
                        pokemonMessage = "Choose a new Pokemon to switch in ("
                        for pokemon in list(protagonist.getTrainerLivePokemonsDict().keys()):
                            pokemonMessage += pokemon + ", "
                        pokemonMessage = pokemonMessage[:-2] + ") : "

                        pokemonInput = ""
                        
                        while pokemonInput not in list(protagonist.getTrainerLivePokemonsDict().keys()):
                            pokemonInput = input(pokemonMessage)
                        else:
                            protagonist.setTrainerActivePokemon(protagonist.getTrainerPokemonsList()[pokemonInput])
            else:
                availableMoves = opponent.getTrainerPokemonsList()[opponent.getTrainerActivePokemon()].getPokemonMovesList()
                availableMoveNames = []

                for key in availableMoves.keys():
                    availableMoveNames.append(key)

                if len(availableMoveNames) < 1:
                    move = availableMoves[availableMoveNames[0]]
                else:
                    move = availableMoves[availableMoveNames[randint(0, len(availableMoveNames) - 1)]]

                if move.getMoveAttribute() == "Attack":
                    move.damage(self, opponent.getTrainerPokemonsList()[opponent.getTrainerActivePokemon()], protagonist.getTrainerPokemonsList()[protagonist.getTrainerActivePokemon()])
                    self.setIsProtagonistTurn(True)