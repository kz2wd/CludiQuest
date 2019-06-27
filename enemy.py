class Enemy:
    def __init__(self, name, attack, magic, health, defense, level):
        self.name = name  # str
        self.attack = attack  # int
        self.magic = magic  # int
        self.health = health  # int
        self.defense = defense  # list of resistances [water, fire, air, earth, physical, magical]
        self.level = level  # int


def enemies_generation():  # very simplified
    enemy_list = []
    for i in range(2):
        enemy_list.append(Enemy("Zrog", 3, 0, 30, [1, 1, 1, 1, 1, 1], 1))
    return enemy_list
