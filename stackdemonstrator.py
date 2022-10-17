import stackobject

mystack = stackobject.Stack()
while True:
    print("which operation do you want to perform??")
    print("1.put")
    print("2.pop")
    print("3.exit")
    operation = input("Enter operation(1,2,3)")

    if operation == "1":
        mystack.put()
    if operation == "2":
        mystack.pop()
    if operation == "3":
        print("End program")
        break


