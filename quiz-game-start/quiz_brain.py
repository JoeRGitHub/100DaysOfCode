#from main import question_bank

class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank

    def has_more_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        game_answer = self.question_list[self.question_number].answer.lower()
        print(f'\nGame answer: {game_answer}')
        print(f'Q{self.question_number}: {question.text}')
        user_input = input("True or False: ").lower().strip()
        self.check_answer(user_input, game_answer)

    def check_answer(self, user_input, game_answer):
        if user_input == game_answer:
            print('\nCorrect!')
            self.question_number += 1
            print(f'question score: {self.question_number}/{len(self.question_list)}')
        else:
            print('\nWrong!')
            print(f'sum question score: {self.question_number}/{len(self.question_list)}')
            self.question_number = len(self.question_list)






