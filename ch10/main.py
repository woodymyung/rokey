from robot_tool import Robot

class Drone(Robot): 

    def __init__(self, name, altitude): 
        super().__init__(name)
        self.altitude = altitude
    
    def move(self): 
        print(f'드론 로봇 {self.name}이 하늘을 비행합니다!')
    


my_drone = Drone('Kelly', 100)
my_drone.move()
my_drone.charge()