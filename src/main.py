#This is where the whole game is set up, including all the types, moves, pokemons, trainers, locations and map.
#The logic for initiating random encounters and trainer encounters is also below.

from random import randint
from copy import deepcopy
from Battle import *
from Pokemon import *
from Trainer import *
from Item import *
from Type import *
from Location import *
from Move import *

def setupTypes():
    global bugType, dragonType, electricType, fightingType, fireType, flyingType, ghostType, grassType, groundType, iceType, normalType, poisonType, psychicType, rockType, waterType

    bugType = Type("Bug")
    dragonType = Type("Dragon")
    electricType = Type("Electric")
    fightingType = Type("Fighting")
    fireType = Type("Fire")
    flyingType = Type("Flying")
    ghostType = Type("Ghost")
    grassType = Type("Grass")
    groundType = Type("Ground")
    iceType = Type("Ice")
    normalType = Type("Normal")
    poisonType = Type("Poison")
    psychicType = Type("Psychic")
    rockType = Type("Rock")
    waterType = Type("Water")

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

def setupMoves():
    global tackle, switch, run

    tackle = Move("Tackle", normalType, "Attack", 40, 100)
    switch = Move("Switch", normalType, "Switch", 0, 0)
    run = Move("Run", normalType, "Run", 0, 0)

    moves = [tackle, switch, run]

    global bugMoves, dragonMoves, electricMoves, fightingMoves, fireMoves, flyingMoves, ghostMoves, grassMoves, groundMoves, iceMoves, normalMoves, poisonMoves, psychicMoves, rockMoves, waterMoves
    
    bugMoves = []
    dragonMoves = []
    electricMoves = []
    fightingMoves = []
    fireMoves = []
    flyingMoves = []
    ghostMoves = []
    grassMoves = []
    groundMoves = []
    iceMoves = []
    normalMoves = []
    poisonMoves = []
    psychicMoves = []
    rockMoves = []
    waterMoves = []

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
    global bulbasaur, ivysaur, venusaur, charmander, charmeleon, charizard, squirtle, wartortle, blastoise, caterpie, metapod, butterfree, weedle, kakuna, beedrill, pidgey, pidgeotto, pidgeot
    global rattata, raticate, spearow, fearow, ekans, arbok, pikachu, raichu, sandshrew, sandslash, nidoranFemale, nidorina, nidoqueen, nidoranMale, nidorino, nidoking, clefairy, clefable
    global vulpix, ninetales, jigglypuff, wigglytuff, zubat, golbat, oddish, gloom, vileplume, paras, parasect, venonat, venomoth, diglett, dugtrio, meowth, persian, psyduck, golduck, mankey, primeape
    global growlithe, arcanine, poliwag, poliwhirl, poliwrath, abra, kadabra, alakazam, machop, machoke, machamp, bellsprout, weepinbell, victreebel, tentacool, tentacruel, geodude, graveler, golem
    global ponyta, rapidash, slowpoke, slowbro, magnemite, magneton, farfetchd, doduo, dodrio, seel, dewgong, grimer, muk, shellder, cloyster, gastly, haunter, gengar, onix, drowzee, hypno
    global krabby, kingler, voltorb, electrode, exeggcute, exeggutor, cubone, marowak, hitmonlee, hitmonchan, lickitung, koffing, weezing, rhyhorn, rhydon, chansey, tangela, kangaskhan, horsea, seadra
    global goldeen, seaking, staryu, starmie, mrmime, scyther, jynx, electabuzz, magmar, pinsir, tauros, magikarp, gyrados, lapras, ditto, eevee, vaporean, jolteon, flareon, porygon, omanyte, omastar
    global kabuto, kabutops, aerodactyl, snorlax, articuno, zapdos, moltres, dratini, dragonair, dragonite, mewtwo, mew

    bulbasaur = Pokemon("Bulbasaur", grassType, 45, 49, 49, 100, 100)
    ivysaur = Pokemon("Ivysaur", grassType, 60, 62, 63, 100, 100)
    venusaur = Pokemon("Venusaur", grassType, 80, 82, 83, 100, 100)
    charmander = Pokemon("Charmander", fireType, 39, 52, 43, 100, 100)
    charmeleon = Pokemon("Charmeleon", fireType, 58, 64, 58, 100, 100)
    charizard = Pokemon("Charizard", fireType, 78, 84, 78, 100, 100)
    squirtle = Pokemon("Squirtle", waterType, 44, 48, 65, 100, 100)
    wartortle = Pokemon("Wartortle", waterType, 59, 63, 80, 100, 100)
    blastoise = Pokemon("Blastoise", waterType, 79, 83, 100, 100, 100)
    caterpie = Pokemon("Caterpie", bugType, 45, 30, 35, 100, 100)
    metapod = Pokemon("Metapod", bugType, 50, 20, 55, 100, 100)
    butterfree = Pokemon("Butterfree", bugType, 60, 45, 50, 100, 100)
    weedle = Pokemon("Weedle", bugType, 40, 35, 30, 100, 100)
    kakuna = Pokemon("Kakuna", bugType, 65, 25, 50, 100, 100)
    beedrill = Pokemon("Beedrill", bugType, 65, 80, 40, 100, 100)
    pidgey = Pokemon("Pidgey", normalType, 40, 45, 40, 100, 100)
    pidgeotto = Pokemon("Pidgeotto", normalType, 63, 60, 55, 100, 100)
    pidgeot = Pokemon("Pidgeot", normalType, 83, 80, 75, 100, 100)
    rattata = Pokemon("Rattata", normalType, 30, 56, 35, 100, 100)
    raticate = Pokemon("Raticate", normalType, 55, 81, 60, 100, 100)
    spearow = Pokemon("Spearow", normalType, 40, 60, 30, 100, 100)
    fearow = Pokemon("Fearow", normalType, 65, 90, 65, 100, 100)
    ekans = Pokemon("Ekans", poisonType, 35, 60, 44, 100, 100)
    arbok = Pokemon("Arbok", poisonType, 60, 85, 69, 100, 100)
    pikachu = Pokemon("Pikachu", electricType, 35, 55, 30, 100, 100)
    raichu = Pokemon("Raichu", electricType, 60, 90, 55, 100, 100)
    sandshrew = Pokemon("Sandshrew", groundType, 50, 75, 85, 100, 100)
    sandslash = Pokemon("Sandslash", groundType, 75, 100, 110, 100, 100)
    nidoranFemale = Pokemon("Nidoran Female", poisonType, 55, 47, 52, 100, 100)
    nidorina = Pokemon("Nidorina", poisonType, 70, 62, 67, 100, 100)
    nidoqueen = Pokemon("Nidoqueen", poisonType, 90, 82, 87, 100, 100)
    nidoranMale = Pokemon("Nidoran Male", poisonType, 46, 57, 40, 100, 100)
    nidorino = Pokemon("Nidorino", poisonType, 61, 72, 57, 100, 100)
    nidoking = Pokemon("Nidoking", poisonType, 81, 92, 77, 100, 100)
    clefairy = Pokemon("Clefairy", normalType, 70, 45, 48, 100, 100)
    clefable = Pokemon("Clefable", normalType, 95, 70, 73, 100, 100)
    vulpix = Pokemon("Vulpix", fireType, 38, 41, 40, 100, 100)
    ninetales = Pokemon("Ninetales", fireType, 73, 76, 75, 100, 100)
    jigglypuff = Pokemon("Jigglypuff", normalType, 115, 45, 20, 100, 100)
    wigglytuff = Pokemon("Wigglytuff", normalType, 140, 70, 45, 100, 100)
    zubat = Pokemon("Zubat", poisonType, 40, 45, 35, 100, 100)
    golbat = Pokemon("Golbat", poisonType, 75, 80, 70, 100, 100)
    oddish = Pokemon("Oddish", grassType, 45, 50, 55, 100, 100)
    gloom = Pokemon("Gloom", grassType, 60, 65, 70, 100, 100)
    vileplume = Pokemon("Vileplume", grassType, 75, 80, 85, 100, 100)
    paras = Pokemon("Paras", bugType, 35, 70, 55, 100, 100)
    parasect = Pokemon("Parasect", bugType, 60, 55, 50, 100, 100)
    venonat = Pokemon("Venonat", bugType, 70, 65, 60, 100, 100)
    venomoth = Pokemon("Venomoth", bugType, 10, 55, 25, 100, 100)
    diglett = Pokemon("Diglett", groundType, 35, 80, 50, 100, 100)
    dugtrio = Pokemon("Dugtrio", groundType, 40, 45, 35, 100, 100)
    meowth = Pokemon("Meowth", normalType, 65, 70, 60, 100, 100)
    persian = Pokemon("Persian", normalType, 50, 52, 48, 100, 100)
    psyduck = Pokemon("Psyduck", waterType, 80, 82, 78, 100, 100)
    golduck = Pokemon("Golduck", waterType, 40, 80, 35, 100, 100)
    mankey = Pokemon("Mankey", fightingType, 65, 105, 60, 100, 100)
    primeape = Pokemon("Primape", fightingType, 55, 70, 45, 100, 100)
    growlithe = Pokemon("Growlithe", fireType, 90, 110, 80, 100, 100)
    arcanine = Pokemon("Arcanine", fireType, 40, 50, 40, 100, 100)
    poliwag = Pokemon("Poliwag", waterType, 65, 65, 65, 100, 100)
    poliwhirl = Pokemon("Poliwhirl", waterType, 90, 85, 95, 100, 100)
    poliwrath = Pokemon("Poliwrath", waterType, 25, 20, 15, 100, 100)
    abra = Pokemon("Abra", psychicType, 40, 35, 30, 100, 100)
    kadabra = Pokemon("Kadabra", psychicType, 55, 50, 45, 100, 100)
    alakazam = Pokemon("Alakazam", psychicType, 70, 80, 50, 100, 100)
    machop = Pokemon("Machop", fightingType, 80, 100, 70, 100, 100)
    machoke = Pokemon("Machoke", fightingType, 90, 130, 80, 100, 100)
    machamp = Pokemon("Machamp", fightingType, 50, 75, 35, 100, 100)
    bellsprout = Pokemon("Bellsprout", grassType, 65, 90, 50, 100, 100)
    weepinbell = Pokemon("Weepinbell", grassType, 80, 105, 65, 100, 100)
    victreebel = Pokemon("Victreebel", grassType, 40, 40, 35, 100, 100)
    tentacool = Pokemon("Tentacool", waterType, 80, 105, 65, 100, 100)
    tentacruel = Pokemon("Tentacruel", waterType, 40, 80, 100, 100, 100)
    geodude = Pokemon("Geodude", rockType, 55, 95, 115, 100, 100)
    graveler = Pokemon("Graveler", rockType, 80, 110, 130, 100, 100)
    golem = Pokemon("Golem", rockType, 50, 85, 55, 100, 100)
    ponyta = Pokemon("Ponyta", fireType, 65, 100, 70, 100, 100)
    rapidash = Pokemon("Rapidash", fireType, 90, 65, 65, 100, 100)
    slowpoke = Pokemon("Slowpoke", waterType, 95, 49, 49, 100, 100)
    slowbro = Pokemon("Slowbro", waterType, 25, 35, 70, 100, 100)
    magnemite = Pokemon("Magnemite", electricType, 50, 60, 95, 100, 100)
    magneton = Pokemon("Magneton", electricType, 52, 65, 55, 100, 100)
    farfetchd = Pokemon("Farfetch'd", normalType, 35, 85, 45, 100, 100)
    doduo = Pokemon("Duduo", normalType, 60, 110, 70, 100, 100)
    dodrio = Pokemon("Dudrio", normalType, 65, 45, 55, 100, 100)
    seel = Pokemon("Seel", waterType, 90, 70, 80, 100, 100)
    dewgong = Pokemon("Dewgong", waterType, 80, 80, 50, 100, 100)
    grimer = Pokemon("Grimer", poisonType, 105, 105, 75, 100, 100)
    muk = Pokemon("Muk", poisonType, 30, 65, 100, 100, 100)
    shellder = Pokemon("Shellder", waterType, 50, 95, 180, 100, 100)
    cloyster = Pokemon("Cloyster", waterType, 30, 35, 30, 100, 100)
    gastly = Pokemon("Gastly", ghostType, 30, 35, 30, 100, 100)
    haunter = Pokemon("Haunter", ghostType, 45, 50, 45, 100, 100)
    gengar = Pokemon("Gengar", ghostType, 60, 65, 60, 100, 100)
    onix = Pokemon("Onix", rockType, 35, 45, 160, 100, 100)
    drowzee = Pokemon("Drowzee", psychicType, 60, 48, 45, 100, 100)
    hypno = Pokemon("Hypno", psychicType, 85, 73, 70, 100, 100)
    krabby = Pokemon("Krabby", waterType, 30, 105, 90, 100, 100)
    kingler = Pokemon("Kingler", waterType, 55, 130, 115, 100, 100)
    voltorb = Pokemon("Voltorb", electricType, 40, 30, 50, 100, 100)
    electrode = Pokemon("Electrode", electricType, 60, 50, 70, 100, 100)
    exeggcute = Pokemon("Exeggcute", grassType, 60, 40, 80, 100, 100)
    exeggutor = Pokemon("Exeggutor", grassType, 95, 95, 85, 100, 100)
    cubone = Pokemon("Cubone", groundType, 50, 50, 95, 100, 100)
    marowak = Pokemon("Marowak", groundType, 60, 80, 110, 100, 100)
    hitmonlee = Pokemon("Hitmonlee", fightingType, 50, 120, 53, 100, 100)
    hitmonchan = Pokemon("Hitmonchan", fightingType, 50, 105, 79, 100, 100)
    lickitung = Pokemon("Lickitung", normalType, 90, 55, 75, 100, 100)
    koffing = Pokemon("Koffing", poisonType, 40, 65, 95, 100, 100)
    weezing = Pokemon("Weezing", poisonType, 65, 90, 120, 100, 100)
    rhyhorn = Pokemon("Rhyhorn", groundType, 80, 85, 95, 100, 100)
    rhydon = Pokemon("Rhydon", groundType, 105, 130, 120, 100, 100)
    chansey = Pokemon("Chansey", normalType, 250, 5, 5, 100, 100)
    tangela = Pokemon("Tangela", grassType, 65, 55, 115, 100, 100)
    kangaskhan = Pokemon("Kangaskhan", groundType, 105, 95, 80, 100, 100)
    horsea = Pokemon("Horsea", waterType, 30, 40, 70, 100, 100)
    seadra = Pokemon("Seadra", waterType, 55, 65, 95, 100, 100)
    goldeen = Pokemon("Goldeen", waterType, 45, 67, 60, 100, 100)
    seaking = Pokemon("Seaking", waterType, 80, 92, 65, 100, 100)
    staryu = Pokemon("Staryu", waterType, 30, 45, 55, 100, 100)
    starmie = Pokemon("Starmie", waterType, 60, 75, 85, 100, 100)
    mrmime = Pokemon("Mr Mime", psychicType, 40, 45, 65, 100, 100)
    scyther = Pokemon("Scyther", bugType, 70, 110, 80, 100, 100)
    jynx = Pokemon("Jynx", iceType, 65, 50, 35, 100, 100)
    electabuzz = Pokemon("Electabuzz", electricType, 65, 50, 35, 100, 100)
    magmar = Pokemon("Magmar", fireType, 65, 83, 57, 100, 100)
    pinsir = Pokemon("Pinsir", bugType, 65, 95, 57, 100, 100)
    tauros = Pokemon("Tauros", normalType, 75, 100, 95, 100, 100)
    magikarp = Pokemon("Magikarp", waterType, 20, 10, 55, 100, 100)
    gyrados = Pokemon("Gyrados", waterType, 95, 125, 79, 100, 100)
    lapras = Pokemon("Lapras", waterType, 130, 85, 80, 100, 100)
    ditto = Pokemon("Ditto", normalType, 48, 48, 48, 100, 100)
    eevee = Pokemon("Eevee", normalType, 55, 55, 50, 100, 100)
    vaporean = Pokemon("Vaporean", waterType, 130, 65, 60, 100, 100)
    jolteon = Pokemon("Jolteon", electricType, 65, 65, 65, 100, 100)
    flareon = Pokemon("Flareon", fireType, 65, 130, 65, 100, 100)
    porygon = Pokemon("Porygon", normalType, 65, 60, 70, 100, 100)
    omanyte = Pokemon("Omanyte", rockType, 35, 40, 100, 100, 100)
    omastar = Pokemon("Omastar", rockType, 70, 60, 125, 100, 100)
    kabuto = Pokemon("Kabuto", rockType, 30, 80, 90, 100, 100)
    kabutops = Pokemon("Kabutops", rockType, 60, 115, 105, 100, 100)
    aerodactyl = Pokemon("Aerodactyl", rockType, 80, 105, 65, 100, 100)
    snorlax = Pokemon("Snorlax", normalType, 160, 110, 65, 100, 100)
    articuno = Pokemon("Articuno", iceType, 90, 85, 100, 100, 100)
    zapdos = Pokemon("Zapdos", electricType, 90, 90, 85, 100, 100)
    moltres = Pokemon("Moltres", fireType, 90, 100, 90, 100, 100)
    dratini = Pokemon("Dratini", dragonType, 41, 64, 45, 100, 100)
    dragonair = Pokemon("Dragonair", dragonType, 61, 84, 65, 100, 100)
    dragonite = Pokemon("Dragonite", dragonType, 91, 134, 95, 100, 100)
    mewtwo = Pokemon("Mewtwo", psychicType, 106, 110, 90, 100, 100)
    mew = Pokemon("Mew", psychicType, 100, 100, 100, 100, 100)

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
    global moonStone, fireStone, thunderStone, waterStone, leafStone, expAll, rareCandy, xAccuracy, xAttack, xDefend, guardSpec

    masterBall = Item("Master Ball", "Ball", 0)
    ultraBall = Item("Ultra Ball", "Ball", 0)
    greatBall = Item("Great Ball", "Ball", 0)
    pokeBall = Item("Poke Ball", "Ball", 0)
    antidote = Item("Antidote", "Medicine", 0)
    burnHeal = Item("Burn Heal", "Medicine", 0)
    iceHeal = Item("Ice Heal", "Medicine", 0)
    awakening = Item("Awakening", "Medicine", 0)
    paralyseHeal = Item("Parlyse Heal", "Medicine", 0)
    fullHeal = Item("Full Heal", "Medicine", 0)
    revive = Item("Revive", "Revive", 0.5)
    maxRevive = Item("Max Revive", "Revive", 1)
    fullRestore = Item("Full Restore", "Health", 0)
    maxPotion = Item("Max Potion", "Health", 0)
    hyperPotion = Item("Hyper Potion", "Health", 200)
    superPotion = Item("Super Potion", "Health", 50)
    potion = Item("Potion", "Health", 20)
    freshWater = Item("Fresh Water", "Health", 30)
    sodaPop = Item("Soda Pop", "Health", 60)
    lemonade = Item("Lemonade", "Health", 80)
    boulderBadge = Item("Boulder Badge", "Badge", 0)
    cascadeBadge = Item("Cascade Badge", "Badge", 0)
    thunderBadge = Item("Thunder Badge", "Badge", 0)
    rainbowBadge = Item("Rainbow Badge", "Badge", 0)
    soulBadge = Item("Soul Badge", "Badge", 0)
    marshBadge = Item("Marsh Badge", "Badge", 0)
    volcanoBadge = Item("Volcano Badge", "Badge", 0)
    earthBadge = Item("Earth Badge", "Badge", 0)
    oldAmber = Item("Old Amber", "Fossil", 0)
    domeFossil = Item("Dome Fossil", "Fossil", 0)
    helixFossil = Item("Helix Fossil", "Fossil", 0)
    moonStone = Item("Moon Stone", "Stone", 0)
    fireStone = Item("Fire Stone", "Stone", 0)
    thunderStone = Item("Thunder Stone", "Stone", 0)
    waterStone = Item("Water Stone", "Stone", 0)
    leafStone = Item("Leaf Stone", "Stone", 0)
    expAll = Item("EXP All", "EXP", 0)
    rareCandy = Item("Rare Candy", "Level", 1)
    xAccuracy = Item("X Accuracy", "Accuracy", 100)
    xAttack = Item("X Attack", "Attack", 50)
    xDefend = Item("X Defend", "Defense", 50)
    guardSpec = Item("Guard Spec.", "Guard Spec.", 0)

