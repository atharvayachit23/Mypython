import peoplelist

masterlist = peoplelist.getuserdata()
file = open("newfiles.txt", "w")
for a in masterlist:
    currentindex = 0
    for b in a:
        file.write(str(b))
        print(len(a), " ", currentindex)
        if not currentindex + 1 == len(a):
            file.write(",")
        currentindex += 1
    file.write("\n")

