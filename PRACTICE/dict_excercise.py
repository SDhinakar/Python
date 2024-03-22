student_marks={
    "Harry":81,
    "Berry":78,
    "Tina":99,
    "Akriti":68,
    "Harsh":56,
    "Prem":42,
    "Anurag":92
}

student_grades={}
for student in student_marks:
    marks=student_marks[student]
    if marks>90:
        student_grades[student]="A+"
    elif marks>80:
        student_grades[student]="A"
    elif marks>70:
        student_grades[student]="B+"
    elif marks>60:
        student_grades[student]="B"
    elif marks>50:
        student_grades[student]="C"
    elif marks>40:
        student_grades[student]="D"
    else:
        student_grades[student]="F"
print(student_grades)