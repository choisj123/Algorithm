
# 백준 1181

N = int(input())
arr = []
for _ in range(N):
    arr.append(input())

unique = list(set(arr)) 
unique.sort(key=lambda x: (len(x), x))

print(*unique, sep="\n")


# 백준 11399
N = int(input())
arr = input().split(" ")

for i in range(len(arr)):
    arr[i] = int(arr[i])

arr.sort()

sum_arr = []

for i in range(len(arr)):
    for j in range(i + 1):
        sum_arr.append(arr[j])

print(sum(sum_arr))

#-----------------------------------

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

total_sum = 0
curren_sum = 0

for a in arr:
    curren_sum += a
    total_sum += curren_sum

print(total_sum)


#-----------------------------------
# 삽입 정렬
N = int(input())
A = list(map(int, input().split()))
S = [0]*N

for i in range(1, N):
    insert_point = i
    insert_value = A[i]

    for j in range(i-1, -1, -1):
        if A[j] < A[i]:
            insert_point = j + 1
            break
        if j == 0:
            insert_point = 0
    
    for j in range(i, insert_point, -1):
        A[j] = A[j-1]
    A[insert_point] = insert_value

S[0] = A[0]

for i in range(1,N):
    S[i] = S[i-1] + A[i]

sum = 0
for i in range(0,N):
    sum += S[i]

print(sum)