# class Instructor: #class is a keyword , Instructor is the name of the class
#     pass
# instructor_1 = Instructor()
# print(type(instructor_1))

class Instructor:
    def __init__(self,instructor_name,address):
        self.name=instructor_name
        self.address=address
        self.followers=0

instructor_1=Instructor("dhina","namakkal")
print(instructor_1.name,instructor_1.address)

print(Instructor("shanmu","namakkal").address)

print(instructor_1.followers)