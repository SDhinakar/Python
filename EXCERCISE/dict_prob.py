student_data=[
{
    "Name":"Vignesh",
    "Roll_no":1011,
    "age":20,
    "course":"CSE"
},
{
    "Name":"Kishore",
    "Roll_no":1022,
    "age":20,
    "course":"CSE"
}
]
def add_new_student(name,roll_no,age,course):
    new_student={}
    new_student["Name"]=name
    new_student["Roll_no"]=roll_no
    new_student["age"]=age
    new_student["course"]=course
    student_data.append(new_student)

add_new_student("Santhosh",1033,22,"CSE")
print(student_data[0])
print(student_data[1])
print(student_data[2])