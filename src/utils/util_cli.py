from os import system, name
from time import sleep

_SLEEPTIME = 0.02


def clear():
    """
    Limpa a tela do terminal enviando o comando 'cls' (Windows)
    ou 'clear' (Linux/Mac).
    """
    system('cls' if name == 'nt' else 'clear')


def quit():
    """
    Encerra o programa com uma mensagem amigável ao usuário.
    """
    exit_msg = '\nThanks for using the English App! See you next time.\n'
    for letter in exit_msg:
        print(letter, end='')
        sleep(_SLEEPTIME)
    exit()
