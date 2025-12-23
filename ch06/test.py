def calculate_sum(nested_list, depth): 

    sum = 0

    len_list = len(nested_list)

    # 리스트의 요소의 타입 체크 
    for i in range(len_list):

        # type: int 
        if type(nested_list[i]) == int :

            # depth 가 짝수이면 더하기 
            if depth % 2 == 0: 
                sum += nested_list[i]
            # depth 가 홀수이면 빼기
            else: 
                sum -= nested_list[i]
                # print(total_num)
        else: 
        # type: list
            # 재귀함수
            sum += calculate_sum(nested_list[i], depth+1)

    return sum
    
depth = 0 
total_num = 0

nested_list = [1, [2, 3], [4, [5, 6]]]
print(calculate_sum(nested_list, depth))
