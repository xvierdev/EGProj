def weekdays():
    """
    Escolhe um dia da semana aleatório e pede para traduzir
    do inglês pro português
    """
    days = {'sunday': 'domingo',
            'monday': 'segunda',
            'tuesday': 'terça',
            'wednesday': 'quarta',
            'thursday': 'quinta',
            'friday': 'sexta',
            'saturday': 'sabado'}
    random_number = 5  # random.randint(0, 6)
    day = list(days.keys())[random_number]
    msg = f'the translation of {day} is: '
    answer = input(msg).strip().lower()
    clean_aswer = answer.replace('-', ' ').split(' ')[0]

    if clean_aswer == days[day]:
        print("is correct")
        print("one more point")
    else:
        print("is not correct")
        print("minus one point")


if __name__ == '__main__':
    weekdays()
