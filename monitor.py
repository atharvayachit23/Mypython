class Monitor:
    def __init__(self,brand, colour, compatible_devices, picture_quality, size):
        self.brand = brand
        self.colour = colour
        self.compatible_devices = compatible_devices
        self.picture_quality = picture_quality
        self.size = size

    def size(self):
        print("size of the monitor diagonally")


mymonitor = Monitor("Lenovo", "black", "laptop,PC", "4K", "15.6 inch")

print(mymonitor)