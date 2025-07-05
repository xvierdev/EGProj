from random import choice


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

    random_geo = choice(list(geoform.keys()))

    msg = f'Translate the {random_geo} to portuguese: '
    answer = input(msg).strip().lower()

    if answer == geoform[random_geo]:
        print('That\'s right!')
    else:
        print(f'I\'s wrong, the correct is \'{geoform[random_geo]}\'!')


if __name__ == '__main__':
    geomtest()
