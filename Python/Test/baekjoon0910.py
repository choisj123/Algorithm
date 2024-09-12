# 백준 10814

import sys

# 1. 문제의 입출력을 받습니다.
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    age, name = sys.stdin.readline().split()
    arr.append([int(age), name])

# 2. 2차원 배열을 정렬합니다. 이 때 1열의 값이 같을 경우, 2열의 정렬 순서는 배열의 원래 순서 유지
arr.sort(key=lambda x: (x[0]))
for i in arr:
    print(i[0], i[1])

