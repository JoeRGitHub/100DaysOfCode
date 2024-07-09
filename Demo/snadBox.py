import random

names = ['James', 'Michael', 'Robert', 'John']
results = {student:random.randint(1,50) for student in names}
print(results)

# Create a dictionary of students who scored more than 40
pass_student = {student:score for student, score in results.items() if score > 20 }
print(pass_student)



