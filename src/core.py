import modules.utils as utils


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
            if not utils.ask_play_again():
                return points
        except KeyboardInterrupt:
            return points
