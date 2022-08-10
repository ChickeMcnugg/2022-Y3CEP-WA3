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
>       -   TODO
>           -   Battles: Reset each trainer's stats and pokemon after the battle to be reused again if encountered again
>           -   Battles: Checkpoint battles and boss battles
>           -   Trainers: Create more trainers so that random encounters are more randomised
>           -   Moves: Include more moves
>           -   UI in general
>           -   Comment purpose of files

## Week 8 (16 Aug - 22 Aug)

## Week 9 (23 Aug - 29 Aug)

## Week 10 (30 Aug - 5 Sep)

## Sep Holiday (5 Sep - 10 Sep) **Submission date is 10 Sep**
