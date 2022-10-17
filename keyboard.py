class Keyboard:
    def __init__(self,brand, colour, compatible_devices, special_feature):
        self.brand = brand
        self.colour = colour
        self.compatible_devices = compatible_devices
        self.special_feature = special_feature

    def special_feature(self):
        print("keyboard is wired")


mykeyboard = Keyboard("HP", "black", "laptop,PC", "Wired",)
