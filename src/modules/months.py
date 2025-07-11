from random import choice
import modules.utils

# escolhe um mês do ano aleatório e traduz do inglês pro português

Months = {
    'January': 'janeiro',
    'February': 'fevereiro',
    'March':  'março',
    'April': 'Abril',
    'May': 'maio',
    'June': 'junho',
    'July': 'julho',
    'August': 'agosto',
    'September': 'setembro',
    'October': 'outubro',
    'November': 'novembro',
    'December': 'dezembro',
}


def start():
    while True:
        english_month = choice(list(Months.keys()))
        print(f"the translation of : '{english_month}' to Portuguese is:")
        user_answer = input("your answer: ").strip().lower()

        if check_answer(english_month, user_answer):
            print("t: the answer is correct!")
            print("one more point!")
        else:
            print("the answer is incorrect.")
            print("minus one point.")
        if not modules.utils.ask_play_again():
            break


def check_answer(english_month, user_answer):
    correct_translation = Months[english_month]
    return user_answer == correct_translation


if __name__ == '__main__':
    start()
