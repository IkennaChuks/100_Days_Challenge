students_scores = {
"Harry": 81,
"Ron":78,
"Hermione":99,
"Draco":74,
"Neville":62
}

students_grade = students_scores

for student in students_grade:
    if students_grade[student] >90 and  students_grade[student] <100:
        students_grade[student] = 'Outstanding'
    elif students_grade[student] >80 and  students_grade[student] <90:
        students_grade[student] = 'Exceeds Expectation'
    elif students_grade[student] >70 and  students_grade[student] <80:
        students_grade[student] = 'Acceptable'
    else:
        students_grade[student] = 'Fail'
        

print(students_grade)