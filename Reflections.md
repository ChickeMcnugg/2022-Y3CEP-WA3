# Final comments
>   -   Overall, most of the essential game components have been done (however bugg it may be)
>   -   Pulling off a 1v1 battle system, map exploration, and inventory system is surprisng to me to say the least

# Improvements
>   -   Things not completed that are in the original game (but game is still playable):
>       -   Trainers' stats are not reset when player leaves during battle
>       -   There is no end game after defeating all of Elite 4
>       -   Player faces Elite 4 in random order
>       -   Some items are impossible to get because they are found when walking around in the actual game (not implemented in this version)
>       -   Items that should not be sold can be sold (No check implemented to prevent this)
>       -   No check implemented beforehand when loading menu options if player even has the money to buy items from a shop
>       -   There is no end game if player loses all their pokemon and is unable to catch more pokemon
>       -   All moves a pokemon can make is displayed
>       -   Player can catch and carry an infinite number of pokemon
>   -   Improvements (besides those pointed out above)
>       -   Refactoring of classes
>           -   Pokemon class -> Type-specific Pokemon classes
>               -   Rather than having a pokemon's type as a parameter, inheritance could have been used
>           -   Trainer class -> Random Encounter Trainers class and Gym Leader class
>               -   This would have allowed for Gym Leaders to have specific abilities during battles (for teh Elite 4, an order could also have been set up)
>       -   Refactoring of code
>           -   Functions that asked for user input and checked whether it was valid could have been its own separate code
>           -   E.g. askInput(options) { return userInput }
>           -   To reduce the repetition of while loops

# Challenges
>   -   Some improvements could have been implemented if I had time (or less academic things to do)
>       -   At some point, I had to stop as it was taking up too much time
>       -   My goal I had set up for myself at the beginning was much bigger than I thought and progress seemed to be going smooth at first
>       -   Towards the end, exams started crowding up time
>       -   I tried to prevent this by getting as much work as possible done early on, but the amount of work was much more than I thought
>   -   I also have other ideas on pushing this project further, which I maybe could have implemented if I went with it early on
>       -   Making the game 3D
>           -   I already have self-created models and a game engine (Unreal)
>           -   But that would have required me to create animations and music, and moving the project into c++, which I felt was not worth it initially
>       -   Making a storyline
>           -   Replicating the actual game would have been good, but that would have involved hard coding a sequece of events and made the whole process much more difficult (compared to the current game which is essentially a while loop)
>       -   Making a spreadsheet with all the information used in main.py
>           -   It would be much better for future reference as well, since the data is detached from the project and could be used elsewhere
>           -   Editing information would also have been much easier