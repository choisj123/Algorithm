import itertools 
# 브루트 포스

# 조합 : 순서 고려 X
# 반복문 사용
# 3개의 조합을 구하기 위해서는 for문 3개, 4개의 조합은 for문 4개 ....
arr = ['A', 'B', 'C']
N = len(arr)

my_comb = []
for i in range(N - 1):
    for j in range(i + 1, N):
        my_comb.append((arr[i], arr[j]))
print(my_comb) # [('A', 'B'), ('A', 'C'), ('B', 'C')]

# 10C3 = 10*9*8 / (3*2*1)

# 조합 내장 함수
# cominations(리스트, 조합수)
# import itertools
# from itertools import combinations
print(list(itertools.combinations(arr,2)))

# 순열(Permutation) : 순서를 고려하여 나열하는 경우의 수
my_permu = []
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        my_permu.append((arr[i], arr[j]))
print(my_permu)

# 순열 내장함수
# permutations(리스트, 순열수)
# import itertools
# from itertools import combinations

print(list(itertools.permutations(arr,2)))

# 10P3 = 10 * 9 * 8