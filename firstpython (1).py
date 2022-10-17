def list_ascending(mylist):
    previousnumber = None
    for i in range(len(mylist)):
        if previousnumber == None:
             previousnumber = mylist[i]
        else:
            previousnumber = mylist[i-1]
            if previousnumber > mylist[i]:
                currentnumber = mylist[i]
                mylist[i-1] = currentnumber
                mylist[i] = previousnumber
    print(mylist)

number_list = [342,3,123, 3,56,-42]
list_ascending(number_list)