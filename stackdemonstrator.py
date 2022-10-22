import stackobject

mystack = stackobject.Stack()
while True:
    print("which operation do you want to perform??")
    print("1.put")
    print("2.pop")
    print("3.print all elements")
    print("4.Exit")
    try:
        operation = int(input("Enter operation(1,2,3,4)"))
        if operation == 1:
            mystack.put()
        if operation == 2:
            mystack.pop()
        if operation == 3:
            mystack.printallelements()
        if operation == 4:
            print("End program")
            break
        if operation > 4 or operation < 1:
            raise TypeError("Enter a valid number 1 or 2 or 3 or 4")
    except:
        print("Enter valid values 1,2,3 or 4")
