def core(quiz):
    points = 0
    print(quiz)
    while True:
        try:
            selected = quiz.get_opt()
            print('Translate ' + selected)
            if quiz.verify_answer(selected, input('Your answer: ')):
                points += 1
                print("Correct!")
            else:
                print("Incorrect!")
            if not ask_play_again():
                return points
        except KeyboardInterrupt:
            return points


def ask_play_again():
    """
    Pergunta ao usuário se ele quer continuar o jogo.

    Solicita ao usuário para digitar 'y' para sim ou 'n' para não.
    Qualquer entrada diferente de 'n' é interpretada como 'sim'.

    Returns:
        bool: False se o usuário digitar 'n', True caso contrário.
    """
    play_again = input('Continue (y/n): ')
    if play_again == 'n':
        return False
    else:
        return True
