class Hero:
    def __init__(self, name, attack, magic, health, defense, element, hp_max):
        self.name = name  # str
        self.attack = attack  # int
        self.magic = magic  # int
        self.health = health  # int
        self.defense = defense  # list of resistances [water, fire, air, earth, physical, magical]
        self.element = element  # list of affinities [water, fire, air, earth]
        self.hp_max = hp_max  # number max of hp
        self.up_point = 0  # number of point for upgrades of attack / hp / elements

