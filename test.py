def parse_command(command): 
    parse_index = 0
    if command == 'STOP':
        return (command, 0)
     
    for i in range(len(command)): 
        if command[i].isdigit(): 
            parse_index = i 
            break
    if parse_index == 0: 
        return (command, 0)
    
    command_type = command[0:parse_index-1]
    command_value = command[parse_index:]

    return(command_type, command_value)
    
command = input('enter the command: ')
return_value = parse_command(command)
print(return_value)