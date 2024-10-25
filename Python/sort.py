# 정렬 

arr = [3, 1, 4, 5, 2]
# arr.sort() # 오름차순
# arr.sort(reverse=True) # 내림차순
print(arr)

# - 선택 정렬
# 최대값 또는 최소값을 찾아 선택을 반복하면서 정렬하는 방식

# 시간 복잡도 = O(N^2)
# 선택 정렬은 구현 방법이 복잡하고, 시간 효율이 좋지 않다

# 1. 리스트 내에서 최소값을 찾는다
# 2. 리스트의 첫번째 값과 최소값을 바꿔준다
# 3. 첫번째를 제외한 리스트 내에서 최소값을 찾는다
# 4. 리스트의 두번쨰 값과 3번의 최소값을 바꿔준다
# 5. 나머지 리스트를 상대로 3~4번을 반복한다

# 오름차순
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]: # 최솟값 구하기
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # i번째와 최솟값을 교환
        print(f"{i+1}번 째 정렬 후 = {arr}")
    return arr

# 내림차순
def selection_sort_reverse(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[min_idx]: # 최댓값 구하기
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # i번째와 최댓값을 교환
        print(f"{i+1}번 째 정렬 후 = {arr}")
    return arr

print(selection_sort(arr))
print(selection_sort_reverse(arr))

# - 버블정렬(거품 정렬)
# 앞에서부터 두 수를 비교해서 큰 수를 뒤로 보내는 것을 반복(swap 연산)
# 가장 큰 수가 맨 뒤에 있기 때문에 다음에는 마지막 전까지만 반복

# 시간복잡도 = O(N^2)
# 다른 정렬 알고리즘에 비해 정렬 시간은 다소 오래 걸리지만,
# 상대적으로 로직이 단순하고, 구현이 쉽다

# 1. 처음 숫자와 두 번째 숫자를 비교해서 앞의 수가 크면 두 수를 바꿔준다
# 2. 두 번째 수와 세 번째 수를 비교해서 앞의 수가 크면 두 수를 바꿔준다
# 3. 마지막 수의 차례가 될 때까지 2번을 반복한다
# 4. 마지막 수 정렬까지 끝나면 처음으로 돌아와 마지막 하나 전까지 다시 변경을 반복한다
# 5. 처음수가 정렬 될 때까지 앞의 정렬을 반복한다

# 선택정렬은 리스트 전체에서 최소값을 찾아서 변경을 했다면 거품 정렬은 계속적으로 변경을 해나가는 구조

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f"버블 변경 리스트 j = {arr}")
        print(f"버블 변경 리스트 i = {arr}")
    return arr

arr = [3, 1, 4, 5, 2]
print(arr)
print(bubble_sort(arr))

# - 삽입 정렬
# 새로운 리스트에 기존 리스트의 값을 위치에 맞게 삽입하면서 정렬하는 방식
# 선택 데이터를 현재 정렬된 데이터 범위 내에서 적절한 위치에 삽입

# 시간복잡도 = O(N^2)
# 느린 편이지만, 구현하기 쉽다

# 1. 리스트에서 첫 번째 값을 꺼내어 새로운 리스트에 넣음
# 2. 두번째 값을 꺼내서 새로운 리스트의 첫번째 값과 비교하여 정렬시킴
# 3. 세번째 값을 2번의 리스트의 정렬된 위치에 삽입시킴
# 4. 마지막 값까지 정렬 중인 리스트에 알맞은 값을 삽입시킴

def insertion_sort(arr):
    new_arr = [arr[0]]
    print(f"1번째 정렬된 리스트 = {new_arr}")

    for i in range(1, len(arr)):
        j = 0
        while j < i and new_arr[j] < arr[i]:
            j += 1
        new_arr.insert(j, arr[i])
        print(f"{i + 1}번째 정렬된 리스트 {j} {i} = {new_arr}")
    return new_arr

arr = [3, 1, 4, 5, 2]
print("최종 정렬된 리스트 = ", insertion_sort(arr))

## 두 개의 리스트가 아니라 하나의 리스트 안에 두 개의 리스트가 있다고 생각하고 수행 가능
def insertion_sort2(arr):
    for i in range(1, len(arr)):
        print(f"{i}번째 새로운 리스트 = {arr[:i]}/ 기존 리스트 = {arr[i:]}")
        j = i
        while 0 < j and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr
arr = [3,1,4,5,2]
print("정렬이 끝난 리스트 = ", insertion_sort2(arr))


# 퀵 정렬
# 기준값(pivot)을 선정해 해당 값보다 작은 데이터와 큰 데이터로 분류하는 것을 반복해 정렬하는 방식

# 시간복잡도 = 평균 : O(nlogn)/ 최악 : O(n^2)
# 기준값이 어떻게 선정되는지가 시간복잡도에 많은 영향을 미침

  

# 병합 정렬 (Merge Sort)
# 이미 정렬된 부분 집합들을 효율적으로 병합해 전체를 정렬하는 방식

# 시간복잡도 = O(nlogn)


# 기수 정렬
# 데이터의 자릿수를 바탕으로 비교해 데이터를 정렬하는 방식


# 정렬 예제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오. (1 <= N <= 1,000)

# 1. 문제의 input 받기
# 2. 배열 오름차순으로 정렬
# 3. 출력

import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline()))

# arr.sort()
for i in range(N - 1):
    for j in range(N - 1 - i):
        if arr[j+1] < arr[j]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

# for a in arr:
#     print(a)
print(*arr, sep="\n")


N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    name, a, b, c = sys.stdin.readline().split()
    arr.append([name, int(a), int(b), int(c)])

arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for a in arr:
    print(a[0])
