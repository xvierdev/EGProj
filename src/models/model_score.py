class Score:
    def __init__(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def __str__(self):
        return f"Score: {self.score}"

    def __eq__(self, other):
        if isinstance(other, Score):
            return self.score == other.score
        return False
