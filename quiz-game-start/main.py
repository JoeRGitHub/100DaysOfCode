from data import question_data
from question_model import Question

question_bank = []

for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

    #print(new_question.text, new_question.answer)

#print(question_bank[0].text)


# new_question = Question("What is my name?", "My name is Yossi!")
#
# print(new_question.text, new_question.answer)

# import random
# play = True
# score = 0
#
#
# while play:
#     for i in random.choices(question_data):
#         print(i["text"])
#         print(i["answer"])
#         user_answer = input("True or False: ").lower().strip()
#         if i["answer"].lower() == user_answer:
#             print("Correct!")
#             score += 1
#             print(f"Your score is: {score} points")
#         else:
#             print("Incorrect!")
#             print(f"Your final score is: {score} points")
#             play = False
