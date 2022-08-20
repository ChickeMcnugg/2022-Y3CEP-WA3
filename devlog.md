# Development Log
> A successful final project is built slowly over many weeks not thrown together at the last minute. To incentivize good project pacing and to let your project mentor stay informed about the status of your work, each week you should add an entry to your log.md file in the development directory.

> Each entry should describe:

> - What goals you had set for the week and whether they were accomplished or not
> - What problems you encountered (if any) that prevented you from meeting your goals
> - What you plan to accomplish or attempt next week

> The development log will be graded for completion, detail, and honesty – not progress. It is much better to truthfully evaluate the work you completed in a week then lie to make the project sound further along then it really is. It is totally acceptable to have an entry that says you tried nothing and accomplished nothing. However if every week starts to say that, both yourself and your project mentor will be able to identify the issue before it becomes impossible to fix.

## Week 5 (26 Jul - 1 Aug)
>   -   30/7
>       -   Started project on recreating Pokemon
>       -   Implemented classes required (Trainers, Pokemons, Types, Moves, Locations, Items, Battles)
>       -   Trainer class
>           -   Includes Name, Pokemons, Items, Location
>           -   Active Pokemon, Fainted Pokemon are kept track of to reference during battles
>           -   Traiers can move to different locations following the map set up in main.py (See Location class)
>           -   Fully functional for now
>       -   Pokemon class
>           -   Includes Name, Type, Max Health, Attack, Defense, Speed, Evasion, Accuracy
>           -   Level and EXP are kept track of to boost an individual Pokemon's stats
>           -   Moves are kept track of to reference during battles
>           -   Other stats are referenced during battles
>           -   Fully functional for now
>       -   Type class
>           -   Includes Name, Type advantage, Type disadvantage, Type immune
>           -   Defined two fold since all types need to be defined first, before advantages, disadvantages and immunity can be defined
>           -   Fully functional for now
>       -   Moves class
>           -   Includes Name, Type, Power, Accuracy
>           -   Only Pokemon of the same type can "learn" the move
>           -   Power and Accuracy are referenced during battles
>           -   Fully functional for now
>       -   Locations class
>           -   Includes Name
>           -   Incorporated into a map system, where neighbouring locations are kept track of
>           -   Trainers can move through the locations, with a chance of random encounters with wild Pokemon
>           -   Fully functional
>       -   Item class
>           -   Includes Name
>           -   Primitive form as not much work was done. It will only be required after implementing battles
>       -   Battle class
>           -   Includes Player and Opponent
>           -   Players use their active pokemon and respective moves to battle until one > player's pokemons have all fainted
>           -   Items can be used to boost pokemon stats
>           -   Currently work in progress and not functional whatsoever
>       -   main.py houses all trainers, pokemon, types, moves, locations available during the game
>           -   Mostly contains set up commands and other features of teh game are contaiend within their respective files
>           -   It is a pain to define all these variables
>       -   TODO
>           -   Trainer: Switch active pokemon
>           -   Battles: Logic for battling and ending battles
>           -   Moves: Include more moves

