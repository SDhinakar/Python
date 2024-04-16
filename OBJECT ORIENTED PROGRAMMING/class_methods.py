class Instructor:
    followers=0  # class object attribute(Static variable)
    def __init__ (self,name,address):
        self.name=name
        self.address=address

    def display(self,subject_name):
        # print( self.name,self.address )
        print(f"Hi, I am learning  from {self.name} the subject {subject_name}")

    def update_followers(self,follower_name):
        self.followers+=1
        

instructor_1=Instructor("jenny","namakkal")
instructor_1.display("python")
instructor_1.update_followers("jenny")
print(instructor_1.followers)

instructor_2=Instructor("shanmu","namakkal")
instructor_2.update_followers("shanmu")
print(instructor_2.followers)
