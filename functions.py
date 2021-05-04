def hi_user(first_name, last_name):
    print("Hello" + " " + first_name + " " + last_name)

hi_user("Bill", "Steves")
hi_user("Steve", "Jobs")

def add_calc(number1, number2):
    answer = number1 + number2
    return answer

added_number = add_calc(5,5)

print(added_number)
print(added_number * 10)