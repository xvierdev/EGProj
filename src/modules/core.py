import logging
from rich import print
from time import sleep
from typing import Optional
from services.service_module import Vocabulary

logging.getLogger(__name__)


def core(quiz_name: str) -> Optional[int]:
    points = 0
    print(quiz_name)
    new_quiz = Vocabulary(quiz_name)
    while True:
        try:
            for i in range(10):
                result = new_quiz.get_random_words()
                if result is not None:
                    pt_br, en_us = result
                    print(f'[bold]Translate the {en_us} to portuguese.')
                    answer = input('> ').strip()
                    if answer == pt_br:
                        points += 1
                        print(f'[yellow]Correct! {points=}')
                    else:
                        print(f'[red]Wrong, corrent is "{pt_br}"')
                else:
                    msg_err = f'categoria {quiz_name} não exitente na database'
                    logging.error(msg_err)
                    raise ValueError(msg_err)
            for i in range(10):
                result = new_quiz.get_random_words()
                if result is not None:
                    pt_br, en_us = result
                    print(f'[bold]Translate {pt_br} to english')
                    answer = input('> ').strip()
                    if answer == en_us:
                        points += 1
                        print(f'[yellow]Correts! {points=}')
                    else:
                        print(f'[red]Wrong, correct is "{en_us}"')
            if not ask_play_again():
                print(f'[orange1]Congratulations, you have a {points} points')
                sleep(2)
                return points

        except KeyboardInterrupt:
            return points


def ask_play_again():
    """
    Pergunta ao usuário se ele quer continuar o jogo.

    Returns:
        bool: False se o usuário digitar 'n', True caso contrário.
    """
    play_again = input('Continue (y/n): ').strip().lower()
    if play_again == 'n':
        return False
    else:
        return True
