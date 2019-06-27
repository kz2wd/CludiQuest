class Hero:
    def __init__(self, name, attack, magic, health, defense, element):
        self.name = name  # str
        self.attack = attack  # int
        self.magic = magic  # int
        self.health = health  # int
        self.defense = defense  # list of resistances [water, fire, air, earth, physical, magical]
        self.element = element  # list of affinities [water, fire, air, earth]
