#This is where the whole game is set up, including all the types, moves, pokemons, trainers, locations and map.
#The logic for initiating random encounters and trainer encounters is also below.

from random import randint
from copy import deepcopy
from Battle import *
from Effect import *
from Pokemon import *
from Trainer import *
from Item import *
from Type import *
from Location import *
from Move import *
from Mart import *

def setupTypes():
    global bugType, dragonType, electricType, fightingType, fireType, flyingType, ghostType, grassType, groundType, iceType, normalType, poisonType, psychicType, rockType, waterType

    bugType         = Type("Bug")
    dragonType      = Type("Dragon")
    electricType    = Type("Electric")
    fightingType    = Type("Fighting")
    fireType        = Type("Fire")
    flyingType      = Type("Flying")
    ghostType       = Type("Ghost")
    grassType       = Type("Grass")
    groundType      = Type("Ground")
    iceType         = Type("Ice")
    normalType      = Type("Normal")
    poisonType      = Type("Poison")
    psychicType     = Type("Psychic")
    rockType        = Type("Rock")
    waterType       = Type("Water")

    bugType.setTypeAdvantageList([poisonType, grassType, psychicType])
    bugType.setTypeDisadvantageList([fightingType, flyingType, ghostType, fireType])
    
    dragonType.setTypeAdvantageList([dragonType])
    
    electricType.setTypeAdvantageList([flyingType, waterType])
    electricType.setTypeDisadvantageList([grassType, electricType, dragonType])
    electricType.setTypeImmuneList([groundType])
    
    fightingType.setTypeAdvantageList([normalType, rockType, iceType])
    fightingType.setTypeDisadvantageList([flyingType, poisonType, bugType, psychicType])
    fightingType.setTypeImmuneList([ghostType])

    fireType.setTypeAdvantageList([bugType, grassType, iceType])
    fireType.setTypeDisadvantageList([rockType, fireType, waterType, dragonType])

    flyingType.setTypeAdvantageList([fightingType, bugType, grassType])
    flyingType.setTypeDisadvantageList([rockType, electricType])

    ghostType.setTypeAdvantageList([ghostType])
    ghostType.setTypeImmuneList([normalType, psychicType])

    grassType.setTypeAdvantageList([groundType, rockType, waterType])
    grassType.setTypeDisadvantageList([flyingType, poisonType, bugType, fireType, grassType, dragonType])
    
    groundType.setTypeAdvantageList([poisonType, rockType, fireType, electricType])
    groundType.setTypeDisadvantageList([bugType, grassType])
    groundType.setTypeImmuneList([flyingType])

    iceType.setTypeAdvantageList([flyingType, groundType, grassType, dragonType])
    iceType.setTypeDisadvantageList([waterType, iceType])
    
    normalType.setTypeDisadvantageList([rockType])
    normalType.setTypeImmuneList([ghostType])

    poisonType.setTypeAdvantageList([bugType, grassType])
    poisonType.setTypeDisadvantageList([poisonType, groundType, rockType, rockType])

    psychicType.setTypeAdvantageList([fightingType, groundType, grassType, dragonType])
    psychicType.setTypeDisadvantageList([waterType, iceType])
    
    rockType.setTypeAdvantageList([flyingType, bugType, fireType, iceType])
    rockType.setTypeDisadvantageList([fightingType, groundType])
    
    waterType.setTypeAdvantageList([groundType, rockType, fireType])
    waterType.setTypeDisadvantageList([waterType, grassType, dragonType])

def setupEffects():
    global burn, freeze, paralysis, poison, sleep
    global effects

    burn        = Effect("Burned", "Attack", 0.0625)
    freeze      = Effect("Frozen", "Move", 0)
    paralysis   = Effect("Paralysed", "Move", 0.75)
    poison      = Effect("Poisoned", "Attack", 0.0625)
    sleep       = Effect("Slept", "Move", 3)

    effects = [burn, freeze, paralysis, poison, sleep]

