class Game:
    def __init__(self):
        self.players_id = []
        self.channel = 0
        self.state = 0
        """
        0 = not started => 1
        1 = adding players => 2
        2 = kit selection + enemies generation + first display action => 3
        3 = fight => 813 or 814
        
        813 = defeat => none
        814 = victory => 5
        5 = upgrade message + new enemies generation => 6
        6 = first display action => 3
        """
        self.enemies = []
        self.fight_round = 0
