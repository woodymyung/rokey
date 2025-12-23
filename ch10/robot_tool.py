class Robot: 
    def __init__(self, name): 
        self.name = name
        self.battery = 100
    
    def move(self): 
        print(f'{self.name} 로봇이 이동합니다')
    
    def charge(self): 
        self.battery = 100
        print(f'{self.name} 로봇이 배터리{self.battery}로 충전 완료되었습니다')


if __name__ == "__main__": 
    my_robot = Robot('James')
    my_robot.move()

