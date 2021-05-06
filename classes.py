class Student:

    def __init__(self, name, age, class_, score):
        self.name = name
        self.age = age
        self.class_ = "student"
        self.score = score

test_1 = int(input("Enter first test score: "))
test_2 = int(input("Enter second test score: "))
test_3 = int(input("Enter third test score: "))



John = Student("John", "21", "", ((test_1 + test_2 + test_3)/3))
Jane = Student("Jane", "22", "", "")

print(getattr(John, "score"))