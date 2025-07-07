from random import choice

from modules.utils import ask_play_again


def geomtest():
    """
    Este módulo pergunta sobre uma forma geométrica em inglês e aguarda
    a resposta do usuário para sua tradução em português.
    """

    geoform = {'square': 'quadrado',
               'triangle': 'triângulo',
               'circle': 'círculo',
               'rectangle': 'retângulo',
               'pentagon': 'pentágono'
               }

    while True:
        random_geo = choice(list(geoform.keys()))

        msg = f'Translate the {random_geo} to portuguese: '
        answer = input(msg).strip().lower()

        if answer == geoform[random_geo]:
            print('That\'s right!')
        else:
            print(f'I\'s wrong, the correct is \'{geoform[random_geo]}\'!')
        if not ask_play_again():
            break


if __name__ == '__main__':
    geomtest()
