students = ['희', '정', '영', '천', '김']
for number, name in enumerate(students):
    print("{}, {}번".format(name, number+1))

students_dict = {"{}번".format(number+1) : name
                 for number, name in enumerate(students)}

print(students_dict)
# 순서는 뒤죽이 박죽이 dict
print(type(students_dict))

scores = [85, 92, 78, 90, 100]
print(students)
for x, y in zip(students, scores) :
    print(x,y)

score_dic = {student : score for student, score in zip (students, scores)}
print(score_dic)
