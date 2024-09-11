# 백준 2309

import itertools

## 리스트
# heights = []
# for i in range(9):
#     heights.append(int(input()))

# total_sum = 0
# result = list(itertools.combinations(heights, 7))

# for r in result:
#     total_sum = sum(r)

#     if total_sum == 100:
#         sorted_r = sorted(r)
#         print(sorted_r)
#         break
    

def print_result(arr, a, b):
    for i in range(9):
        if i == a or i == b:
            continue
        print(arr[i])

# 1. input 받기
heights = []
for i in range(9):
    heights.append(int(input()))

# 2. 아홉 난쟁이 키의 합 미리 구해두기
total_sum = sum(heights)
# 3. 미리 정렬
heights.sort()

# 4. 9명 중 2명을 제외하는 모든 경우의 수를 탐색하는 for loop 구현
found = False
for i in range(9):
    if found:
        break
    for j in range(i + 1, 9):
        # 5. 제외된 2명을 빼고 총 합이 100인지 확인
        now = total_sum - heights[i] - heights[j]

        # 6. 100이면 출력, for loop 탈출  
        if now == 100:
            print_result(heights, i, j)
            found = True
            break
            