>   -   31/7
>       -   Found bug of initiating random encounter regardless of whether protagonist actually changes locations. Fixed.
>       -   Moves seem to be out of the question as each move has its own special cases taht need to be individually implemented. So each mvoe would have to be its own class, or at least have its own method under the Moves class. Might tackle towards teh end when fully developing the game
>       -   Turn based battles have been fully implemented functionally. It took much longer than expected because of my indecisiveness on which file to put commands in, and how to implements Moves
>       -   UI for everything has yet to be done
>       -   I do not know how I am going to implement wild pokemon and trainer pokemons
>           -   Maybe I can create a base pokemon then for every variant I create a temporary copy
>       -   Trainer class
>           -   Location is now kept track of for completionist's sake (Location has reference to Trainer and Trainer has reference to Location)
>           -   Fainted Pokemon hve been mvoed to separate a list to not reference during battles (Only "live" pokemon can be used)
>       -   Moves class
>           -   Houses damage() method to reference during battles (Pokemon moves based on inflicting damage)
>       -   Location class
>           -   Created pokemon list, planning to use for random encounters
>       -   Pokemon Class
>           -   Implemented EXP and Levels, but they do not interact with pokemon stats yet
>           -   Created owner attribute for completionist's sake (Trainer references Pokemon and Pokemon references Trainer) although wild pokemon have not been implemented
>       -   Battle class
>           -   Whose turn it is determined by a boolean isProtagonistTurn
>           -   Procedure:
>               -   Provide list of available moves player can choose, for player to choose
>               -   execute move (Currently only attacks)
>               -   Check if opponent pokemon has fainted (Currently battle ends when active pokemon faints)
>           -   Could probably simplify by making the procedure its own command
>       -   TODO
>       -   Trainer: Switch active pokemon
>       -   Battles: Checkpoint battles and boss battles
>       -   Pokemon: Wild pokemon and random encounters
>       -   Moves: Include more moves
>       -   UI in general
>       -   Full rewrite of code to make it more efficient (way later towards the end)

## Week 6 (2 Aug - 8 Aug)

>   -   6/8
>       -   Implemented switching of Trainer's active pokemon
>       -   During switching, old active pokemon disappears and is replaced by new active pokemon. When switching back from the new to old active pokemon, the key name does not appear
>       -   Need to rethink how all lists will be implemented. Should be changed to dictionaries with keys to make it easier to reference any single element.
>       -   TODO
>           -   Trainer: Switch active pokemon
>           -   Battles: Checkpoint battles and boss battles
>           -   Pokemon: Wild pokemon and random encounters
>           -   Moves: Include more moves
>           -   UI in general
>           -   Full rewrite of code to make it more efficient (way later towards the end)
>   -   7/8
>       -   Began rewriting some code to make accessing information easier
>           -   List attributes of the Trainer class have been switched to dictionaries so that it is easier to access individual pokemon by their name only
>           -   Same applies for pokemon moves, so that it can be more easily printed during battle and referenced elsewhere
>           -   Choosing a new pokemon and choosing a move to play during battle is its own separate function since it is called at multiple times
>       -   pokemonSpeed removed as it has no use now, but maybe will be inserted back at a later stage
>       -   Fixed bug of not removing trainers from Location when leaving the location
>       -   Implemented AI version of choosing moves during battle, and new pokemon when the active pokemon has fainted
>       -   TODO
>           -   Battles: Checkpoint battles and boss battles
>           -   Pokemon: Wild pokemon and random encounters
>           -   Moves: Include more moves
>           -   UI in general

