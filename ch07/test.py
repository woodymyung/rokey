"""import keyword 

def check_keyword(word): 
    if word in keyword.kwlist: 
        print('unavailable')
    else:
        print('available')

check_keyword(list)"""



"""def swap(list): 

    # list 의 길이를 파악
    length = len(list)

    # 만약 배열이 비어있으면 종료
    if length == 0: 
        return 
    
    for i in range(length):
        for j in range(i+1, length): 
            if list[j] < list[i]: 
                list[i], list[j] = list[j], list[i]
    
    return list

list = [3, 10, 38, 7, -1, 3, 0]

print(swap(list))"""

# def swap(idx, list): 
#     length = len(list)
    
#     if length == 0: 
#         return 

#     print(f'{idx}번째 루프 -----')

#     if idx == length-1:
#         print('기저조건')
#         return list

#     for i in range(idx+1, length):
#         print(f'{i}번째 숫자 vs {idx}번째 숫자 비교')
#         if list[idx] > list[i]: 
#             list[idx], list[i] = list[i], list[idx]
#             # print(list)

#     idx += 1
#     return swap(idx, list) 

# idx = 0
# list = [3, 10, 38, 7, -1, 3, 0]
# # print(id(list))

# print(swap(idx, list))
# # print(id(list))



# def find_max(data_list):
#     # 1. 기저 조건: 리스트에 숫자가 하나면 그게 최대값이다.
#     if len(data_list) == 1:
#         return data_list[0]
    
#     # 2. 재귀 단계: 나(첫 번째)와 나머지 중 최대값을 비교한다.
#     # 나머지 리스트에서 최대값을 찾아오라고 시킴 (재귀 호출)
#     sub_max = find_max(data_list[1:])
    
#     # 3. '내'가 할 일: 내 값과 남이 찾아온 값 중 큰 걸 선택해서 위로 보낸다.
#     if data_list[0] > sub_max:
#         return data_list[0]
#     else:
#         return sub_max

# # 실행
# data_list = [7, 3, 15, 22, 1, 9, 11]
# print(find_max(data_list))



# def reverse_string(s): 

#     # 종료 조건: 한 글자라면 결과는 자기 자신 
#     if len(s) == 1: 
#         return s
    
#     # 내가 할 일: 마지막 글자를 고르기
#     last_char = s[-1]

#     # 재귀 단계: 마지막 글자와 마지막 글자를 제외한 글자를 합치기
#     return last_char + reverse_string(s[:-1]) 


# s = input('s: ')
# print(reverse_string(s))


# def total_sum(data): 

#     # 종료 조건 : 리스트의 길이가 0이면 반환 
#     if type(data) == list and len(data) == 0: 
#         total_add = 0
#         return total_add

#     # 남이 할 일: 요소를 검사하고 int 면 더하기 + type 이면 다시 검사하기

#     if type(data[0]) == int: 
#         return data[0] + total_sum(data[1:])
#     else: 
#         return total_sum(data[0]) + total_sum(data[1:])

        
# data = [1, 2, [3, 4], [5, [6, 7]], 8]
# print(total_sum(data))


# def total_sum(data):

#     if type(data) == int: 
#         return data 
    
#     if len(data) == 0: 
#         return 0
    
#     return total_sum(data[0]) + total_sum(data[1:])

# data = [1, 2, [3, 4], [5, [6, 7]], 8]
# print(total_sum(data)) # 출력: 36


# def fibonacci(n): 

#     if n == 1 or n == 2:
#         return 1
    
#     return fibonacci(n-1) + fibonacci(n-2)


# print(fibonacci(7))


# def gcd(a, b): 

#     if a == 0 or b == 0: 
#         return 

#     if a % b == 0: 
#         return b
    
#     return gcd(b, a%b)


# print(gcd(40, 3))



# def combination(n, r): 

#     if n == r:
#         return 1
    
#     if r == 1: 
#         return n
    
#     if r == 0: 
#         return 0
    
#     return combination(n-1, r-1) + combination(n-1, r)

# print(combination(5,1))






# def solve_maze(x, y, track):
#     # 1. 기저 조건: 미로 범위를 벗어난 경우
#     if x < 0 or x >= 5 or y < 0 or y >= 5:
#         return 0

#     # 2. 기저 조건: 벽(1)이거나 이미 방문한 길인 경우
#     if maze[x][y] == 1:
#         return 0

#     # 현재 칸을 포함하므로 track을 1 증가
#     track += 1

#     # 3. 기저 조건: 목적지(2)에 도착한 경우
#     if maze[x][y] == 2:
#         return track

#     # --- 재귀 단계 및 백트래킹 ---
    
#     # [백트래킹 시작] 현재 위치를 벽(1)으로 막아 무한 루프 방지
#     original_value = maze[x][y]
#     maze[x][y] = 1

#     # 사방 탐색 결과를 리스트에 담기
#     results = [
#         solve_maze(x - 1, y, track), # 상
#         solve_maze(x + 1, y, track), # 하
#         solve_maze(x, y - 1, track), # 좌
#         solve_maze(x, y + 1, track)  # 우
#     ]

#     # [백트래킹 해제] 탐색이 끝났으므로 다음 경로를 위해 다시 길(0)로 복구
#     maze[x][y] = original_value

#     # 4. 결과 도출: 성공한 경로(0보다 큰 값)들 중 최솟값 선택
#     success_paths = [r for r in results if r > 0]
    
#     return min(success_paths) if success_paths else 0

# # 테스트용 미로 (0: 통로, 1: 벽, 2: 목적지)
# # 두 갈래 길 중 (4,4)까지 가는 지름길을 찾아야 함
# maze = [
#     [0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 0],
#     [0, 0, 0, 1, 0],
#     [1, 1, 0, 0, 0],
#     [1, 1, 1, 1, 2]
# ]

# result = solve_maze(0, 0, 0)

# if result > 0:
#     print(f"최단 탈출 경로: {result}칸")
# else:
#     print("탈출구가 없습니다.")