def setupMap():
    global palletTown, viridianCity, pewterCity, ceruleanCity, saffronCity, vermilionCity, celadonCity, lavendarCity, fuschiaCity, cinnibarIsland
    global victoryRoad, viridianForest, mountMoon, rockTunnel, powerPlant, radioTower, silphCo, seafoamIslands, tohjoFalls
    global indigoPlateau, mountSilver, diglettCave, billHouse
    global route1, route2, route3, route4, route5, route6, route7, route8, route9, route10, route11, route12, route13, route14, route15, route16, route17, route18, route19, route20, route21, route22, route24, route25, route26, route27, route28

    palletTown = Location("Pallet Town")
    viridianCity = Location("Viridian City")
    pewterCity = Location("Pewter City")
    ceruleanCity = Location("Cerulean City")
    saffronCity = Location("Saffron City")
    vermilionCity = Location("Vermilion City")
    celadonCity = Location("Celandon City")
    lavendarCity = Location("Lavendar City")
    fuschiaCity  = Location("Fuschia City")
    cinnibarIsland = Location("Cinnibar Island")

    victoryRoad = Location("Victory Road")
    viridianForest = Location("Viridian Forest")
    mountMoon = Location("Mount Moon")
    rockTunnel = Location("Rock Tunnel")
    powerPlant = Location("Power Plant")
    radioTower = Location("RadioTower")
    silphCo = Location("Silph Co.")
    seafoamIslands = Location("Seafoam Islands")
    tohjoFalls = Location("Tohjo Falls")

    indigoPlateau = Location("Indigo Plateau")
    mountSilver = Location("Mount Silver")
    diglettCave = Location("Diglett's Cave")
    billHouse = Location("Bill's House")

    route1 = Location("Route 1")
    route2 = Location("Route 2")
    route3 = Location("Route 3")
    route4 = Location("Route 4")
    route5 = Location("Route 5")
    route6 = Location("Route 6")
    route7 = Location("Route 7")
    route8 = Location("Route 8")
    route9 = Location("Route 9")
    route10 = Location("Route 10")
    route11 = Location("Route 11")
    route12 = Location("Route 12")
    route13 = Location("Route 13")
    route14 = Location("Route 14")
    route15 = Location("Route 15")
    route16 = Location("Route 16")
    route17 = Location("Route 17")
    route18 = Location("Route 18")
    route19 = Location("Route 19")
    route20 = Location("Route 20")
    route21 = Location("Route 21")
    route22 = Location("Route 22")
    route24 = Location("Route 24")
    route25 = Location("Route 25")
    route26 = Location("Route 26")
    route27 = Location("Route 27")
    route28 = Location("Route 28")

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
    route18.setTwoWayLocationNeighbour(fuschiaCity, "East")
    fuschiaCity.setTwoWayLocationNeighbour(route19, "South")
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
    route15.setTwoWayLocationNeighbour(fuschiaCity, "West")
    route22.setTwoWayLocationNeighbour(victoryRoad, "West")
    victoryRoad.setTwoWayLocationNeighbour(indigoPlateau, "North")
    victoryRoad.setTwoWayLocationNeighbour(route28, "West")
    route28.setTwoWayLocationNeighbour(mountSilver, "West")
    victoryRoad.setTwoWayLocationNeighbour(route26, "South")
    route26.setTwoWayLocationNeighbour(route27, "South")
    route27.setTwoWayLocationNeighbour(tohjoFalls, "West")

    palletTown.addLocationPokemon([magikarp, poliwag, goldeen, tentacool])
    route1.addLocationPokemon([rattata, pidgey])
    viridianCity.addLocationPokemon([magikarp, poliwag, goldeen, tentacool])
    viridianForest.addLocationPokemon([caterpie, metapod, weedle, kakuna, pikachu])
    route2.addLocationPokemon([caterpie, pidgey, rattata])
    diglettCave.addLocationPokemon([diglett, dugtrio])
    route21.addLocationPokemon([pidgey, pidgeotto, rattata, raticate, tangela, tentacool, magikarp, poliwag, goldeen, shellder, horsea, staryu])
    cinnibarIsland.addLocationPokemon([magikarp, poliwag, goldeen, shellder, horsea, staryu])
    route3.addLocationPokemon([pidgey, spearow, jigglypuff])
    mountMoon.addLocationPokemon([clefairy, zubat, paras, geodude])
    route4.addLocationPokemon([rattata, spearow, ekans, sandshrew, magikarp, poliwag, goldeen, psyduck, krabby])
    ceruleanCity.addLocationPokemon([magikarp, poliwag, goldeen, psyduck, krabby, jynx])
    route24.addLocationPokemon([caterpie, metapod, weedle, kakuna, pidgey, oddish, abra, bellsprout, magikarp, poliwag, goldeen, psyduck, krabby])
    route25.addLocationPokemon([caterpie, metapod, weedle, kakuna, pidgey, oddish, abra, bellsprout, magikarp, poliwag, goldeen, psyduck, krabby])
    route9.addLocationPokemon([rattata, spearow, ekans])
    rockTunnel.addLocationPokemon([zubat, geodude, machop, onix])
    route10.addLocationPokemon([spearow, ekans, sandshrew, voltorb, magikarp, poliwag, goldeen, poliwhirl, slowpoke])
    powerPlant.addLocationPokemon([pikachu, raichu, magnemite, magneton, voltorb, electabuzz, electrode, zapdos])
    radioTower.addLocationPokemon([gastly, haunter, cubone, marowak])
    route5.addLocationPokemon([pidgey, oddish, meowth, mankey, bellsprout])
    silphCo.addLocationPokemon([lapras])
    route8.addLocationPokemon([pidgey, ekans, sandshrew, vulpix, meowth, mankey, growlithe])
    route7.addLocationPokemon([pidgey, vulpix, oddish, meowth, mankey, growlithe, bellsprout])
    celadonCity.addLocationPokemon([magikarp, poliwag, goldeen, poliwhirl, slowpoke])
    route16.addLocationPokemon([rattata, raticate, spearow, doduo, snorlax])
    route17.addLocationPokemon([raticate, spearow, fearow, doduo, magikarp, poliwag, goldeen, tentacool, krabby])
    route18.addLocationPokemon([raticate, spearow, fearow, doduo, magikarp, poliwag, goldeen, tentacool, krabby, lickitung])
    fuschiaCity.addLocationPokemon([magikarp, poliwag, goldeen, krabby, seaking])
    route19.addLocationPokemon([tentacool, magikarp, poliwag, goldeen, shellder, horsea, staryu])
    route20.addLocationPokemon([tentacool, magikarp, poliwag, goldeen, shellder, horsea, staryu])
    seafoamIslands.addLocationPokemon([zubat, golbat, psyduck, golduck, slowpoke, slowbro, seel, shellder, krabby, horsea, staryu])
    route6.addLocationPokemon([pidgey, oddish, meowth, mankey, bellsprout, magikarp, poliwag, goldeen, shellder, krabby])
    vermilionCity.addLocationPokemon([farfetchd, magikarp, poliwag, goldeen, shellder, krabby])
    route11.addLocationPokemon([spearow, ekans, sandshrew, drowzee, magikarp, poliwag, goldeen, shellder, krabby, nidorina])
    route12.addLocationPokemon([pidgey, oddish, gloom, venonat, bellsprout, weepinbell, magikarp, poliwag, goldeen, tentacool, krabby, snorlax])
    route13.addLocationPokemon([pidgey, oddish, gloom, venonat, bellsprout, weepinbell, ditto, magikarp, poliwag, goldeen, tentacool, krabby])
    route14.addLocationPokemon([pidgey, oddish, gloom, venonat, bellsprout, weepinbell, ditto, magikarp, poliwag, goldeen])
    route15.addLocationPokemon([pidgeot, pidgeotto, oddish, gloom, venonat, bellsprout, weepinbell, ditto])
    route22.addLocationPokemon([rattata, spearow, nidoranMale, nidoranFemale, magikarp, poliwag, goldeen])
    victoryRoad.addLocationPokemon([zubat, golbat, machop, machoke, geodude, graveler, onix, marowak, moltres, venomoth])
    indigoPlateau.addLocationPokemon([magikarp, goldeen, poliwag])