def setupMoves():
    global absorb, dreamEater, leechLife, megaDrain, highJumpKick, jumpKick, acidArmour, barrier, harden, withdraw, tailWhip, screech, meditate, growth, swordsDance
    global doubleTeam, minimise, flash, kinesis, sandAttack, smokescreen, barrage, bonemerang, cometPunch, doubleKick, furyAttack, furySwipes, pinMissile, spikeCannon, blizzard
    global iceBeam, icePunch, bodySlam, glare, lick, stunSpore, thunder, thunderPunch, thunderWave, thunderShock, thunderbolt, ember, fireBlast, firePunch, flamethrower
    global hypnosis, lovelyKiss, sing, sleepPowder, spore, poisonGas, poisonPowder, poisonSting, sludge, smog, toxic, cut, drillPeck, eggBomb, hornAttack
    global hydroPump, megaKick, megaPunch, peck, rockThrow, scratch, slam, strength, tackle, vineWhip, viseGrip, waterGun, wingAttack, dragonRage, sonicBoom
    global explosion, selfDestruct, fissure, hornDrill

    absorb          = Move("Absorb",            grassType,      "Leech",                20,     100)
    dreamEater      = Move("Dream Eater",       psychicType,    "Leech",                100,    100)
    leechLife       = Move("Leech Life",        bugType,        "Leech",                80,     100)
    megaDrain       = Move("Mega Drain",        grassType,      "Leech",                40,     100)
    highJumpKick    = Move("High Jump Kick",    fightingType,   "MissHit",              130,    90)
    jumpKick        = Move("Jump Kick",         fightingType,   "MissHit",              100,    95)
    acidArmour      = Move("Acid Armour",       poisonType,     "Gain Defense",         50,     100)
    barrier         = Move("Barrier",           psychicType,    "Gain Defense",         50,     100)
    harden          = Move("Harden",            normalType,     "Gain Defense",         25,     100)
    withdraw        = Move("Withdraw",          waterType,      "Gain Defense",         25,     100)    
    tailWhip        = Move("Tail Whip",         normalType,     "Lower Defense",        25,     100)
    screech         = Move("Screech",           normalType,     "Lower Defense",        50,     85)
    meditate        = Move("Meditate",          psychicType,    "Gain Attack",          25,     100)
    growth          = Move("Growth",            normalType,     "Gain Attack",          25,     100)
    swordsDance     = Move("Swords Dance",      normalType,     "Gain Attack",          50,     100)
    doubleTeam      = Move("Double Team",       normalType,     "Gain Evasiveness",     25,     100)
    minimise        = Move("Minimise",          normalType,     "Gain Evasiveness",     50,     100)
    flash           = Move("Flash",             normalType,     "Lower Accuracy",       25,     100)
    kinesis         = Move("Kinesis",           psychicType,    "Lower Accuracy",       25,     80)
    sandAttack      = Move("Sand Attack",       groundType,     "Lower Accuracy",       25,     100)
    smokescreen     = Move("Smokescreen",       normalType,     "Lower Accuracy",       25,     100)
    barrage         = Move("Barrage",           normalType,     "Multiple Hits",        15,     90)
    bonemerang      = Move("Bonemerang",        groundType,     "Multiple Hits",        50,     90)
    cometPunch      = Move("Comet Punch",       normalType,     "Multiple Hits",        18,     85)
    doubleKick      = Move("Double Kick",       fightingType,   "Multiple Hits",        30,     100)
    furyAttack      = Move("Fury Attack",       normalType,     "Multiple Hits",        15,     85)
    furySwipes      = Move("Fury Swipes",       normalType,     "Multiple Hits",        18,     80)
    pinMissile      = Move("Pin Missile",       bugType,        "Multiple Hits",        25,     95)
    spikeCannon     = Move("Spike Cannon",      normalType,     "Multiple Hits",        20,     100)
    blizzard        = Move("Blizzard",          iceType,        "Effect",               110,    70,     [freeze])
    iceBeam         = Move("Ice Beam",          iceType,        "Effect",               90,     100,    [freeze])
    icePunch        = Move("Ice Punch",         iceType,        "Effect",               75,     100,    [freeze])
    bodySlam        = Move("Body Slam",         normalType,     "Effect",               85,     100,    [paralysis])
    glare           = Move("Glare",             normalType,     "Effect",               0,      100,    [paralysis])
    lick            = Move("Lick",              ghostType,      "Effect",               30,     100,    [paralysis])
    stunSpore       = Move("Stun Spore",        grassType,      "Effect",               0,      75,     [paralysis])
    thunder         = Move("Thunder",           electricType,   "Effect",               110,    70,     [paralysis])
    thunderPunch    = Move("Thunder Punch",     electricType,   "Effect",               75,     100,    [paralysis])
    thunderShock    = Move("Thunder Shock",     electricType,   "Effect",               40,     100,    [paralysis])
    thunderWave     = Move("Thunder Wave",      electricType,   "Effect",               0,      90,     [paralysis])
    thunderbolt     = Move("Thunderbolt",       electricType,   "Effect",               90,     100,    [paralysis])
    ember           = Move("Ember",             fireType,       "Effect",               40,     100,    [burn])
    fireBlast       = Move("Fire Blast",        fireType,       "Effect",               110,    85,     [burn])
    firePunch       = Move("Fire Punch",        fireType,       "Effect",               75,     100,    [burn])
    flamethrower    = Move("Flamethrower",      fireType,       "Effect",               90,     100,    [burn])
    hypnosis        = Move("Hypnosis",          psychicType,    "Effect",               0,      60,     [sleep])
    lovelyKiss      = Move("Lovely Kiss",       normalType,     "Effect",               0,      75,     [sleep])
    sing            = Move("Sing",              normalType,     "Effect",               0,      55,     [sleep])
    sleepPowder     = Move("Sleep Powder",      grassType,      "Effect",               0,      75,     [sleep])
    spore           = Move("Spore",             grassType,      "Effect",               0,      100,    [sleep])
    poisonGas       = Move("Poison Gas",        poisonType,     "Effect",               0,      90,     [poison])
    poisonPowder    = Move("Poison Powder",     poisonType,     "Effect",               0,      75,     [poison])
    poisonSting     = Move("Poison Sting",      poisonType,     "Effect",               15,     100,    [poison])
    sludge          = Move("Sludge",            poisonType,     "Effect",               65,     100,    [poison])
    smog            = Move("Smog",              poisonType,     "Effect",               30,     70,     [poison])
    toxic           = Move("Toxic",             poisonType,     "Effect",               0,      90,     [poison])
    cut             = Move("Cut",               normalType,     "Attack",               50,     95)	
    drillPeck       = Move("Drill Peck",        flyingType,     "Attack",               80,     100)	
    eggBomb         = Move("Egg Bomb",          normalType,     "Attack",               100,    75)
    hornAttack      = Move("Horn Attack",       normalType,     "Attack",               65,     100)
    hydroPump       = Move("Hydro Pump",        waterType,      "Attack",               110,    80)
    megaKick        = Move("Mega Kick",         normalType,     "Attack",               120,    75)
    megaPunch       = Move("Mega Punch",        normalType,     "Attack",               80,     85)
    peck            = Move("Peck",              flyingType,     "Attack",               35,     100)
    rockThrow       = Move("Rock Throw",        rockType,       "Attack",               50,     90)
    scratch         = Move("Scratch",           normalType,     "Attack",               40,     100)	
    slam            = Move("Slam",              normalType,     "Attack",               80,     75)	
    strength        = Move("Strength",          normalType,     "Attack",               80,     100)	
    tackle          = Move("Tackle",            normalType,     "Attack",               40,     100)	
    vineWhip        = Move("Vine Whip",         grassType,      "Attack",               45,     100)	
    viseGrip        = Move("Vise Grip",         normalType,     "Attack",               55,     100)	
    waterGun        = Move("Water Gun",         waterType,      "Attack",               40,     100)	
    wingAttack      = Move("Wing Attack",       flyingType,     "Attack",               60,     100)
    dragonRage      = Move("Dragon Rage",       dragonType,     "Constant Attack",      40,     100)
    sonicBoom       = Move("Sonic Boom",        normalType,     "Constant Attack",      20,     90)
    explosion       = Move("Explosion",         normalType,     "Faint",                250,    100)
    selfDestruct    = Move("Self-Destruct",     normalType,     "Faint",                200,    100)
    fissure         = Move("Fissure",           groundType,     "KO",                   0,      30)
    hornDrill       = Move("Horn Drill",        normalType,     "KO",                   0,      30)    
    
    moves = [absorb, dreamEater, leechLife, megaDrain, highJumpKick, jumpKick, acidArmour, barrier, harden, withdraw, tailWhip, screech, meditate, growth, swordsDance, doubleTeam, minimise, flash, kinesis, sandAttack, smokescreen, barrage, bonemerang, cometPunch, doubleKick, furyAttack, furySwipes, pinMissile, spikeCannon, blizzard, iceBeam, icePunch, bodySlam, glare, lick, stunSpore, thunder, thunderPunch, thunderWave, thunderShock, thunderbolt, ember, fireBlast, firePunch, flamethrower, hypnosis, lovelyKiss, sing, sleepPowder, spore, poisonGas, poisonPowder, poisonSting, sludge, smog, toxic, cut, drillPeck, eggBomb, hornAttack, hydroPump, megaKick, megaPunch, peck, rockThrow, scratch, slam, strength, tackle, vineWhip, viseGrip, waterGun, wingAttack, dragonRage, sonicBoom, explosion, selfDestruct, fissure, hornDrill]

    global bugMoves, dragonMoves, electricMoves, fightingMoves, fireMoves, flyingMoves, ghostMoves, grassMoves, groundMoves, iceMoves, normalMoves, poisonMoves, psychicMoves, rockMoves, waterMoves
    
    bugMoves        = []
    dragonMoves     = []
    electricMoves   = []
    fightingMoves   = []
    fireMoves       = []
    flyingMoves     = []
    ghostMoves      = []
    grassMoves      = []
    groundMoves     = []
    iceMoves        = []
    normalMoves     = []
    poisonMoves     = []
    psychicMoves    = []
    rockMoves       = []
    waterMoves      = []

    moveCategories = [bugMoves, dragonMoves, electricMoves, fightingMoves, fireMoves, flyingMoves, ghostMoves, grassMoves, groundMoves, iceMoves, normalMoves, poisonMoves, psychicMoves, rockMoves, waterMoves]

    for move in moves:
        if move.getMoveType() == bugType:
            bugMoves.append(move)
        elif move.getMoveType() == dragonType:
            dragonMoves.append(move)
        elif move.getMoveType() == electricType:
            electricMoves.append(move)
        elif move.getMoveType() == fightingType:
            fightingMoves.append(move)
        elif move.getMoveType() == fireType:
            fireMoves.append(move)
        elif move.getMoveType() == flyingType:
            flyingMoves.append(move)
        elif move.getMoveType() == ghostType:
            ghostMoves.append(move)
        elif move.getMoveType() == grassType:
            grassMoves.append(move)
        elif move.getMoveType() == groundType:
            groundMoves.append(move)
        elif move.getMoveType() == iceType:
            iceMoves.append(move)
        elif move.getMoveType() == poisonType:
            poisonMoves.append(move)
        elif move.getMoveType() == psychicType:
            psychicMoves.append(move)
        elif move.getMoveType() == rockType:
            rockMoves.append(move)
        elif move.getMoveType() == waterType:
            waterMoves.append(move)
        else:
            for category in moveCategories:
                category.append(move)

