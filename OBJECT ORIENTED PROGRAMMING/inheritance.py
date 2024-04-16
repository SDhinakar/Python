class Human:
    def __init__(self):
             self.num_eyes=2
             self.num_nose=1

    def eat(self):
        print("I can eat.")
    def work(self):
        print("I can work.")

class Male(Human): #Inheritance is a mechanism in which a new class is derived from an existing class
    def __init__(self,name):
        super().__init__()
        self.name=name
    def sleep(self):
        print("I can sleep.")

    def work(self):
        super().work() # super() is a built-in function that returns a temporary object of the superclass that allows you to call its methods.
        print("I can work hard.")


male_1=Male("Aakash")
male_1.eat()
male_1.sleep()
male_1.work()
print(male_1.num_eyes)