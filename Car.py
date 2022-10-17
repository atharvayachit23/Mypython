x=int(input("Enter acceleratorAngle-"))
y=int(input("Enter gearnumber-"))
z=int(input("Enter timeInSeconds-"))
class Car:
    model = None
    type = None
    year = None
    company = None
    color = None
    wheeldimensions = None
    numberofseats = None
    airbags = None
    groundclearence = None
    parkingccamera = None
    bootspace = None
    enginecc = None
    maxspeed = None
    fueltankcapacity =None
    speaker = None
    airConditioner = None
    sunroof = None
    drive = None    
def engineSpeed(accelaratorAngle):
    match accelaratorAngle:
        case 30:
            return 500
        case 25:
            return 1500
        case 20:
            return 2000
        case 15:
            return 2500
        case 10:
            return 3000
        case 5:
            return 3500
        case 0:
            return 4000
        case default:
            return 500
def gearnumber(speed):
    match speed:
        case 0:
            return speedsByGear["0"]
        case 1:
            return speedsByGear["1"]
        case 2:
            return speedsByGear["2"]
        case 3:
            return speedsByGear["3"]
        case 4:
            return speedsByGear["4"]
        case 5:
            return speedsByGear["5"]
        case -1:
            return speedsByGear["-1"]
        case default:
            return speedsByGear["0"]
def speedAfterstart(timeInSeconds):
    match timeInSeconds:
        case 0:
            return vehicleSpeedInTime["0"]
        case 5:
            return vehicleSpeedInTime["20"]
        case 10:
            return vehicleSpeedInTime["45"]
        case 15:
            return vehicleSpeedInTime["70"]
        case 20:
            return vehicleSpeedInTime["95"]
        case 25:
            return vehicleSpeedInTime["120"]
        case 30:
            return vehicleSpeedInTime["145"]
        case 35:
            return vehicleSpeedInTime["170"]
        case default:
            return vehicleSpeedInTime["0"]
speedsByGear = {
    "1": [0, 5, 10, 15, 20, 25, 30],
    "2":[15, 20, 25, 30,  35, 40],
    "3":[25, 30,  35, 40, 45, 50 ,55 ,60],
    "4":[40, 45, 50 ,55 ,60,65,70,75,80,85,90, 95,100],
    "5":[50 ,55 ,60, 65, 70, 75, 80, 85, 90, 95, 100,105, 110, 115, 120, 125, 130,135,140],
    "-1":[0, 5, 10, 15, 20, 25, 30],
    "0":[0]
    }
vehicleSpeedByEngineSpeed ={
    "500":[0,5],
    "1500":[0,5,10,15,20],
    "2000":[0,5,10,15,20,25,30,35,40],
    "2500":[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90, 95,100],
    "3000":[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90, 95,100,105, 110, 115, 120, 125, 130,135,140],
}

vehicleSpeedInTime ={
    "0":[0],
    "5":[0,5,10,15,20],
    "10":[0,5,10,15,20,25,30,35,40,45],
    "15":[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70],
    "20":[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95],
    "25":[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120],
    "30":[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145],
    "35":[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170],
}
def drive(self,gearnumber,accelaratorangle,timeInSeconds):
    currentSpeedRange = gearnumber(gearnumber)
    currentEngineSpeed = engineSpeed(accelaratorangle)
    timeAfterVehicleStarted = speedAfterstart(timeInSeconds)
    if gearnumber == 0:
        print("max speed=0")
    if gearnumber == 1:
        print(" max speed=30")
    if gearnumber == 2:
        print("max speed =40")
    if gearnumber == 3:
        print("max speed=60")
    if gearnumber == 4:
        print("max speed=100")
    if gearnumber == 5:
        print("max speed=140")
    if gearnumber ==-1:
        print("max speed=30")
    if accelaratorangle in range(25,30):
        print("engineSpeed=500")
    if accelaratorangle in range(20,25):
        print("engineSpeed=1500")
    if accelaratorangle in range(15,20):
        print("engineSpeed=2000")
    if accelaratorangle in range(10,15):
        print("enginespeed=2500")
    if accelaratorangle in range(5,10):
        print("enginespeed=3000")
    if accelaratorangle in range(0,5):
        print("enginespeed=3500")
    if timeInSeconds == 0:
        print("car speed is zero")
    if timeInSeconds in range(0,5):
        print("car max speed is 20")
    if timeInSeconds in range(5,10):
        print("car max speed is 45")
    if timeInSeconds in range(10,15):
        print("car max speed is 70")
    if timeInSeconds in range(15,20):
        print("car max speed is 95")
    if timeInSeconds in range(20,25):
        print("car max speed is 120")
    if timeInSeconds in range(25,30):
        print("car maxx speed is 145")
c1 =Car
print(c1.drive)