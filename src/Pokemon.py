class Pokemon:
    def __init__(self, pokemonName, pokemonType, pokemonLevel, pokemonMaxHealth, pokemonAttack, pokemonDefense, pokemonSpeed, pokemonEvasion, pokemonAccuracy, pokemonMovesList):
        self.pokemonName = pokemonName
        self.pokemonType = pokemonType
        self.pokemonLevel = pokemonLevel
        self.pokemonMaxHealth = pokemonMaxHealth
        self.pokemonHealth = pokemonMaxHealth
        self.pokemonEXP = 0
        self.pokemonAttack = pokemonAttack
        self.pokemonDefense = pokemonDefense
        self.pokemonSpeed = pokemonSpeed
        self.pokemonEvasion = pokemonEvasion
        self.pokemonAccuracy = pokemonAccuracy
        self.pokemonMovesList = pokemonMovesList
    
    def __repr__(self):
        return "This is a " + self.pokemonType + ", Level " + str(self.pokemonLevel) + " " + self.pokemonName + "."
    
    def getPokemonName(self):
        return self.pokemonName
    
    def getPokemonType(self):
        return self.pokemonType
    
    def getPokemonLevel(self):
        return self.pokemonLevel
    
    def getPokemonHealth(self):
        return self.pokemonHealth
    
    def getPokemonAttack(self):
        return self.pokemonAttack
    
    def getPokemonDefense(self):
        return self.pokemonDefense
    
    def getPokemonSpeed(self):
        return self.pokemonSpeed
    
    def getPokemonEvasion(self):
        return self.pokemonEvasion
    
    def getPokemonAccuracy(self):
        return self.pokemonAccuracy
    
    def getPokemonEXP(self):
        return self.pokemonEXP

    def setup():
        bulbasaur = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        ivysaur = Pokemon("Ivysaur", grassType, 5, 60, 62, 63, 60, 1, 1)
        venusaur = Pokemon("Venusaur", grassType, 5, 80, 82, 83, 80, 1, 1)
        charmander = Pokemon("Charmander", grassType, 5, 39, 52, 43, 65, 1, 1)
        charmeleon = Pokemon("Charmeleon", grassType, 5, 58, 64, 58, 80, 1, 1)
        charizard = Pokemon("Charizard", grassType, 5, 78, 84, 78, 100, 1, 1)
        squirtle = Pokemon("Squirtle", grassType, 5, 44, 48, 65, 43, 1, 1)
        wartortle = Pokemon("Wartortle", grassType, 5, 59, 63, 80, 58, 1, 1)
        blastoise = Pokemon("Blastoise", grassType, 5, 79, 83, 100, 78, 1, 1)
        caterpie = Pokemon("Caterpie", grassType, 5, 45, 30, 35, 45, 1, 1)
        metapod = Pokemon("Metapod", grassType, 5, 50, 20, 55, 30, 1, 1)
        butterfree = Pokemon("Butterfree", grassType, 5, 60, 45, 50, 70, 1, 1)
        weedle = Pokemon("Weedle", grassType, 5, 40, 35, 30, 50, 1, 1)
        kakuna = Pokemon("Kakuna", grassType, 5, 65, 25, 50, 35, 1, 1)
        beedrill = Pokemon("Beedrill", grassType, 5, 65, 80, 40, 75, 1, 1)
        pidgey = Pokemon("Pidgey", grassType, 5, 40, 45, 40, 56, 1, 1)
        pigeotto = Pokemon("Pidgeotto", grassType, 5, 63, 60, 55, 71, 1, 1)
        pidgeot = Pokemon("Pidgeot", grassType, 5, 83, 80, 75, 91, 1, 1)
        rattata = Pokemon("Rattata", grassType, 5, 30, 56, 35, 72, 1, 1)
        raticate = Pokemon("Raticate", grassType, 5, 55, 81, 60, 97, 1, 1)
        spearow = Pokemon("Spearow", grassType, 5, 40, 60, 30, 70, 1, 1)
        fearow = Pokemon("Fearow", grassType, 5, 65, 90, 65, 100, 1, 1)
        ekans = Pokemon("Ekans", grassType, 5, 35, 60, 44, 55, 1, 1)
        arbok = Pokemon("Arbok", grassType, 5, 60, 85, 69, 80, 1, 1)
        pikachu = Pokemon("Pikachu", grassType, 5, 35, 55, 30, 90, 1, 1)
        raichu = Pokemon("Raichu", grassType, 5, 60, 90, 55, 100, 1, 1)
        sandshrew = Pokemon("Sandshrew", grassType, 5, 50, 75, 85, 40, 1, 1)
        sandslash = Pokemon("Sandslash", grassType, 5, 75, 100, 110, 65, 1, 1)
        nidoranFemale = Pokemon("Nidoran Female", grassType, 5, 55, 47, 52, 41, 1, 1)
        nidorina = Pokemon("Nidorina", grassType, 5, 70, 62, 67, 56, 1, 1)
        nidoqueen = Pokemon("Nidoqueen", grassType, 5, 90, 82, 87, 76, 1, 1)
        nidoranMale = Pokemon("Nidoran Male", grassType, 5, 46, 57, 40, 50, 1, 1)
        nidorino = Pokemon("Nidorino", grassType, 5, 61, 72, 57, 65, 1, 1)
        nidoking = Pokemon("Nidoking", grassType, 5, 81, 92, 77, 85, 1, 1)
        clefairy = Pokemon("Clefairy", grassType, 5, 70, 45, 48, 35, 1, 1)
        clefable = Pokemon("Clefable", grassType, 5, 95, 70, 73, 60, 1, 1)
        vulpix = Pokemon("Vulpix", grassType, 5, 38, 41, 40, 65, 1, 1)
        ninetales = Pokemon("Ninetales", grassType, 5, 73, 76, 75, 100, 1, 1)
        jigglypuff = Pokemon("Jigglypuff", grassType, 5, 115, 45, 20, 20, 1, 1)
        wigglytuff = Pokemon("Wigglytuff", grassType, 5, 140, 70, 45, 45, 1, 1)
        zubat = Pokemon("Zubat", grassType, 5, 40, 45, 35, 55, 1, 1)
        golbat = Pokemon("Golbat", grassType, 5, 75, 80, 70, 90, 1, 1)
        oddish = Pokemon("Oddish", grassType, 5, 45, 50, 55, 30, 1, 1)
        gloom = Pokemon("Gloom", grassType, 5, 60, 65, 70, 40, 1, 1)
        vileplume = Pokemon("Vileplume", grassType, 5, 75, 80, 85, 50, 1, 1)
        paras = Pokemon("Paras", grassType, 5, 35, 70, 55, 25, 1, 1)
        parasect = Pokemon("Parasect", grassType, 5, 60, 55, 50, 45, 1, 1)
        venonat = Pokemon("Venonat", grassType, 5, 70, 65, 60, 90, 1, 1)
        venomoth = Pokemon("Venomoth", grassType, 5, 10, 55, 25, 95, 1, 1)
        diglett = Pokemon("Diglett", grassType, 5, 35, 80, 50, 120, 1, 1)
        dugtrio = Pokemon("Dugtrio", grassType, 5, 40, 45, 35, 90, 1, 1)
        meowth = Pokemon("Meowth", grassType, 5, 65, 70, 60, 115, 1, 1)
        persian = Pokemon("Persian", grassType, 5, 50, 52, 48, 55, 1, 1)
        psyduck = Pokemon("Psyduck", grassType, 5, 80, 82, 78, 85, 1, 1)
        golduck = Pokemon("Golduck", grassType, 5, 40, 80, 35, 70, 1, 1)
        mankey = Pokemon("Mankey", grassType, 5, 65, 105, 60, 95, 1, 1)
        primeape = Pokemon("Primape", grassType, 5, 55, 70, 45, 60, 1, 1)
        growlithe = Pokemon("Growlithe", grassType, 5, 90, 110, 80, 95, 1, 1)
        arcanine = Pokemon("Arcanine", grassType, 5, 40, 50, 40, 90, 1, 1)
        poliwag = Pokemon("Poliwag", grassType, 5, 65, 65, 65, 90, 1, 1)
        poliwhirl = Pokemon("Poliwhirl", grassType, 5, 90, 85, 95, 70, 1, 1)
        poliwrath = Pokemon("Poliwrath", grassType, 5, 25, 20, 15, 90, 1, 1)
        abra = Pokemon("Abra", grassType, 5, 40, 35, 30, 105, 1, 1)
        kadabra = Pokemon("Kadabra", grassType, 5, 55, 50, 45, 120, 1, 1)
        alakazam = Pokemon("Alakazam", grassType, 5, 70, 80, 50, 35, 1, 1)
        machop = Pokemon("Machop", grassType, 5, 80, 100, 70, 45, 1, 1)
        machoke = Pokemon("Machoke", grassType, 5, 90, 130, 80, 55, 1, 1)
        machamp = Pokemon("Machamp", grassType, 5, 50, 75, 35, 40, 1, 1)
        bellsprout = Pokemon("Bellsprout", grassType, 5, 65, 90, 50, 55, 1, 1)
        weepinbell = Pokemon("Weepinbell", grassType, 5, 80, 105, 65, 70, 1, 1)
        victreebel = Pokemon("Victreebel", grassType, 5, 40, 40, 35, 70, 1, 1)
        tentacool = Pokemon("Tentacool", grassType, 5, 80, 105, 65, 100, 1, 1)
        tentacruel = Pokemon("Tentacruel", grassType, 5, 40, 80, 100, 20, 1, 1)
        geodude = Pokemon("Geodude", grassType, 5, 55, 95, 115, 35, 1, 1)
        graveler = Pokemon("Graveler", grassType, 5, 80, 110, 130, 45, 1, 1)
        golem = Pokemon("Golem", grassType, 5, 50, 85, 55, 90, 1, 1)
        ponyta = Pokemon("Ponyta", grassType, 5, 65, 100, 70, 105, 1, 1)
        rapidash = Pokemon("Rapidash", grassType, 5, 90, 65, 65, 15, 1, 1)
        slowpoke = Pokemon("Slowpoke", grassType, 5, 95, 49, 49, 45, 1, 1)
        slowbro = Pokemon("Slowbro", grassType, 5, 25, 35, 70, 45, 1, 1)
        magnemite = Pokemon("Magnemite", grassType, 5, 50, 60, 95, 70, 1, 1)
        magneton = Pokemon("Magneton", grassType, 5, 52, 65, 55, 60, 1, 1)
        farfetchd = Pokemon("Farfetch'd", grassType, 5, 35, 85, 45, 75, 1, 1)
        doduo = Pokemon("Duduo", grassType, 5, 60, 110, 70, 100, 1, 1)
        dodrio = Pokemon("Dudrio", grassType, 5, 65, 45, 55, 45, 1, 1)
        seel = Pokemon("Seel", grassType, 5, 90, 70, 80, 70, 1, 1)
        dewgong = Pokemon("Dewgong", grassType, 5, 80, 80, 50, 25, 1, 1)
        grimer = Pokemon("Grimer", grassType, 5, 105, 105, 75, 50, 1, 1)
        muk = Pokemon("Muk", grassType, 5, 30, 65, 100, 40, 1, 1)
        shellder = Pokemon("Shellder", grassType, 5, 50, 95, 180, 70, 1, 1)
        cloyster = Pokemon("Cloyster", grassType, 5, 30, 35, 30, 80, 1, 1)

        
        gastly = Pokemon("Gastly", grassType, 5, 45, 49, 49, 45, 1, 1)
        haunter = Pokemon("Haunter", grassType, 5, 45, 49, 49, 45, 1, 1)
        gengar = Pokemon("Gengar", grassType, 5, 45, 49, 49, 45, 1, 1)
        onix = Pokemon("Onix", grassType, 5, 45, 49, 49, 45, 1, 1)
        drowzee = Pokemon("Drowzee", grassType, 5, 45, 49, 49, 45, 1, 1)
        hypno = Pokemon("Hypno", grassType, 5, 45, 49, 49, 45, 1, 1)
        krabby = Pokemon("Krabby", grassType, 5, 45, 49, 49, 45, 1, 1)
        kingler = Pokemon("Kingler", grassType, 5, 45, 49, 49, 45, 1, 1)
        voltorb = Pokemon("Voltorb", grassType, 5, 45, 49, 49, 45, 1, 1)
        electrode = Pokemon("Electrode", grassType, 5, 45, 49, 49, 45, 1, 1)
        exeggcute = Pokemon("Exeggcute", grassType, 5, 45, 49, 49, 45, 1, 1)
        exeggutor = Pokemon("Exeggutor", grassType, 5, 45, 49, 49, 45, 1, 1)
        cubone = Pokemon("Cubone", grassType, 5, 45, 49, 49, 45, 1, 1)
        marowak = Pokemon("Marowak", grassType, 5, 45, 49, 49, 45, 1, 1)
        hitmonlee = Pokemon("Hitmonlee", grassType, 5, 45, 49, 49, 45, 1, 1)
        hitmonchan = Pokemon("Hitmonchan", grassType, 5, 45, 49, 49, 45, 1, 1)
        lickitung = Pokemon("Lickitung", grassType, 5, 45, 49, 49, 45, 1, 1)
        koffing = Pokemon("Koffing", grassType, 5, 45, 49, 49, 45, 1, 1)
        weezing = Pokemon("Weezing", grassType, 5, 45, 49, 49, 45, 1, 1)
        rhyhorn = Pokemon("Rhyhorn", grassType, 5, 45, 49, 49, 45, 1, 1)
        rhydon = Pokemon("Rhydon", grassType, 5, 45, 49, 49, 45, 1, 1)
        chansey = Pokemon("Chansey", grassType, 5, 45, 49, 49, 45, 1, 1)
        tangela = Pokemon("Tangela", grassType, 5, 45, 49, 49, 45, 1, 1)
        kangaskhan = Pokemon("Kangaskhan", grassType, 5, 45, 49, 49, 45, 1, 1)
        horsea = Pokemon("Horsea", grassType, 5, 45, 49, 49, 45, 1, 1)
        seadra = Pokemon("Seadra", grassType, 5, 45, 49, 49, 45, 1, 1)
        goldeen = Pokemon("Goldeen", grassType, 5, 45, 49, 49, 45, 1, 1)
        seaking = Pokemon("Seaking", grassType, 5, 45, 49, 49, 45, 1, 1)
        staryu = Pokemon("Staryu", grassType, 5, 45, 49, 49, 45, 1, 1)
        starmie = Pokemon("Starmie", grassType, 5, 45, 49, 49, 45, 1, 1)
        mrmime = Pokemon("Mr Mime", grassType, 5, 45, 49, 49, 45, 1, 1)
        scyther = Pokemon("Scyther", grassType, 5, 45, 49, 49, 45, 1, 1)
        jynx = Pokemon("Jynx", grassType, 5, 45, 49, 49, 45, 1, 1)
        electabuzz = Pokemon("Electabuzz", grassType, 5, 45, 49, 49, 45, 1, 1)
        magmar = Pokemon("Magmar", grassType, 5, 45, 49, 49, 45, 1, 1)
        pinsir = Pokemon("Pinsir", grassType, 5, 45, 49, 49, 45, 1, 1)
        tauros = Pokemon("Tauros", grassType, 5, 45, 49, 49, 45, 1, 1)
        magikarp = Pokemon("Magikarp", grassType, 5, 45, 49, 49, 45, 1, 1)
        gyrados = Pokemon("Gyrados", grassType, 5, 45, 49, 49, 45, 1, 1)
        lapras = Pokemon("Lapras", grassType, 5, 45, 49, 49, 45, 1, 1)
        ditto = Pokemon("Ditto", grassType, 5, 45, 49, 49, 45, 1, 1)
        eevee = Pokemon("Eevee", grassType, 5, 45, 49, 49, 45, 1, 1)
        vaporean = Pokemon("Vaporean", grassType, 5, 45, 49, 49, 45, 1, 1)
        jolteon = Pokemon("Jolteon", grassType, 5, 45, 49, 49, 45, 1, 1)
        flareon = Pokemon("Flareon", grassType, 5, 45, 49, 49, 45, 1, 1)
        porygon = Pokemon("Porygon", grassType, 5, 45, 49, 49, 45, 1, 1)
        omanyte = Pokemon("Omanyte", grassType, 5, 45, 49, 49, 45, 1, 1)
        omastar = Pokemon("Omastar", grassType, 5, 45, 49, 49, 45, 1, 1)
        kabuto = Pokemon("Kabuto", grassType, 5, 45, 49, 49, 45, 1, 1)
        kabutops = Pokemon("Kabutops", grassType, 5, 45, 49, 49, 45, 1, 1)
        aerodactyl = Pokemon("Aerodactyl", grassType, 5, 45, 49, 49, 45, 1, 1)
        snorlax = Pokemon("Snorlax", grassType, 5, 45, 49, 49, 45, 1, 1)
        articuno = Pokemon("Articuno", grassType, 5, 45, 49, 49, 45, 1, 1)
        zapdos = Pokemon("Zapdos", grassType, 5, 45, 49, 49, 45, 1, 1)
        moltres = Pokemon("Moltres", grassType, 5, 45, 49, 49, 45, 1, 1)
        dratini = Pokemon("Dratini", grassType, 5, 45, 49, 49, 45, 1, 1)
        dragonair = Pokemon("Dragonair", grassType, 5, 45, 49, 49, 45, 1, 1)
        dragonite = Pokemon("Dragonite", grassType, 5, 45, 49, 49, 45, 1, 1)
        mewtwo = Pokemon("Mewtwo", grassType, 5, 45, 49, 49, 45, 1, 1)
        mew = Pokemon("Mew", grassType, 5, 45, 49, 49, 45, 1, 1)