path = './pizza_file1.txt'

with open(path, 'r', encoding='utf-8') as file: 
    lines = file.readlines()
    pizza_list = []
    for line in lines: 
        print(line.split()[0])
        pizza_list.append(line.split()[0])

print(pizza_list)

wooDnwlaud98^dy