def setupTrainers():
    global protagonist

    protagonist = Trainer("Ace", {"Venusaur": venusaur, "Weedle": weedle}, {}, palletTown)

    global botanist
    
    botanist = Trainer("Botanist", {"Charmeleon": charmeleon}, {}, route1)

def setup():
    #Creates types and type advantages for use in battles
    setupTypes()

    #Creates and assigns moves with the corresponding pokemon types for use in battles
    setupMoves()

    #Creates pokemons to be referenced for encounters
    setupPokemon()

    #Creates items to be referenced for encounters
    setupItems()

    #Creates and orders locations
    setupMap()

    #Creates trainers that can be played against, and the player protagonist
    setupTrainers()
    
setup()

while True:
    direction = input("Direction to move: ")
    
    #Wait until user's input is valid
    while direction not in ["North", "South", "East", "West"]:
        direction = input("Direction to move: ")
    else:
        #Check if the player can move in the given direction
        if protagonist.moveToLocation(direction):
            #Check if the player can fight any trainer
            if len(protagonist.getTrainerLivePokemonsDict()) != 0:
                #Roll chance for random encounter
                if randint(1, 100) > 0:
                    availablePokemon = list(protagonist.getTrainerLocation().getLocationPokemonDict().keys())
                    randomPokemon = deepcopy(protagonist.getTrainerLocation().getLocationPokemonDict()[availablePokemon[randint(0, len(availablePokemon) - 1)]])
                    randomEncounter = PokemonEncounter(protagonist, randomPokemon)
                    randomEncounter.startBattle()

                    # #Randomly pick a trainer from those in the current location
                    # trainers = protagonist.getTrainerLocation().getLocationTrainersDict()
                    # del(trainers[protagonist.getTrainerName()])
                    
                    # if len(trainers) != 0:
                    #     opponent = trainers[list(trainers.keys())[randint(0, len(trainers) - 1)]]
                        
                    #     #Check if the opponent has available pokemon to fight
                    #     if opponent.getTrainerActivePokemon() != "":
                    #         #Start battle
                    #         battle = TrainerEncounter(protagonist, opponent)
                    #         battle.startBattle()