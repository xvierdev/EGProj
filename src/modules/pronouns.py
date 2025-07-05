import random


def pronouns_test():

    response_quest1 = ["ele"]
    response_quest2 = ["ela"]
    response_quest3 = ["eles", "elas"]
    response_quest4 = ["voce", "voçe"]
    response_quest5 = ["eu"]
    random_pronoun = random.randint(1, 4)
    match random_pronoun:

        case 1:

            quest1 = input("A tradução de 'he' é: ")

            if quest1.lower() == response_quest1[0].lower():
                print('Correct!')

            else:
                print('incorrect')

        case 2:

            quest2 = input("A tradução de 'she' é: ")

            if quest2.lower() == response_quest2[0].lower():
                print('Correct')

            else:
                print('Incorrect!')

        case 3:

            quest3 = input("A tradução de 'they' é: ")

            if quest3.lower() == response_quest3[0].lower():
                print('Correct!')

            elif quest3.lower() == response_quest3[1].lower():
                print('Correct!')

            else:
                print('incorrect!')

        case 4:

            quest4 = input("A tradução de 'you' é: ")

            if quest4.lower() == response_quest4[0].lower():
                print('Correct!')

            elif quest4.lower() == response_quest4[1].lower():
                print('Correct!')

            else:
                print('Incorrect!')

        case 5:

            quest5 = input("A tradução de 'I' é: ")

            if quest5.lower() == response_quest5[0].lower():
                print('Correct!')

            else:
                print('Incorrect!')


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

        # Pronomes Possessivos (alguns exemplos, pois variam em gênero e número)
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
