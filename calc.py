print('''
add- to add x & y
subtract- to subtract x & y
multiply- to multiply x & y
divide- to divide x & y
exponentiation- to raise x to y ''')
x = int(input("x (enter a value): "))
y = int((input("y (enter another value):")))
add = x + y
subtract = x - y
multiply = x * y
divide = x / y
exponent = x ** y
choice = input("choice: add/subtract/multiply/divide/exponentiation \n")
if choice in ("add", "subtract", "multiply", "divide", "exponentiation"):
    if choice == "add":
        print(x, '+', y, '=', add)
    if choice == "subtact":
        print(x, "-", y, '=', subtract)
    if choice  == "multiply":
        print(x, "x", y, "=", multiply)
    if choice == "divide":
        print(x, "/", y, "=", divide)
    if choice == "exponentiation":
        print(x, "^", y, "=", exponent)  
