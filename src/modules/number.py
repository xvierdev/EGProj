from num2words import num2words
from random import randint
from modules import eng_quiz


class NumberTest(eng_quiz.EnglishQuiz):
    def __init__(self):
        self.title = "Number Test Module"
        self.opt = None  # This will be set in the numbers function

    def get_opt(self):
        randomNumber = randint(0, 1000)
        return num2words(randomNumber)

    def verify_answer(self, selected, answer):
        return answer.strip().lower() == num2words(selected, lang='pt_BR')
