import traceback


def Addition(a, b):
    return a+b


def Subtraction(a, b):
    return a-b


def Multiplication(a, b):
    return a*b


def Division(a, b):
    return a/b


def Square(a):
    return a*a


lastOperationFlag = False
operation = None

while True:
    if not lastOperationFlag:
        print("Which operations you want to do??")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5 Square")
        print("6 End Program")
    try:
        if not lastOperationFlag:
            operation = int(input("Enter operation(1,2,3,4,5,6)"))
        if operation in (1, 2, 3, 4):
            try:
                a = int(input("Enter a number"))
                b = int(input("Enter second number"))
            except:
                lastOperationFlag = True
                raise ValueError("Not a number")
        if operation == 5:
            try:
                a = int(input("Enter a number"))
            except:
                lastOperationFlag = True
                raise ValueError("Not a number")
        if operation == 6:
            print("End Program")
            break

        if operation == 1:
            print(a, "+", b, "=", Addition(a, b))

        if operation == 2:
            print(a, "-", b, "=", Subtraction(a, b))

        if operation == 3:
            print(a, "*", b, "=", Multiplication(a, b))

        if operation == 4:
            print(a, "/", b, "=", Division(a, b))

        if operation == 5:
            print(a, "*", a, "=", Square(a))
        if operation > 6 or operation < 1:
            raise TypeError("Enter valid values 1,2,3,4,5 or 6")

        lastOperationFlag = False
    except ValueError:
        print("Enter valid number, try again")
    except:
        lastOperationFlag = False
    finally:
        a = None
        b = None
