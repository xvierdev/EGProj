from random import choice
from modules.utils import ask_play_again


def weekdays():
    """
    Escolhe um dia da semana aleatório e pede para traduzir
    do inglês pro português
    """
    days = {'sunday': 'domingo',
            'monday': 'segunda',
            'tuesday': 'terça',
            'wednesday': 'quarta',
            'thursday': 'quinta',
            'friday': 'sexta',
            'saturday': 'sábado'}
    while True:
        day = choice(list(days.keys()))
        msg = f'the translation of {day} is: '
        answer = input(msg).strip().lower()
        clean_aswer = answer.replace('-', ' ').split(' ')[0]

        if clean_aswer == days[day]:
            print("is correct")
            print("one more point")
        else:
            print("is not correct")
            print("minus one point")

        if not ask_play_again():
            break


if __name__ == '__main__':
    weekdays()
