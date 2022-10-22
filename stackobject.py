class Stack:
    def __init__(self ):
        self.container = []

    def put(self):
        num = int(input("Enter a number"))
        self.container.append(num)

        return self.container
    def pop(self):

        if len(self.container) > 0:
            numlast = self.container[-1]
            print("Removing last number", numlast)
            self.container.remove(numlast)

    def printallelements(self):
        if len(self.container) > 0:
            for i in range(len(self.container)):
                print(self.container[i])
