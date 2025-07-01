import random
random_number = random.randint(1, 7)

def weekdays():
    """
    Escolhe um dia da semana aleatório e pede para traduzir do inglês pro português
    Detalhe: ele tem uma variável onde armazena todos os ponto. O nome dessa variável é points
    """

    match random_number:
        
        case 1:
            question1 = input("the translation of sunday is: ")
            if question1 == "domingo" or question1 == "Domingo":
                print("is correct")
                print("one more point")
                # points += 1

            else:
                print("is not correct")
                print("minus one point")
                # points -= 1

        case 2:
            question2 = input("the translation of monday is: ")
            if question2 == "segunda" or question2 == "segunda-feira" or question2 == "Segunda" or question2 == "Segunda-feira":
                print("is correct")
                print("one more point")
                # points += 1

            else:
                print("is not correct")
                print("minus one point")
                # points -= 1

        case 3:
            question3 = input("the translation of tuesay is: ")
            if question3 == "terça" or question3 == "terça-feira" or question3 == "Terça" or question3 == "Terça-feira":
                print("is correct")
                print("one more point")
                # points += 1

            else:
                print("is not correct")
                print("minus one point")
                # points -= 1

        case 4:
            question4 = input("the translation of wednesday is: ")
            if question4 == "quarta" or question4 == "quarta-feira" or question4 == "Quarta" or question4 == "Quarta-feira":
                print("is correct")
                print("one more point")
                # points += 1

            else:
                print("is not correct")
                print("minus one point")
                # points -= 1

        case 5:
            question5 = input("the translation of thursday is: ")
            if question5 == "quinta" or question5 == "quinta-feira" or question5 == "Quinta" or question5 == "Quinta-feira":
                print("is correct")
                print("one more point")
                # points += 1

            else:
                print("is not correct")
                print("minus one point")
                # points -= 1

        case 6:
            question6 = input("the translation of friday is: ")
            if question6 == "sexta" or question6 == "sexta-feira" or question6 == "Sexta" or question6 == "Sexta-feira":
                print("is correct")
                print("one more point")
                # points += 1

            else:
                print("is not correct")
                print("minus one point")
                # points -= 1

        case 7:
            question7 = input("the translation of saturday is: ")
            if question7 == "sábado" or question7 == "Sábado":
                print("is correct")
                print("one more point")
                # points += 1

            else:
                print("is not correct")
                print("minus one point")
                # points -= 1

    # print("total points", points)
