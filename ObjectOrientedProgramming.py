class MyClass:
    x = 5

print(MyClass.x)
p1 = MyClass()
print(p1.x)
p1.x=10
print(p1.x)
p2=MyClass()
print(p2.x)

class MyClassWithInit:
    def __init__(self):
        print("MyClassWithInit initialized")
        self.x = 5

    def __str__(self):
        return f"MyClassWithInit [x={self.x}]"

    def myfunction(self):
        print("Hello I am of Object type MyClassWithInit --> ",self)

p3=MyClassWithInit()
print(p3.x)
p3.myfunction()

