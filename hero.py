class Hero:
    def __init__(self, name, attack, magic, health, defense, element, level, xp, type):
        self.name = name  # str
        self.attack = attack  # int
        self.magic = magic  # int
        self.health = health  # int
        self.defense = defense  # list of resistances [water, fire, air, earth, physical, magical]
        self.element = element  # list of affinities [water, fire, air, earth]
        self.level = level  # int
        self.xp = xp  # int
        self.type = type  # int define the class


knight = Hero("Knight", 5, 1, 12, [1, 1, 1, 1, 1, 1], [0, 0, 0, 0], 1, 0, 1)
paladin = Hero("Paladin", 4, 1, 15, [1, 1, 1, 1, 1, 1], [0, 0, 0, 0], 1, 0, 2)
wizard = Hero("Wizard", 10, 1, 10, [1, 1, 1, 1, 1, 1], [0, 0, 0, 0], 1, 0, 3)
archer = Hero("Archer", 7, 1, 7, [1, 1, 1, 1, 1, 1], [0, 0, 0, 0], 1, 0, 4)
