import psutil

# 전체 가상 메모리 정보 가져오기
mem = psutil.virtual_memory()

# 1. 전체 용량 (Total)
# bytes 단위로 나오기 때문에 1024의 3제곱(GB)으로 나눠줍니다.
total_gb = mem.total / (1024 ** 3)

# 2. 사용 가능한 용량 (Available)
available_gb = mem.available / (1024 ** 3)

# 3. 사용 중인 퍼센트 (Percent)
percent = mem.percent

print(f"전체 메모리 용량: {total_gb:.2f} GB")
print(f"사용 가능한 용량: {available_gb:.2f} GB")
print(f"메모리 점유율: {percent}%")