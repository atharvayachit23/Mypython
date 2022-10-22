with open("data.txt", "r") as ifile:
    count = 0
    for line in ifile:
        print(line)
        count += 1
        if count == 10:
            break
