def check_command(command): 
    if command == 'SELF_DESTRUCT': 
        raise Exception 
    print(f'명령어 승인: {command}')

user_command = input('명령어 입력: ')

try: 
    check_command(user_command)
except Exception:
    print('경고: 위험한 명령입니다!')