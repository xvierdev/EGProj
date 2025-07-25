from random import shuffle
from string import ascii_uppercase
_LETTERS = ascii_uppercase


class Question:
    def __init__(self, phrase: str, correct_answer: str,
                 *incorrect_answers: str):
        self.question_phrase = phrase
        self.correct_answer = correct_answer
        self.alternatives = incorrect_answers
        self.all_alternatives: dict[str, str] = {}
        self.correct_alternative = ''
        alternatives = list(incorrect_answers)
        alternatives.append(self.correct_answer)
        if len(alternatives) > len(_LETTERS):
            raise ValueError('O número de argumentos excedeu o limite.')
        shuffle(alternatives)
        for i in range(len(alternatives)):
            self.all_alternatives[_LETTERS[i]] = alternatives[i]
            if alternatives[i] == self.correct_answer:
                self.correct_alternative = _LETTERS[i]

    def __repr__(self) -> str:
        return (
            f"Question(question_phrase='{self.question_phrase}', "
            f"correct_answer='{self.correct_answer}', "
            f"alternatives={self.alternatives})"
        )

    def __str__(self) -> str:
        alternative_lines = []
        for key, value in self.all_alternatives.items():
            alternative_lines.append(f'{key}) {value}')
        alternatives_str = '\n'.join(alternative_lines)
        return (
            f"Question: '{self.question_phrase}'\n{alternatives_str}"
        )

    def check_answer(self, answer: str) -> bool:
        return answer == self.correct_alternative
