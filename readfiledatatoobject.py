mylist = []
file = open("data.txt", "r")
linebyline = file.readlines()


for a in linebyline:
    currentrowdata = a.replace("\n", "").split(',')
    mylist.append(currentrowdata)

print(mylist)
