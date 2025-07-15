from modules import eng_quiz
title = "Months Test Module"
months = {
    'January': 'Janeiro',
    'February': 'Fevereiro',
    'March':  'Março',
    'April': 'Abril',
    'May': 'Maio',
    'June': 'Junho',
    'July': 'Julho',
    'August': 'Agosto',
    'September': 'Setembro',
    'October': 'Outubro',
    'November': 'Novembro',
    'December': 'Dezembro',
}


class MonthsTest(eng_quiz.EnglishQuiz):
    def __init__(self):
        self.opt = months
        self.title = title
