from time import sleep

class Trainer:
    def __init__(self, trainerName, trainerLivePokemonsDict, trainerItemsDict, trainerLocation):
        self.trainerName = trainerName
        self.trainerLivePokemonsDict = trainerLivePokemonsDict
        for pokemonKey in self.trainerLivePokemonsDict:
            self.trainerLivePokemonsDict[pokemonKey].setPokemonOwner(self)
        self.trainerActivePokemon = list(trainerLivePokemonsDict.keys())[0]
        self.trainerFaintedPokemonDict = {}
        self.trainerItemsDict = trainerItemsDict
        self.trainerLocation = trainerLocation
        trainerLocation.addLocationTrainer(self)
    
    def __repr__(self):
        output = self.trainerName + " the trainer has "

        if len(self.trainerLivePokemonsDict) == 0:
            output += "no pokemons "
        else:
            for pokemonKey in self.trainerLivePokemonsDict:
                output += "a " + pokemonKey + ", "
        
        output += "and "

        if len(self.trainerItemsDict) == 0:
            output += "no items"
        else:
            for itemKey in range(0, len(self.trainerItemsDict) - 1):
                output += "a " + itemKey + ", "
            
            output += "and a " + self.trainerItemsDict[-1]
        
        output += "."

        return output
    
    def getTrainerName(self):
        return self.trainerName
    
    def getTrainerLivePokemonsDict(self):
        return self.trainerLivePokemonsDict
    
    def getTrainerFaintedPokemonsDict(self):
        return self.trainerFaintedPokemonDict

    def setFaintedPokemon(self, newPokemon):
        #Move the fainted pokemon from the live dictionary to fainted dictionary
        self.trainerFaintedPokemonDict[newPokemon.getPokemonName().capitalize()] = newPokemon
        del(self.trainerLivePokemonsDict[newPokemon.getPokemonName().capitalize()])

        #Reset trainer's active pokemon
        self.trainerActivePokemon = ""
    
    def getTrainerActivePokemon(self):
        return self.trainerActivePokemon
    
    def setTrainerActivePokemon(self, newPokemon):
        self.trainerActivePokemon = newPokemon.getPokemonName().capitalize()
        print(self.trainerName + " chooses " + newPokemon.getPokemonName() + ".")
        sleep(1)
    
    def getTrainerItemsList(self):
        return self.trainerItemsList

    def getTrainerLocation(self):
        return self.trainerLocation

    def setTrainerLocation(self, newLocation):
        #Reference location in Trainer, and trainer in Location
        self.trainerLocation = newLocation
        newLocation.addLocationTrainer(self)
        print(self.trainerName + " is now in " + newLocation.getLocationName() + ".")
        sleep(1)

    def moveToLocation(self, newDirection):
        sleep(1)

        #Check if the input is valid
        if newDirection in self.trainerLocation.getLocationNeighboursDict():
            self.setTrainerLocation(self.trainerLocation.getLocationNeighboursDict()[newDirection])
            return True
        else:
            print("It is a dead end. Please try again.")
            sleep(1)
            return False
    
    def checkFainted(self):
        if len(self.trainerLivePokemonsDict) == 0:
            print(self.trainerName + " has no more pokemon able to participate in battle.")
            sleep(1)
            return True
        else:
            return False

    def choosePokemon(self):
        #UI    
        pokemonMessage = "Choose a pokemon ("
        for pokemon in list(self.trainerLivePokemonsDict.keys()):
            pokemonMessage += pokemon + ", "
        pokemonMessage = pokemonMessage[:-2] + ") : "

        pokemonInput = ""

        #Wait until user's input is valid
        while pokemonInput not in self.trainerLivePokemonsDict:
            pokemonInput = input(pokemonMessage)
        else:
            self.trainerActivePokemon = pokemonInput
            sleep(1)
            print(self.trainerName + " chooses " + pokemonInput)