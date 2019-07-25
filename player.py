
import hero


class Player:
    def __init__(self, user, kit, turn):
        self.user = user
        if kit == 0:
            self.kit = hero.Hero("Knight", 5, 1, 12, [1, 1, 1, 1, 1, 1], [0, 0, 0, 0], 12)
        if kit == 1:
            self.kit = hero.Hero("Paladin", 4, 2, 15, [0.8, 0.8, 0.8, 0.8, 0.8, 0.8], [0, 0, 0, 0], 15)
        if kit == 2:
            self.kit = hero.Hero("Wizard", 2, 5, 10, [1, 1, 1, 1, 1, 1], [0, 0, 0, 0], 10)
        if kit == 3:
            self.kit = hero.Hero("Archer", 7, 1, 7, [1, 1, 1, 1, 1, 1], [0, 0, 0, 0], 7)
        self.turn = turn
