from services.service_module import Vocabulary


def core(quiz: str):
    points = 0
    print(quiz)
    new_quiz = Vocabulary(quiz)
    while True:
        try:
            pt_br, en_us = new_quiz.get_random_words()
            print(f'Translate the "{en_us}"')
            answer = input('> ').strip()
            if answer == pt_br:
                points += 1
                print(f'Correct! {points=}')
            else:
                print(f'Wrong, corrent is "{pt_br}"')
            if not ask_play_again():
                break
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
