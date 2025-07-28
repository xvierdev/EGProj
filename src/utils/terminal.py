from os import system, name


def clear():
    """
    Limpa a tela do terminal enviando o comando 'cls' (Windows)
    ou 'clear' (Linux/Mac).
    """
    system('cls' if name == 'nt' else 'clear')
