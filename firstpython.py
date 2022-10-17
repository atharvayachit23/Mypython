def find_factors(x):
    factorsa = []
    for y in range(1, int(x / 2) + 1):
        if x % y == 0:
            factorsa.append(y)
    return factorsa
def find_LCM(p,q):
    factorsa=find_factors(p)
    factorsb=find_factors(q)
    a = int(input("factorsa"))
    flag = False
    if a > 1:
        for q in range(2, a):
            if (a % b) == 0:
                flag = True
                break

    if flag:
        print(a, "is not a Prime number")
    else:
        print(a, "is a prime number")


