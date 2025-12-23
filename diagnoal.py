import numpy as np

# 1. 원래 행렬 M 정의
M = np.array([
    [1, 1],
    [0, 2]
])

# 2. 우리가 구한 고유벡터와 고유값 정의
# v1: x축 (고유값 1)
v1 = np.array([1, 0])
lambda_1 = 1

# v2: 45도 대각선 (고유값 2)
v2 = np.array([1, 1])
lambda_2 = 2

print("--- [1] 방향 일치 확인 (Mv = λv) ---")

# v1에 행렬 M을 곱해봅니다 (변환)
transformed_v1 = M @ v1
print(f"1. 원래 v1      : {v1}")
print(f"2. 변환된 v1    : {transformed_v1}")
print(f"3. 람다 * v1    : {lambda_1 * v1}")
print(f"결과: {'방향이 일치함' if np.array_equal(transformed_v1, lambda_1 * v1) else '불일치'}")
print("-" * 30)

# v2에 행렬 M을 곱해봅니다
transformed_v2 = M @ v2
print(f"1. 원래 v2      : {v2}")
print(f"2. 변환된 v2    : {transformed_v2}")
print(f"3. 람다 * v2    : {lambda_2 * v2}")
print(f"결과: {'방향이 일치함' if np.array_equal(transformed_v2, lambda_2 * v2) else '불일치'}")

print("\n--- [2] 기저축 정렬 확인 (대각화) ---")

# 고유벡터들을 열로 세워 만든 기저변경 행렬 P
P = np.column_stack((v1, v2))
print(f"기저변경 행렬 P :\n{P}")

# P의 역행렬
P_inv = np.linalg.inv(P)

# 고유기저 세상에서의 행렬 D = P^(-1) @ M @ P
D = P_inv @ M @ P

print(f"\n고유기저 세상의 행렬 D (반올림):\n{np.round(D)}")