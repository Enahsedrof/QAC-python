while True:
    try:

        mark = int(input("Please enter your mark: "))
    except ValueError:
        print("Sorry, I didn't understand that please enter mark as a number")

        continue
    else:
        break

if mark > 85:
    grade = "distinction"

elif mark >= 65: 
    grade = "pass" 

else:
    grade = "fail"

print("Your grade is a", grade, "well done?!?" )