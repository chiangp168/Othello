class GameController:
    """Maintains the state of the game."""
    def __init__(self, WIDTH, HEIGHT, CELL, score_sheet):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.cell = CELL
        self.total_col = self.WIDTH // self.cell
        self.total_row = self.HEIGHT // self.cell
        self.player_wins = False
        self.computer_wins = False
        self.tie = False
        self.score_recorded = False
        self.score_sheet = score_sheet
        self.is_over = False

    def input_name(self, name):
        """Save the user's input name.
        STRING -> NONE"""
        self.name = name

    def record_score(self, player_score):
        if not self.score_recorded:
            self.score_recorded = True
            self.score_sheet.record_score(player_score)

    def game_stop(self, white_score, black_score, total_disks):
        """Check if the board is filled up or if there are no
        more legal moves, then update game status.
        INT, INT, INT, BOOLEAN -> NONE"""
        if total_disks == self.total_col * self.total_row or self.is_over:
            if black_score > white_score:
                self.player_wins = True
            elif white_score > black_score:
                self.computer_wins = True
            else:
                self.tie = True
            self.is_over = True

    def update(self, white_score, black_score, total_disks):
        """Print out game status and the number of tiles
        when computer or player wins.
        INT, INT, INT, BOOLEAN -> NONE"""
        self.game_stop(white_score, black_score, total_disks)
        player_score = (self.name, black_score)
        text_size = 50
        pixels_away_mid_height = 50
        pixels_away_mid_width = 130
        if self.computer_wins:
            fill(100, 21, 21)
            textSize(text_size)
            text("YOU LOST!!", self.WIDTH/2 - pixels_away_mid_width,
                 self.HEIGHT/2 - pixels_away_mid_height)
            print("Game is over! YOU LOST!!")
            print("Black Tile " + str(black_score))
            print("White Tile " + str(white_score))
            self.record_score(player_score)

        if self.player_wins:
            fill(100, 21, 21)
            textSize(text_size)
            text("YOU WIN!!!", self.WIDTH/2 - pixels_away_mid_width,
                 self.HEIGHT/2 - pixels_away_mid_height)
            print("Game is over! YOU WIN!!!")
            print("Black Tile " + str(black_score))
            print("White Tile " + str(white_score))
            self.record_score(player_score)

        if self.tie:
            fill(100, 21, 21)
            textSize(text_size)
            text("It's a tie!!!", self.WIDTH/2 - pixels_away_mid_width,
                 self.HEIGHT/2 - pixels_away_mid_height)
            print("Game is over! It's a tie!!!")
            print("Black Tile " + str(black_score))
            print("White Tile " + str(white_score))
            self.record_score(player_score)