def setupPokemon():
    global bulbasaur, ivysaur, venusaur, charmander, charmeleon, charizard, squirtle, wartortle, blastoise, caterpie, metapod, butterfree, weedle, kakuna, beedrill
    global pidgey, pidgeotto, pidgeot, rattata, raticate, spearow, fearow, ekans, arbok, pikachu, raichu, sandshrew, sandslash, nidoranFemale, nidorina
    global nidoqueen, nidoranMale, nidorino, nidoking, clefairy, clefable, vulpix, ninetales, jigglypuff, wigglytuff, zubat, golbat, oddish, gloom, vileplume
    global paras, parasect, venonat, venomoth, diglett, dugtrio, meowth, persian, psyduck, golduck, mankey, primeape, growlithe, arcanine, poliwag
    global poliwhirl, poliwrath, abra, kadabra, alakazam, machop, machoke, machamp, bellsprout, weepinbell, victreebel, tentacool, tentacruel, geodude, graveler
    global golem, ponyta, rapidash, slowpoke, slowbro, magnemite, magneton, farfetchd, doduo, dodrio, seel, dewgong, grimer, muk, shellder
    global cloyster, gastly, haunter, gengar, onix, drowzee, hypno, krabby, kingler, voltorb, electrode, exeggcute, exeggutor, cubone, marowak
    global hitmonlee, hitmonchan, lickitung, koffing, weezing, rhyhorn, rhydon, chansey, tangela, kangaskhan, horsea, seadra, goldeen, seaking, staryu
    global starmie, mrmime, scyther, jynx, electabuzz, magmar, pinsir, tauros, magikarp, gyrados, lapras, ditto, eevee, vaporean, jolteon
    global flareon, porygon, omanyte, omastar, kabuto, kabutops, aerodactyl, snorlax, articuno, zapdos, moltres, dratini, dragonair, dragonite, mewtwo
    global mew

    bulbasaur       = Pokemon("Bulbasaur",          grassType,      45,     49,     49,     45,     64)
    ivysaur         = Pokemon("Ivysaur",            grassType,      60,     62,     63,     45,     142)
    venusaur        = Pokemon("Venusaur",           grassType,      80,     82,     83,     45,     263)
    charmander      = Pokemon("Charmander",         fireType,       39,     52,     43,     45,     62)
    charmeleon      = Pokemon("Charmeleon",         fireType,       58,     64,     58,     45,     142)
    charizard       = Pokemon("Charizard",          fireType,       78,     84,     78,     45,     267)
    squirtle        = Pokemon("Squirtle",           waterType,      44,     48,     65,     45,     63)
    wartortle       = Pokemon("Wartortle",          waterType,      59,     63,     80,     45,     142)
    blastoise       = Pokemon("Blastoise",          waterType,      79,     83,     100,    45,     265)
    caterpie        = Pokemon("Caterpie",           bugType,        45,     30,     35,     255,    39)
    metapod         = Pokemon("Metapod",            bugType,        50,     20,     55,     120,    72)
    butterfree      = Pokemon("Butterfree",         bugType,        60,     45,     50,     45,     198)
    weedle          = Pokemon("Weedle",             bugType,        40,     35,     30,     255,    39)
    kakuna          = Pokemon("Kakuna",             bugType,        65,     25,     50,     120,    72)
    beedrill        = Pokemon("Beedrill",           bugType,        65,     80,     40,     45,     198)
    pidgey          = Pokemon("Pidgey",             normalType,     40,     45,     40,     255,    50)
    pidgeotto       = Pokemon("Pidgeotto",          normalType,     63,     60,     55,     120,    122)
    pidgeot         = Pokemon("Pidgeot",            normalType,     83,     80,     75,     45,     290)
    rattata         = Pokemon("Rattata",            normalType,     30,     56,     35,     255,    51)
    raticate        = Pokemon("Raticate",           normalType,     55,     81,     60,     127,    145)
    spearow         = Pokemon("Spearow",            normalType,     40,     60,     30,     255,    52)
    fearow          = Pokemon("Fearow",             normalType,     65,     90,     65,     90,     155)
    ekans           = Pokemon("Ekans",              poisonType,     35,     60,     44,     255,    58)
    arbok           = Pokemon("Arbok",              poisonType,     60,     85,     69,     90,     157)
    pikachu         = Pokemon("Pikachu",            electricType,   35,     55,     30,     190,    112)
    raichu          = Pokemon("Raichu",             electricType,   60,     90,     55,     75,     243)
    sandshrew       = Pokemon("Sandshrew",          groundType,     50,     75,     85,     255,    60)
    sandslash       = Pokemon("Sandslash",          groundType,     75,     100,    110,    90,     158)
    nidoranFemale   = Pokemon("Nidoran Female",     poisonType,     55,     47,     52,     235,    55)
    nidorina        = Pokemon("Nidorina",           poisonType,     70,     62,     67,     120,    128)
    nidoqueen       = Pokemon("Nidoqueen",          poisonType,     90,     82,     87,     45,     253)
    nidoranMale     = Pokemon("Nidoran Male",       poisonType,     46,     57,     40,     235,    55)
    nidorino        = Pokemon("Nidorino",           poisonType,     61,     72,     57,     120,    128)
    nidoking        = Pokemon("Nidoking",           poisonType,     81,     92,     77,     45,     253)
    clefairy        = Pokemon("Clefairy",           normalType,     70,     45,     48,     150,    113)
    clefable        = Pokemon("Clefable",           normalType,     95,     70,     73,     25,     242)
    vulpix          = Pokemon("Vulpix",             fireType,       38,     41,     40,     190,    60)
    ninetales       = Pokemon("Ninetales",          fireType,       73,     76,     75,     75,     177)
    jigglypuff      = Pokemon("Jigglypuff",         normalType,     115,    45,     20,     170,    95)
    wigglytuff      = Pokemon("Wigglytuff",         normalType,     140,    70,     45,     50,     218)
    zubat           = Pokemon("Zubat",              poisonType,     40,     45,     35,     255,    49)
    golbat          = Pokemon("Golbat",             poisonType,     75,     80,     70,     90,     159)
    oddish          = Pokemon("Oddish",             grassType,      45,     50,     55,     255,    64)
    gloom           = Pokemon("Gloom",              grassType,      60,     65,     70,     120,    138)
    vileplume       = Pokemon("Vileplume",          grassType,      75,     80,     85,     45,     245)
    paras           = Pokemon("Paras",              bugType,        35,     70,     55,     190,    57)
    parasect        = Pokemon("Parasect",           bugType,        60,     55,     50,     75,     142)
    venonat         = Pokemon("Venonat",            bugType,        70,     65,     60,     190,    61)
    venomoth        = Pokemon("Venomoth",           bugType,        10,     55,     25,     75,     158)
    diglett         = Pokemon("Diglett",            groundType,     35,     80,     50,     255,    53)
    dugtrio         = Pokemon("Dugtrio",            groundType,     40,     45,     35,     50,     149)
    meowth          = Pokemon("Meowth",             normalType,     65,     70,     60,     255,    58)
    persian         = Pokemon("Persian",            normalType,     50,     52,     48,     90,     154)
    psyduck         = Pokemon("Psyduck",            waterType,      80,     82,     78,     190,    64)
    golduck         = Pokemon("Golduck",            waterType,      40,     80,     35,     75,     175)
    mankey          = Pokemon("Mankey",             fightingType,   65,     105,    60,     190,    61)
    primeape        = Pokemon("Primape",            fightingType,   55,     70,     45,     75,     159)
    growlithe       = Pokemon("Growlithe",          fireType,       90,     110,    80,     190,    70)
    arcanine        = Pokemon("Arcanine",           fireType,       40,     50,     40,     75,     194)
    poliwag         = Pokemon("Poliwag",            waterType,      65,     65,     65,     255,    60)
    poliwhirl       = Pokemon("Poliwhirl",          waterType,      90,     85,     95,     120,    135)
    poliwrath       = Pokemon("Poliwrath",          waterType,      25,     20,     15,     45,     255)
    abra            = Pokemon("Abra",               psychicType,    40,     35,     30,     200,    62)
    kadabra         = Pokemon("Kadabra",            psychicType,    55,     50,     45,     100,    140)
    alakazam        = Pokemon("Alakazam",           psychicType,    70,     80,     50,     50,     250)
    machop          = Pokemon("Machop",             fightingType,   80,     100,    70,     180,    61)
    machoke         = Pokemon("Machoke",            fightingType,   90,     130,    80,     90,     142)
    machamp         = Pokemon("Machamp",            fightingType,   50,     75,     35,     45,     253)
    bellsprout      = Pokemon("Bellsprout",         grassType,      65,     90,     50,     255,    60)
    weepinbell      = Pokemon("Weepinbell",         grassType,      80,     105,    65,     120,    137)
    victreebel      = Pokemon("Victreebel",         grassType,      40,     40,     35,     45,     245)
    tentacool       = Pokemon("Tentacool",          waterType,      80,     105,    65,     190,    67)
    tentacruel      = Pokemon("Tentacruel",         waterType,      40,     80,     100,    60,     180)
    geodude         = Pokemon("Geodude",            rockType,       55,     95,     115,    255,    60)
    graveler        = Pokemon("Graveler",           rockType,       80,     110,    130,    120,    137)
    golem           = Pokemon("Golem",              rockType,       50,     85,     55,     45,     248)
    ponyta          = Pokemon("Ponyta",             fireType,       65,     100,    70,     190,    82)
    rapidash        = Pokemon("Rapidash",           fireType,       90,     65,     65,     60,     175)
    slowpoke        = Pokemon("Slowpoke",           waterType,      95,     49,     49,     190,    63)
    slowbro         = Pokemon("Slowbro",            waterType,      25,     35,     70,     70,     172)
    magnemite       = Pokemon("Magnemite",          electricType,   50,     60,     95,     190,    65)
    magneton        = Pokemon("Magneton",           electricType,   52,     65,     55,     60,     163)
    farfetchd       = Pokemon("Farfetch'd",         normalType,     35,     85,     45,     45,     132)
    doduo           = Pokemon("Duduo",              normalType,     60,     110,    70,     190,    62)
    dodrio          = Pokemon("Dudrio",             normalType,     65,     45,     55,     45,     165)
    seel            = Pokemon("Seel",               waterType,      90,     70,     80,     190,    65)
    dewgong         = Pokemon("Dewgong",            waterType,      80,     80,     50,     75,     166)
    grimer          = Pokemon("Grimer",             poisonType,     105,    105,    75,     190,    65)
    muk             = Pokemon("Muk",                poisonType,     30,     65,     100,    75,     175)
    shellder        = Pokemon("Shellder",           waterType,      50,     95,     180,    190,    61)
    cloyster        = Pokemon("Cloyster",           waterType,      30,     35,     30,     60,     184)
    gastly          = Pokemon("Gastly",             ghostType,      30,     35,     30,     190,    62)
    haunter         = Pokemon("Haunter",            ghostType,      45,     50,     45,     90,     142)
    gengar          = Pokemon("Gengar",             ghostType,      60,     65,     60,     45,     250)
    onix            = Pokemon("Onix",               rockType,       35,     45,     160,    45,     77)
    drowzee         = Pokemon("Drowzee",            psychicType,    60,     48,     45,     190,    66)
    hypno           = Pokemon("Hypno",              psychicType,    85,     73,     70,     75,     169)
    krabby          = Pokemon("Krabby",             waterType,      30,     105,    90,     225,    65)
    kingler         = Pokemon("Kingler",            waterType,      55,     130,    115,    60,     166)
    voltorb         = Pokemon("Voltorb",            electricType,   40,     30,     50,     190,    66)
    electrode       = Pokemon("Electrode",          electricType,   60,     50,     70,     60,     172)
    exeggcute       = Pokemon("Exeggcute",          grassType,      60,     40,     80,     90,     65)
    exeggutor       = Pokemon("Exeggutor",          grassType,      95,     95,     85,     45,     186)
    cubone          = Pokemon("Cubone",             groundType,     50,     50,     95,     190,    64)
    marowak         = Pokemon("Marowak",            groundType,     60,     80,     110,    75,     149)
    hitmonlee       = Pokemon("Hitmonlee",          fightingType,   50,     120,    53,     45,     159)
    hitmonchan      = Pokemon("Hitmonchan",         fightingType,   50,     105,    79,     45,     159)
    lickitung       = Pokemon("Lickitung",          normalType,     90,     55,     75,     45,     77)
    koffing         = Pokemon("Koffing",            poisonType,     40,     65,     95,     190,    68)
    weezing         = Pokemon("Weezing",            poisonType,     65,     90,     120,    60,     172)
    rhyhorn         = Pokemon("Rhyhorn",            groundType,     80,     85,     95,     120,    69)
    rhydon          = Pokemon("Rhydon",             groundType,     105,    130,    120,    60,     170)
    chansey         = Pokemon("Chansey",            normalType,     250,    5,      5,      30,     395)
    tangela         = Pokemon("Tangela",            grassType,      65,     55,     115,    45,     87)
    kangaskhan      = Pokemon("Kangaskhan",         groundType,     105,    95,     80,     45,     172)
    horsea          = Pokemon("Horsea",             waterType,      30,     40,     70,     225,    59)
    seadra          = Pokemon("Seadra",             waterType,      55,     65,     95,     60,     154)
    goldeen         = Pokemon("Goldeen",            waterType,      45,     67,     60,     225,    64)
    seaking         = Pokemon("Seaking",            waterType,      80,     92,     65,     60,     158)
    staryu          = Pokemon("Staryu",             waterType,      30,     45,     55,     225,    68)
    starmie         = Pokemon("Starmie",            waterType,      60,     75,     85,     60,     182)
    mrmime          = Pokemon("Mr Mime",            psychicType,    40,     45,     65,     45,     161)
    scyther         = Pokemon("Scyther",            bugType,        70,     110,    80,     45,     100)
    jynx            = Pokemon("Jynx",               iceType,        65,     50,     35,     45,     159)
    electabuzz      = Pokemon("Electabuzz",         electricType,   65,     50,     35,     45,     172)
    magmar          = Pokemon("Magmar",             fireType,       65,     83,     57,     45,     173)
    pinsir          = Pokemon("Pinsir",             bugType,        65,     95,     57,     45,     175)
    tauros          = Pokemon("Tauros",             normalType,     75,     100,    95,     45,     172)
    magikarp        = Pokemon("Magikarp",           waterType,      20,     10,     55,     255,    40)
    gyrados         = Pokemon("Gyrados",            waterType,      95,     125,    79,     45,     189)
    lapras          = Pokemon("Lapras",             waterType,      130,    85,     80,     45,     187)
    ditto           = Pokemon("Ditto",              normalType,     48,     48,     48,     35,     101)
    eevee           = Pokemon("Eevee",              normalType,     55,     55,     50,     45,     65)
    vaporean        = Pokemon("Vaporean",           waterType,      130,    65,     60,     45,     184)
    jolteon         = Pokemon("Jolteon",            electricType,   65,     65,     65,     45,     184)
    flareon         = Pokemon("Flareon",            fireType,       65,     130,    65,     45,     184)
    porygon         = Pokemon("Porygon",            normalType,     65,     60,     70,     45,     79)
    omanyte         = Pokemon("Omanyte",            rockType,       35,     40,     100,    45,     71)
    omastar         = Pokemon("Omastar",            rockType,       70,     60,     125,    45,     173)
    kabuto          = Pokemon("Kabuto",             rockType,       30,     80,     90,     45,     71)
    kabutops        = Pokemon("Kabutops",           rockType,       60,     115,    105,    45,     173)
    aerodactyl      = Pokemon("Aerodactyl",         rockType,       80,     105,    65,     45,     180)
    snorlax         = Pokemon("Snorlax",            normalType,     160,    110,    65,     25,     189)
    articuno        = Pokemon("Articuno",           iceType,        90,     85,     100,    3,      290)
    zapdos          = Pokemon("Zapdos",             electricType,   90,     90,     85,     3,      290)
    moltres         = Pokemon("Moltres",            fireType,       90,     100,    90,     3,      290)
    dratini         = Pokemon("Dratini",            dragonType,     41,     64,     45,     45,     60)
    dragonair       = Pokemon("Dragonair",          dragonType,     61,     84,     65,     45,     147)
    dragonite       = Pokemon("Dragonite",          dragonType,     91,     134,    95,     45,     300)
    mewtwo          = Pokemon("Mewtwo",             psychicType,    106,    110,    90,     3,      340)
    mew             = Pokemon("Mew",                psychicType,    100,    100,    100,    45,     300)

    pokemons = [bulbasaur, ivysaur, venusaur, charmander, charmeleon, charizard, squirtle, wartortle, blastoise, caterpie, metapod, butterfree, weedle, kakuna, beedrill, pidgey, pidgeotto, pidgeot, rattata, raticate, spearow, fearow, ekans, arbok, pikachu, raichu, sandshrew, sandslash, nidoranFemale, nidorina, nidoqueen, nidoranMale, nidorino, nidoking, clefairy, clefable, vulpix, ninetales, jigglypuff, wigglytuff, zubat, golbat, oddish, gloom, vileplume, paras, parasect, venonat, venomoth, diglett, dugtrio, meowth, persian, psyduck, golduck, mankey, primeape, growlithe, arcanine, poliwag, poliwhirl, poliwrath, abra, kadabra, alakazam, machop, machoke, machamp, bellsprout, weepinbell, victreebel, tentacool, tentacruel, geodude, graveler, golem, ponyta, rapidash, slowpoke, slowbro, magnemite, magneton, farfetchd, doduo, dodrio, seel, dewgong, grimer, muk, shellder, cloyster, gastly, haunter, gengar, onix, drowzee, hypno, krabby, kingler, voltorb, electrode, exeggcute, exeggutor, cubone, marowak, hitmonlee, hitmonchan, lickitung, koffing, weezing, rhyhorn, rhydon, chansey, tangela, kangaskhan, horsea, seadra, goldeen, seaking, staryu, starmie, mrmime, scyther, jynx, electabuzz, magmar, pinsir, tauros, magikarp, gyrados, lapras, ditto, eevee, vaporean, jolteon, flareon, porygon, omanyte, omastar, kabuto, kabutops, aerodactyl, snorlax, articuno, zapdos, moltres, dratini, dragonair, dragonite, mewtwo, mew]

    for pokemon in pokemons:
        if pokemon.getPokemonType() == bugType:
            for move in bugMoves:
                pokemon.addPokemonMoves(move)
        elif pokemon.getPokemonType() == dragonType:
            for move in dragonMoves:
                pokemon.addPokemonMoves(move)
        elif pokemon.getPokemonType() == electricType:
            for move in electricMoves:
                pokemon.addPokemonMoves(move)
        elif pokemon.getPokemonType() == fightingType:
            for move in fightingMoves:
                pokemon.addPokemonMoves(move)
        elif pokemon.getPokemonType() == fireType:
            for move in fireMoves:
                pokemon.addPokemonMoves(move)
        elif pokemon.getPokemonType() == flyingType:
            for move in flyingMoves:
                pokemon.addPokemonMoves(move)
        elif pokemon.getPokemonType() == ghostType:
            for move in ghostMoves:
                pokemon.addPokemonMoves(move)
        elif pokemon.getPokemonType() == grassType:
            for move in grassMoves:
                pokemon.addPokemonMoves(move)
        elif pokemon.getPokemonType() == groundType:
            for move in groundMoves:
                pokemon.addPokemonMoves(move)
        elif pokemon.getPokemonType() == normalType:
            for move in normalMoves:
                pokemon.addPokemonMoves(move)
        elif pokemon.getPokemonType() == poisonType:
            for move in poisonMoves:
                pokemon.addPokemonMoves(move)
        elif pokemon.getPokemonType() == psychicType:
            for move in psychicMoves:
                pokemon.addPokemonMoves(move)
        elif pokemon.getPokemonType() == rockType:
            for move in rockMoves:
                pokemon.addPokemonMoves(move)
        else:
            for move in waterMoves:
                pokemon.addPokemonMoves(move)

