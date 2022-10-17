class Mouse:

    def __init__(self, brand, colour, connectivity,special_features):
        self.brand = brand
        self.colour = colour
        self.connectivity = connectivity
        self.special_features = special_features

    def special_features(self):
        print("mouse is wired")


mymouse = Mouse("intel", "black", "USB", "Wired")

