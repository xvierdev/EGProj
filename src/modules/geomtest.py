import random


def geomtest():

    random_geo = random.randint(1, 5)

    match random_geo:

        case 1:

            quest1 = input("A tradução de 'Square' é: ")

            if quest1 == 'quadrado':
                print('Correct!')

            elif quest1 == 'Quadrado':
                print('Correct!')

            else:
                print('Incorrect!\nCorrect answer: Quadrado')

        case 2:

            quest2 = input("A tradução de 'Triangle' é: ")

            if quest2 == 'Triângulo':
                print('Correct!')

            elif quest2 == 'triângulo':
                print('Correct!')

            else:
                print("Incorrect!\n Correct answer: Triângulo")

        case 3:

            quest3 = input("A tradução de 'Circle' é: ")

            if quest3 == 'Círculo':
                print('Correct!')

            elif quest3 == 'círculo':
                print('Correct!')

            else:
                print('Incorrect!\nCorrect answer: Círculo')

        case 4:

            quest4 = input("A tradução de 'Rectangle' é: ")

            if quest4 == 'Retângulo':
                print('Correct!')

            elif quest4 == 'retângulo':
                print('Correct!')

            else:
                print('Incorrect!\nCorrect answer: Retângulo')

        case 5:

            quest5 = input("A tradução de 'Pentagon' é: ")

            if quest5 == 'Pentágono':
                print('Correct!')

            elif quest5 == 'pentágono':
                print('Correct!')

            else:
                print('Incorrect\nCorrect answer: Pentágono')


geomtest()
