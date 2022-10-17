def Addition():
    return lambda a,b: a+b


def Subtraction():
    return lambda a,b: a-b


def Multiplication():
    return lambda a,b: a*b


def Division():
    return lambda a,b: a/b

def Square():
    return lambda a: a*a


print("which operations you want to do??")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5 Square")
print("6 End Program")

a = None
b = None

while True:
    operation = input("Enter operation(1,2,3,4,5,6)")
    if operation in ("1", "2", "3", "4"):
        a = int(input("Enter a number - "))
        b = int(input("Enter second number - "))
    if operation == "5":
        a = int(input("Enter a number"))
    if operation == ("6"):
        print("End Program")


    if operation == "1":
        addition = Addition()
        print(a, "+", b, " = ", addition(a, b))

    if operation == "2":
        print(a, "-", b, " = ", a-b)

    if operation == "3":
        print(a, "*", b, " = ", a*b)

    if operation == "4":
        print(a, "/", b, " = ", (a/b))

    if operation == "5":
        print(a,"*",a,"=",(a*a))
    break
