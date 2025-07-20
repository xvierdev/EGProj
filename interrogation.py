def interrogquest():
    

    print('\n                                      =========================')
    print('                                      |interrogative sentences| ')
    print('                                      =========================\n')



    print("\n       Antes de começarmos a passar as frases afirmativas para interrogativas vai aqui um exemplo!\n\n          Afirmativa: 'John will make the dinner.'\n       Interrogativa: 'Will John make the dinner?'\n\n          Afirmativa: 'Mary got a book.'\n       Interrogativa: 'Has Mary got a book?'\n\n============================================================================================================================================")
    print('\nNesse caso, percebemos que, na afirmativa temos: sujeito + verbo principal  e   na interrogativa: verbo auxiliar + sujeito + verbo principal\nSeguindo essa lógica, a alternativa correta da seguinte frase afirmativa para interrogativa seria a letra:\n\n')

     
    points = 0
    
    pergunta1 = input('"John watches Breaking Bad"\n\nA) Watches John Breaking Bad?\nB) Breaking Bad John watches?\nC) Does John watch Breaking Bad?\nD) Does John watches Breaking Bad?\n\nResposta: ').strip().upper()
    
    if pergunta1 == 'C':
        print('Correct!')
        points += 1
     

    else: 
        print('Incorrect!')

    print('------------------------------------------------')



    pergunta2 = input('\n"Marco lives in Japan"\n\nA) Lives Marco in Japan?\nB) Does Marco live in Japan?\nC) Do Marco live in Japan?\nD) Marco live in Japan?\n\nReposta: ').strip().upper()

    if pergunta2 == 'B':
        print('Correct!')
        points += 1

    else:
        print('Incorrect!')



    print('==============================================================================')
    print('\nAgora é hora de escrever! Reescreva as frases afirmativas para interrogativas!')


 #Alternei entre upper e lower nas duas frases porque estava testando o comando


    phconstructor1 = input('\n1) "Mariene plays volleyball" \n\nReescreva: ').upper()

    if phconstructor1 == 'DOES MARIENE PLAY VOLLEYBALL?':
        print('-> Perfect! Your answer is correct!')

    else: 
        print(' -> The answer is incorrect!\nCorrect answer: Does Mariene play volleyball?')
        
    print('------------------------------------------------')




    phconstructor2 = input ('\n\n2) "Sam likes to play videogames"\n\nReescreva: ').lower()
    
    if phconstructor2 == 'does sam like to play videogames?':
        print('-> Correct!!')
        points += 1

    else:
        print(' -> Your answer is incorrect!\nCorrect answer: Does Sam like to play videogames?')

    print('------------------------------------------------')
    



    phconstructor3 = input('\n\n3) "Olivia will travel to Italy"\n\nReescreva: ').lower()

    if phconstructor3 == 'will olivia travel to italy?':
        print('-> You answer is right!')
        points += 1

    else:
        print(' -> Your answer is wrong!\nCorrect answer: Will Olivia travel to Italy?')

    print('------------------------------------------------')




    phconstructor4 = input('\n\n4) "Josh eats an apple every day"\n\nReescreva: ').lower()

    if phconstructor4 == 'does josh eat an apple every day?':
        print('-> Your answer is... CORRECT!')
        points += 1

    else:
        print(' -> Your answer is... incorrect! :( \nCorrect answer: Does Josh eat an apple every day?')

    print('------------------------------------------------')




    phconstructor5 = input('\n\n5) "Tyler wants to travel\n\nReescreva: ').lower()

    if phconstructor5 == 'does tyler want to travel?':
        print('-> Your answer is correct!! CONGRATS!!')
        points += 1

    else:
        print(' -> Your answer is WRONG >:(\nCorrect answer: Does Tyler want to travel?')

    print('------------------------------------------------')




    phconstructor6 = input('\n\n6) "Edwin is making an animatronic"\n\nReescreva: ').lower()

    if phconstructor6 == 'is edwin making an animatronic?':
        print('-> Correct!')
        points += 1

    else:
        print('-> Your answer is incorrect... ;(\nCorrect answer: Is Edwin making an animatronic?')

    print('------------------------------------------------')




    phconstructor7 = input('\n\n7) "Kendrick is cooking\n\nReescreva: ').lower()

    if phconstructor7 == 'is kendrick cooking?':
        print('-> Your answer is right! :)')
        points += 1

    else:
        print(' -> Wrong!\nCorrect answer: Is kendrick cooking? ')

    print('------------------------------------------------')




    phconstructor8 = input("\n\n8) He's taking his dog for a walk\n\nReescreva: ").lower()

    if phconstructor8 == 'is he going to take his dog for a walk?':
        print('-> Correct!')
        points += 1

    else:
        print(' -> Incorrect!\nCorrect answer: Is he going to take his dog for a walk?')

    print('------------------------------------------------')




    phconstructor9 = input('\n\n9) "They are going to build a mall"\n\nReescreva: ').lower()

    if phconstructor9 == 'are they going to build a mall?':
        print('-> Your answer is right!!! :))))))))')
        points += 1

    else:
        print(' -> Wrong...\nCorrect answer: Are they going to build a mall?')

    print('------------------------------------------------')




    phconstructor10 = input('\n\n10) "Chris and Joseph are going to school"\n\nReescreva: ').lower()

    if phconstructor10 == 'are chris and joseph going to school?':
        print('-> CORRECT ANSWER!!!')
        points += 1

    else:
        print('Incorrect.... ;(\nCorrect answer: Are Chris and Joseph going to school?')
        
    print('-----------------------------------------------------')

    print('                  Resultado: \n')


    if points >= 6:
        print(f'Parabéns!! você ganhou {points} pontos :)')

    elif points < 6:
        print(f"Continue estudando e a melhora virá... você ganhou {points} pontos.")

    print('==============================================================')

    

interrogquest()