def setupItems():
    global masterBall, ultraBall, greatBall, pokeBall, antidote, burnHeal, iceHeal, awakening, paralyseHeal, fullHeal, revive, maxRevive, fullRestore, maxPotion, hyperPotion, superPotion, potion
    global freshWater, sodaPop, lemonade, boulderBadge, cascadeBadge, thunderBadge, rainbowBadge, soulBadge, marshBadge, volcanoBadge, earthBadge, oldAmber, domeFossil, helixFossil
    global moonStone, fireStone, thunderStone, waterStone, leafStone, expAll, rareCandy, xAccuracy, xAttack, xDefend

    masterBall      = Item("Master Ball",       0,      0,      "Ball",         0)
    ultraBall       = Item("Ultra Ball",        1200,   600,    "Ball",         150)
    greatBall       = Item("Great Ball",        600,    300,    "Ball",         200)
    pokeBall        = Item("Poke Ball",         200,    100,    "Ball",         255)
    antidote        = Item("Antidote",          100,    50,     "Medicine",     [poison])
    burnHeal        = Item("Burn Heal",         250,    125,    "Medicine",     [burn])
    iceHeal         = Item("Ice Heal",          250,    125,    "Medicine",     [freeze])
    awakening       = Item("Awakening",         200,    100,    "Medicine",     [sleep])
    paralyseHeal    = Item("Parlyse Heal",      200,    100,    "Medicine",     [paralysis])
    fullHeal        = Item("Full Heal",         600,    300,    "Medicine",     [poison, burn, freeze, sleep, paralysis])
    revive          = Item("Revive",            1500,   750,    "Revive",       0.5)
    maxRevive       = Item("Max Revive",        0,      2000,   "Revive",       1)
    fullRestore     = Item("Full Restore",      3000,   1500,   "Health",       0)
    maxPotion       = Item("Max Potion",        2500,   1250,   "Health",       0)
    hyperPotion     = Item("Hyper Potion",      1200,   600,    "Health",       200)
    superPotion     = Item("Super Potion",      700,    350,    "Health",       50)
    potion          = Item("Potion",            300,    150,    "Health",       20)
    freshWater      = Item("Fresh Water",       200,    100,    "Health",       30)
    sodaPop         = Item("Soda Pop",          300,    150,    "Health",       60)
    lemonade        = Item("Lemonade",          350,    175,    "Health",       80)
    boulderBadge    = Item("Boulder Badge",     0,      0,      "Badge",        0)
    cascadeBadge    = Item("Cascade Badge",     0,      0,      "Badge",        0)
    thunderBadge    = Item("Thunder Badge",     0,      0,      "Badge",        0)
    rainbowBadge    = Item("Rainbow Badge",     0,      0,      "Badge",        0)
    soulBadge       = Item("Soul Badge",        0,      0,      "Badge",        0)
    marshBadge      = Item("Marsh Badge",       0,      0,      "Badge",        0)
    volcanoBadge    = Item("Volcano Badge",     0,      0,      "Badge",        0)
    earthBadge      = Item("Earth Badge",       0,      0,      "Badge",        0)
    oldAmber        = Item("Old Amber",         0,      0,      "Fossil",       0)
    domeFossil      = Item("Dome Fossil",       0,      0,      "Fossil",       0)
    helixFossil     = Item("Helix Fossil",      0,      0,      "Fossil",       0)
    moonStone       = Item("Moon Stone",        0,      0,      "Stone",        0)
    fireStone       = Item("Fire Stone",        2100,   1050,   "Stone",        0)
    thunderStone    = Item("Thunder Stone",     2100,   1050,   "Stone",        0)
    waterStone      = Item("Water Stone",       2100,   1050,   "Stone",        0)
    leafStone       = Item("Leaf Stone",        2100,   1050,   "Stone",        0)
    expAll          = Item("EXP All",           0,      0,      "EXP",          0)
    rareCandy       = Item("Rare Candy",        0,      2400,   "Level",        1)
    xAccuracy       = Item("X Accuracy",        950,    475,    "Accuracy",     20)
    xAttack         = Item("X Attack",          500,    250,    "Attack",       20)
    xDefend         = Item("X Defend",          550,    275,    "Defense",      20)

