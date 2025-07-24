class Question:
    def __init__(self, phrase, correct_answer, *other):
        self.question_phrase = phrase
        self.correct_aswer = correct_answer
        self.alternatives = other

    def __repr__(self) -> str:
        return (
            f"Question(question_phrase='{self.question_phrase}', "
            f"correct_aswer='{self.correct_aswer}', "
            f"alternatives={self.alternatives})"
        )

    def __str__(self) -> str:
        return (
            f"Question: '{self.question_phrase}'\n"
            f"Correct Answer: '{self.correct_aswer}'\n"
            f"Alternatives: {self.alternatives}"
        )

    def ask_question(self):
        from random import shuffle
        letters = 'ABCDE'
        options = list(self.alternatives)
        options.append(self.correct_aswer)
        if options:
            shuffle(options)
            for i in range(len(options)):
                print(f'{letters[i]}) {options[i]}')
