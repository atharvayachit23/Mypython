mylist = [19, 16, 73, 86, 4,67,987,75,86,53,87,64,54,589]
for i in range(len(mylist)):
    for j in range(i, len(mylist)):
        if mylist[i] > mylist[j]:
            min = mylist[j]
            mylist[i], mylist[j] = mylist[j], mylist[i]


print(mylist)






