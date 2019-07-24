class Game:
    def __init__(self):
        self.players_id = []
        self.channel = 0
        self.state = 0
        """
        0 = not started
        1 = adding players
        2 = kit selection + enemies generation + first display action
        3 = fight + end ?
        """
        self.enemies = []
