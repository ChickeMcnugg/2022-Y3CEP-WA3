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

    def startBattle(_trainerProtagonist, _trainerOpponent):
        battle = Battle(_trainerProtagonist, _trainerOpponent)
        
        print(battle)
        protagonist = battle.getTrainerProtagonist()
        opponent = battle.getTrainerOpponent()

        print(opponent.getTrainerName() + " chooses " + opponent.getTrainerActivePokemon() + ".")
        print(protagonist.getTrainerName() + " chooses " + protagonist.getTrainerActivePokemon() + ".")

        while not battle.getIsEnded():
            if battle.getIsProtagonistTurn():
                availableMoves = protagonist.getTrainerPokemonsList()[protagonist.getTrainerActivePokemon()].getPokemonMovesList()
                availableMoveNames = []

                for key in availableMoves.keys():
                    availableMoveNames.append(key)

                moveMessage = "Choose your move ("
                for move in availableMoveNames:
                    moveMessage += move + ", "
                moveMessage = moveMessage[:-2] + ") : "

                moveInput = ""
                
                while moveInput not in availableMoveNames:
                    moveInput = input(moveMessage)
                else:
                    move = availableMoves[moveInput]
                    
                    if move.getMoveAttribute() == "Attack":
                        move.damage(battle, protagonist.getTrainerPokemonsList()[protagonist.getTrainerActivePokemon()], opponent.getTrainerPokemonsList()[opponent.getTrainerActivePokemon()])
                        battle.setIsProtagonistTurn(False)
                    elif move.getMoveAttribute() == "Switch":
                        availablePokemon = protagonist.getTrainerPokemonsList()
                        del(availablePokemon[protagonist.getTrainerActivePokemon()])
                        availablePokemonNames = []

                        for key in availablePokemon.keys():
                            availablePokemonNames.append(key)

                        pokemonMessage = "Choose a new Pokemon to switch in ("
                        for pokemon in availablePokemonNames:
                            pokemonMessage += pokemon + ", "
                        pokemonMessage = pokemonMessage[:-2] + ") : "

                        pokemonInput = ""
                        
                        while pokemonInput not in availablePokemonNames:
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
                    move.damage(battle, opponent.getTrainerPokemonsList()[opponent.getTrainerActivePokemon()], protagonist.getTrainerPokemonsList()[protagonist.getTrainerActivePokemon()])
                    battle.setIsProtagonistTurn(True)