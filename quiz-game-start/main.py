from quiz_brain import question_bank

class QuizBrain:
    def __init__(self):
        self.question_number = 0
        self.question_list = question_bank
    def next_question(self):
        for i in range(len(self.question_list)):
            question = self.question_list[i]
            game_answer = self.question_list[i].answer
            print(f'\nGame answer: {game_answer}')
            print(f'Q{i}: {question.text}')

            user_input = input("True or False: ").lower().strip()
            if user_input == game_answer.lower():
                print('\nCorrect!')
                self.question_number += 1
                print(f'question score: {self.question_number}/{len(self.question_list)}')
            else:
                print('\nWrong!')
                print(f'sum question score: {self.question_number}/{len(self.question_list)}')
                return

        print('Good job! End of questions')


quiz = QuizBrain()
quiz.next_question()


