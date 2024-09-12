# 백준 5635

import sys

# 람다식 이용
# N = int(sys.stdin.readline())
# arr = []

# for i in range(N):
#     name, dd, mm, yyyy = sys.stdin.readline().strip().split()
#     arr.append([name, int(dd), int(mm), int(yyyy)])

# # 정렬
# arr.sort(key=lambda x: (x[3], x[2], x[1]))

# print(arr[N-1][0])
# print(arr[0][0])


# 리스트 저장 순서를 바꿔서 sort() 자체로 정렬
# N = int(sys.stdin.readline())
# arr = []

# for i in range(N):
#     name, dd, mm, yyyy = sys.stdin.readline().strip().split()
#     arr.append([int(yyyy), int(mm), int(dd), name])

# # 정렬
# arr.sort()

# print(arr[N-1][3])
# print(arr[0][3])


# 백준 25305

# N, K = map(int, sys.stdin.readline().strip().split())
# arr = list(map(int,sys.stdin.readline().strip().split()))

# arr.sort(reverse=True)
# print(arr[K-1])




# 백준 2947

arr = list(map(int, sys.stdin.readline().strip().split()))

for i in range(5):
    for j in range(5-i-1):
        if(arr[j+1] < arr[j]):
            arr[j+1], arr[j] = arr[j], arr[j+1]
            print(*arr, sep=" ")