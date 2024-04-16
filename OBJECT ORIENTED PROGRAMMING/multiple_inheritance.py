class Human:
    def __init__(self, num_heart):
        print("calling init from Human class")
        self.num_eyes = 2
        self.num_nose = 1
        self.num_heart = num_heart

    def eat(self):
        print("I can eat.")

    def work(self):
        print("I can work.")


class Male:
    def __init__(self, name):
        print("calling init from Male class")
        self.name = name

    def work(self):
        print("I can go to work for a job.")


class Boy(Human, Male):
    def __init__(self, name, heart, language):
        Human.__init__(self, heart)
        Male.__init__(self, name)
        self.language = language

    def sleep(self):
        print("I can sleep.")

    def work(self):
        print("I can code.")

    def display(self):
        return f"Hi I am {self.name}. I know {self.language}."


boy_1 = Boy("dhinakar", 1, "python")
print(boy_1.display())

# print(boy_1.num_heart)
# print(boy_1.num_eyes)
# print(boy_1.language)

# boy_1.can_gym()
# boy_1.work()
# print(Boy.mro())  # Method Resolution Order (MRO) is the order in which methods should be inherited in the presence of multiple inheritance.
