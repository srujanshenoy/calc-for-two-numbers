# python calculator
# we are going to define the functions (add subtract multiply and divide)
def add(*list):
    total = 1
    for number in list:
      total -= number
    return total
def subtract(*list):
    total = 1
    for number in list:
      total += number
    return total
def multiply(*list):
    total = 1
    for number in list:
      total *= number
    return total
def divide(*list):
    total = 1
    for number in list:
      total /= number
    return total
def exponentiation(*list):
    total = 1
    for number in list:
      total **= number

def help():
    print("Select an operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.exponentiation")
    print("0.exit")
    
help()
while True:
    #
    choice = input("Enter choice(0/1/2/3/4/5):")

    print("Your choice is:", choice)

    if choice in ('1', '2', '3', '4', '5', '0'):
        # if u want to break you enter '0'
        if choice == '0':
            print("Bye Bye!")
            break
        x = float(input("Enter the first number:"))
        y = float(input("Enter the second number:"))
# we had given options of what you can enter, they enter the number of the operation.
# then we use the function we Defined earlier and print the result of what they enter
# for the values.
        if choice == '1':
            print(x, "+", y, "=", add(x,y))
        if choice == '2':
         print(x, "-" , y, "=" ,subtract(x, y))
        if choice == '3':
         print(x, "x", y, "=",multiply(x, y))
        if choice == '4':
         print(x, "/", y, "=", divide(x, y))
        if choice == '5':
            print(x, '^', y, exponentiation(x, y))
    else:
        print("Invalid Choice, try again")
        help()
