x=str("3")
y=int(3)
z=float(3)

print(x,y,z)
x = 5
y = "John"
print(x,y)
fruits=("apple","banana","cherry")
mytuple=fruits*2

print(mytuple)

thisset={"apple","banana","cherry"}

thisset={"apple","banana","cherry"}
thisset.add("orange")
print("banana" in thisset)
thisset.discard("orange")

print(thisset)

thisset={"apple","banana","cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)

allset=thisset.union(tropical)
print(allset)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

print(thisdict)
thisdict.popitem()

print(thisdict)

for x in thisdict.items():
    print(x)

    mydict=thisdict.copy()
    print(mydict)

    mydict = dict(thisdict)
    print(mydict)

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

  a = 200
  b = 33
  c = 500
  if a > b or a > c:
      print("At least one of the conditions is True")


x=20

if x>10:
    print("Above ten,")
    if x>21:
        print("and also above 20!")
    else:
        print("but not above 20.")
i = 1
while i < 6:
    print(i)
    i += 1

def my_function():
  print("Hello from a function")


my_function()



def myfunc(n):
    return lambda ax: ax * n


mydoubler = myfunc(2)
mytrippler = myfunc(3)
print(mydoubler(11))
print(mytrippler(11))


addn = lambda aa,bb: aa+bb


print(addn(1,2))