def setupMap():
    global palletTown, viridianCity, pewterCity, ceruleanCity, saffronCity, vermilionCity, celadonCity, lavendarCity, fuchsiaCity, cinnibarIsland
    global victoryRoad, viridianForest, mountMoon, rockTunnel, powerPlant, radioTower, silphCo, seafoamIslands, tohjoFalls
    global indigoPlateau, mountSilver, diglettCave, billHouse
    global route1, route2, route3, route4, route5, route6, route7, route8, route9, route10, route11, route12, route13, route14, route15, route16, route17, route18, route19, route20, route21, route22, route23, route24, route25, route26, route27, route28

    palletTown      = Location("Pallet Town")
    viridianCity    = Location("Viridian City")
    pewterCity      = Location("Pewter City")
    ceruleanCity    = Location("Cerulean City")
    saffronCity     = Location("Saffron City")
    vermilionCity   = Location("Vermilion City")
    celadonCity     = Location("Celandon City")
    lavendarCity    = Location("Lavendar City")
    fuchsiaCity     = Location("Fuschia City")
    cinnibarIsland  = Location("Cinnibar Island")
    victoryRoad     = Location("Victory Road")
    viridianForest  = Location("Viridian Forest")
    mountMoon       = Location("Mount Moon")
    rockTunnel      = Location("Rock Tunnel")
    powerPlant      = Location("Power Plant")
    radioTower      = Location("RadioTower")
    silphCo         = Location("Silph Co.")
    seafoamIslands  = Location("Seafoam Islands")
    tohjoFalls      = Location("Tohjo Falls")
    indigoPlateau   = Location("Indigo Plateau")
    mountSilver     = Location("Mount Silver")
    diglettCave     = Location("Diglett's Cave")
    billHouse       = Location("Bill's House")
    route1          = Location("Route 1")
    route2          = Location("Route 2")
    route3          = Location("Route 3")
    route4          = Location("Route 4")
    route5          = Location("Route 5")
    route6          = Location("Route 6")
    route7          = Location("Route 7")
    route8          = Location("Route 8")
    route9          = Location("Route 9")
    route10         = Location("Route 10")
    route11         = Location("Route 11")
    route12         = Location("Route 12")
    route13         = Location("Route 13")
    route14         = Location("Route 14")
    route15         = Location("Route 15")
    route16         = Location("Route 16")
    route17         = Location("Route 17")
    route18         = Location("Route 18")
    route19         = Location("Route 19")
    route20         = Location("Route 20")
    route21         = Location("Route 21")
    route22         = Location("Route 22")
    route23         = Location("Route 23")
    route24         = Location("Route 24")
    route25         = Location("Route 25")
    route26         = Location("Route 26")
    route27         = Location("Route 27")
    route28         = Location("Route 28")

    palletTown.setTwoWayLocationNeighbour(route1, "North")
    palletTown.setTwoWayLocationNeighbour(route21, "South")
    route1.setTwoWayLocationNeighbour(viridianCity, "North")
    viridianCity.setTwoWayLocationNeighbour(viridianForest, "North")
    viridianCity.setTwoWayLocationNeighbour(route22, "West")
    viridianForest.setTwoWayLocationNeighbour(route2, "North")
    route2.setTwoWayLocationNeighbour(diglettCave, "East")
    route2.setTwoWayLocationNeighbour(pewterCity, "North")
    pewterCity.setTwoWayLocationNeighbour(route3, "East")
    route3.setTwoWayLocationNeighbour(mountMoon, "East")
    mountMoon.setTwoWayLocationNeighbour(route4, "East")
    route4.setTwoWayLocationNeighbour(ceruleanCity, "East")
    ceruleanCity.setTwoWayLocationNeighbour(route24, "North")
    route24.setTwoWayLocationNeighbour(route25, "East")
    route25.setTwoWayLocationNeighbour(billHouse, "East")
    ceruleanCity.setTwoWayLocationNeighbour(route9, "East")
    route9.setTwoWayLocationNeighbour(rockTunnel, "East")
    rockTunnel.setTwoWayLocationNeighbour(route10, "South")
    route10.setTwoWayLocationNeighbour(powerPlant, "South")
    powerPlant.setTwoWayLocationNeighbour(radioTower, "South")
    radioTower.setTwoWayLocationNeighbour(lavendarCity, "South")
    lavendarCity.setTwoWayLocationNeighbour(route8, "West")
    route8.setTwoWayLocationNeighbour(saffronCity, "West")
    saffronCity.setTwoWayLocationNeighbour(silphCo, "North")
    silphCo.setTwoWayLocationNeighbour(route5, "North")
    route5.setTwoWayLocationNeighbour(ceruleanCity, "North")
    saffronCity.setTwoWayLocationNeighbour(route7, "West")
    route7.setTwoWayLocationNeighbour(celadonCity, "West")
    celadonCity.setTwoWayLocationNeighbour(route16, "West")
    route16.setTwoWayLocationNeighbour(route17, "South")
    route17.setTwoWayLocationNeighbour(route18, "South")
    route18.setTwoWayLocationNeighbour(fuchsiaCity, "East")
    fuchsiaCity.setTwoWayLocationNeighbour(route19, "South")
    route19.setTwoWayLocationNeighbour(route20, "South")
    route20.setTwoWayLocationNeighbour(seafoamIslands, "West")
    seafoamIslands.setTwoWayLocationNeighbour(cinnibarIsland, "West")
    cinnibarIsland.setTwoWayLocationNeighbour(route21, "North")
    saffronCity.setTwoWayLocationNeighbour(route6, "South")
    route6.setTwoWayLocationNeighbour(vermilionCity, "South")
    vermilionCity.setTwoWayLocationNeighbour(route11, "East")
    route11.setTwoWayLocationNeighbour(route12, "East")
    route12.setTwoWayLocationNeighbour(lavendarCity, "North")
    route12.setTwoWayLocationNeighbour(route13, "South")
    route13.setTwoWayLocationNeighbour(route14, "West")
    route14.setTwoWayLocationNeighbour(route15, "South")
    route15.setTwoWayLocationNeighbour(fuchsiaCity, "West")
    route22.setTwoWayLocationNeighbour(victoryRoad, "West")
    victoryRoad.setTwoWayLocationNeighbour(route23, "North")
    route23.setOneWayLocationNeighbours(victoryRoad, "North")
    victoryRoad.setTwoWayLocationNeighbour(route28, "West")
    route28.setTwoWayLocationNeighbour(mountSilver, "West")
    victoryRoad.setTwoWayLocationNeighbour(route26, "South")
    route26.setTwoWayLocationNeighbour(route27, "South")
    route27.setTwoWayLocationNeighbour(tohjoFalls, "West")

    palletTown.addLocationPokemon(      [[magikarp, 5],         [poliwag, 10],          [goldeen, 10],          [tentacool, 15]])
    viridianCity.addLocationPokemon(    [[magikarp, 5],         [poliwag, 10],          [goldeen, 10],          [tentacool, 15]])
    ceruleanCity.addLocationPokemon(    [[magikarp, 5],         [poliwag, 10],          [goldeen, 10],          [psyduck, 15],          [krabby, 15],           [jynx, 15]])
    vermilionCity.addLocationPokemon(   [[farfetchd, 15],       [magikarp, 5],          [poliwag, 10],          [goldeen, 10],          [shellder, 15],         [krabby, 15]])
    celadonCity.addLocationPokemon(     [[magikarp, 5],         [poliwag, 10],          [goldeen, 10],          [poliwhirl, 23],        [slowpoke, 15]])
    fuchsiaCity.addLocationPokemon(     [[magikarp, 5, 15],     [poliwag, 10],          [goldeen, 10, 15],      [krabby, 15],           [seaking, 23]])
    cinnibarIsland.addLocationPokemon(  [[magikarp, 5],         [poliwag, 10],          [goldeen, 10, 15],      [shellder, 15],         [horsea, 15],           [staryu, 15]])
    victoryRoad.addLocationPokemon(     [[zubat, 22, 26],       [golbat, 40, 41],       [machop, 22, 24],       [machoke, 41, 45],      [geodude, 24, 26],      [graveler, 41, 43],     [onix, 36, 45],         [marowak, 40, 43],      [moltres, 50],          [venomoth, 40]])
    viridianForest.addLocationPokemon(  [[caterpie, 3, 5],      [metapod, 4, 6],        [weedle, 3, 5],         [kakuna, 4, 6],         [pikachu, 3, 5]])   
    mountMoon.addLocationPokemon(       [[clefairy, 8, 12],     [zubat, 6, 12],         [paras, 8, 12],         [geodude, 7, 10]])  
    rockTunnel.addLocationPokemon(      [[zubat, 15, 18],       [geodude, 15, 17],      [machop, 15, 18],       [onix, 13, 17]])    
    powerPlant.addLocationPokemon(      [[pikachu, 20, 24],     [raichu, 33, 36],       [magnemite, 21, 33],    [magneton, 32, 35],     [voltorb, 21, 40],      [electabuzz, 33, 36],   [electrode, 43],        [zapdos, 50]])  
    radioTower.addLocationPokemon(      [[gastly, 18, 24],      [haunter, 25, 30],      [cubone, 20, 24],       [marowak, 30]]) 
    silphCo.addLocationPokemon(         [[lapras, 15]])     
    seafoamIslands.addLocationPokemon(  [[zubat, 21],           [golbat, 29, 32],       [psyduck, 28, 33],      [golduck, 37, 39],      [slowpoke, 28, 33],     [slowbro, 37, 39],      [seel, 28, 33],         [dewgong, 37, 38],      [shellder, 28, 33],     [krabby, 28, 33],   [kingler, 37, 39],  [horsea, 28, 33],   [seadra, 37, 39],   [staryu, 28, 33],   [magikarp, 5],  [poliwag, 10],  [goldeen, 10],  [articuno, 50]])
    indigoPlateau.addLocationPokemon(   [[magikarp, 5],         [goldeen, 10],          [poliwag, 10]]) 
    diglettCave.addLocationPokemon(     [[diglett, 15, 22],     [dugtrio, 29, 31]])     
    route1.addLocationPokemon(          [[rattata, 2, 5],       [pidgey, 2, 4]])        
    route2.addLocationPokemon(          [[caterpie, 3, 5],      [weedle, 3, 5],         [pidgey, 3, 5],         [rattata, 2, 5]])   
    route3.addLocationPokemon(          [[pidgey, 6, 8],        [spearow, 5, 8],        [jigglypuff, 3, 7]])    
    route4.addLocationPokemon(          [[rattata, 8, 12],      [spearow, 8, 12],       [ekans, 6, 12],         [sandshrew, 6, 12],     [magikarp, 5],          [poliwag, 10],          [goldeen, 10, 15],      [psyduck, 15],          [krabby, 15]])
    route5.addLocationPokemon(          [[pidgey, 13, 16],      [oddish, 13, 16],       [meowth, 10, 16],       [mankey, 10, 16],       [bellsprout, 13, 16]])  
    route6.addLocationPokemon(          [[pidgey, 13, 16],      [oddish, 13, 16],       [meowth, 10, 16],       [mankey, 10, 16],       [bellsprout, 13, 16],   [magikarp, 5],          [poliwag, 10],          [goldeen, 10],          [shellder, 15],         [krabby, 15]])
    route7.addLocationPokemon(          [[pidgey, 19, 22],      [vulpix, 18, 20],       [oddish, 19, 22],       [meowth, 17, 20],       [mankey, 17, 20],       [growlithe, 18, 20],    [bellsprout, 19, 22]])  
    route8.addLocationPokemon(          [[pidgey, 18, 20],      [ekans, 17, 19],        [sandshrew, 17, 19],    [vulpix, 15, 18],       [meowth, 18, 20],       [mankey, 18, 20],       [growlithe, 15, 18]])   
    route9.addLocationPokemon(          [[rattata, 14, 17],     [spearow, 13, 17],      [ekans, 11, 17],        [sandshrew, 11, 17]])   
    route10.addLocationPokemon(         [[spearow, 13, 17],     [ekans, 11, 17],        [sandshrew, 11, 17],    [voltorb, 14, 17],      [magikarp, 5],          [poliwag, 10],          [goldeen, 10],          [poliwhirl, 23],        [slowpoke, 15]])
    route11.addLocationPokemon(         [[spearow, 13, 17],     [ekans, 12, 15],        [sandshrew, 12, 15],    [drowzee, 9, 15],       [magikarp, 5],          [poliwag, 10],          [goldeen, 10],          [shellder, 15],         [krabby, 15],           [nidorina, 15]])
    route12.addLocationPokemon(         [[pidgey, 23, 27],      [oddish, 22, 26],       [gloom, 28, 30],        [venonat, 24, 26],      [bellsprout, 22, 26],   [weepinbell, 28, 30],   [magikarp, 5, 15],      [poliwag, 10],          [goldeen, 10, 15],      [tentacool, 5],     [krabby, 15],       [snorlax, 30]])
    route13.addLocationPokemon(         [[pidgey, 25, 27],      [oddish, 22, 26],       [gloom, 28, 30],        [venonat, 24, 26],      [bellsprout, 22, 26],   [weepinbell, 28, 30],   [ditto, 25],            [magikarp, 5, 15],      [poliwag, 10],          [goldeen, 10, 15],  [tentacool, 5],     [krabby, 15]])
    route14.addLocationPokemon(         [[pidgey, 26],          [pidgeotto, 28, 30],    [oddish, 22, 26],       [gloom, 30],            [venonat, 24, 26],      [bellsprout, 22, 26],   [weepinbell, 30],       [ditto, 23],            [magikarp, 5],          [poliwag, 10],      [goldeen, 10]])
    route15.addLocationPokemon(         [[pidgeot, 23],         [pidgeotto, 28, 30],    [oddish, 22, 26],       [gloom, 30],            [venonat, 26, 28],      [bellsprout, 22, 26],   [weepinbell, 30],       [ditto, 26]])   
    route16.addLocationPokemon(         [[rattata, 18, 22],     [raticate, 23, 25],     [spearow, 20, 22],      [doduo, 18, 22],        [snorlax, 30]]) 
    route17.addLocationPokemon(         [[raticate, 25, 29],    [spearow, 20, 22],      [fearow, 25, 27],       [doduo, 24, 28],        [magikarp, 5, 15],      [poliwag, 10],          [goldeen, 10, 15],      [tentacool, 5],         [krabby, 15]])
    route18.addLocationPokemon(         [[raticate, 25, 29],    [spearow, 20, 22],      [fearow, 25, 29],       [doduo, 24, 28],        [magikarp, 5, 15],      [poliwag, 10],          [goldeen, 10, 15],      [tentacool, 5],         [krabby, 15],           [lickitung, 15]])
    route19.addLocationPokemon(         [[tentacool, 5, 40],    [magikarp, 5],          [poliwag, 10],          [goldeen, 10, 15],      [shellder, 15],         [horsea, 15],           [staryu, 15]])  
    route20.addLocationPokemon(         [[tentacool, 5, 40],    [magikarp, 5],          [poliwag, 10],          [goldeen, 10, 15],      [shellder, 15],         [horsea, 15],           [staryu, 15]])  
    route21.addLocationPokemon(         [[pidgey, 21, 23],      [pidgeotto, 30, 32],    [rattata, 21, 23],      [raticate, 30],         [tangela, 28, 32],      [tentacool, 5, 40],     [magikarp, 5],          [poliwag, 10],          [goldeen, 10, 15],      [shellder, 15],     [horsea, 15],       [staryu, 15]])
    route22.addLocationPokemon(         [[rattata, 2, 4],       [spearow, 3, 5],        [nidoranMale, 3, 4],    [nidoranFemale, 2, 4],  [magikarp, 5],          [poliwag, 10],          [goldeen, 10, 15]])
    route23.addLocationPokemon(         [[spearow, 26],         [fearow, 38, 43],       [ekans, 26],            [arbok, 41],            [sandshrew, 26],        [sandslash, 41],        [ditto, 33, 43],        [magikarp, 5],          [poliwag, 10],          [goldeen, 10],      [slowbro, 23],      [kingler, 23],      [seadra, 23],       [seaking, 23]])
    route24.addLocationPokemon(         [[caterpie, 7],         [metapod, 8],           [weedle, 7],            [kakuna, 8],            [pidgey, 12, 13],       [oddish, 12, 14],       [abra, 8, 12],          [bellsprout, 12, 14],   [magikarp, 5],          [poliwag, 10],      [goldeen, 10, 15],  [psyduck, 15],      [krabby, 15]])
    route25.addLocationPokemon(         [[caterpie, 8],         [metapod, 7, 9],        [weedle, 8],            [kakuna, 7, 9],         [pidgey, 13],           [oddish, 12, 14],       [abra, 10, 12],         [bellsprout, 12, 14],   [magikarp, 5],          [poliwag, 10],      [goldeen, 10, 15],  [psyduck, 15],      [krabby, 15]])

