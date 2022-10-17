class CPU:
    def __init__(self, brand, colour, operating_system, ram, storage, core,total_usb_ports,manufacturer):
        self.brand = brand
        self.colour = colour
        self.operating_system = operating_system
        self.ram = ram
        self.Storage = storage
        self.Core = core
        self.total_usb_ports = total_usb_ports
        self.maufacturer = manufacturer

    def operating_system(self):
        print("Start Computer")
        print("Control and run Computer Processes")


myCPU = CPU("Lenovo", "grey", "Windows 11", "8GB", "512GB", "i5", "2", "Intel")