## Week 7 (9 Aug - 15 Aug)
>   -   9/8
>       -   Fixed bug of starting battles even though the protagonist has no available pokemon
>       -   Fixed bug of not updating active pokemon when player switches pokemon during battle
>       -   Fixed minor bugs and typos
>       -   Implemented type advantages during battle
>           -   Having an advantage doubles the damage, having a disadvantage halves the damage, being immune cancels out the damage
>       -   Added time delays between print messages for ease of reading and understanding sequence of events
>           -   Actions taken during battle can still be clearer by signaling whose turn it is and providing to see the current condition of the battle
>       -   Wrote appropriate comments for each function and steps in the function
>           -   Can also write comments for each file describing the purpose of each file
>       -   TODO
>           -   Battles: Prevent player from switching to the same pokemon by removing the option
>           -   Battles: Print pokemon information after switching to it
>           -   Battles: Allow the player to run away
>           -   Battles: Reset each trainer's stats and pokemon after the battle to be reused again if encountered again
>           -   Battles: Checkpoint battles and boss battles
>           -   Battles: Print whose turn it is when switching turns
>           -   Trainers: Create more trainers so that random encounters are more randomised
>           -   Pokemon: Wild pokemon and random encounters
>           -   Moves: Include more moves
>           -   UI in general
>           -   Comment purpose of files
>   -   10/8
>       -   Fixed bug of protagonist being able to switch to the same pokemon by not giving the option
>           -   Technically, the bug still exists but the player does not know that it is possible
>           -   Should fix it in the future by not counting the same pokemon as a valid input
>       -   Removed option to switch pokemon when there are no available pokemon to switch to
>       -   Included more UI into battles to make it easier to understand what is happening
>           -   Whose turn it is during the battle when it switches
>           -   Move used by pokemon
>           -   Effectiveness of damage based on type
>       -   Added the ability for the player to run away from encounters
>       -   Moved running away and switching pokemon out of a pokemon's move set, instead putting it as an available option before choosing pokemon moves
>           -   This is similar to the original game where the layer is given 4 options to fight, switch pokemon, run away or use items in their bag
>       -   Implemented random encounters by generating a random pokemon for the player to battle against
>           -   Random pokemon is picked from a pool of selected pokemon to mimic the actual game where certain areas only spwan certain pokemon
>           -   Initially separated pokemon encounters from trainer encounters but later merged both as there were many places where the code was repeated
>               -   It was mainly UI that changed between the two so if statements were just used to replace the splitting
>       -   Included descriptors for each file to make the functions clearer
>       -   Changed the power of a move to be a booster of the pokemon's attack, rather than a multiplier, because there was not enough damage dealt in general
>       -   Implemented items that can be used during and outside encounters
>           -   Some items from the original game were excluded for now but may be included in the future if time permits
>       -   Implemented logic for choosing items to use as anther function under the Trainer class
>       -   Item class
>           -   Contains the item's name, attribute and power
>               -   Attribute is how the item affects battles and power is the intensity value
>               -   E.g. Health potions contribute to Health (attribute), by increasing a pokemon's health by 30 (power)
>       -   Effect class
>           -   Contains the effects's name, attribute and power, similar to the item class
>       -   Implemented logic for items to cancel out effects, but the effects have not been implemented yet
>       -   TODO
>           -   Battles: Reset each trainer's stats and pokemon after the battle to be reused again if encountered again
>               -   Unsure if should do this because trainers are used more as checks to see if the player has attained a certain level of skill and power
>           -   Battles: Checkpoint battles and boss battles
>           -   Effect: Effects on pokemon
>           -   Trainers: Create more trainers so that random trainer encounters are more randomised
>           -   Moves: Include more moves
>           -   UI in general, especially intro UI to the game
>           -   Test code written today (most of it is not tested)
>   -   13/8
>       -   Debugged previously written and untested code
>       -   Made if-else conditions easier to read by putting the condition with less code at the bottom, instead of the bottom
>       -   Integrated random pokemon encounters into trainer encounters
>           -   If there are no trainers to battle against, the random pokemon encounter will happen
>           -   Trainers act like checkpoints in the game to test a player's skill and power level for now, but may change later into development
>       -   Implemented effects of all effects
>           -   Moves wth the same type as the effect will cause the opponent to get the effect
>           -   Every turn, if a pokemon is frozen, sleeping or paralysed, it cannot fight
>               -   A counter in the Pokemon class keeps count of how many turns the pokemon cannot fight
>           -   Every turn, if a pokemon is burned or poisoned, it will take damage
>       -   Damage is switched back from being an addition of power to a multiplier of power because it was too high
>       -   Organised set up functions
>       -   Began including all possible moves as of current code functions
>       -   TODO
>           -   Battles: Reset each trainer's stats and pokemon after the battle to be reused again if encountered again
>               -   Unsure if should do this because trainers are used more as checks to see if the player has attained a certain level of skill and power
>           -   Battles: Checkpoint battles and boss battles
>           -   Effect: Sleep, Paralysis and Freezing on pokemon
>           -   Trainers: Create more trainers so that random trainer encounters are more randomised
>           -   Moves: Include more moves
>           -   UI in general, especially intro UI to the game
>   -   14/8
>       -   Finished inlcuding all possible moves
>       -   Fixed bug of not adding ice moves to ice type pokemon
>       -   Restructured damage() function to implement various move types (Changing stats, Effects, etc.)
>           -   Moved checking of battle end out of Move class to Battle class
>           -   Effects are not stored in every move anymore. Only when a move has an attribute linked to an effect, the effect is stored in the move
>           -   Effects as such do not have types anymore
>           -   Using moves is its own function under the Battle class, so checking attributes of moves is more identifiable, and also because it repeats during the opponent's turn
>       -   Added new function to Pokemon class to change pokemon evasion stat for use during battles
>       -   Fainted pokemons' stats reset to base stats + level boosts after battles because they are considered out of the battle and items used during battle do not apply outside the battle
>       -   Damage formula has been adjusted to the actual calculation used in-game, and is calculated first before any logic
>       -   Made the percentage threshold for random pokemon encounters a variable for easier identification and changing in the future
>       -   Found bug of not being to start random encounters in locations which do not spawn pokemon and fixed with simple conditional
>       -   Organised set ups into table-like structure for way easier editing
>       -   TODO list below is finally ordered by importance
>       -   TODO
>           -   Items: Capturing with pokeball
>           -   Battles: Reset each trainer's stats and pokemon after the battle to be reused again if encountered again
>               -   Unsure if should do this because trainers are used more as checks to see if the player has attained a certain level of skill and power
>           -   Battles: Checkpoint battles and boss battles
>           -   Trainers: Create more trainers so that random trainer encounters are more randomised
>           -   Clean up comments in code
>           -   UI in general, especially intro UI to the game

