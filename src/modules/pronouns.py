from random import choice

from modules.utils import ask_play_again


def pronouns_test():

    pronouns = {'I': 'eu',
                'you': ('você', 'vocês'),
                'he': 'ele',
                'she': 'ela',
                'it': ('isso', 'isto', 'aquilo'),
                'we': 'nós',
                'they': ('eles', 'elas'),
                'someone': 'alguém',
                'something': 'algo',
                'everyone': ('todos', 'todas'),
                'everything': 'tudo',
                'nobody': 'ninguém',
                'nothing': 'nada',
                'any': 'qualquer',
                'some': ('algum', 'alguma')}
    while True:
        pronoun = choice(list(pronouns.keys()))
        answer = input(f'A tradução de \'{pronoun}\' é: ').strip().lower()
        if answer in pronouns[pronoun]:
            print('Correct')
        else:
            print('Incorrect')
        if not ask_play_again():
            break


if __name__ == '__main__':
    pronouns_test()

    # TODO: implement this.
    """
    pronouns = {
        # Pronomes Pessoais do Caso Reto (Subjetivos)
        'I': 'eu',
        'you (singular, informal)': 'tu',  # ou 'você' no Brasil
        'he': 'ele',
        'she': 'ela',
        # ou 'isso' dependendo do contexto
        'it': 'ele/ela (para coisas/animais)',
        'we': 'nós',
        'you (plural, informal)': 'vocês',  # ou 'vós' (formal/antigo)
        'they': 'eles/elas',

        # Pronomes Pessoais do Caso Oblíquo (Objetivos) - Comuns
        'me': 'me/mim',
        'you (singular, informal, obj)': 'te',
        'him': 'o/lhe',
        'her': 'a/lhe',
        'it (obj)': 'o/a',  # ou 'lhe' para complemento indireto
        'us': 'nos',
        'you (plural, informal, obj)': 'vos/lhes',  # ou 'vocês'
        'them': 'os/as/lhes',

        # Pronomes Possessivos (variam em gênero e número)
        'my': 'meu/minha',
        'your (singular, informal)': 'teu/tua',
        'his': 'dele/dela',
        'her (possessive)': 'dela',
        'its': 'dele/dela (para coisas/animais)',
        'our': 'nosso/nossa',
        'your (plural, informal)': 'de vocês',  # ou 'vosso/vossa'
        'their': 'deles/delas',

        # Pronomes Demonstrativos
        'this': 'este/esta/isto',
        'that': 'esse/essa/isso',
        'that (distant)': 'aquele/aquela/aquilo',

        # Pronomes Indefinidos (alguns exemplos)
        'someone': 'alguém',
        'something': 'algo',
        'everyone': 'todos/todas',
        'everything': 'tudo',
        'nobody': 'ninguém',
        'nothing': 'nada',
        'any': 'qualquer',
        'some': 'algum/alguma',

        # Pronomes Interrogativos
        'who': 'quem',
        'what': 'o quê/que',
        'which': 'qual',
        'whose': 'de quem',

        # Pronomes Relativos
        'who (relative)': 'quem',
        'which (relative)': 'que/o qual/a qual',
        'that (relative)': 'que',
        'whose (relative)': 'cujo/cuja'
    }"""
