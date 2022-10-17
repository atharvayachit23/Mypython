def Addition(a,b):
    return lambda a,b: a+b

def Subtraction(a,b):
    return lambda a,b: a-b

def Multiplication(a,b):
    return lambda a,b: a*b

def Division(a,b):
    return lambda a,b: a/b


print("which operations you want to do??")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5 End program")

while True:
    operation = input("Enter operation(1,2,3,4,5)")
    if operation in ("1", "2", "3", "4"):
        a = int(input("Enter a number"))
        b = int(input("Enter second number"))

    if operation == ("5"):
        print("End Program")

    if operation == "1":
        print(a, "+", b, "=", Addition(a, b))

    if operation == "2":
        print(a, "-", b, "=", Subtraction(a, b))

    if operation == "3":
        print(a, "*", b, "=", Multiplication(a, b))

    if operation == "4":
        print(a, "/", b, "=", Division(a, b))

    if operation == ("5"):
        print("End Program")

    break