def determine_grade(scores):
    if scores >= 70 and scores <= 100:
        return 'A'
    elif scores >= 60 and scores <= 69:
        return 'B'
    elif scores >= 50 and scores <= 59:
        return 'C'
    elif scores >= 40 and scores <= 49:
        return 'D'
    else:
        return 'You failed!'
      

print("Welcome to Grade Calculator")
name = input("What is your name? ")
physics = int(input("Please enter your physics mark: "))
chemistry = int(input("Please enter your chemistry mark: "))
maths = int(input("Please enter your maths mark: "))

percentage = (physics + chemistry + maths)/3
print(name + ", your percentage score is: " + str(percentage) + "%")

grade = determine_grade(percentage)
print(name + ", your percentage score is " + grade)