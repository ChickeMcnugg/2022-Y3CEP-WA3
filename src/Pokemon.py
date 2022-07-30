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
        ivysaur = Pokemon("Ivysaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        venusaur = Pokemon("Venusaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        charmander = Pokemon("Charmander", grassType, 5, 45, 49, 49, 45, 1, 1)
        charmeleon = Pokemon("Charmeleon", grassType, 5, 45, 49, 49, 45, 1, 1)
        charizard = Pokemon("Charizard", grassType, 5, 45, 49, 49, 45, 1, 1)
        squirtle = Pokemon("Squirtle", grassType, 5, 45, 49, 49, 45, 1, 1)
        wartortle = Pokemon("Wartortle", grassType, 5, 45, 49, 49, 45, 1, 1)
        blastoise = Pokemon("Blastoise", grassType, 5, 45, 49, 49, 45, 1, 1)
        caterpie = Pokemon("Caterpie", grassType, 5, 45, 49, 49, 45, 1, 1)
        metapod = Pokemon("Metapod", grassType, 5, 45, 49, 49, 45, 1, 1)
        butterfree = Pokemon("Butterfree", grassType, 5, 45, 49, 49, 45, 1, 1)
        weedle = Pokemon("Weedle", grassType, 5, 45, 49, 49, 45, 1, 1)
        kakuna = Pokemon("Kakuna", grassType, 5, 45, 49, 49, 45, 1, 1)
        beedrill = Pokemon("Beedrill", grassType, 5, 45, 49, 49, 45, 1, 1)
        pidgey = Pokemon("Pidgey", grassType, 5, 45, 49, 49, 45, 1, 1)
        pigeotto = Pokemon("Pidgeotto", grassType, 5, 45, 49, 49, 45, 1, 1)
        pidgeot = Pokemon("Pidgeot", grassType, 5, 45, 49, 49, 45, 1, 1)
        rattata = Pokemon("Rattata", grassType, 5, 45, 49, 49, 45, 1, 1)
        raticate = Pokemon("Raticate", grassType, 5, 45, 49, 49, 45, 1, 1)
        spearow = Pokemon("Spearow", grassType, 5, 45, 49, 49, 45, 1, 1)
        fearow = Pokemon("Fearow", grassType, 5, 45, 49, 49, 45, 1, 1)
        ekans = Pokemon("Ekans", grassType, 5, 45, 49, 49, 45, 1, 1)
        arbok = Pokemon("Arbok", grassType, 5, 45, 49, 49, 45, 1, 1)
        pikachu = Pokemon("Pikachu", grassType, 5, 45, 49, 49, 45, 1, 1)
        raichu = Pokemon("Raichu", grassType, 5, 45, 49, 49, 45, 1, 1)
        sandshrew = Pokemon("Sandshrew", grassType, 5, 45, 49, 49, 45, 1, 1)
        sandslash = Pokemon("Sandslash", grassType, 5, 45, 49, 49, 45, 1, 1)
        nidoranFemale = Pokemon("Nidoran Female", grassType, 5, 45, 49, 49, 45, 1, 1)
        nidorina = Pokemon("Nidorina", grassType, 5, 45, 49, 49, 45, 1, 1)
        nidoqueen = Pokemon("Nidoqueen", grassType, 5, 45, 49, 49, 45, 1, 1)
        nidoranMale = Pokemon("Nidoran Male", grassType, 5, 45, 49, 49, 45, 1, 1)
        nidorino = Pokemon("Nidorino", grassType, 5, 45, 49, 49, 45, 1, 1)
        nidoking = Pokemon("Nidoking", grassType, 5, 45, 49, 49, 45, 1, 1)
        clefairy = Pokemon("Clefairy", grassType, 5, 45, 49, 49, 45, 1, 1)
        clefable = Pokemon("Clefable", grassType, 5, 45, 49, 49, 45, 1, 1)
        vulpix = Pokemon("Vulpix", grassType, 5, 45, 49, 49, 45, 1, 1)
        ninetales = Pokemon("Ninetales", grassType, 5, 45, 49, 49, 45, 1, 1)
        jigglypuff = Pokemon("Jigglypuff", grassType, 5, 45, 49, 49, 45, 1, 1)
        wigglytuff = Pokemon("Wigglytuff", grassType, 5, 45, 49, 49, 45, 1, 1)
        zubat = Pokemon("Zubat", grassType, 5, 45, 49, 49, 45, 1, 1)
        golbat = Pokemon("Golbat", grassType, 5, 45, 49, 49, 45, 1, 1)
        oddish = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        gloom = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        vileplume = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        paras = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        parasect = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        venonat = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        venomoth = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        diglett = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        dugtrio = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        meowth = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        persian = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        psyduck = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        golduck = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        mankey = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        primeape = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        growlithe = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        arcanine = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        poliwag = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        poliwhirl = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        poliwrath = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        abra = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        kadabra = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        alakazam = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        machop = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        machoke = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        machamp = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        bellsprout = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        weepinbell = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        victreebel = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        tentacool = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        tentacruel = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        geodude = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        graveler = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        golem = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        ponyta = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        rapidash = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        slowpoke = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        slowbro = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        magnemite = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        magneton = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        farfetchd = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        doduo = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        dodrio = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        seel = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        dewgong = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        grimer = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        muk = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        shellder = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        cloyster = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        gastly = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        haunter = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        gengar = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        onix = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        drowzee = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        hypno = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        krabby = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        kingler = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        voltorb = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        electrode = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        exeggcute = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        exeggutor = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        cubone = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        marowak = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        hitmonlee = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        hitmonchan = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        lickitung = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        koffing = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        weezing = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        rhyhorn = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        rhydon = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        chansey = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        tangela = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        kangaskhan = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        horsea = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        seadra = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        goldeen = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        seaking = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        staryu = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        starmie = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        mrmime = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        scyther = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        jynx = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        electabuzz = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        magmar = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        pinsir = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        tauros = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        magikarp = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        gyrados = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        lapras = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        ditto = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        eevee = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        vaporean = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        jolteon = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        flareon = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        porygon = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        omanyte = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        omastar = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        kabuto = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        kabutops = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        aerodactyl = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        snorlax = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        articuno = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        zapdos = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        moltres = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        dratini = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        dragonair = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        dragonite = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        mewtwo = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)
        mew = Pokemon("Bulbasaur", grassType, 5, 45, 49, 49, 45, 1, 1)