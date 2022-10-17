container = [23, 56, 76, 34, 66]


def put():
    num = int(input("Enter a number"))
    container.append(num)

    return container


print(put())


def pop():
    numlast = container[-1]

    print("Removing last number", numlast)
    container.remove(numlast)

    return container


print(pop())
print(pop())
