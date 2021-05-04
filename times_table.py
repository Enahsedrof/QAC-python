def table(number):
    for i in range(1, 100):
        print(number,'x', i, '=', number*i)

x= int(input("Enter a number: "))

times_table = table(x)