def setupShops():
    viridianCityMart    = Mart("Viridian City Mart",    viridianCity,   {"Poke Ball": pokeBall})
    pewterCityMart      = Mart("Pewter City Mart",      pewterCity,     {})
    ceruleanCityMart    = Mart("Cerulean City Mart",    ceruleanCity,   {})
    vermilionCityMart   = Mart("Vermilion City Mart",   vermilionCity,  {})
    lavendarTownMart    = Mart("Lavendar Town Mart",    lavendarCity,   {})
    saffronCityMart     = Mart("Saffron City Mart",     saffronCity,    {})
    fuchsiaCityMart     = Mart("Fuchsia City Mart",     fuchsiaCity,    {})
    cinnibarIslandMart  = Mart("Cinnibar Island Mart",  cinnibarIsland, {})
    indigoPlateauMart   = Mart("Indigo Plateau Mart",   indigoPlateau,  {})

def setupTrainers():
    global brock

    brockGeodude = deepcopy(geodude)
    brockGeodude.setPokemonLevel(12)
    brockOnix = deepcopy(onix)
    brockOnix.setPokemonLevel(14)
    brock = Trainer("Brock", {"Geodude": brockGeodude, "Onix": brockOnix}, {}, pewterCity)

    global misty
    
    mistyStaryu = deepcopy(staryu)
    mistyStaryu.setPokemonLevel(18)
    mistyStarmie = deepcopy(starmie)
    mistyStarmie.setPokemonLevel(21)
    misty = Trainer("Misty", {"Staryu": mistyStaryu, "Starmie": mistyStarmie}, {}, ceruleanCity)

    global ltSurge

    ltSurgeVoltorb = deepcopy(voltorb)
    ltSurgeVoltorb.setPokemonLevel(21)
    ltSurgePikachu = deepcopy(pikachu)
    ltSurgePikachu.setPokemonLevel(18)
    ltSurgeRaichu = deepcopy(raichu)
    ltSurgeRaichu.setPokemonLevel(24)
    ltSurge = Trainer("Lt. Surge", {"Voltorb": ltSurgeVoltorb, "Pikachu": ltSurgePikachu, "Raichu": ltSurgeRaichu}, {}, vermilionCity)

    global erika
    
    erikaVictreebel = deepcopy(victreebel)
    erikaVictreebel.setPokemonLevel(29)
    erikaTangela = deepcopy(tangela)
    erikaTangela.setPokemonLevel(24)
    erikaVileplume = deepcopy(vileplume)
    erikaVileplume.setPokemonLevel(29)
    erika = Trainer("Erika", {"Victreebel": erikaVictreebel, "Tangela": erikaTangela, "Vileplume": erikaVileplume}, {}, celadonCity)
    
    global koga
    
    kogaKoffing = deepcopy(koffing)
    kogaKoffing.setPokemonLevel(37)
    kogaMuk = deepcopy(muk)
    kogaMuk.setPokemonLevel(39)
    kogaKoffing2 = deepcopy(koffing)
    kogaKoffing2.changePokemonName("Koffing2")
    kogaKoffing2.setPokemonLevel(37)
    kogaWeezing = deepcopy(weezing)
    kogaWeezing.setPokemonLevel(43)
    koga = Trainer("Koga", {"Koffing": kogaKoffing, "Muk": kogaMuk, "Koffing2": kogaKoffing2, "Weezing": kogaWeezing}, {}, fuchsiaCity)

    global sabrina
    
    sabrinaKadabra = deepcopy(kadabra)
    sabrinaKadabra.setPokemonLevel(38)
    sabrinaMrMime = deepcopy(mrmime)
    sabrinaMrMime.setPokemonLevel(37)
    sabrinaVenomoth = deepcopy(venomoth)
    sabrinaVenomoth.setPokemonLevel(38)
    sabrinaAlakazam = deepcopy(alakazam)
    sabrinaAlakazam.setPokemonLevel(43)
    sabrina = Trainer("Sabrina", {"Kadabra": sabrinaKadabra, "Mr Mime": sabrinaMrMime, "Venomoth": sabrinaVenomoth, "Alakazam": sabrinaAlakazam}, {}, saffronCity)

    global blaine
    
    blaineGrowlithe = deepcopy(growlithe)
    blaineGrowlithe.setPokemonLevel(42)
    blainePonyta = deepcopy(ponyta)
    blainePonyta.setPokemonLevel(40)
    blaineRapidash = deepcopy(rapidash)
    blaineRapidash.setPokemonLevel(42)
    blaineArcanine = deepcopy(arcanine)
    blaineArcanine.setPokemonLevel(47)
    blaine = Trainer("Blaine", {"Growlithe": blaineGrowlithe, "Ponyta": blainePonyta, "Rapidash": blaineRapidash, "Arcanine": blaineArcanine}, {}, cinnibarIsland)

    global giovanni
    
    giovanniRhyhorn = deepcopy(rhyhorn)
    giovanniRhyhorn.setPokemonLevel(45)
    giovanniDugtrio = deepcopy(dugtrio)
    giovanniDugtrio.setPokemonLevel(42)
    giovanniNidoqueen = deepcopy(nidoqueen)
    giovanniNidoqueen.setPokemonLevel(44)
    giovanniNidoking = deepcopy(nidoking)
    giovanniNidoking.setPokemonLevel(45)
    giovanniRhydon = deepcopy(rhydon)
    giovanniRhydon.setPokemonLevel(50)
    giovanni = Trainer("Giovanni", {"Rhyhorn": giovanniRhyhorn, "Dugtrio": giovanniDugtrio, "Nidoqueen": giovanniNidoqueen, "Nidoking": giovanniNidoking, "Rhydon": giovanniRhydon}, {}, viridianCity)
    
    global lorelei
    loreleiDewgong = deepcopy(dewgong)
    loreleiDewgong.setPokemonLevel(54)
    loreleiCloyster = deepcopy(cloyster)
    loreleiCloyster.setPokemonLevel(53)
    loreleiSlowbro = deepcopy(slowbro)
    loreleiSlowbro.setPokemonLevel(54)
    loreleiJynx = deepcopy(jynx)
    loreleiJynx.setPokemonLevel(56)
    loreleiLapras = deepcopy(lapras)
    loreleiLapras.setPokemonLevel(56)
    lorelei = Trainer("Lorelei", {"Dewgong": loreleiDewgong, "Cloyster": loreleiCloyster, "Slowbro": loreleiSlowbro, "Jynx": loreleiJynx, "Lapras": loreleiLapras}, {}, indigoPlateau)

    global bruno
    brunoOnix = deepcopy(onix)
    brunoOnix.setPokemonLevel(53)
    brunoHitmonchan = deepcopy(hitmonchan)
    brunoHitmonchan.setPokemonLevel(55)
    brunoHitmonlee = deepcopy(hitmonlee)
    brunoHitmonlee.setPokemonLevel(55)
    brunoOnix2 = deepcopy(onix)
    brunoOnix2.changePokemonName("Onix2")
    brunoOnix2.setPokemonLevel(56)
    brunoMachamp = deepcopy(machamp)
    brunoMachamp.setPokemonLevel(58)
    bruno = Trainer("Bruno", {"Onix": brunoOnix, "Hitmonchan": brunoHitmonchan, "Hitmonlee": brunoHitmonlee, "Onix2": brunoOnix2, "Machamp": brunoMachamp}, {}, indigoPlateau)

    global agatha
    agathaGengar = deepcopy(gengar)
    agathaGengar.setPokemonLevel(56)
    agathaGolbat = deepcopy(golbat)
    agathaGolbat.setPokemonLevel(56)
    agathaHaunter = deepcopy(haunter)
    agathaHaunter.setPokemonLevel(55)
    agathaArbok = deepcopy(arbok)
    agathaArbok.setPokemonLevel(58)
    agathaGengar2 = deepcopy(gengar)
    agathaGengar2.changePokemonName("Gengar2")
    agathaGengar2.setPokemonLevel(60)
    agatha = Trainer("Agatha", {"Gengar": agathaGengar, "Golbat": agathaGolbat, "Haunter": agathaHaunter, "Arbok": agathaArbok, "Gengar2": agathaGengar2}, {}, indigoPlateau)

    global lance
    lanceGyrados = deepcopy(gyrados)
    lanceGyrados.setPokemonLevel(58)
    lanceDragonair = deepcopy(dragonair)
    lanceDragonair.setPokemonLevel(56)
    lanceDragonair2 = deepcopy(dragonair)
    lanceDragonair2.changePokemonName("Dragonair2")
    lanceDragonair2.setPokemonLevel(56)
    lanceAerodactyl = deepcopy(aerodactyl)
    lanceAerodactyl.setPokemonLevel(60)
    lanceDragonite = deepcopy(dragonite)
    lanceDragonite.setPokemonLevel(62)
    lance = Trainer("Lance", {"Gyrados": lanceGyrados, "Dragonair": lanceDragonair, "Dragonair2": lanceDragonair2, "Aerodactyl": lanceAerodactyl, "Dragonite": lanceDragonite}, {}, indigoPlateau)

