w = str(input("Enter word -"))
l = list(w)
for i in range(len(l)):
    for j in range(i + 1):
        print(l[j], end="")
    print("")

for i in reversed(range(len(l))):
    for j in (range(i + 1)):
        print(l[j], end="")
    print("")

# for i in range(len  (l)):
#     for j in range(i + 1):
#         print(l[j], end="")
#     print("")
# for i in range(len(l)):
#     for j in range(i + 1):
#         print(   l[j], end="")
#     print("")
# for i in range(len(l)):
#     for j in range(i+1):
#         print(l[0:j], end="")
#     print("")
# for i in range(len(l)):
#     for j in range(i+1):
#         print(l[j], end="   ")
#     print("")
# for i in range(len(l)):
#     for space in range(i+1):
#         print(l[j], end="")
#     print("")
# for i in range(len(l)):
#     for j in range(i+1):
#         print(l[j-i], end="")
#     print("")
# for i in reversed(range(len(l))):
#     for j in (range(1 , i+1)):
#         print(l[i-j], end="")
#     print("")
# for i in (range(len(l))):
#     for j in (range(i+1)):
#         for k in (range(j+1)):
#             print(l[i-j], end="")
#     print("")
# for i in reversed(range(len(l))):
#     for j in (range(i+1)):
#         print(l[i-j], end="")
#     print("")
# for i in (range(len(l))):
#     for j in (range(i+j)):
#         print(l[(i-j)], end="")
#     print("")
# for i in reversed(range(len(l))):
#     for j in (range(i+1)):
#         print(l[j-i-1], end="")
#     print("")
# for i in (range(len(l))):
#     for j in (range(i + 1)):
#         print(l[j - i - 1], end="")
#     print("")
#
# for i in (range(len(l))):
#     for j in (range(i + 1)):
#         print(l[j - i], end="")
#     print("")
# for i in (range(len(l))):
#     for j in (range(i + 1)):
#         print(l[j-i], end="")
#     print("")
# for i in reversed(range(len(l))):
#     for j in (range(i+1)):
#         print(l[(i-j)])
#     print("")
# for i in range(len(l)):
#     for j in range(i + 1):
#         for k in range( j+1):
#             for m in range( k+1):
#                 print(l[m], end="")
#     print("")
# for i in (range(len(l))):
#     for j in range(i + 1):
#         print(l[j-i], end="")
#     print("   ")
# for i in (range(len(l))):
#     for j in range(i + 1):
#         print(   l[j-i], end="   ")
#     print("")
# for i in (range(len(l))):
#     for j in range(i):
#         for j in range(i+1):
#             for j in range(i+2):
#                 print(l[i], end="")
#     print("")
# for i in (range(len(l))):
#     for j in range(i + 1):
#         print(   l[j-i], end="   ")
#     print("")
# for i in (range(len(l))):
#     for j in range(i):
#         for j in range(i+1):
#             for j in range(i+2):
#                 print(l[j], end="")
#     print("")

for i in reversed(range(len(l))):
    for k in range(len(l)-i-1):
        print(" ", end="")
    for j in range(i + 1):
        print(l[j], end="")
    print("")

for i in range(len(l)):
    for k in range(len(l)-i-1):
        print(" ", end="")
    for j in range(i + 1):
        print(l[j], end="")
    print("")
