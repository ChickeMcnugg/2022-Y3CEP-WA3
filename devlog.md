# Development Log
> A successful final project is built slowly over many weeks not thrown together at the last minute. To incentivize good project pacing and to let your project mentor stay informed about the status of your work, each week you should add an entry to your log.md file in the development directory.

> Each entry should describe:

> - What goals you had set for the week and whether they were accomplished or not
> - What problems you encountered (if any) that prevented you from meeting your goals
> - What you plan to accomplish or attempt next week

> The development log will be graded for completion, detail, and honesty – not progress. It is much better to truthfully evaluate the work you completed in a week then lie to make the project sound further along then it really is. It is totally acceptable to have an entry that says you tried nothing and accomplished nothing. However if every week starts to say that, both yourself and your project mentor will be able to identify the issue before it becomes impossible to fix.

## Week 5 (26 Jul - 1 Aug)
-   Started project on recreating Pokemon
-   Implemented classes required (Trainers, Pokemons, Types, Moves, Locations, Items, Battles)

-   Trainer class
    -   Includes Name, Pokemons, Items, Location
    -   Active Pokemon, Fainted Pokemon are kept track of to reference during battles
    -   Traiers can move to different locations following the map set up in main.py (See Location class)
    -   Fully functional for now
-   Pokemon class
    -   Includes Name, Type, Max Health, Attack, Defense, Speed, Evasion, Accuracy
    -   Level and EXP are kept track of to boost an individual Pokemon's stats
    -   Moves are kept track of to reference during battles
    -   Other stats are referenced during battles
    -   Fully functional for now
-   Type class
    -   Includes Name, Type advantage, Type disadvantage, Type immune
    -   Defined two fold since all types need to be defined first, before advantages, disadvantages and immunity can be defined
    -   Fully functional for now
-   Moves class
    -   Includes Name, Type, Power, Accuracy
    -   Only Pokemon of the same type can "learn" the move
    -   Power and Accuracy are referenced during battles
    -   Fully functional for now
-   Locations class
    -   Includes Name
    -   Incorporated into a map system, where neighbouring locations are kept track of
    -   Trainers can move through the locations, with a chance of random encounters with wild Pokemon
    -   Fully functional
-   Item class
    -   Includes Name
    -   Primitive form as not much work was done. It will only be required after implementing battles
-   Battle class
    -   Includes Player and Opponent
    -   Players use their active pokemon and respective moves to battle until one player's pokemons have all fainted
    -   Items can be used to boost pokemon stats
    -   Currently work in progress and not functional whatsoever

-   main.py houses all trainers, pokemon, types, moves, locations available during the game
    -   Mostly contains set up commands and other features of teh game are contaiend within tehir respective files
    -   It is a pain to define all these variables

-   TODO
    -   Trainer: Switch active pokemon
    -   Battles: Logic for battling and ending battles
    -   Moves: Include more moves

## Week 6 (2 Aug - 8 Aug)

## Week 7 (9 Aug - 15 Aug)

## Week 8 (16 Aug - 22 Aug)

## Week 9 (23 Aug - 29 Aug)

## Week 10 (30 Aug - 5 Sep)

## Sep Holiday (5 Sep - 10 Sep) **Submission date is 10 Sep**
