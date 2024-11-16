#Дополнительное практическое задание по модулю: "Базовые структуры данных".
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_students = list(students)
sorted_list_students = sorted(list_students)
#print(sorted_list_students)
sum_grade = 0
middle_grade = []
middle_grade_round = []
for i in range(len(grades)):
    for j in range(len(grades[i])):
        # print(grades[i][j], end = ' ')
        sum_grade += grades[i][j]
    middle_grade.append(sum_grade/len(grades[i]))
    middle_grade_round.append(round(sum_grade/len(grades[i])))
    # print(' ',middle_grade[i])
students_middle_grades = dict(zip(list_students, middle_grade))
students_middle_grades_round = dict(zip(list_students, middle_grade_round))
print(students_middle_grades)
# print(students_middle_grades_round)
