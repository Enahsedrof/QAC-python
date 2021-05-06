class Student:

    def __init__(self, name, age, studentclass):
        self.name = name
        self.age = age
        self.studentclass = "student"

    def scoreavg(self, Test1, Test2, Test3):
        avg = (Test1 + Test2 + Test3)/3
        return avg
        





Ben = Student("John", 21, '1A')
print ("Students Name: ", Ben.name)
print ("Students Age: ", Ben.age)
print ("Students class: ", Ben.studentclass)
print (Ben.scoreavg(12,6,8))
Jane = Student("Jane", "22", "")

