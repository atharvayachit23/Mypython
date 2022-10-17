class Cycle:
    #brakes = None
    #wheels = None
    #paddle = None

    def __init__(self, brakes, wheels, paddle):
        self.brakes = brakes
        self.wheels = wheels
        self.paddle = paddle
        print("Initializing cycle object with values")

    def brake(self):
        print("slow down")
        print("stop cycle")

    def paaddle(self):
        print("move forward")

    def turnleft(self):
        print("turn left")

    def turnright(self):
        print("turn right")


#herocycle = Cycle()
#herocycle.brake()
#herocycle.paaddle()
#herocycle.turnleft()
#herocycle.turnright()
##erocycle.brakes = "disc brakes"
#herocycle.wheels = 2
#herocycle.paddle = "medium"
#bsaslrcycle = Cycle()
#bsaslrcycle.brakes = "regular brakes"
#bsaslrcycle.wheels = 2
#bsaslrcycle.paddle = "medium"
#print(bsaslrcycle.brakes)
herocycle2 = Cycle(2,2,"medium")
print(herocycle2.brakes)