def setup():
    #Creates types and type advantages for use in battles
    setupTypes()

    #Creates effects for use in battles
    setupEffects()

    #Creates and assigns moves with the corresponding pokemon types for use in battles
    setupMoves()

    #Creates pokemons to be referenced for encounters
    setupPokemon()

    #Creates items to be referenced for encounters
    setupItems()

    #Creates and orders locations
    setupMap()

    #Creates and places shops in locations around the map
    setupShops()

    #Creates trainers that can be played against, and the player protagonist
    setupTrainers()

    global randomEncounterChancePercentage

    randomEncounterChancePercentage = 60

def intro():
    print("------------------- POKEMON\u2122 Red Version -------------------")
    print("----------------- By Tan Teng Fong, Christopher -----------------")

    print("Hello there! Welcome to the world of Pokemon!")
    print("My name is OAK! People call me the Pokemon Prof!")
    print("This world is inhabited by creatures called Pokemon.")
    print("For some people, Pokemon are pets. Others use them to fight.")
    print("Myself...")
    print("I study Pokemon as a profession.")

def setupPlayer():
    playerName = input("First, what is your name? : ")
    print("Right, so your name is " + playerName + ".")
    print(playerName + "! Your very own Pokemon legend is about to unfold!")
    print("A world of dreams and adventures awaits! Let's go!")
    
    global protagonist

    starterInput = ""
    while starterInput not in ["Bulbasaur", "Charmander", "Squirtle"]:
        starterInput = input("Choose you starter Pokemon (Bulbasaur, Charmander, Squirtle) : ")

    nameInput = ""
    while nameInput == "":
        nameInput = input("What is your Pokemon's name? : ").strip()

    if starterInput == "Bulbasaur":
        starterPokemon = deepcopy(bulbasaur)    
    elif starterInput == "Charmander":
        starterPokemon = deepcopy(charmander)
    else:
        starterPokemon = deepcopy(squirtle)
    
    starterPokemon.changePokemonName(nameInput)
    protagonist = Trainer(playerName, {f"{nameInput}": starterPokemon}, {}, palletTown)

