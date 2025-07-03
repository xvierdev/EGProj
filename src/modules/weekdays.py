import random
# points = 0

def weekdays():
    """
    Escolhe um dia da semana aleatório e pede para traduzir do inglês pro português
    """
    random_number = random.randint(1, 7)
    match random_number:

        case 1:
            question1 = input("the translation of sunday is: ")
            if question1 in ["domingo", "Domingo"]:
                print("is correct")
                print("one more point")
                # points += 1

            else:
                print("is not correct")
                print("minus one point")
                # points -= 1

        case 2:
            question2 = input("the translation of monday is: ")
            if question2 in ["segunda", "segunda-feira", "Segunda", "Segunda-feira"]:
                print("is correct")
                print("one more point")
                # points += 1

            else:
                print("is not correct")
                print("minus one point")
                # points -= 1

        case 3:
            question3 = input("the translation of tuesay is: ")
            if question3 in ["terça", "terça-feira", "Terça", "Terça-feira"]:
                print("is correct")
                print("one more point")
                # points += 1

            else:
                print("is not correct")
                print("minus one point")
                # points -= 1

        case 4:
            question4 = input("the translation of wednesday is: ")
            if question4 in ["quarta", "quarta-feira", "Quarta", "Quarta-feira"]:
                print("is correct")
                print("one more point")
                # points += 1

            else:
                print("is not correct")
                print("minus one point")
                # points -= 1

        case 5:
            question5 = input("the translation of thursday is: ")
            if question5 in ["quinta", "quinta-feira", "Quinta", "Quinta-feira"]:
                print("is correct")
                print("one more point")
                # points += 1

            else:
                print("is not correct")
                print("minus one point")
                # points -= 1

        case 6:
            question6 = input("the translation of friday is: ")
            if question6 in ["sexta", "sexta-feira", "Sexta", "Sexta-feira"]:
                print("is correct")
                print("one more point")
                # points += 1

            else:
                print("is not correct")
                print("minus one point")
                # points -= 1

        case 7:
            question7 = input("the translation of saturday is: ")
            if question7 in ["sábado", "Sábado"]:
                print("is correct")
                print("one more point")
                # points += 1

            else:
                print("is not correct")
                print("minus one point")
                # points -= 1

    # print("total points", points)
