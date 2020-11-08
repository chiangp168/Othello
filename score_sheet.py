import re
import os.path


class ScoreSheet:
    def __init__(self, filename):
        """Attributes."""
        self.filename = filename
        self.opened_file = None

    def read_top_score(self, file_name):
        """Read the first line and extract the integer in score.txt file.
        STRING -> NONE or INT"""
        if os.path.isfile(self.filename):
            with open(self.filename, "r") as f:
                first_line = next(f, None)
                if first_line:
                    return int(first_line.split()[-1])
        return None

    def record_score(self, new_player_score):
        """Create score.txt for first player, and record new highest
        score to first line or new score to the end of the file.
        TUPLE -> NONE"""
        new_player, new_score = new_player_score
        new_line = new_player + " " + str(new_score)
        top_score = self.read_top_score(self.filename)
        if top_score is None:
            with open(self.filename, "w") as f:
                f.write(new_line + "\n")
        elif int(new_score) >= top_score:
            all_names = []
            all_names.append(new_line)
            with open(self.filename, "r") as f:
                for line in f:
                    all_names.append(line.strip())
            with open(self.filename, "w") as f:
                for line in all_names:
                    f.write(line + "\n")
        else:
            with open(self.filename, "a") as f:
                f.write(new_line + "\n")