####################################################################################################

setup()
intro()
setupPlayer()
while True:
    availableActions = ["Travel"]
    actionMessage = "What do you want to do? (Travel"
    if protagonist.getTrainerLocation().getLocationMart() != None:
        actionMessage += ", Shop"
        availableActions.append("Shop")
    if len(protagonist.getTrainerLivePokemonsDict()) != 0:
        actionMessage += ", Walk Around"
        availableActions.append("Walk Around")
    actionMessage += ") : "

    actionInput = ""
    while actionInput not in availableActions:
        actionInput = input(actionMessage)
    
    if actionInput == "Travel":
        #UI
        directionMessage = "Direction to move ("
        for dir in protagonist.getTrainerLocation().getLocationNeighboursDict().keys():
            directionMessage += dir + ", "
        directionMessage = directionMessage[:-2] + ") : "

        direction = ""

        #Wait until user's input is valid
        while direction not in protagonist.getTrainerLocation().getLocationNeighboursDict().keys():
            direction = input(directionMessage)
        else:
            protagonist.moveToLocation(direction)
    elif actionInput == "Shop":
        protagonist.getTrainerLocation().getLocationMart().openShop(protagonist)
    else:
        #Check if there are trainers to fight
        trainers = deepcopy(protagonist.getTrainerLocation().getLocationTrainersDict())
        del(trainers[protagonist.getTrainerName()])
        
        #Randomly pick a trainer from those in the current location
        if len(trainers) != 0:
            opponent = trainers[list(trainers.keys())[randint(0, len(trainers) - 1)]]
            
            #Check if the opponent has available pokemon to fight
            if opponent.getTrainerActivePokemon() != "":
                #Start battle
                battle = Encounter(protagonist, opponent)
                battle.startBattle()
        else:
            #Roll chance for random encounter
            if randint(1, 100) > randomEncounterChancePercentage:
                availablePokemon = protagonist.getTrainerLocation().getLocationPokemonDict()
                availablePokemonNames = list(availablePokemon.keys())

                #Check if there spawnable pokemon to fight
                if len(availablePokemon) != 0:
                    randomPokemonSet = availablePokemon[availablePokemonNames[randint(0, len(availablePokemon) - 1)]]
                    randomPokemon = deepcopy(randomPokemonSet[0])
                    
                    if len(randomPokemonSet) == 2:
                        randomPokemon.setPokemonLevel(randomPokemonSet[1])
                    else:
                        randomPokemon.setPokemonLevel(randint(randomPokemonSet[1], randomPokemonSet[2]))
                    
                    randomEncounter = Encounter(protagonist, randomPokemon)
                    randomEncounter.startBattle()