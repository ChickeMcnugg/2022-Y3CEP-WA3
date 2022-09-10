#The Trainer class contains a trainer's name, pokemons, items and location.
#A trainer's pokemon and items are referenced during battles.
#A trainer's location is tracked to trigger special events like boss battles and checkpoints, and also affect the pokemon that can appear during random encounters.

from time import sleep

class Trainer:
    def __init__(self, trainerName, trainerLivePokemonsDict, trainerItemsDict, trainerLocation):
        self.trainerName = trainerName
        self.trainerMoney = 3000
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
    
    def getTrainerMoney(self):
        return self.trainerMoney
    
    def addTrainerMoney(self, newMoney):
        #newMoney can be negative if money is spent
        self.trainerMoney += newMoney

        #Different output messages depending on whetehr money was spent or gained
        if newMoney >= 0:
            print(self.trainerName + " gained " + str(newMoney) + " Poke Dollars.")
        else:
            print(self.trainerName + " spent " + str(-newMoney) + " Poke Dollars.")

    def getTrainerLivePokemonsDict(self):
        return self.trainerLivePokemonsDict
    
    def addTrainerLivePokemonsDict(self, newPokemon):
        #Stores the new pokemon with its name as the key so that same pokemon can be stored, as long as they have different names
        self.trainerLivePokemonsDict[newPokemon.getPokemonName()] = newPokemon

        #Pokemon stores information on trainer to be accessed during battles
        newPokemon.setPokemonOwner(self)
    
    def getTrainerFaintedPokemonsDict(self):
        return self.trainerFaintedPokemonDict

    def setFaintedPokemon(self, newPokemon):
        #Move the fainted pokemon from the live dictionary to fainted dictionary
        self.trainerFaintedPokemonDict[newPokemon.getPokemonName().capitalize()] = newPokemon
        del(self.trainerLivePokemonsDict[newPokemon.getPokemonName().capitalize()])

        #Reset trainer's active pokemon
        self.trainerActivePokemon = ""
    
    def revivePokemon(self, newPokemon):
        #Move the fainted pokemon from the fainted dictionary to live dictionary
        self.trainerLivePokemonDict[newPokemon.getPokemonName().capitalize()] = newPokemon
        del(self.trainerFaintedPokemonsDict[newPokemon.getPokemonName().capitalize()])
    
    def getTrainerActivePokemon(self):
        return self.trainerActivePokemon
    
    def setTrainerActivePokemon(self, newPokemon):
        #Used when initialising battles or when previous pokemon in battle has fainted
        self.trainerActivePokemon = newPokemon.getPokemonName().capitalize()
        print(self.trainerName + " chooses " + newPokemon.getPokemonName() + ".")
        sleep(1)
    
    def getTrainerItemsDict(self):
        return self.trainerItemsDict
    
    def addTrainerItem(self, newItem, itemCounter):
        #If the item is already in inventory, add one to the inventory counter, else make a new key to store the new item
        if newItem.getItemName() not in list(self.trainerItemsDict.keys()):
            self.trainerItemsDict[newItem.getItemName()] = [newItem, itemCounter]
        else:
            self.trainerItemsDict[newItem.getItemName()][1] += itemCounter
        
        print(self.trainerName + " now has " + str(self.trainerItemsDict[newItem.getItemName()][1]) + " " + newItem.getItemName() + ".")
    
    def useTrainerItem(self, newItem, itemCounter):
        self.trainerItemsDict[newItem.getItemName()][1] -= itemCounter

        #Check if there are still items, else remove the key as there are no more items
        if self.trainerItemsDict[newItem.getItemName()][1] <= 0:
            del(self.trainerItemsDict[newItem.getItemName()])
        
        print(self.trainerName + " now has " + str(self.trainerItemsDict[newItem.getItemName()][1]) + " " + newItem.getItemName() + ".")

    def getTrainerLocation(self):
        return self.trainerLocation

    def setTrainerLocation(self, newLocation):
        #Reference location in Trainer, and trainer in Location
        self.trainerLocation = newLocation
        newLocation.addLocationTrainer(self)
        print(self.trainerName + " is now in " + newLocation.getLocationName() + ".")
        sleep(1)

    def moveToLocation(self, newDirection):
        #Remove the location reference in Trainer, and the trainer reference in Location
        sleep(1)
        self.trainerLocation.removeLocationTrainer(self)
        self.setTrainerLocation(self.trainerLocation.getLocationNeighboursDict()[newDirection])
    
    def checkFainted(self):
        #Used duriung battles to check if a trainer has pokemon left to continue battling
        if len(self.trainerLivePokemonsDict) == 0:
            print(self.trainerName + " has no more pokemon able to participate in battle.")
            sleep(1)
            return True
        else:
            return False

    def choosePokemon(self):
        #Provide pokemon options
        availablePokemon = list(self.trainerLivePokemonsDict.keys())
        if self.trainerActivePokemon != "":
            availablePokemon.remove(self.trainerActivePokemon)

        #UI
        pokemonMessage = "Choose a pokemon ("
        for pokemon in availablePokemon:
            pokemonMessage += pokemon + ", "
        pokemonMessage = pokemonMessage[:-2] + ") : "

        pokemonInput = ""

        #Wait until user's input is valid
        while pokemonInput not in self.trainerLivePokemonsDict:
            pokemonInput = input(pokemonMessage)

        self.trainerActivePokemon = pokemonInput
        sleep(1)
        print(self.trainerName + " chooses " + pokemonInput)
        print(self.getTrainerLivePokemonsDict()[self.trainerActivePokemon])
    
    def chooseItem(self):
        #Provide item options
        availableItems = list(self.trainerItemsDict.keys())
        
        #UI
        itemMessage = "Choose an item to use ("
        for item in availableItems:
            itemMessage += item + ", "
        itemMessage = itemMessage[:-2] + ") : "

        itemInput = ""
        
        #Wait until user's input is valid
        while itemInput not in availableItems:
            itemInput = input(itemMessage)
        
        item = self.trainerItemsDict[itemInput][0]
        self.useTrainerItem(item, 1)
        print(self.trainerName + " used a " + item.getItemName() + ".")
        sleep(1)
        return item