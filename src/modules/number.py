from num2words import num2words
from random import randint


def numbers():
    while True:
        randomNumber = 0
        level = 2

        if level <= 1:  # Quanto maior o nível, maior a margem
            randomNumber = randint(0, 9)
        else:
            randomNumber = randint(0, 1000)

        number = num2words(randomNumber)
        numberBR = num2words(randomNumber, lang='pt_BR')

        print(f"O que é '{number}' em português?")
        response = input("> ")
        if response == numberBR:
            print("Você acertou")
            input()
        else:
            print("Você errou")
            input()


if __name__ == '__main__':
    numbers()
