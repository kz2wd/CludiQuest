class Enemy:
    def __init__(self, name, attack, magic, health, defense, level, type):
        self.name = name  # str
        self.attack = attack  # int
        self.magic = magic  # int
        self.health = health  # int
        self.defense = defense  # list of resistances [water, fire, air, earth, physical, magical]
        self.level = level  # int
        self.type = type  # int define enemy type
