# 1. input 받기
N = int(input())
arr = []
for _ in range(N):
    arr.append(input())

# 2. 중복 제거
unique = list(set(arr)) 

# 3. 정렬
unique.sort(key=lambda x: (len(x), x))

# 4. 출력
print(*unique, sep="\n")