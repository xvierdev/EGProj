from random import choice
# TODO: separete this in database.
opt = {'op1': 'option1', 'op2': 'option2', 'op3': 'option3'}
title = "Functional Test Module"


class EnglishQuiz:
    def __init__(self):
        self.opt = opt
        self.title = title

    def __str__(self):
        return self.title

    def get_opt(self):
        return choice(list(self.opt.keys()))

    def verify_answer(self, selected, answer):
        return answer.strip().lower() == self.opt[selected].strip().lower()
