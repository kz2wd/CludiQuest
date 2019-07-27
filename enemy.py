class Enemy:
    def __init__(self, name, attack, magic, health, defense, level, hp_max):  # !!
        self.name = name  # str
        self.attack = attack  # int
        self.magic = magic  # int
        self.health = health  # int
        self.defense = defense  # list of resistances [water, fire, air, earth, physical, magical]
        self.level = level  # int
        self.hp_max = hp_max


def enemies_generation(fight_round):  # very simplified
    enemy_list = []

    if fight_round == 0:
        for i in range(2):
            enemy_list.append(Enemy("Zrog", 2, 0, 20, [1, 1, 1, 1, 1, 1], 1, 20))

    elif fight_round == 1:

        enemy_list.append(Enemy("Gridon", 4, 0, 17, [1, 1, 1, 1, 1, 1.4], 1, 17))
        enemy_list.append(Enemy("Baloud", 1, 0, 58, [1, 1, 1, 1, 0.6, 1.2], 1, 58))
        enemy_list.append(Enemy("Zrog", 2, 0, 20, [1, 1, 1, 1, 1, 1], 1, 20))

    elif fight_round == 2:

        enemy_list.append(Enemy("Krepto", 8, 0, 65, [1, 1, 1, 1, 1.4, 1], 1, 65))
        enemy_list.append(Enemy("Baloud", 1, 0, 58, [1, 1, 1, 1, 0.6, 1.2], 1, 58))

    elif fight_round == 3:

        for i in range(2):
            enemy_list.append(Enemy("Gridon", 4, 0, 17, [1, 1, 1, 1, 1, 1.4], 1, 17))
        enemy_list.append(Enemy("Zrog", 2, 0, 20, [1, 1, 1, 1, 1, 1], 1, 20))

    elif fight_round == 4:
        enemy_list.append(Enemy("Goeloss", 3, 0, 340, [2, 4, 0, 0.5, 2, 3], 1, 340))

    elif fight_round == 5:
        enemy_list.append(Enemy("Guardian", 15, 0, 100, [1, 0.5, 3, 2, 1.5, 0.8], 1, 100))

    elif fight_round == 6:
        for i in range(4):
            enemy_list.append(Enemy("Lost Soul", 5, 0, 8, [0.5, 0.5, 0.5, 0.5, 0.1, 1], 1, 8))

    else:
        enemy_list.append(Enemy("Smoonauvin", 20, 0, 9999, [5, 5, 5, 5, 5, 5], 1, 9999))

    return enemy_list



