def calculator(x, y, mode='plus'): 
    if mode == 'plus':
        return x + y
    else: 
        return x - y 

x = float(input('type_x: '))
y = float(input('type_y: '))
mode = input('mode?: ')

answer = calculator(x, y, mode)

print(answer)