# # 로봇 설계도 
# class Robot:
#     serial_number = 0
#     def __init__(self, name): 
#         self.name = name
#         Robot.serial_number += 1
#         self.serial_number = Robot.serial_number
#         self.battery = Battery()

#     def work(self, cost=10):
#         self.battery.use(cost)
#         print(f'로봇이 작동합니다')

# # 배터리 설계도 
# class Battery: 

#     def __init__(self): 
#         self.capacity = 100
#         self.level = 80
    
#     def charge(self, amount): 
#         if self.level + amount > self.capacity: 
#             raise ValueError
#         self.level += amount
    
#     def use(self, amount):
#         if amount > self.level:
#             raise ValueError
#         self.level -= amount
    
#     def __str__(self):
#         return f'[Battery: {self.level} / {self.capacity}]'



# # 로봇 객체 

# # 용접 로봇 
# class WeldingRobot(Robot): 

#     def __init__(self, name):
#         super().__init__(name)
    
#     def work(self): 
#         self.battery.use(15)
#         print(f'{self.name} 로봇이 강력한 불꽃으로 용접을 시작합니다')
    

# # 도색 로봇 
# class PaintingRobot(Robot): 

#     def __init__(self, name):
#         super().__init__(name)
    
#     def work(self): 
#         self.battery.use(8)
#         print(f'{self.name} 로봇이 고르게 도색 작업을 수행합니다')


# # 로봇 관리 설계도(컨트롤러)
# class Factory:
    
#     def __init__(self, name): 
#         self.name = name
#         self.list = []
    
#     def produce_robot(self, type, name):
#         if type == 'WeldingRobot': 
#             self.list.append(WeldingRobot(name))
#         elif type == 'PaintingRobot':
#             self.list.append(PaintingRobot(name))
#         else:
#             raise ValueError
        
#     def operate_all(self):
#         for i in self.list:
#             i.work()
    
#     def show_inventory(self):
#         for i in self.list:
#             print(i.name, i.serial_number, i.battery)

# my_factory = Factory('woody\'s factory')
# my_factory.produce_robot('WeldingRobot', 'welbot')
# my_factory.produce_robot('PaintingRobot', 'paintbot')
# my_factory.operate_all()
# my_factory.show_inventory()

# class Robot: 

#     def __init__(self, name): 
#         self.name = name
    
#     def check_address(self): 
#         print(f'self의 주소: {id(self)}')
#         print(f'self.name의 주소: {id(self.name)} ')
    

# robotObject = Robot('woody')
# robotObject.check_address()

# print(f'robotObject의 주소: {id(robotObject)}')
# print(f'woody의 주소: {id('woody')}')

class Robot:

    total_battery = 0 

    def __init__(self, name):
        self.name = name
        self.total_battery = Robot.total_battery

robot = Robot('woody')

# 객체의 힙 공간에 저장된 인스턴스 변수 명단 확인
print(robot.__dict__) 
# 출력 예: {'name': 'woody'}