## Week 8 (16 Aug - 22 Aug)

>   -   16/8
>       -   Brainstorming for possible future implementation
>           -   Each location's spawnable pokemon have a range of levels
>           -   Add the ability to assign a pokemon's level when initialising it
>           -   Redo dealing with invalid inputs for moving to locations, and choosing pokemon, moves and items (Exception Handling)
>           -   The player cannot run away from Trainer encounters
>           -   Trainers will be split into two groups: Checkpoint Trainers and Random Trainers
>               -   Checkpoint Trainers are compulsory to defeat in order to progress on to other locations (The map locks certain locations depending on player's progress)
>               -   Checkpoint Trainers's stats will have to be reset if the player loses the fight
>               -   Random trainers work like random pokemon encounters, and exist for the player to gain more EXP at a time instead of spending long hours grinding
>       -   TODO
>           -   Redo exepcetion handling for invalid inputs for moving locations, and choosing pokemon, move and item
>           -   Pokemon: Ability to assign level when initialising
>           -   Items: Capturing with pokeball
>           -   Battle: Fix range of levels of random encounter pokemon depending on location
>           -   Battles: Checkpoint Trainers and Elite Four
>           -   Battles: Reset Checkpoint Trainer's stats and pokemon if player loses encounter
>           -   Trainers: Create more trainers so that random trainer encounters are more randomised
>           -   Clean up comments in code
>           -   UI in general, especially intro UI to the game
>   -   19/8
>       -   TODO
>           -   Items: Capturing with pokeball
>           -   Battle: Fix range of levels of random encounter pokemon depending on location
>           -   Battles: Checkpoint Trainers and Elite Four
>           -   Battles: Reset Checkpoint Trainer's stats and pokemon if player loses encounter
>           -   Trainers: Create more trainers so that random trainer encounters are more randomised
>           -   Clean up comments in code
>           -   UI in general, especially intro UI to the game
>   -   20/8
>       -   TODO
>           -   Battles: Reset Checkpoint Trainer's stats and pokemon if player loses encounter
>           -   Battles: Fix order of Elite 4 Trainers and include Blue
>           -   Battles: Recalculate EXP gained after winning
>           -   Shop: UI
>           -   Shop: Implement currency
>           -   UI in general, especially intro UI to the game

## Week 9 (23 Aug - 29 Aug)

## Week 10 (30 Aug - 5 Sep)

## Sep Holiday (5 Sep - 10 Sep) **Submission date is 10 Sep**
