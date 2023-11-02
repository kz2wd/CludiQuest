
import hero


class Player:
    def __init__(self, user, kit, turn):
        self.user = user
        if kit == 0:
            self.kit = hero.Hero("Knight", 6, 1, 12, [1, 1, 1, 1, 1, 1], [0, 0, 0, 0], 12)
        elif kit == 1:
            self.kit = hero.Hero("Paladin", 2, 2, 17, [0.8, 0.8, 0.8, 0.8, 0.8, 0.8], [0, 0, 0, 0], 17)
        elif kit == 2:
            self.kit = hero.Hero("Wizard", 2, 5, 10, [1, 1, 1, 1, 1, 1], [0, 0, 0, 0], 10)
        elif kit == 3:
            self.kit = hero.Hero("Archer", 7, 1, 8, [1, 1, 1, 1, 1, 1], [0, 0, 0, 0], 8)
        self.turn = turn
