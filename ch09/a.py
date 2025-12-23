# class Phone: 
#     def __init__(self, maker, year, color):
#         print('휴대폰 생성')
#         self.maker = maker
#         self.year = year
#         self.color = color
    
#     def info(self): 
#         print(self.maker, self.year, self.color)

#     def setInfo(self, maker, year, color): 
#         self.maker = maker
#         self.year = year
#         self.color = color
    
# my_phone = Phone('애플', 2020, '그레이')
# my_phone.info()
# my_phone.setInfo('삼성', 2024, '블랙')

class Robot:
    robot_name = 'Adam'

robot_1 = Robot()
robot_1.robot_name = 'James'


class Robot2:
    def __init__(self, name):
        self.name = name

robot_2 = Robot2('David')