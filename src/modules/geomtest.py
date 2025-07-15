from modules import eng_quiz
title = "Geometric Test Module"
geoform = {
    'square': 'quadrado',
    'triangle': 'triângulo',
    'circle': 'círculo',
    'rectangle': 'retângulo',
    'pentagon': 'pentágono'
}


class GeometryTest(eng_quiz.EnglishQuiz):
    def __init__(self):
        # super().__init__()
        self.opt = geoform
        self.title = title
