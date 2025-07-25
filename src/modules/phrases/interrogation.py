from modules.phrases.question import Question

welcome_msg = '\
=========================\n\
|interrogative sentences|\n\
=========================\n\
\n\
Antes de começarmos a passar as frases afirmativas para interrogativas\
vai aqui um exemplo!\n\
Afirmativa: \'John will make the dinner.\'\n\
Interrogativa: \'Will John make the dinner?\'\n\
\n\
Afirmativa: \'Mary got a book.\'\n\
Interrogativa: \'Has Mary got a book?\'\n\
\n\
' + '=' * 138 + '\n\
Nesse caso, percebemos que, na afirmativa temos: sujeito + verbo principal \
e na interrogativa: verbo auxiliar + sujeito + verbo principal.\n\
Seguindo essa lógica, a alternativa correta da seguinte frase afirmativa \
para interrogativa seria a letra:\n'


def interrogquest():
    print(welcome_msg)
    points = 0

    p1 = Question(
        'John watches Breaking Bad',
        'Does John watch Breaking Bad?',
        'Watches John Breaking Bad?',
        'Breaking Bad John watches?',
        'Does John watches Breaking Bad?'
    )

    p2 = Question(
        'Marco lives in Japan',
        'Does Marco live in Japan?',
        'Lives Marco in Japan?',
        'Do Marco live in Japan?',
        'Marco live in Japan?'
    )

    print(p1)
    answer = input('> ').strip().upper()[0]
    if p1.check_answer(answer):
        print("Correct!")
        points += 1
    else:
        print("Incorrect!")

    print('-' * 48)

    print(p2)
    answer = input('> ').strip().upper()[0]
    if p2.check_answer(answer):
        print("Correct!")
        points += 1
    else:
        print("Incorrect!")

    print('=' * 78)
    print()
    print(
        'Agora é hora de escrever! Reescreva as ',
        'frases afirmativas para interrogativas!'
    )

    print()
    print('1) "Mariene plays volleyball"')
    print()
    phconstructor1 = input('Reescreva: ').upper()

    if phconstructor1 == "DOES MARIENE PLAY VOLLEYBALL?":
        print("-> Perfect! Your answer is correct!")

    else:
        print(' -> The answer is incorrect!')
        print('Correct answer: Does Mariene play volleyball?')

    print("------------------------------------------------")
    print()
    print('2) "Sam likes to play videogames"')
    print()
    phconstructor2 = input('Reescreva: ').lower()

    if phconstructor2 == "does sam like to play videogames?":
        print("-> Correct!!")
        points += 1

    else:
        print(' -> Your answer is incorrect!')
        print('Correct answer: Does Sam like to play videogames?')

    print("------------------------------------------------")

    print()
    print('3) "Olivia will travel to Italy"')
    print()

    phconstructor3 = input('Reescreva: ').lower()

    if phconstructor3 == "will olivia travel to italy?":
        print("-> You answer is right!")
        points += 1

    else:
        print(' -> Your answer is wrong!')
        print('Correct answer: Will Olivia travel to Italy?')

    print("------------------------------------------------")

    print()
    print('4) "Josh eats an apple every day"')
    print()

    phconstructor4 = input('Reescreva: ').lower()

    if phconstructor4 == "does josh eat an apple every day?":
        print("-> Your answer is... CORRECT!")
        points += 1

    else:
        print(' -> Your answer is... incorrect! :(')
        print('Correct answer: Does Josh eat an apple every day?')

    print("------------------------------------------------")

    print()
    print('5) "Tyler wants to travel"')
    print()

    phconstructor5 = input('Reescreva: ').lower()

    if phconstructor5 == "does tyler want to travel?":
        print("-> Your answer is correct!! CONGRATS!!")
        points += 1

    else:
        print(' -> Your answer is WRONG >:(')
        print('Correct answer: Does Tyler want to travel?')

    print("------------------------------------------------")

    print()
    print('6) "Edwin is making an animatronic"')
    print()

    phconstructor6 = input('Reescreva: ').lower()

    if phconstructor6 == "is edwin making an animatronic?":
        print("-> Correct!")
        points += 1

    else:
        print('-> Your answer is incorrect... ;(')
        print('Correct answer: Is Edwin making an animatronic?')

    print("------------------------------------------------")

    print()
    print('7) "Kendrick is cooking"')
    print()

    phconstructor7 = input('Reescreva: ').lower()

    if phconstructor7 == "is kendrick cooking?":
        print("-> Your answer is right! :)")
        points += 1

    else:
        print(' -> Wrong!')
        print('Correct answer: Is kendrick cooking? ')

    print("------------------------------------------------")

    print()
    print('8) "He\'s taking his dog for a walk"')
    print()

    phconstructor8 = input("Reescreva: ").lower()

    if phconstructor8 == "is he going to take his dog for a walk?":
        print("-> Correct!")
        points += 1

    else:
        print(' -> Incorrect!')
        print('Correct answer: Is he going to take his dog for a walk?')

    print("------------------------------------------------")

    print()
    print('9) "They are going to build a mall"')
    print()

    phconstructor9 = input('Reescreva: ').lower()

    if phconstructor9 == "are they going to build a mall?":
        print("-> Your answer is right!!! :))))))))")
        points += 1

    else:
        print(' -> Wrong...')
        print('Correct answer: Are they going to build a mall?')

    print("------------------------------------------------")

    print()
    print('10) "Chris and Joseph are going to school"')
    print()

    phconstructor10 = input('Reescreva: ').lower()

    if phconstructor10 == "are chris and joseph going to school?":
        print("-> CORRECT ANSWER!!!")
        points += 1

    else:
        print('Incorrect.... ;(')
        print('Correct answer: Are Chris and Joseph going to school?')

    print("-----------------------------------------------------")

    print()
    print("Resultado:")
    print()

    if points >= 6:
        print(f'Parabéns!! você ganhou {points} pontos :)')

    elif points < 6:
        print(f"Continue estudando e a melhora virá ... \
              você ganhou {points} pontos.")

    print("==============================================================")


if __name__ == '__main__':
    interrogquest()
