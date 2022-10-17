try:
    print(x)
except:
    print("ERROR CODE 1: Error - x is undefined!!!")

try:

    #
    print(y)
    #Transfer funds
        #Insufficient funds
        #Account name invalid
        #Account name and Account owner name mismatch
        #Account locked
        #Account closed
        #Account exceeds daily limit
        #Fraudulent transaction

except:
    print("ERROR CODE 2: Error - y is undefined!!!")


try:
    print(z)
except NameError:
    print("z variable name is undefined")
except:
    print("General error")

try:
    print("Helllo")
except:
    print("z variable name is undefined")
else:
    print("General error")

try:
    print("adasdasd")
except:
    print("zz not defined")
finally:
    print("In finally block, you can clean up stuff here")

x = int(input("Enter a number: "))
if x < 0:
    raise Exception("Number should be larger than 0")


print("Hello World!!!")
