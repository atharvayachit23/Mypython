def Addition(a,b):
    return a+b


def Subtraction(a,b):
    return a-b


def Multiplication(a,b):
    return a*b


def Division(a,b):
    return a/b


def Square(a):
    return a*a


print("which operations you want to do??")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5 Square")
print("6 End Program")
while True:
    operation=input("Enter operation(1,2,3,4,5,6)")
    if operation in ("1","2","3","4"):
        a=int(input("Enter a number"))
        b=int(input("Enter second number"))
    if operation == "5":
        a = int(input("Enter a number"))
    if operation == "6":
        print("End Program")

    if operation == "1":
        print(a,"+",b,"=",Addition(a,b))

    if operation == "2":
        print(a,"-",b,"=",Subtraction(a,b))

    if operation == "3":
        print(a,"*",b,"=",Multiplication(a,b))

    if operation == "4":
        print(a,"/",b,"=",Division(a,b))

    if operation == "5":
        print(a,"*",a,"=",Square(a))
    break