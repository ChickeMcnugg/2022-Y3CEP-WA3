from random import randint
from Battle import *
from Pokemon import *
from Trainer import *
from Items import *
from Types import *
from Map import *
from Moves import *

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
    global tackle

    tackle = Moves("Tackle", normalType, "Attack", 40, 100)

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
    
    moves = [tackle]

    for move in moves:
        if move.getMoveType() == normalType:
            normalMoves.append(move)
        elif move.getMoveType() == bugType:
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
        else:
            waterMoves.append(move)

def setupPokemon():
    global bulbasaur, ivysaur, venusaur, charmander, charmeleon, charizard, squirtle, wartortle, blastoise, caterpie, metapod, butterfree, weedle, kakuna, beedrill, pidgey, pidgeotto, pidgeot
    global rattata, raticate, spearow, fearow, ekans, arbok, pikachu, raichu, sandshrew, sandslash, nidoranFemale, nidorina, nidoqueen, nidoranMale, nidorino, nidoking, clefairy, clefable
    global vulpix, ninetales, jigglypuff, wigglytuff, zubat, golbat, oddish, gloom, vileplume, paras, parasect, venonat, venomoth, diglett, dugtrio, meowth, persian, psyduck, golduck, mankey, primeape
    global growlithe, arcanine, poliwag, poliwhirl, poliwrath, abra, kadabra, alakazam, machop, machoke, machamp, bellsprout, weepinbell, victreebel, tentacool, tentacruel, geodude, graveler, golem
    global ponyta, rapidash, slowpoke, slowbro, magnemite, magneton, farfetchd, doduo, dodrio, seel, dewgong, grimer, muk, shellder, cloyster, gastly, haunter, gengar, onix, drowzee, hypno
    global krabby, kingler, voltorb, electrode, exeggcute, exeggutor, cubone, marowak, hitmonlee, hitmonchan, lickitung, koffing, weezing, rhyhorn, rhydon, chansey, tangela, kangaskhan, horsea, seadra
    global goldeen, seaking, staryu, starmie, mrmime, scyther, jynx, electabuzz, magmar, pinsir, tauros, magikarp, gyrados, lapras, ditto, eevee, vaporean, jolteon, flareon, porygon, omanyte, omastar
    global kabuto, kabutops, aerodactyl, snorlax, articuno, zapdos, moltres, dratini, dragonair, dragonite, mewtwo, mew

    bulbasaur = Pokemon("Bulbasaur", grassType, 45, 49, 49, 45, 100, 100)
    ivysaur = Pokemon("Ivysaur", grassType, 60, 62, 63, 60, 100, 100)
    venusaur = Pokemon("Venusaur", grassType, 80, 82, 83, 80, 100, 100)
    charmander = Pokemon("Charmander", fireType, 39, 52, 43, 65, 100, 100)
    charmeleon = Pokemon("Charmeleon", fireType, 58, 64, 58, 80, 100, 100)
    charizard = Pokemon("Charizard", fireType, 78, 84, 78, 100, 100, 100)
    squirtle = Pokemon("Squirtle", waterType, 44, 48, 65, 43, 100, 100)
    wartortle = Pokemon("Wartortle", waterType, 59, 63, 80, 58, 100, 100)
    blastoise = Pokemon("Blastoise", waterType, 79, 83, 100, 78, 100, 100)
    caterpie = Pokemon("Caterpie", bugType, 45, 30, 35, 45, 100, 100)
    metapod = Pokemon("Metapod", bugType, 50, 20, 55, 30, 100, 100)
    butterfree = Pokemon("Butterfree", bugType, 60, 45, 50, 70, 100, 100)
    weedle = Pokemon("Weedle", bugType, 40, 35, 30, 50, 100, 100)
    kakuna = Pokemon("Kakuna", bugType, 65, 25, 50, 35, 100, 100)
    beedrill = Pokemon("Beedrill", bugType, 65, 80, 40, 75, 100, 100)
    pidgey = Pokemon("Pidgey", normalType, 40, 45, 40, 56, 100, 100)
    pidgeotto = Pokemon("Pidgeotto", normalType, 63, 60, 55, 71, 100, 100)
    pidgeot = Pokemon("Pidgeot", normalType, 83, 80, 75, 91, 100, 100)
    rattata = Pokemon("Rattata", normalType, 30, 56, 35, 72, 100, 100)
    raticate = Pokemon("Raticate", normalType, 55, 81, 60, 97, 100, 100)
    spearow = Pokemon("Spearow", normalType, 40, 60, 30, 70, 100, 100)
    fearow = Pokemon("Fearow", normalType, 65, 90, 65, 100, 100, 100)
    ekans = Pokemon("Ekans", poisonType, 35, 60, 44, 55, 100, 100)
    arbok = Pokemon("Arbok", poisonType, 60, 85, 69, 80, 100, 100)
    pikachu = Pokemon("Pikachu", electricType, 35, 55, 30, 90, 100, 100)
    raichu = Pokemon("Raichu", electricType, 60, 90, 55, 100, 100, 100)
    sandshrew = Pokemon("Sandshrew", groundType, 50, 75, 85, 40, 100, 100)
    sandslash = Pokemon("Sandslash", groundType, 75, 100, 110, 65, 100, 100)
    nidoranFemale = Pokemon("Nidoran Female", poisonType, 55, 47, 52, 41, 100, 100)
    nidorina = Pokemon("Nidorina", poisonType, 70, 62, 67, 56, 100, 100)
    nidoqueen = Pokemon("Nidoqueen", poisonType, 90, 82, 87, 76, 100, 100)
    nidoranMale = Pokemon("Nidoran Male", poisonType, 46, 57, 40, 50, 100, 100)
    nidorino = Pokemon("Nidorino", poisonType, 61, 72, 57, 65, 100, 100)
    nidoking = Pokemon("Nidoking", poisonType, 81, 92, 77, 85, 100, 100)
    clefairy = Pokemon("Clefairy", normalType, 70, 45, 48, 35, 100, 100)
    clefable = Pokemon("Clefable", normalType, 95, 70, 73, 60, 100, 100)
    vulpix = Pokemon("Vulpix", fireType, 38, 41, 40, 65, 100, 100)
    ninetales = Pokemon("Ninetales", fireType, 73, 76, 75, 100, 100, 100)
    jigglypuff = Pokemon("Jigglypuff", normalType, 115, 45, 20, 20, 100, 100)
    wigglytuff = Pokemon("Wigglytuff", normalType, 140, 70, 45, 45, 100, 100)
    zubat = Pokemon("Zubat", poisonType, 40, 45, 35, 55, 100, 100)
    golbat = Pokemon("Golbat", poisonType, 75, 80, 70, 90, 100, 100)
    oddish = Pokemon("Oddish", grassType, 45, 50, 55, 30, 100, 100)
    gloom = Pokemon("Gloom", grassType, 60, 65, 70, 40, 100, 100)
    vileplume = Pokemon("Vileplume", grassType, 75, 80, 85, 50, 100, 100)
    paras = Pokemon("Paras", bugType, 35, 70, 55, 25, 100, 100)
    parasect = Pokemon("Parasect", bugType, 60, 55, 50, 45, 100, 100)
    venonat = Pokemon("Venonat", bugType, 70, 65, 60, 90, 100, 100)
    venomoth = Pokemon("Venomoth", bugType, 10, 55, 25, 95, 100, 100)
    diglett = Pokemon("Diglett", groundType, 35, 80, 50, 120, 100, 100)
    dugtrio = Pokemon("Dugtrio", groundType, 40, 45, 35, 90, 100, 100)
    meowth = Pokemon("Meowth", normalType, 65, 70, 60, 115, 100, 100)
    persian = Pokemon("Persian", normalType, 50, 52, 48, 55, 100, 100)
    psyduck = Pokemon("Psyduck", waterType, 80, 82, 78, 85, 100, 100)
    golduck = Pokemon("Golduck", waterType, 40, 80, 35, 70, 100, 100)
    mankey = Pokemon("Mankey", fightingType, 65, 105, 60, 95, 100, 100)
    primeape = Pokemon("Primape", fightingType, 55, 70, 45, 60, 100, 100)
    growlithe = Pokemon("Growlithe", fireType, 90, 110, 80, 95, 100, 100)
    arcanine = Pokemon("Arcanine", fireType, 40, 50, 40, 90, 100, 100)
    poliwag = Pokemon("Poliwag", waterType, 65, 65, 65, 90, 100, 100)
    poliwhirl = Pokemon("Poliwhirl", waterType, 90, 85, 95, 70, 100, 100)
    poliwrath = Pokemon("Poliwrath", waterType, 25, 20, 15, 90, 100, 100)
    abra = Pokemon("Abra", psychicType, 40, 35, 30, 105, 100, 100)
    kadabra = Pokemon("Kadabra", psychicType, 55, 50, 45, 120, 100, 100)
    alakazam = Pokemon("Alakazam", psychicType, 70, 80, 50, 35, 100, 100)
    machop = Pokemon("Machop", fightingType, 80, 100, 70, 45, 100, 100)
    machoke = Pokemon("Machoke", fightingType, 90, 130, 80, 55, 100, 100)
    machamp = Pokemon("Machamp", fightingType, 50, 75, 35, 40, 100, 100)
    bellsprout = Pokemon("Bellsprout", grassType, 65, 90, 50, 55, 100, 100)
    weepinbell = Pokemon("Weepinbell", grassType, 80, 105, 65, 70, 100, 100)
    victreebel = Pokemon("Victreebel", grassType, 40, 40, 35, 70, 100, 100)
    tentacool = Pokemon("Tentacool", waterType, 80, 105, 65, 100, 100, 100)
    tentacruel = Pokemon("Tentacruel", waterType, 40, 80, 100, 20, 100, 100)
    geodude = Pokemon("Geodude", rockType, 55, 95, 115, 35, 100, 100)
    graveler = Pokemon("Graveler", rockType, 80, 110, 130, 45, 100, 100)
    golem = Pokemon("Golem", rockType, 50, 85, 55, 90, 100, 100)
    ponyta = Pokemon("Ponyta", fireType, 65, 100, 70, 105, 100, 100)
    rapidash = Pokemon("Rapidash", fireType, 90, 65, 65, 15, 100, 100)
    slowpoke = Pokemon("Slowpoke", waterType, 95, 49, 49, 45, 100, 100)
    slowbro = Pokemon("Slowbro", waterType, 25, 35, 70, 45, 100, 100)
    magnemite = Pokemon("Magnemite", electricType, 50, 60, 95, 70, 100, 100)
    magneton = Pokemon("Magneton", electricType, 52, 65, 55, 60, 100, 100)
    farfetchd = Pokemon("Farfetch'd", normalType, 35, 85, 45, 75, 100, 100)
    doduo = Pokemon("Duduo", normalType, 60, 110, 70, 100, 100, 100)
    dodrio = Pokemon("Dudrio", normalType, 65, 45, 55, 45, 100, 100)
    seel = Pokemon("Seel", waterType, 90, 70, 80, 70, 100, 100)
    dewgong = Pokemon("Dewgong", waterType, 80, 80, 50, 25, 100, 100)
    grimer = Pokemon("Grimer", poisonType, 105, 105, 75, 50, 100, 100)
    muk = Pokemon("Muk", poisonType, 30, 65, 100, 40, 100, 100)
    shellder = Pokemon("Shellder", waterType, 50, 95, 180, 70, 100, 100)
    cloyster = Pokemon("Cloyster", waterType, 30, 35, 30, 80, 100, 100)
    gastly = Pokemon("Gastly", ghostType, 30, 35, 30, 80, 100, 100)
    haunter = Pokemon("Haunter", ghostType, 45, 50, 45, 95, 100, 100)
    gengar = Pokemon("Gengar", ghostType, 60, 65, 60, 110, 100, 100)
    onix = Pokemon("Onix", rockType, 35, 45, 160, 70, 100, 100)
    drowzee = Pokemon("Drowzee", psychicType, 60, 48, 45, 42, 100, 100)
    hypno = Pokemon("Hypno", psychicType, 85, 73, 70, 67, 100, 100)
    krabby = Pokemon("Krabby", waterType, 30, 105, 90, 50, 100, 100)
    kingler = Pokemon("Kingler", waterType, 55, 130, 115, 75, 100, 100)
    voltorb = Pokemon("Voltorb", electricType, 40, 30, 50, 100, 100, 100)
    electrode = Pokemon("Electrode", electricType, 60, 50, 70, 140, 100, 100)
    exeggcute = Pokemon("Exeggcute", grassType, 60, 40, 80, 40, 100, 100)
    exeggutor = Pokemon("Exeggutor", grassType, 95, 95, 85, 55, 100, 100)
    cubone = Pokemon("Cubone", groundType, 50, 50, 95, 35, 100, 100)
    marowak = Pokemon("Marowak", groundType, 60, 80, 110, 45, 100, 100)
    hitmonlee = Pokemon("Hitmonlee", fightingType, 50, 120, 53, 87, 100, 100)
    hitmonchan = Pokemon("Hitmonchan", fightingType, 50, 105, 79, 76, 100, 100)
    lickitung = Pokemon("Lickitung", normalType, 90, 55, 75, 30, 100, 100)
    koffing = Pokemon("Koffing", poisonType, 40, 65, 95, 35, 100, 100)
    weezing = Pokemon("Weezing", poisonType, 65, 90, 120, 60, 100, 100)
    rhyhorn = Pokemon("Rhyhorn", groundType, 80, 85, 95, 25, 100, 100)
    rhydon = Pokemon("Rhydon", groundType, 105, 130, 120, 40, 100, 100)
    chansey = Pokemon("Chansey", normalType, 250, 5, 5, 50, 100, 100)
    tangela = Pokemon("Tangela", grassType, 65, 55, 115, 60, 100, 100)
    kangaskhan = Pokemon("Kangaskhan", groundType, 105, 95, 80, 90, 100, 100)
    horsea = Pokemon("Horsea", waterType, 30, 40, 70, 60, 100, 100)
    seadra = Pokemon("Seadra", waterType, 55, 65, 95, 85, 100, 100)
    goldeen = Pokemon("Goldeen", waterType, 45, 67, 60, 63, 100, 100)
    seaking = Pokemon("Seaking", waterType, 80, 92, 65, 68, 100, 100)
    staryu = Pokemon("Staryu", waterType, 30, 45, 55, 85, 100, 100)
    starmie = Pokemon("Starmie", waterType, 60, 75, 85, 115, 100, 100)
    mrmime = Pokemon("Mr Mime", psychicType, 40, 45, 65, 90, 100, 100)
    scyther = Pokemon("Scyther", bugType, 70, 110, 80, 105, 100, 100)
    jynx = Pokemon("Jynx", iceType, 65, 50, 35, 95, 100, 100)
    electabuzz = Pokemon("Electabuzz", electricType, 65, 50, 35, 95, 100, 100)
    magmar = Pokemon("Magmar", fireType, 65, 83, 57, 105, 100, 100)
    pinsir = Pokemon("Pinsir", bugType, 65, 95, 57, 93, 100, 100)
    tauros = Pokemon("Tauros", normalType, 75, 100, 95, 110, 100, 100)
    magikarp = Pokemon("Magikarp", waterType, 20, 10, 55, 80, 100, 100)
    gyrados = Pokemon("Gyrados", waterType, 95, 125, 79, 81, 100, 100)
    lapras = Pokemon("Lapras", waterType, 130, 85, 80, 60, 100, 100)
    ditto = Pokemon("Ditto", normalType, 48, 48, 48, 48, 100, 100)
    eevee = Pokemon("Eevee", normalType, 55, 55, 50, 55, 100, 100)
    vaporean = Pokemon("Vaporean", waterType, 130, 65, 60, 65, 100, 100)
    jolteon = Pokemon("Jolteon", electricType, 65, 65, 65, 130, 100, 100)
    flareon = Pokemon("Flareon", fireType, 65, 130, 65, 65, 100, 100)
    porygon = Pokemon("Porygon", normalType, 65, 60, 70, 40, 100, 100)
    omanyte = Pokemon("Omanyte", rockType, 35, 40, 100, 35, 100, 100)
    omastar = Pokemon("Omastar", rockType, 70, 60, 125, 55, 100, 100)
    kabuto = Pokemon("Kabuto", rockType, 30, 80, 90, 55, 100, 100)
    kabutops = Pokemon("Kabutops", rockType, 60, 115, 105, 80, 100, 100)
    aerodactyl = Pokemon("Aerodactyl", rockType, 80, 105, 65, 30, 100, 100)
    snorlax = Pokemon("Snorlax", normalType, 160, 110, 65, 30, 100, 100)
    articuno = Pokemon("Articuno", iceType, 90, 85, 100, 85, 100, 100)
    zapdos = Pokemon("Zapdos", electricType, 90, 90, 85, 100, 100, 100)
    moltres = Pokemon("Moltres", fireType, 90, 100, 90, 90, 100, 100)
    dratini = Pokemon("Dratini", dragonType, 41, 64, 45, 50, 100, 100)
    dragonair = Pokemon("Dragonair", dragonType, 61, 84, 65, 70, 100, 100)
    dragonite = Pokemon("Dragonite", dragonType, 91, 134, 95, 80, 100, 100)
    mewtwo = Pokemon("Mewtwo", psychicType, 106, 110, 90, 130, 100, 100)
    mew = Pokemon("Mew", psychicType, 100, 100, 100, 100, 100, 100)

    pokemons = [bulbasaur, ivysaur, venusaur, charmander, charmeleon, charizard, squirtle, wartortle, blastoise, caterpie, metapod, butterfree, weedle, kakuna, beedrill, pidgey, pidgeotto, pidgeot, rattata, raticate, spearow, fearow, ekans, arbok, pikachu, raichu, sandshrew, sandslash, nidoranFemale, nidorina, nidoqueen, nidoranMale, nidorino, nidoking, clefairy, clefable, vulpix, ninetales, jigglypuff, wigglytuff, zubat, golbat, oddish, gloom, vileplume, paras, parasect, venonat, venomoth, diglett, dugtrio, meowth, persian, psyduck, golduck, mankey, primeape, growlithe, arcanine, poliwag, poliwhirl, poliwrath, abra, kadabra, alakazam, machop, machoke, machamp, bellsprout, weepinbell, victreebel, tentacool, tentacruel, geodude, graveler, golem, ponyta, rapidash, slowpoke, slowbro, magnemite, magneton, farfetchd, doduo, dodrio, seel, dewgong, grimer, muk, shellder, cloyster, gastly, haunter, gengar, onix, drowzee, hypno, krabby, kingler, voltorb, electrode, exeggcute, exeggutor, cubone, marowak, hitmonlee, hitmonchan, lickitung, koffing, weezing, rhyhorn, rhydon, chansey, tangela, kangaskhan, horsea, seadra, goldeen, seaking, staryu, starmie, mrmime, scyther, jynx, electabuzz, magmar, pinsir, tauros, magikarp, gyrados, lapras, ditto, eevee, vaporean, jolteon, flareon, porygon, omanyte, omastar, kabuto, kabutops, aerodactyl, snorlax, articuno, zapdos, moltres, dratini, dragonair, dragonite, mewtwo, mew]

    for pokemon in pokemons:
        if pokemon.getPokemonType() == normalType:
            for move in normalMoves:
                pokemon.addMove(move)

def setupTrainers():
    global protagonist

    protagonist = Trainer("Ace", [snorlax, ivysaur], [])
    protagonist.placeInLocation(palletTown)

    global botanist
    
    botanist = Trainer("Botanist", [bulbasaur, venusaur], [])
    botanist.placeInLocation(route1)


def setup():
    setupMap()
    setupTypes()
    setupMoves()
    setupPokemon()
    setupTrainers()
    
setup()

while True:
    direction = input("Direction to move: ")
    while direction not in ["North", "South", "East", "West"]:
        direction = input("Direction to move: ")
    else:
        protagonist.moveToLocation(direction)

        if randint(1, 100) > 0:
            trainers = protagonist.getTrainerLocation().getLocationTrainersList()
            trainers.remove(protagonist)
            
            if len(trainers) != 0:
                opponent = trainers[randint(0, len(trainers) - 1)]
                Battle.startBattle(protagonist, opponent)