class Team():
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0
    def add_player(self, player_name):
        self.players.append(player_name)
    def has_player(self, player_name):
        for person in self.players:
            if person == player_name:
                return True
        return False
    def points(self):
        return self.points
    def play_game(self, did_win):
        if did_win:
            self.points += 3
