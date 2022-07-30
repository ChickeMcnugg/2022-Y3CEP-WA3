class Battle:
    def __init__(self, trainerProtagonist, trainerOpponent):
        self.trainerProtagonist = trainerProtagonist
        self.trainerOpponent = trainerOpponent
    
    def __repr__(self):
        return "This is a battle between " + self.trainerProtagonist + " and " + self.trainerOpponent + "."
    
    def getTrainerProtagonist(self):
        return self.trainerProtagonist
    
    def getTrainerOpponent(self):
        return self.trainerOpponent

    def startBattle(_trainerProtagonist, _trainerOpponent):
        battle = Battle(_trainerProtagonist, _trainerOpponent)
        
        print(battle)
        protagonist = battle.getTrainerProtagonist()
        opponent = battle.getTrainerOpponent()

        print(opponent.getTrainerName() + " chooses " + opponent.getTrainerActivePokemon().getPokemonName() + ".")
        print(protagonist.getTrainerName() + " chooses " + protagonist.getTrainerActivePokemon().getPokemonName() + ".")

        move = input("Choose your move " + protagonist.getTrainerActivePokemon().getMoves())