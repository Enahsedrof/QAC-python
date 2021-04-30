while True:
    try:

        income = int(input("Please enter your taxable income: "))
    except ValueError:
        print("Sorry, I didn't understand that please enter taxable income as a number")

        continue
    else:
        break

if income <= 12570:
    tax = 0

elif income <= 50270: 
    tax = (income - 12570) * 0.20 

elif income <= 150000:
    tax = (income - 12570) * 0.40  

else:
    tax = (income - 12570) * 0.45 

print("You owe £", tax, "pounds in tax!" )