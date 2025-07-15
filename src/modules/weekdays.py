from modules import eng_quiz
title = 'Weekdays'
days = {
    'sunday': 'domingo',
    'monday': 'segunda',
    'tuesday': 'terça',
    'wednesday': 'quarta',
    'thursday': 'quinta',
    'friday': 'sexta',
    'saturday': 'sábado'
}


class WeekdaysTest(eng_quiz.EnglishQuiz):
    def __init__(self):
        self.opt = days
        self.title = title
