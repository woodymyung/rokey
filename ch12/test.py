with open('./계좌1.txt', 'r') as file: 

    lines = file.readlines()
    accountDict = {}
    for line in lines:
        temp_key = line.split()[0]
        temp_value = line.split()[1]
        accountDict[temp_key] = temp_value

print(accountDict) 
print(file.closed)

