mylist = ["a","z","t","d","c"]
for i in range(len(mylist)):
    for j in range(i, len(mylist)):
        if mylist[i] > mylist[j]:
            min = mylist[j]
            mylist[i], mylist[j] = mylist[j], mylist[i]
print(mylist)
